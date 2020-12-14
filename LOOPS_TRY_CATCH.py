largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    try :
        num = float(num)
        for i in num :
            if num > largest :
                largest = num


        for k in num :
            if smallest < num :
               smallest = num


    except:
        print('invalid input')
    if num == "done" : break
    print(num)

print("Maximum", largest)
print("Minimum", smallest)
