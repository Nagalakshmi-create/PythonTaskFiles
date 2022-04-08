#read any text file from current directory try to find vowels from it as well as print occurances of all words in a dictionary

import re

text=open("/home/neosoft/Documents/PythonFiles/textfile.txt",'r')
x=text.read()

vowels=['a','e','i','o','u']

count_vowels=0

for i in x.lower():
    if i in vowels:
        count_vowels+=1

print(count_vowels)

words=[]
words_dict={}

y = re.sub("[.,']", "" , x.lower())

for i in y.split():
    if i == "":
        pass
    else:
        words.append(i)

    words_dict[i]=words.count(i)

print(words_dict)