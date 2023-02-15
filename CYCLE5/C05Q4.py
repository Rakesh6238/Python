import pandas as pd
#df=pd.read_csv("Financial Sample.csv")
#print(df[["Segment","Country"]])
#print(df.tail())
#print(df.head())
#print(df)

#using usecols
df=pd.read_csv("studentdetails.csv",usecols=["Roll No","Student Name","CO1"])
print(df)