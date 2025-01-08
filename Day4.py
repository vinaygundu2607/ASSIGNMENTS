n=int(input("Enter n value:"))

sum=0
for i in range(2,n+1,2):
    sum += i
print("Sum of N even form 1 to ",n,":",sum)


#using method as second method
def sum_of_even(n):
    sum=0
    for i in range(2,n+1,2):
        sum+=i
        
    return sum
n=int(input("Enter n value:"))
sum_of_N_even=sum_of_even(n)
print("sum of n even numbers 1 to  ",n,":",sum_of_N_even)