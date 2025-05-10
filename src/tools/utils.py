import json
from typing import Any




def format_tool_output(tool_message: Any) -> str:
	"""
	Formats the tool message into a JSON string ensuring it's always a valid str.

	Args:
	    tool_message (Any): The tool message to be converted (typically a dict).

	Returns:
	    str: JSON formatted string representation of the tool message.
	"""
	return json.dumps(tool_message, ensure_ascii=False)


def read_file(file_path: str) -> str:
	"""
	Read the content of a file and return it as a string.

	Args:
	    file_path (str): Path to the file to be read.

	Returns:
	    str: Content of the file.
	"""
	with open(file_path, "r", encoding="utf-8") as f:
		return f.read()