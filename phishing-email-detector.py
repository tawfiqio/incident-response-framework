import re

def detect_phishing(email_text):
    phishing_keywords = ["urgent", "verify your account", "limited-time offer", "click here"]
    
    for keyword in phishing_keywords:
        if re.search(keyword, email_text, re.IGNORECASE):
            print("🚨 Potential Phishing Attempt Detected!")
            return True
    
    print("✅ Email appears legitimate.")
    return False

if __name__ == "__main__":
    sample_email = "URGENT: Your account has been locked! Click here to verify."
    detect_phishing(sample_email)
