from sys import argv

script, file_name = argv
txt = open(file_name)
filetext = txt.read()
txt.close()

alphabet = {}

for i in range(97,123):
	letter = chr(i)
	alphabet[letter] = 0

filetext.lower()

for char in filetext:
	if alphabet.get(char) != None:
		alphabet[char] += 1

for item in alphabet:
	print alphabet[item]