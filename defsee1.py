Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def see1(word,phrase):
	splitPhrase=phrase.split(" ")
	numOfWord=splitPhrase.count(word)
	return numOfWord
print(see1("sloths", "i love sloths because sloths are cool"))
SyntaxError: invalid syntax
>>> SyntaxError: invalid syntax
SyntaxError: invalid syntax
>>> def see1(word,phrase):
	splitPhrase=phrase.split(" ")
	numOfWord=splitPhrase.count(word)
	return numOfWord

>>> print(see1("sloths", "i love sloths because sloths are cool"))
2
>>> 