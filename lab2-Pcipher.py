#!/usr/bin/python3
#Roshan Shah
#Lab 2 Crypto 100

#importing numpy function.
#It provides a high-performance multidimensional array object, and tools for working with the arrays.
import numpy as np 

#initiating our word variable that will be encrypted
word = "MARYHADALITTLELAMB"

#provide a key word used to encrypt and change it to a list of its alphabets
key="STUDENT"
key = list(key)

#this function from numpy returns the indices that would sort alphabets in our key
sortkey = np.argsort(key)
print (sortkey)

#initialize a loop that runs until the length of the word to be encrypted
#increment of i will be the lenght of the key
#slice the word into pieces that is equal to the lenght of the key
#if the length of slice is less than the lenght of key, then add "X"s to make it equal to the lenght of the key
for i in range(0, len(word), len(key)): 
   wordslice = word[i:i+len(key)]
   if (len(wordslice) == len(key)):
      print (wordslice)
   elif (len(wordslice) < len(key)):
      wordslice += "X" * (len(key)-len(wordslice))
      print (wordslice)

#initiaze a variable to store encrypted text
#take letters in individual word slices and move it to corresponsing indices derived from the argsort() function above
#output the scrambled letters(encrypted)     
   encrypt_word=""
   for num in sortkey:
      encrypt_word += wordslice[num]
   print(encrypt_word)   



