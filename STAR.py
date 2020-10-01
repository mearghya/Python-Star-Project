print("enter the number\n")
i=int(input())
print("enter the boolean number '0' or '1'\n")
z=int(input())
u=bool(z)
a=0
while 1:
    if u is False:
        while a<i:
            print((i-a)*"*")
            break
        a=a+1
    else:
        while a<i:
            print((a+1)*"*")
            break
        a=a+1
print("Thanks\n")
print("Is this helpful?")
input()
