import re

numbers = '1422 11422-7903 11598 11678787 11678-23 11723 11898-111 22222222-6666 14567-999999 11111-2222'

regex = re.compile(r"(\b\d{5}-\d{4}\b|\b\d{5}\b\s)")

matches = re.findall(regex, numbers)

for i in matches:
    print(i)

