
import json
from agno.tools import tool

from qdrant_client import QdrantClient
from langchain_openai import OpenAIEmbeddings
from src.config import PROJECT_PATH, QDRANT_URL, QDRANT_API_KEY, OPENAI_API_KEY, COLLECTIONS, FAS_STANDARDS



embeddings= OpenAIEmbeddings(model="text-embedding-ada-002", api_key=OPENAI_API_KEY)
qdrant_client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY, prefer_grpc=True)



@tool 
def retrieval_tool(query: str, collection_name : str) -> str:
    """
    Retrieves relevant information from the provided collection based on the provided query.
    Args:
        query (str): The query to search for in the vector store.
        collection_name (str): The name of the collection to search in.

    Returns:
        str: The retrieved information from the collection.

    """
        
    # Check if the collection exists
    if not qdrant_client.collection_exists(collection_name):
        return (f"Collection {collection_name} does not exist.")
    
    # Get the vector for the query
    query_vector = embeddings.embed_text(query)
    # Perform the search
    search_result = qdrant_client.search(
        collection_name=collection_name,
        query_vector=query_vector,
        limit=10,  # Limit the number of results
        score_threshold=0.7,  # Minimum score threshold for results
        with_payload=True,  # Include payload in the results
    )

    return json.dumps([result.payload.get("content",[]) for result in search_result])
