# count the number of times the each number appears in the following list
x = [1,2,3,3,4,4,4,5,4,4,3,2,1]
accumulator_4 = 0
for i in x:
    if i == 4:
        accumulator_4 += 1
print(f"There are {accumulator_4} 4s in the list")

y = {}
for i in x: 
    if i not in y:
        y[i]=1 
    else:
        y[i]=y[i]+1 
print(y)
