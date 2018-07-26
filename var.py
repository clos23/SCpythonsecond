print("17")
print 17
print 17.23

print(type("17"))
print(type(17))
print(type(17.23))

x = ("17")
y = 17

print x + str(y)
print int(x)+y
#cannot add a string with a interger, likewise with others. 
#However is possible through making a string an interger or in vice-versa.

y = y+1
if x == y:
    print("yay")
elif x < y:
    print("bigger")
elif x > y:
    print("smaller")
else:
    print("nay")
    