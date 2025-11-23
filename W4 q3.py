n = 2
p = int(input("enter your no."))
t = n ** p - 1
if t > 1:
 for i in range (2,t):
     if t % i == 0:
        print("no. is not prime",t)
        break
 else:
        print("no. is prime",t)
else:
    print("no.is not prime",t)
