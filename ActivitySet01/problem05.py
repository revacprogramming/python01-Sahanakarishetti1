# Functions


def computepay(h, r):
    return(h,r)


h = float(input("Enter hours? "))
r = float(input("Enter rate per hour? "))

p = computepay(h, r)
if h>40:
  n=40*r
  e=(h-40)*1.5*r
  p=n+e
else:
  p=h*r
print("Pay", p)
