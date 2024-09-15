import re

# Sample text containing email addresses
text = """
Hello, you can contact us at support@example.com or sales@example.co.uk.
You can also reach out to john.doe123@work-email.com or jane_doe@company-inc.org for further assistance.
Invalid emails like test@com or @example.com should not be matched.
"""

# Define the regex pattern for a valid email
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Search for all matching email addresses in the text
matches = re.findall(pattern, text)

# Print the matches
if matches:
    print(f"Found {len(matches)} email addresses:")
    for match in matches:
        print(match)
else:
    print("No valid email addresses found.")
