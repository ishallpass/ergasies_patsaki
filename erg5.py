#python3.8
a=" "#random string 
f=open("paragraph.txt","r")
z="" 
dnlist=[] #final list
words=""# the list for the file
words=f.read()
words=words.split()#break to list
for i in words: #simple array do the final tweaks and send it to the final list word per word
      l=len(i)
      if l>3:
            z=i[1:]+i[0:1]+"ay "
            dnlist.append(z)
print (dnlist)
f.close
            
