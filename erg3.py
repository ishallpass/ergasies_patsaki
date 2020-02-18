#python_3.8
def func():
      a=[];b=[];z=0;s=0;q=0
      c=0;t=0
      prcl={}
      prdctl={}
      x=int(input("dose 1 gia na eisageis tis thmes dose otidipote allo arithmo gia na stamatiseis"))
      while x==1:
            p=str(input("dose proion: "))
            t=input('dose timh proiodos": ')
            prdctl.update({p:str(c)})
            prcl.update({t:str(c)})
            c+=1
            x=int(input("dose 1 gia na eisageis tis thmes dose otidipote allo arithmo gia na stamatiseis"))
            for i in prcl:
                  a.append(i)
            for i in a:
                  b.append(float(i))
      s=sum(map(float,b))
      t=s*0.24
      z=t+s
      print ("foros",t,"timh",s,"synolo",z)
func()
