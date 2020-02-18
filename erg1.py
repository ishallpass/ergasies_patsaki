#python 3.8.1
vowels=["a" , 'e' , 'i' , 'u' ,'y','o']
big_words=[]#lista me ths megaliteres lexis
dnlist=[]
words_txt=" "#lista me lexhs tou arxeiou
f=open("paragraph.txt","r")
words_txt = f.read()#diavazei
words_txt= words_txt.split()#kanei split
l=len(words_txt)
for i in range (0,l,1):#bubblesort
      for j in range(0,l-i-1 ):
            if len(words_txt[j])<len(words_txt[j+1]):
                  words_txt[j],words_txt[j+1]=words_txt[j+1],words_txt[j]
top5=words_txt[0:5]
table = str.maketrans(dict.fromkeys('aeiuyoAEOIUY'))
for i in top5:
      z=i.translate(table)
      dnlist.append(z)
top5.clear()
for i in dnlist:
      top5.append(i[::-1])
for i in top5:
      print (i)
f.close()
