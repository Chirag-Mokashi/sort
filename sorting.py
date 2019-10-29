
#def sort(list):                          #bubble sort
 #   for i in range(0,len(list),+1):
 #       for j in range(len(list)-1):
   #         if list[j]>list[j+1]:
    #            temp=list[j]
     #           list[j]=list[j+1]
      #          list[j+1]=temp

def sort(list):                    #selection sort
    for i in range(0,len(list)-1-1,1):
        a=i
        for j in  range(i+1,len(list)-1,1):
            if list[a]>list[j]:
                temp=list[a]
                list[a]=list[j]
                list[j]=temp


list=[5,8,9,1,2,7]
sort(list)
print(list)







