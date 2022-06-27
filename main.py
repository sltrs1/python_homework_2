import re
from typing import Collection, Counter

# ----------------------------------------

temps = []
flag = 0
t = 0
while flag == 0:
    inp = input("Enter temperature: ")
    if inp.isdigit():
        temps.append( float(inp) )
    else:
        if inp == "":
            flag = 1

if len(temps) == 0:
    print("No data")
else:
    print("Average temperature is ", (sum(temps)/len(temps)) )

# ----------------------------------------

phrase = input("Enter sentence: ")
phrase_replacred = phrase.replace("o", "*")
print(phrase_replacred)

# ----------------------------------------

spec_symbols = "@#$%^&*_=+~<>"
text = """Жили у бабуси два веселых гуся,
Один - серый, другой - белый,
Два веселых гуся,
Один - серый, другой - белый,
Два веселых гуся!"""

print(text)

text_lower = text.lower()
text_form = re.split(' |, |\n|-|!|,', text_lower)

while "" in text_form: text_form.remove("")

print(text_form)

coll = Counter(text_form)

print(coll)

iter_text = text_lower[:]

max_s = len(spec_symbols)

if max_s < len(coll):
    print("Too much words, only", max_s, "will be replaced")

i = 0
for key in coll:
    if i >= max_s:
        break
    if coll[key] > 1:
        iter_text = iter_text.replace(key, spec_symbols[i]*len(key))
        i += 1

print(iter_text)