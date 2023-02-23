cy=int(input("enter the current year"))
fy=int(input("enter the final year"))
for i in range(cy,fy):
    if i%4==0 and i%100!=0:
        print(i)
    elif i%100==0 and i%400==0:
        print(i)
        