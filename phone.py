import re
phone_number_regex = r"(\+254|0)?(7[0-9]{8})"
text = "Call me at 0712345678 or 0723456789 or 0734567890"
matches = re.findall(phone_number_regex, text)
for match in matches:
    print(match[1]) 