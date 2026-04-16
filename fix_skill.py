import subprocess
import os

# Read correct UTF-8 content from workspace
workspace_file = r"C:\Users\hp\.openclaw\workspace\skills\math-course-manager\SKILL.md"
with open(workspace_file, "rb") as f:
    content_bytes = f.read()

# Write to a clean temp file
temp_file = r"C:\Users\hp\xiaochong-math\temp_clean_skill.md"
with open(temp_file, "wb") as f:
    f.write(content_bytes)

# Create blob and get SHA
repo = r"C:\Users\hp\xiaochong-math"
result = subprocess.run(
    ["git", "hash-object", "-w", temp_file],
    cwd=repo, capture_output=True, text=False
)
blob_sha = result.stdout.strip().decode("ascii")
print(f"Blob SHA: {blob_sha}")

# Update index
index_entry = f"100644 {blob_sha} 0\t.skills/math-course-manager/SKILL.md\n"
proc = subprocess.Popen(
    ["git", "update-index", "--index-info"],
    cwd=repo, stdin=subprocess.PIPE
)
proc.communicate(index_entry.encode("ascii"))
print(f"Index updated with exit code: {proc.returncode}")

# Cleanup
os.remove(temp_file)

# Commit and push
subprocess.run(["git", "commit", "-m", "fix: correct UTF-8 encoding for SKILL.md via clean blob"], cwd=repo)
subprocess.run(["git", "push"], cwd=repo)
print("Done")
