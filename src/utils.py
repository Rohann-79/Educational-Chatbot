import re

def clean_text(text):
    return re.sub(r"[^a-zA-Z0-9\s]", "", text.lower())

if __name__ == "__main__":
    print(clean_text("Hello! How are you?"))
