import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
	if w in data:
		return data[w]
	elif len(get_close_matches(w,data.keys()))>0:
		yn= input("Did you mean %s instead? Type Y for Yes or type N for No. " % get_close_matches(w,data.keys())[0])
		if yn == 'Y':
			return data[get_close_matches(w,data.keys())[0]]
		elif yn == 'N':
			return "The word does not exist"
		else:
			return "We do not understand your query."
	else:
		return "The word does not exist please double check it."

word = input("Enter the word: ").lower()

output = translate(word)

if type(output) == list:
	for item in output:
		print(item)
else:
	print(output)