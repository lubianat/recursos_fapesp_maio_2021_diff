with open("text.txt", "r") as f:
  text = f.read()

with open("text_lower.txt", "w") as f:
  text_lower = text.lower()
  f.write(text_lower)