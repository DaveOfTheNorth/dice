from random import randint
x = input()
z=0
for i in range(100):
    y = (randint(1,6))
    print(y)
    if y==x:
        z+=1
    print(z)
        
print(x,"rolled",z/100,"% of the time.")
        
