from langchain_mistralai import MistralAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from ..config import MISTRAL_API_KEY, QDRANT_URL, QDRANT_API_KEY, HF_TOKEN, OPENAI_API_KEY
# from langchain_qdrant import QdrantVectorStore
from tqdm import tqdm
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, PointStruct
from langchain_core.documents import Document
from uuid import uuid4

# embeddings = MistralAIEmbeddings(
#     model="mistral-embed",
#     api_key=MISTRAL_API_KEY
# )

embeddings = OpenAIEmbeddings(model="text-embedding-ada-002", api_key=OPENAI_API_KEY)


def embed_text(text):
    return embeddings.embed_query(text)


def embed_documents(documents):
    return embeddings.embed_documents(documents)



def prepare_docs(chunks):
    docs = [Document(page_content=doc) for doc in chunks]
    uuids = [str(uuid4()) for _ in range(len(docs))]
    # Convert documents to payload format
    payloads = [{"content": doc.page_content, "metadata": doc.metadata} for doc in docs]
    return docs, uuids, payloads






def upload_qdrant(chunks, collection_name, VECTOR_SIZE=1536, DISTANCE=Distance.COSINE):

    # Test connection first before trying operations
    try:
        qdrant_client = QdrantClient(
            url=QDRANT_URL,
            api_key=QDRANT_API_KEY,
            prefer_grpc=False,  # Use HTTP for cloud connection
            timeout=10  # Adding timeout for faster feedback
        )
        # Simple operation to test connection
        collections = qdrant_client.get_collections()
        print(f"Successfully connected to Qdrant. Available collections: {collections}")
        
        # Only proceed if connection was successful
        if not qdrant_client.collection_exists(collection_name):
            print(f"Creating new collection: {collection_name}")
            qdrant_client.create_collection(
                collection_name=collection_name,
                vectors_config=VectorParams(size=VECTOR_SIZE, distance=DISTANCE),
            )
        else:
            print(f"Collection {collection_name} already exists")
        
        # Now upload points
        docs, uuids, payloads = prepare_docs(chunks)
        embeddings = embed_documents(chunks)  # Assuming this function exists
        
        points = [PointStruct(id=unique_id, payload=payload, vector=embedding) 
                 for unique_id, payload, embedding in zip(uuids, payloads, embeddings)]
        
        # Upload in batches to avoid timeouts for large datasets
        batch_size = 100
        for i in tqdm(range(0, len(points), batch_size), desc="Uploading points"):
            batch = points[i:i+batch_size]
            qdrant_client.upsert(
                collection_name=collection_name,
                points=batch
            )
        print(f"Successfully uploaded {len(points)} points to collection '{collection_name}'")
        
    except Exception as e:
        print(f"Error during upload: {str(e)}")
        raise



