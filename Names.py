

import re

name1 = "Karen.Zepeda"

name2 = "Kevin.Meyer"

def firstLast(fullName):
	match  =  re.search("(.+)\.(.+)",fullName)
	if match:
		print("First: "+match.group(1))
		print("Last: "+match.group(2))

firstLast(name1)

firstLast(name2)