import os
import hashlib

def detect_ransomware(file_path):
    original_hash = hashlib.md5(open(file_path, "rb").read()).hexdigest()
    
    print(f"🔍 Monitoring {file_path} for ransomware activity...")
    
    while True:
        current_hash = hashlib.md5(open(file_path, "rb").read()).hexdigest()
        if current_hash != original_hash:
            print(f"🚨 File {file_path} has been modified! Possible encryption attack detected!")
            break

if __name__ == "__main__":
    detect_ransomware("important_document.txt")
