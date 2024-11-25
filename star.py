import re

text = "The quick brown fox jumps over the lazy dog"
pattern = r"qu.*k" 
matches = re.findall(pattern, text)
print(matches)  

