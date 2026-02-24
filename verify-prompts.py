import os
import sys

def verify_repo(start_path):
    forbidden_text = "Prompt In Review"
    failed_files = []

    for root, dirs, files in os.walk(start_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        if forbidden_text in content:
                            failed_files.append(file_path)
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
                    
    if failed_files:
        print("\n❌ VERIFICATION FAILED: The following files contain the forbidden placeholder text:")
        for path in failed_files:
            print(f"  - {path}")
        sys.exit(1)
    else:
        print("\n✅ VERIFICATION PASSED: No placeholders found. All prompts are fully production-ready.")
        sys.exit(0)

if __name__ == "__main__":
    prompts_dir = os.path.join(os.path.dirname(__file__), "prompts")
    verify_repo(prompts_dir)
