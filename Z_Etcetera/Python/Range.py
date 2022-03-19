""" usually used for "For loop"
range(start, stop, step)
start(Optional). An integer number specifying at which position to start. Default is 0
stop(Required). integer number which ends (Not included)
step(Optional). interval between numbers Default is 1
"""
# range(start, stop)
range1= range(1, 5)
for i in range1:
    print(i) 
# return 1, 2, 3, 4 

# range(stop)
range2 = range(4)
for i in range2:
    print(i)
# return 0, 1, 2, 3

# range(start, stop, step)
range3 = range(0, 10, 2)
for i in range3:
    print(i)
# return 0, 2, 4, 6, 8