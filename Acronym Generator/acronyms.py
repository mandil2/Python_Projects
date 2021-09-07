import os
os.system('cls')

userInput= input('Enter a phrase: ')
words=userInput.split()
acronym=''
noAcronym=['of','in','by','and','to']
for word in words:
    if word not in noAcronym:
        acronym+=word[0].upper()
print('The acronym of the given phrase is:',acronym)