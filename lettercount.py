from sys import argv

script, file_name = argv
txt = open(file_name)
filetext = txt.read()
txt.close()

filetext.lower()

alphabet = [0] * 26

for char in filetext:
	if 97 <= ord(char) <= 122:
		alphabet[ord(char)-97] += 1

for item in alphabet:
	print item