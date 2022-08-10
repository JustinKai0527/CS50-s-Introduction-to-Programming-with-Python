import validators

if validators.email(input("What's your email address? ")):
    print("Valid")
else:
    print("Invalid")

import re

email = input("What's your email address? ").strip()

if matches := re.search("^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]\
                        {0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$",
                        email, re.IGNORECASE)

    print("Valid")
else:
    print("Invalid")