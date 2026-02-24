import os
import requests
import json

REPO_URL = "https://api.github.com/repos/x1xhlol/system-prompts-and-models-of-ai-tools/contents"
PROMPTS_DIR = os.path.join(os.path.dirname(__file__), "prompts")


def download_file(github_url, local_path):
    print(f"Downloading {github_url} -> {local_path}")
    response = requests.get(github_url)
    if response.status_code == 200:
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        with open(local_path, "wb") as f:
            f.write(response.content)
    else:
        print(f"Failed to download {github_url}")

def crawl_repo(path=""):
    url = f"{REPO_URL}/{path}"
    response = requests.get(url)
    if response.status_code == 200:
        items = response.json()
        for item in items:
            # We skip assets/dia/v0/open source/github files to focus strictly on tools
            if path == "" and item["name"] in [".github", "assets", "README.md", "README_ZH.md", "LICENSE.md", "Open Source prompts", "dia", "v0 Prompts and Tools"]:
                continue
            
            if item["type"] == "dir":
                crawl_repo(item["path"])
            elif item["type"] == "file":
                # Ensure it goes into our prompts directory
                if path != "":
                    # Fix mapping differences based on our scaffold
                    local_dir = path
                    if local_dir == "Cursor Prompts":
                         local_dir = "Cursor"
                    local_path = os.path.join(PROMPTS_DIR, local_dir, getattr(item, 'name', item['name']))
                    download_file(item["download_url"], local_path)

if __name__ == "__main__":
    print("Starting download of actual prompt files...")
    crawl_repo()
    print("Done!")
