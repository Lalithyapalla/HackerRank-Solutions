import json
import os
import re
import subprocess

# Path to your extracted JSON file
json_file_path = "laali0625_data.json/laali0625_data.json"
if not os.path.exists(json_file_path):
    json_file_path = "laali0625_data.json"

with open(json_file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

submissions = data.get("submissions", [])
print(f"Found {len(submissions)} submissions. Re-indexing historical timeline...")

for sub in submissions:
    challenge = sub.get("challenge", "unknown_challenge")
    challenge_clean = re.sub(r'[\\/*?:"<>|!]', "", challenge).replace(" ", "_")
    
    language = sub.get("language", "text")
    code = sub.get("code", "")
    
    # Extract the original historical timestamp from HackerRank data
    # Safe fallback to today if date field is missing
    sub_date = sub.get("created_at", "") 
    
    ext_map = {
        "python": "py", "python3": "py", "pypy3": "py",
        "cpp": "cpp", "cpp14": "cpp", "c": "c",
        "java": "java", "java8": "java", "javascript": "js", "sql": "sql"
    }
    ext = ext_map.get(language.lower(), "txt")
    
    folder_name = language.upper().strip()
    os.makedirs(folder_name, exist_ok=True)
    
    file_path = os.path.join(folder_name, f"{challenge_clean}.{ext}")
    with open(file_path, "w", encoding="utf-8") as out_file:
        out_file.write(code)
        
    # If a valid submission timestamp exists, commit it using that date!
    if sub_date:
        try:
            # Stage the specific file
            subprocess.run(["git", "add", file_path], check=True)
            
            # Inject historical dates into Git environment variables
            env = os.environ.copy()
            env["GIT_AUTHOR_DATE"] = sub_date
            env["GIT_COMMITTER_DATE"] = sub_date
            
            commit_msg = f"Solve {challenge} (Historical Sync)"
            subprocess.run(["git", "commit", "-m", commit_msg], env=env, check=True, stdout=subprocess.DEVNULL)
        except Exception as e:
            pass

print("🎉 Local timeline rebuilt with historical dates!")