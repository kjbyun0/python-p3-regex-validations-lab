import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"([A-Z][a-z]*[\s\-\'])*[A-Z][a-z]*"
name_regex = re.compile(name)

phone_number = r"((([\(]?[0-9]{3,4}[\)]\s?)|([0-9]{3,4}[\-]))[0-9]{3,4}[\-][0-9]{4})|([0-9]{10,12})"
phone_regex = re.compile(phone_number)

email_address = r"[A-Za-z]+[A-Za-z0-9]*\.?[A-Za-z0-9]+@[A-Za-z_\-]+\.[A-Za-z]{2,3}"
email_regex = re.compile(email_address)
