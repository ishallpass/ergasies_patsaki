#python3.8
x=str(input("dose lexh: "))
z=""
for i in x:
      z=z+(str(ord(i)))#turns it to binary
print ("ascii code dex:",z)
z=int(z)
if z>1:
      for i in range(2,z):
            if (z % i) == 0:#checks if its a prime or not
                  print(z,"is not a prime number")
                  break
      else:
            print (z,"is a prime number")
