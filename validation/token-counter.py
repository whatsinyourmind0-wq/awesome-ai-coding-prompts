import sys
import json
import tiktoken
from pathlib import Path

def count_tokens(text: str, model: str = "gpt-4") -> int:
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        # Fallback to cl100k_base
        encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))

def main():
    if len(sys.argv) < 2:
        print("Usage: python token-counter.py <path_to_markdown_file>")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(json.dumps({"error": f"File {file_path} not found."}, indent=2))
        sys.exit(1)

    content = file_path.read_text(encoding='utf-8')
    tokens = count_tokens(content)
    
    print(json.dumps({
        "file": str(file_path.name),
        "tokens": tokens,
        "model_encoding": "cl100k_base"
    }, indent=2))

if __name__ == "__main__":
    main()
