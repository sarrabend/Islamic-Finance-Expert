from qdrant_client import QdrantClient
from ..config import QDRANT_URL, QDRANT_API_KEY

def test_qdrant_connection():
    try:
        client = QdrantClient(
            url=QDRANT_URL,
            api_key=QDRANT_API_KEY,
            prefer_grpc=False
        )
        # Try to get collections info
        collections = client.get_collections()
        print("Successfully connected to Qdrant!")
        print(f"Available collections: {collections}")
        return True
    except Exception as e:
        print(f"Connection error: {str(e)}")
        print(f"URL: {QDRANT_URL}")
        return False

if __name__ == "__main__":
    test_qdrant_connection() 