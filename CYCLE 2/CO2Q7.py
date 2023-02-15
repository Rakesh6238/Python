string=input("enter the string:")
if string.endswith('ing'):
    string+='ly'
elif len(string)>=1:
    string+='ing'
print(string)    