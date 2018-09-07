def fizzbuzz(A,B):
    A=[]
    B=[]
    A=input("Enter listA")
    B=input("Enter listB")

    C=len(A)+len(B)
    if (C%3==0):
        print("fizz")
    elif(C%5==0):
        print("buzz")
    elif(C%3==0 and C%5==0):
        print("fizzbuzz")
    else:
        print("fizzbuzz")
fizzbuzz(A,B)        


    