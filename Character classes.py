import re

pattern = "[aeiou]"
if re.match(pattern, "edfifd") :
    print("matched 1")

pattern = "[a-z]"
if re.match(pattern, "gdfifd") :
    print("matched 2")

pattern = "[A-Z][a-z][0-9]"
if re.match(pattern, "Ka8edfifd") :
    print("matched 3")