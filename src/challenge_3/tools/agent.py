from agno.tools import tool
import os 
from qdrant_client import QdrantClient
from langchain_openai import OpenAIEmbeddings

from .utils import read_file, format_tool_output
from src.config import PROJECT_PATH, QDRANT_URL, QDRANT_API_KEY, OPENAI_API_KEY, COLLECTIONS, FAS_STANDARDS


embeddings= OpenAIEmbeddings(model="text-embedding-ada-002", api_key=OPENAI_API_KEY)
qdrant_client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY, prefer_grpc=True)



@tool 
def list_collections() -> str:
    """
    Lists all the collections in the Qdrant database.

    Returns:
        str: List of collection names.
    """

    # Get the list of collections
    return format_tool_output(COLLECTIONS)


@tool 
def get_standards() -> str:
    """
    List the standards to focus on.
    - Useful for the translate agent to perform accurate translation.

    Returns:
        str: json like string of the different standards, their code and their descriptions
    """

    return format_tool_output(FAS_STANDARDS)

@tool 
def retrieval_tool(query: str) -> str:
    """
    Retrieves relevant information from the provided collection based on the provided query.
    Args:
        query (str): The query to search for in the vector store.
        collection_name (str): The name of the collection to search in.

    Returns:
        str: The retrieved information from the collection.

    """
    collection_name = "shariaa-standards"
        
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

    return format_tool_output([result.payload.get("content",[]) for result in search_result])

