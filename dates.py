import re
date_regex = r"\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2}|\d{2} \w+ \d{4}"
text = "The meeting is on 12/31/2023 or 2024-11-21 or 21 November 2024"
matches = re.findall(date_regex, text)
for match in matches:
    print(match)