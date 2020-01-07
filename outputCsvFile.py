import csv

a = "What's you name?"
b = "What's your company?"
c = "How old are you?"
info1 = [a,b,c]

def create(x,y,z):
    with open(x,y) as f:
        w = csv.writer(f, delimiter=",")
        w.writerow(z)
        
create("../Desktop/info.csv","w",info1)

for i in range(1,5):
    a1= input("What's you name: ")
    b1= input("What's your company: ") 
    c1= input("How old are you: ")
    info2 = [a1,b1,c1]
    create("../Desktop/info.csv","a",info2)

