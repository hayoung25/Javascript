# Python3 code to demonstrate the
# working of set() on list and tuple
# Returns : An empty set if no element is passed. "@Non-repeating" element iterable modified as passed as argument. 
 
# initializing list
lis1 = [ 3, 4, 1, 4, 5 ]
 
# initializing tuple
tup1 = (3, 4, 1, 4, 5)
 
# Printing iterables before conversion
print("The list before conversion is : " + str(lis1))
# The list before conversion is : [3, 4, 1, 4, 5]


print("The tuple before conversion is : " + str(tup1))
# The tuple before conversion is : (3, 4, 1, 4, 5)

# Iterables after conversion are
# notice distinct and elements
print("The list after conversion is : " + str(set(lis1)))
# The list after conversion is : {1, 3, 4, 5}

print("The tuple after conversion is : " + str(set(tup1)))
# The tuple after conversion is : {1, 3, 4, 5}

