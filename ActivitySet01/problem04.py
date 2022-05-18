# Conditional Execution

hrs = input("Enter Hours:")
h = float(hrs)
rate=input("enter rate:")
r=float(rate)

if h>40 :
    
    hnr=40*r
    hmr=1.5*(h-40)*r
    
    hsr=hmr+hnr
    
    print( hsr)    

else :


 rmh=h*r

 print( rmh)
 


