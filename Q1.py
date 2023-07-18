"""
Q. I got 9 friends made visiting 73 cities over 2 countries, when I was 18 years old 3 years ago and 
that time the year was 2017.
Output: ["9","73","2","18","3","2017"]
"""


abs = "I got 9 friends made visiting 73 cities over 2 countries, when I was 18 years old 3 years ago and that time the year was 2017"
a = []
text = ""

for num in abs:
    if (num.isdigit()):
        text += num
    if num == " " and text:
         a.append(text)
         text = ""
         
if text:
 a.append(text)
print(a) 

# Another method
print(list(filter(lambda x : x[0].isdigit(), abs.split()))) 


# Another method: Regular Expressions
import re

# find all that satisfies the regex in 'a' string
a = re.findall('\d+', str(a))
print(a)

