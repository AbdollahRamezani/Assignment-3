while True:
    def kmm(x,y):
            n=z=0
            j=abs(x*y)+1

            if abs(x)>abs(y):
               n=abs(x)
            else:
                abs(y)
            for i in range (n,j):
                if i%x ==0 and  i%y ==0  :
                 z=i
                 break        
            return(z)   
    x=int(input("Enter Number 1 :  ")    ) 
    y=int(input("Enter Number 2 : ")    ) 
    Result=kmm(x,y)
    print("KMM: ",Result)       