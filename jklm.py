import pyperclip

import mouse
import time
import keyboard
from keyboard import press
import random


def typeIt(word):
    '''
    Moves cursor to box and types word with random speeds
    '''
    global words
    mouse.move(300, 1080)
    mouse.click('left')
    time.sleep(1)
    print(word)
    for letter in word:
        keyboard.press(letter)
        time.sleep(random.randrange(1, 20)/125)
    keyboard.press('enter')
    #print(f'word {word}')
    words.remove(word)
    mouse.move(1250, 1000)
    mouse.click('left')

def chooseBest(validWords):
    '''
    Returns best guess from validWords
    '''
    global alphabetCopy
    bestWords = {word.strip():0 for word in validWords}

    for word in bestWords:
        wordLetters = removeDupes(word)
        for letter in wordLetters:
            if letter in alphabetCopy:
                bestWords[word] += 1

    wordsSorted = sorted(bestWords.items(), key=lambda d: d[1])
    for i in range(1, len(wordsSorted)+1):
        try:
            #print(f'return val {(wordsSorted[-1][0], wordsSorted[-1 * i][1][1])}')
            return (wordsSorted[-1 * i][0])
        except:
            pass


def removeDupes(word):
    '''
    returns word but with removed duplicate letters
    '''
    letters = []
    for letter in word:
        if letter not in letters:
            letters.append(letter)
    return letters

pattern = input("Enter letters to be searched for: ")
alphabet = ['a' , 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabetCopy = alphabet.copy()

with open('words.csv', 'r') as words:
    
    # load all words and turn them lowercase
    words = words.read().splitlines()
    for i, word in enumerate(words):
        words[i] = word.lower()

    while (pattern != 'EXIT'):

        validWords = []
        for word in words:
            if pattern in word:
                validWords.append(word.lower())
        try:
            word  = chooseBest(validWords)
        except:
            print('No answer')
        typeIt(word)
        
        # remove used letters from alphabet copy
        for letter in word:
            if letter in alphabetCopy:
                alphabetCopy.remove(letter)
        
        # check if alphabet needs to be reset
        if len(alphabetCopy) == 0:
            alphabetCopy = alphabet.copy()

        pattern = input("Enter letters to be searched for: ")
