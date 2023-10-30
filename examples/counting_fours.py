# count the number of times the number 4 appears in the following list
x = [1,2,3,3,4,4,4,5,4,4,3,2,1]
accumulator = 0
for i in x:
    if i == 4:
        accumulator += 1
print(f"There are {accumulator} 4s in the list")
