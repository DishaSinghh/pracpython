import pickle
f=open("binary.dat",'ab')
l=[]
while True:
    rno=input("enter rno ")
    name=input("enter name")
    r=[rno,name]
    l.append(r)
    ask=input("do you want to enter more values")
    if ask=="no":
        break
pickle.dump(l,f)
f.close()
