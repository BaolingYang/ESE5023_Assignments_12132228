
# 1. Flowchart: Print_values
# Ask users to input 3 numbers to assign a,b,c
a=float(input("please input the 1st number as the value of a:"))
b=float(input("please input the 2nd number as the value of b:"))
c=float(input("please input the 3rd number as the value of c:"))
# Compare number size for a,b,c
if(a>b):
    if(b>c):
        # Based on the number size of a,b,c, assign x,y,z 
        x=a
        y=b
        z=c
        # Output the value of (x+y-10*z)
        print("x+y-10*z = ", x+y-10*z)
    elif(a>c):
        x=a
        y=c
        z=b
        print("x+y-10*z = ", x+y-10*z)
    else:
        x=c
        y=a
        z=b
        print("x+y-10*z = ", x+y-10*z)
elif(b>c):
    print(None)
else:    
    x=c
    y=b
    z=a
    print("x+y-10*z = ", x+y-10*z)


# 2. Continuous celing function
from math import *
import numpy as np
# Ask users to input the range and the item number to create a random list
M=int(input("Please input the range of the positive intergers (>0):"))
N=int(input("Please input the number of positive intergers:"))
list=np.random.randint(1,M+1,N)
print("The random list is shown below:\n",list)
# Define a function F(x) to get the value of F(x) = F(ceil(x/3)) + 2x, where F(1) = 1
y=0
def F(x):
    if(x==1):
        return 1
    else:
        y=F(ceil(x/3))+2*x
        return y
# Use a "for" loop and the function F(x) to get the value of F(list[i])
for i in range(N):
    print ("x=", list[i],",F(x)=", F(list[i]))


# 3. Dice Rolling
# 3.1 Find_number_of_ways
# Set the total number of dices(D)
D=10
# Define a function to calculate the probability of sum X for D dices
prob=0
def Prob(D,X):
    # For each dice, the probability to toss“0/1/2/3/4/5/6” is (1/6).
    # When sum X is equal to the number of dices(D), the probability is (1/6)^D
    if X==D:
        return pow(1/6,D)
    # When sum X is smaller than D or larger than 6D, the probability is 0
    if X<D or X>6*D:
        return 0
    else:
    # The probability of sum X for D dices is equal to the probability of 
    # sum (X-a) for (D-1) dices, where "a" is the potint of the last dice, belonging to 0-6.
    # Inspired from https://blog.csdn.net/yue_luo_/article/details/95517498
        prob = (Prob(D-1, X-1) + Prob(D-1, X-2) + Prob(D-1, X-3) + Prob(D-1, X-4) + Prob(D-1, X-5) + Prob(D-1, X-6))*1/6  
        return prob
# Define a function to calculate the number of ways to reach sum X
def Find_number_of_ways(X):
    # The total number of ways is (6^10). The number of ways for each sum(X) is probability*(6^10).
    print("The number of ways is",round(Prob(D,X)*(6**10)))
# Ask users to input a sum X and find its number of ways
x=int(input("Please input a sum X:"))
Find_number_of_ways(x)

# 3.2 List: Number_of_ways
# Use a "for" loop to calculate 51 times to get Number_of_ways for sum X, 10-60 respectively.(Consume around 2.5 minutes)
Number_of_ways=[]
for i in range(10,61):
    ways_number=round(Prob(D,i)*(6**10))
    Number_of_ways.append(ways_number)
print("Number of ways are listed below\n", Number_of_ways)


# 4.Dynamic programming
import numpy as np
import math
# 4.1 Random_integer function
# Ask users to decide the size of an array and create an array
N=int(input("Please input the number of elements to create an array:"))
Random_interger=np.random.randint(0,11,N)
print(Random_interger)

# 4.2 Sum_averages function
# Define a function to calculate the sum of subset average(SA)
def Sum_averages(array):
    SA=0
    # For an array with N elements, sum of all subset average with n elements (n<=N) is equal to (array.sum() * C(N-1,n-1)/n)
    # Here use a "for" loop to achieve the sum of C(N-1,n-1)/n for all subsets, whose element number increasing from 1 to N
    # Discussed with Wenting Yuan and inspired from https://www.geeksforgeeks.org/sum-average-subsets/
    for i in range(0,len(array)):
        SA+=(math.factorial(len(array)-1)/math.factorial(len(array)-1-i)/math.factorial(i))/(i+1)
    SA=SA*array.sum()
    return SA
print("The Sum_averages for each subset is:\n", Sum_averages(Random_interger))

# 4.3 Total_sum_set function
import matplotlib.pyplot as plt
Total_sum_set=[]
# Use a "for" loop to calculate Sum_averages for random list with N increasing from 1 to 100
# Each result of Sum_averages(np.random.randint(0,11,j+1)) appended in the Total_sum_set
for j in range(100):
    sum=Sum_averages(np.random.randint(0,11,j+1))
    Total_sum_set.append(sum)
print("Sum_averages with N increasing from 1 to 100 are shown below:\n",Total_sum_set)
# Plot Total_sum_set
x=np.arange(1,101,1)
y=Total_sum_set
plt.plot(x, y, ls="-", lw=2, label="plot line:Total_sum_set vs. len(Random_interger)")
plt.legend()
plt.show()


# 5. Path counting
# 5.1 Create a matrix
import numpy as np
# Ask users to decide the size of a matrix and create a matrix
N = int(input("Please input the number of rows:"))
M = int(input("Please input the number of columns:"))
arr=np.random.randint(2,size=(N,M))
arr[0,0]=1
arr[N-1,M-1]=1
print(arr)

# 5.2 Count_path function
# Define a function Count_path(matrix,a,b) to count the pathway for a specific matrix, where "a" is row number, "b" is column number.
# Regard each element as a point, the pathway number to a point is equal to the pathway number to
# its upper point plus that of its left point, because it was only allowed to move either rightward or downward.
# Inspired from https://www.geeksforgeeks.org/count-number-of-ways-to-reach-destination-in-a-maze/?ref=rp
def Count_path(matrix,a,b):
    # Substract 1 from each element for counting purposes, and the matrix is refilled by -1 or 0, which were 0 or 1 before, respectively.
    matrix=np.add(matrix,-1)
    # Initialize the leftmost column
    for i in range(a):
        # If meet a blockage, break the loop
        if(matrix[i,0] != 0):
            break
        # If meet an access, each element plus 1, which means the pathway number from entrance[0,0] to the element[i,0] is 1
        else:
            matrix[i,0] +=1
    # Initialize the uppermost row, whose solution is similar to the leftmost column      
    for j in range(b):
        if(matrix[0,j] != 0):
            break
        else:
            matrix[0,j] +=1
    # Since the pathway number to a point is equal to the pathway number to its upper point plus that of its left point,
    # two "for" loops were used to count the pathways for each point, up to the last element[a-1,b-1]
    for i in range(1,a,1):
        for j in range(1,b,1):
            if(matrix[i,j] != 0):
                continue
            if(matrix[i-1,j] >0):
                matrix[i,j] += matrix[i-1,j]
            if(matrix[i,j-1] >0):
                matrix[i,j] += matrix[i,j-1]
    Count_path = matrix[a-1,b-1]
    # Return the pathway number of the last element[a-1,b-1]
    if (Count_path >= 0):
        return Count_path
    # If the value of last element[a-1,b-1] is smaller than zero, return 0
    else:
        return 0
# Print the pathway number for the matrix in 5.1
print(Count_path(arr,N,M))

# 5.3 Count_path function
# Calculate the mean pathway number for 1000 runs by refilling new random matrix
sum_path=0
for k in range(1000):
    sum_path += Count_path(np.random.randint(2,size=(10,8)),10,8)
print("The mean of Count_path for matrixes with size(10,8) from the 1000 runs is\n", sum_path/1000)    

