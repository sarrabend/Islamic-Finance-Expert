from .preprocessing import split_md, parse_pdf
from .embedding import upload_qdrant
from ..config import PROJECT_PATH
import os 

if __name__ == "__main__":
    pdf_path = os.path.join(PROJECT_PATH, "data", "test.pdf")
    md_content, response_dict = parse_pdf(pdf_path)
    chunks = split_md(md_content, chunk_size=1000, chunk_overlap=200)
    upload_qdrant(chunks, "test")
