word=dict()
text=input("enter the text")
words=text.split(" ")
for i in words:
    if i in word:
        word[i]+=1
    else:
        word[i]=1
print(word)
