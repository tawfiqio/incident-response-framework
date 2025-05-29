import os
import time

def analyze_disk(file_path):
    metadata = {
        "Filename": os.path.basename(file_path),
        "Size": os.path.getsize(file_path),
        "Last Modified": time.ctime(os.path.getmtime(file_path))
    }

    print(f"🕵️ Disk Forensics - Metadata:\n{metadata}")

if __name__ == "__main__":
    analyze_disk("/path/to/suspicious_file.img")
