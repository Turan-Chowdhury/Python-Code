import re

pattern = "color"
text = "Red is a color, i love red color"

if re.match(pattern, text) :
    print("Match")
else :
    print("Not matched")

if re.search(pattern, text) :
    print("Match")
else :
    print("Not matched")

match = re.search(pattern, text)
if match :
    print(match.start())
    print(match.end())
    print(match.span())

print(re.findall(pattern, text))

print(re.sub(pattern, "colour", text, count=1))

