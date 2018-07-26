for n in range(1,1000):
    if(n % 3 == 0):
        if (n % 5 == 0):
            sum = sum + n
        else:
            sum = sum + n
    elif(n % 5 == 0):
        sum = sum + n
    else:
        sum = sum
    
        
print(sum)

       