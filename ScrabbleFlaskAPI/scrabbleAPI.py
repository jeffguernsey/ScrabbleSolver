from flask import Flask, jsonify
import os
import json
#Custom Trie class
from DictionaryTrie import Trie 

def populateTrie(MainTrie):
    #Use a relative path to retrieve our dictionary
    CWD = os.getcwd()
    assetPath = os.path.relpath('Assets\\engmix.txt', CWD)
    file = open(assetPath,"r",errors='ignore')

    #Setup the Trie as well as a dictionary of lower case letters
    letterInAlphabet = 'abcdefghijklmnopqrstuvwxyz'
    Alphabet = {}
    for letter in letterInAlphabet:
        Alphabet[letter] = True

    #For each word in the file insert it into the trie if it only consists of letters
    for word in file:
        flag = False
        for letter in word.lower().strip():
            if letter not in Alphabet:
                flag = True
                break
        if flag:
            continue

        MainTrie.insert(word.lower().strip())

    return MainTrie

def setUpTrie():
    #Setup up our Trie and populate it with the contents of the dictionary
    MainTrie = Trie("")

    populateTrie(MainTrie)

    return MainTrie


def stringBucketSort(words):
    equalLengthStrings = {}
    for word in words:
        if len(word) in equalLengthStrings:
            equalLengthStrings[len(word)].append(word)
        else:
            equalLengthStrings[len(word)] = [word]

    stringsSortedByLength = []
    for key in equalLengthStrings.keys():
        stringsSortedByLength.append(equalLengthStrings[key])
    return stringsSortedByLength


from flask import Flask

app = Flask(__name__)

#Initializes our Trie with a version of the english dictionary
scrabbleTrie = setUpTrie()

#Binds the get_task function to the http GET method
@app.route('/scrabbleSolver/api/<string:letters>', methods=['GET'])
def get_task(letters):
    wordList = {}
    found = {}
    #Get all words that can be built using letters
    scrabbleTrie.getAllConstrainedWords(2,20,sorted(list(letters)),wordList,found)
    #bucket sort the words by length
    stringsSortedByLength = stringBucketSort(list(wordList.keys()))
    #Return our array of arrays sorted by item length, largest words first
    print(stringsSortedByLength)
    return jsonify(sorted(stringsSortedByLength,key = lambda x: -len(x[0])))


if __name__ == '__main__':
    app.run(debug=True)