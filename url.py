import re
url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
text = "Visit our website at https://www.netflix.com or https://www.hulu.com for more information."
urls = re.findall(url_pattern, text)
print("Extracted URLs:", urls)
