import os
from mistralai import Mistral
from pathlib import Path
from mistralai import DocumentURLChunk, ImageURLChunk, TextChunk
import json
from mistralai.models import OCRResponse
from IPython.display import Markdown, display

from langchain_text_splitters import MarkdownHeaderTextSplitter # type: ignore
from langchain_text_splitters import RecursiveCharacterTextSplitter


from src.config import PROJECT_PATH,MISTRAL_API_KEY
from src.data_processing.utils import save_images

client = Mistral(api_key=MISTRAL_API_KEY)


def ocr_to_markdown(ocr_response: OCRResponse) -> str:
  markdowns: list[str] = []
  for page in ocr_response.pages:
    markdowns.append(page.markdown)

  return "\n\n".join(markdowns)

def parse_pdf(pdf_path: str) -> str:
    pdf_file = Path(pdf_path)


    uploaded_file = client.files.upload(
        file={
            "file_name": pdf_file.stem,
            "content": pdf_file.read_bytes(),
        },
        purpose="ocr",
    )

    signed_url = client.files.get_signed_url(file_id=uploaded_file.id, expiry=1)

    pdf_response = client.ocr.process(document=DocumentURLChunk(document_url=signed_url.url), model="mistral-ocr-latest", include_image_base64=True)

    response_dict = json.loads(pdf_response.json())
    json_string = json.dumps(response_dict, indent=4)
    return ocr_to_markdown(pdf_response), response_dict

    

def split_md(md_content, chunk_size, chunk_overlap):
    '''
    Splits the markdown content into chunks of children
    Args : 
        md_content : Markdown content
        chunk_size : Size of the chunk
        chunk_overlap : Overlap between chunks
    '''
    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
        ("####", "Header 4"),
    ]

    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
    md_header_splits = markdown_splitter.split_text(md_content)
    markdown_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, 
                                                chunk_overlap=chunk_overlap, 
                                                add_start_index=True)
    chunks = []
    for parent in md_header_splits:
        children = markdown_splitter.split_text(parent.page_content)
        headers = [value for value in parent.metadata.values()]

        headers_text = "\n".join(headers) if headers else " "

        for child in children:
            child = headers_text + "\n" + child
            chunks.append(child)
    return chunks
