'''
 . (any character)
 ^ $ (start, end)
 * (0 or more)
 + (1 or more)
 ? (0 or 1)
 {and}
'''

import re

pattern = "col..r"
if re.match(pattern, "colour") :
    print("matched for .")

pattern = "^col..r$"
if re.match(pattern, "colour") :
    print("matched for ^ abd $")

pattern = "a*"
if re.match(pattern, "colour") :
    print("matched for *")

pattern = "a+"
if re.match(pattern, "aolour") :
    print("matched for +")

pattern = "a+b"
if re.match(pattern, "aaabolour") :
    print("matched for +")

pattern = "ice(-)?cream"
if re.match(pattern, "icecream") :
    print("matched for ?")

pattern = "ice(-)?cream"
if re.match(pattern, "ice-cream") :
    print("matched for ?")

pattern = "a{1,3}$"
if re.match(pattern, "aa") :
    print("matched for {}")

pattern = "a{1,3}$"
if re.match(pattern, "aagfgfgd") :
    print("matched for {}")