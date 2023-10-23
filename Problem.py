l = 0
m = 0
p = 0
for i in range(3):
    print("enter the name of the customer n'",i+1,":")
    a = input()
    n = int(input("enter the number of items : "))
    for j in range(n):
        print("Give the price of the item n'",j+1,":")
        b = float(input())
        if i == 0 :
            x = a
            c = b + b * 0.15 - b * 0.02
            l += c
        if i == 1 :
            d = b + b * 0.15 - b * 0.02
            m += d
            y = a
        if i == 2 :
            e = b + b * 0.15 - b * 0.02
            p += e
            z = a
print("The Total to be paid for the customer",x,":",l,"DH")
print("The Total to be paid for the customer",y,":",m,"DH")
print("The Total to be paid for the customer",z,":",p,"DH")