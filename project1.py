#WAP to print the second largest number in a given list
a=int(input('Enter number of terms:'))
list1=[]
for i in range(a):
    no=eval(input('Enter the number:'))
    list1.append(no)
mx=max(list1[0],list1[1])
secondmax=min(list1[0],list1[1])
n=len(list1)
for i in range(2,n):
    if list1[i]>mx:
        secondmax=mx
        mx=list1[i]
    elif list1[i]<mx:
        if list1[i]>secondmax:
            secondmax=list1[i]
print(secondmax)


        
    






    









        
    
    
    
    

    
    
    
    
 
