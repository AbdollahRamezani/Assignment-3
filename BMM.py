while True:
    def bmm(x,y):
            n=z=0
            if abs(x)>abs(y):
               n=abs(x)
            else:
                abs(y)
            for i in range (1,n+1):
                if abs(x)%i ==0 and  abs(y)%i ==0  :
                    z=i
            return(z)   
    x=int(input("Enter Number 1 :  ")    ) 
    y=int(input("Enter Number 2 : ")    ) 
    Result=bmm(x,y)
    print("BMM: ",Result)       