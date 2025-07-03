import json

file_path = "logicspice_chunks.jsonl"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, 1):
            if line.strip():
                try:
                    item = json.loads(line)
                    if not isinstance(item, dict):
                        print(f"Error at line {line_number}: Not a dictionary: {line.strip()}")
                    elif "content" not in item:
                        print(f"Error at line {line_number}: Missing 'content' key: {line.strip()}")
                    else:
                        print(f"Line {line_number}: Valid chunk with content: {item['content'][:50]}...")
                except json.JSONDecodeError as e:
                    print(f"Error at line {line_number}: Invalid JSON: {line.strip()}. Error: {e}")
            else:
                print(f"Warning at line {line_number}: Empty line")
except FileNotFoundError:
    print(f"Error: File {file_path} not found.")
except Exception as e:
    print(f"Error reading file {file_path}: {e}")