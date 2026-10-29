import re

# Sample text containing email addresses
text = """
Contact us at sanika@gmail.com, student123@yahoo.com,
admin@college.edu and support@example.org.
"""

# Regular expression to find email addresses
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Find all email addresses
emails = re.findall(pattern, text)

# Display the results
print("Email addresses found:")
for email in emails:
    print(email)