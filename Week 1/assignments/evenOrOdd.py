num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")
if num < 2:
    print("The number is Not Prime")
else:
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print("The number is Prime")
    else:
        print("The number is Not Prime")