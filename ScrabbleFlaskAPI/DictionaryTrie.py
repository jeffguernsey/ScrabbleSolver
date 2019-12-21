import os
import sys
import random
class Trie:
	#Initialize class variable
	def __init__(self,letter):
		self.isWord = False #Flag that represents whether or not we have arrived at a complete word
		self.letter = letter #letter represented by this node of the Trie
		self.nextLetters  = {}#Using a dictionary is actually less memory than using 26 size arrays

	def containsWord(self,word):
		if not word and self.isWord:
			return True
		elif not word:
			return False
		if word[0] in self.nextLetters:
			return self.nextLetters[word[0]].containsWord(word[1:])
		else:
			return False

	def insertLetter(self,letter):
		self.nextLetters[letter] = Trie(letter)
		return True

	def hasNextLetter(self,letter):
		return letter in self.nextLetters

	def setAsWord(self):
		self.isWord = True

	def insert(self,word):
		if word == "":
			self.setAsWord()
			return True
		if word[0] not  in self.nextLetters:
			self.insertLetter(word[0])
		self.nextLetters[word[0]].insert(word[1:])
		return True

	def sizeInBytes(self):
		currentObjectSize = sys.getsizeof(self.isWord) + sys.getsizeof(self.letter) + sys.getsizeof(self.nextLetters)
		for node in self.nextLetters.values():
			currentObjectSize += node.sizeInMB()
		return currentObjectSize

	def getRandomWord(self,length,word = ""):
		currentWord = word + self.letter
		if len(currentWord) == length:
			if self.isWord == True:
				return currentWord,True
			else:
				return word,False

		#Shuffle possible next letters
		#This allows us to randomly choose the next point
		#Since we are guaranteed a word down each path this does not incur an O(n) penalty
		arr = list(self.nextLetters.values())
		random.shuffle(arr)
		if not arr:
			return "",False
		for node in arr:
			answer,found = node.getRandomWord(length,currentWord)
			if found == True:
				return answer, True
		return "",False
		
	def getRandomConstrainedWord(self,length,letters,word = ''):
		currentWord = word + self.letter
		if len(currentWord) == length:
			if self.isWord == True:
				return currentWord,True
			else:
				return word,False
		#Shuffle possible next letters
		#This allows us to randomly choose the next point
		#Since we are guaranteed a word down each path this does not incur an O(n) penalty
		random.shuffle(letters)

		for i in range(len(letters)):
			if letters[i] not in self.nextLetters:
				continue
			answer,found = self.nextLetters[letters[i]].getRandomConstrainedWord(length,letters[:i] + letters[i+1:],currentWord)
			if found == True:
				return answer, True
		return "",False

	def getAllConstrainedWords(self,minLength,maxLength,letters,wordList,found,word = '' ):
		#This function returns all words that can be made using the provided letters that have a length between the min and max length
		currentWord = word + self.letter
		if currentWord in found:
			return
		found[currentWord] = True
		if len(currentWord) >= minLength and len(currentWord) <= maxLength:
			if self.isWord == True:
				wordList[currentWord] = True

		for i in range(len(letters)):
			if letters[i] not in self.nextLetters:
				continue
			self.nextLetters[letters[i]].getAllConstrainedWords(minLength,maxLength,letters[:i] + letters[i+1:],wordList,found,currentWord)
