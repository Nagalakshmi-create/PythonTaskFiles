import re
text=open("/home/neosoft/Downloads/read.txt",'r')
x=text.read()

vowels=['a','e','i','o','u']

count_vowels=0

for i in x.lower():
    if i in vowels:
        count_vowels+=1

print(count_vowels)

words=[]
words_dict={}
y = re.sub("[^a-zA-Z]"," ",x.lower())
z=y.split(" ")
print(z)
for i in y.split(" "):
    if i == "":
        words_dict = words_dict
    else:
        words.append(i)

    words_dict[i]=words.count(i)

print(words_dict)