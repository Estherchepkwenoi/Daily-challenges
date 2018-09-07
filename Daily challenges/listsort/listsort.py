def mylist():
    list_sort=[2,0,6,5,1,7,'z','a']
    list_of_even=[]
    list_of_odd=[]
    list_of_char=[]
    list_of_other=[]
    dict_B={}
    for k in list_sort:
        if isinstance(k,int):
            if(k%2==0):
                list_of_even.append(k)
            else:
                list_of_odd.append(k)
        elif isinstance(k,char):
            list_of_char.append(k)
        else:
            list_of_other.append(k)
    dict_B["evens"]=list.sort(list_of_even)
    dict_B["odds"]=list.sort(list_of_odd)
    dict_B["chars"]=list.sort(list_of_char)
    dict_B["others"]=list.sort(list_of_others)
    print(dict_B)

list_sort


            
