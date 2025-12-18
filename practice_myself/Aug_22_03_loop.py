# s: store sum of all numbers
s = 0
n = int(input("Enter number "))
# run loop n times
# stop: n+1 (bcause range nver include stop number in result)
for i in range(1, n+1, 1):
    #add current number to sum variable
    s += i
print("\n")  #/n은 여기서 띄어쓰기기능.
print("Sum is: ", s)