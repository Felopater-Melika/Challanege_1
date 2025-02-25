import re

with open('text.txt', 'r') as file:
    text = file.read()

phone_pattern = re.compile(r'\(?\d{3}\)?[ -.]?\d{3}[ -.]?\d{4}')
email_pattern = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")

phones = phone_pattern.findall(text)
emails = email_pattern.findall(text)

print("Phone Numbers:")
for phone in phones:
    print(phone)

print("\nEmail Addresses:")
for email in emails:
    print(email)
