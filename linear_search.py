def linear_search(myList,item):
    for i in range(len(myList)):
        if myList[i]==item:
            return i
    return None

myList = [1,7,6,5,8]
print("Element in List :", myList)
chosen = int(input("enter searching element:"))

result = linear_search(myList,chosen)
if result== None:
     print("Element not found in the list")
else:
     print( "Element " + str(chosen) + " is found at position %d" %(result))
