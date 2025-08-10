import hashlib

def calculate_hash(file_path):
    """Calculate SHA256 hash of a file."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        return None
    except PermissionError:
        print(f"[ERROR] Permission denied: {file_path}")
        return None

# Get file paths from user
file1 = input("Enter path of original file: ").strip('"')
file2 = input("Enter path of file to compare: ").strip('"')

# Calculate hashes
hash1 = calculate_hash(file1)
hash2 = calculate_hash(file2)

# Compare results
if hash1 and hash2:
    print(f"\nHash of Original File: {hash1}")
    print(f"Hash of Compared File: {hash2}")
    if hash1 == hash2:
        print("\n✅ Files are identical (no changes detected).")
    else:
        print("\n⚠️ Files are different (changes detected).")
