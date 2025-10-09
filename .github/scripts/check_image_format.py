import sys
import re
import os

def is_image_format(text):
    # Regular expression pattern to match the specified image formats
    pattern = re.compile(r'^\s*([a-zA-Z0-9\*._-]+/[a-zA-Z0-9\*._-]+:[a-zA-Z0-9\*._-]+|[a-zA-Z0-9\*._-]+/[a-zA-Z0-9\*._-]+/[a-zA-Z0-9\*._-]+:[a-zA-Z0-9\*._-]+|[a-zA-Z0-9\*._-]+:[a-zA-Z0-9\*._-]+)\s*$', re.MULTILINE)
    lines = text.strip().split('\n')
    for line in lines:
        if not pattern.match(line):
            return False
    return True

def main():
    body = sys.argv[1]
    result = is_image_format(body)
    
    # Use GITHUB_OUTPUT environment file instead of deprecated set-output
    github_output = os.getenv('GITHUB_OUTPUT')
    if github_output:
        with open(github_output, 'a') as f:
            f.write(f"is_image_format={str(result).lower()}\n")
    else:
        # Fallback for local testing
        print(f"::set-output name=is_image_format::{str(result).lower()}")

if __name__ == "__main__":
    main()
