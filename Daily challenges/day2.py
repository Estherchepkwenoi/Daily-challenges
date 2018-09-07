def my_Vowels():
    Vowels=["a","e","i","o","u"]
    letter=input("Enter a string:")
    dup_x=set(letter)
    dup_x=len(letter)-len(dup_x)
    count=0
    vowl=""
    for i in Vowels:
        for i in letter:
            count+=i
            print((vowl,count))
my_Vowels()            
        


            
            
            
