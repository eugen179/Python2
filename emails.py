import re

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
text = "You can contact me at maisheugene@gmail.com or support@example.com anytime."
emails = re.findall(email_pattern, text)
print("Extracted emails:", emails)
match = re.match(email_pattern, text)
if match:
    print("Match found at the beginning:", match.group())
else:
    print("No match at the beginning.")
search = re.search(email_pattern, text)
if search:
    print("Search found an email:", search.group())
else:
    print("No email found in the string.")
