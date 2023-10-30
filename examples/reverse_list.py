# given an arbitrary list x reverse the list without using the reverse() or reversed() functions
x = [1,2,3,'a',{'b':'c'}, None, -42]
y=[]
for i in range(len(x)):
    y.append(x[len(x)-(i+1)])
print(y)
# ok whore here's what's up--> we used i + 1 because it starts at zero so as it goes up to 6 it is subtracting the length of 6 so it goes to zero at the end reversing the order 
#so 6 - (0+1) then 6 - (1+1) and those are then the value inside x(value) so it goes x(6) x(5) x(4) etc 
# and we dom't print it because then it isn't in list format we have to make another list y and append the values through the function we made 