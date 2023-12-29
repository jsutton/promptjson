import json
import sys
from jsonschema import validate
from jsonschema.exceptions import ValidationError

def load_json_file(file_path):
    """
    Load and return the JSON data from a file.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)
    except json.JSONDecodeError as jde:
        print(f"Invalid JSON format: {jde.msg}")
        sys.exit(1)

# Load PromptScript JSON Schema from external file
try:
    prompt_script_schema = load_json_file('schema/prompt_script_schema.json')
except Exception as e:
    print(f"Failed to load schema: {e}")
    sys.exit(1)

def validate_prompt_script(prompt_script_json):
    """
    Validate the given JSON data against the PromptScript schema.
    """
    try:
        validate(instance=prompt_script_json, schema=prompt_script_schema)
        print("Validation successful.")
    except ValidationError as ve:
        print(f"Validation error: {ve.message}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python promptscript_validator.py <file_to_validate>")
        sys.exit(2)
    file_to_validate = sys.argv[1]
    prompt_script_json = load_json_file(file_to_validate)
    validate_prompt_script(prompt_script_json)