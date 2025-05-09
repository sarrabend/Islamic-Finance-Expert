from .preprocessing import split_md, parse_pdf
from .embedding import upload_qdrant
from ..config import PROJECT_PATH
import os 

if __name__ == "__main__":
    # pdf_path = os.path.join(PROJECT_PATH, "data", "shariaah_standards_part2.pdf")
    # md_content, response_dict = parse_pdf(pdf_path)
    with open("C:/Users/pc/Desktop/IsDBI/code/Islamic-Finance-Expert/output/parsed_at-altmkyn_alaqtsady.md", "r") as f:
        md_content=f.read()
    chunks = split_md(md_content, chunk_size=1000, chunk_overlap=300)
    upload_qdrant(chunks, "at-tamkin-al-aqtsady-arabic")
