def computepay(h,r):
    if h =40:
        a= h * r
        return a
    if h >40:
        b= ((h-40) * (r*0.5)) + h * r
        return b


hrs = input("Enter Hours:")
rate=input("Enter rate:")
h=float(hrs)
r=float(rate)


p = computepay(h,r)
print("Pay",p)
