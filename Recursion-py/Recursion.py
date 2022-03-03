### Recursion <Sum>
def sum_to_one(n):
  if n == 1:
    return n
  print("Recursing with input: {0}".format(n))

  # Here is recursion 
  return n + sum_to_one(n - 1)

# Test
print(sum_to_one(7))


### Recursion <Set>
def power_set(my_list):

    # base case: an empty list
    if len(my_list) == 0:
        return [[]]

    # recursive step: subsets without first element
    power_set_without_first = power_set(my_list[1:])

    # subsets with first element
    with_first = [ [my_list[0]] + rest for rest in power_set_without_first ]

    # return combination of the two
    return with_first + power_set_without_first

# Test
universities = ['MIT', 'UCLA', 'Stanford', 'NYU']
power_set_of_universities = power_set(universities)

for set in power_set_of_universities:
  print(set)


### Recurssion <Flatten>
def flatten(my_list):
  result = []
  for i in my_list:
    if isinstance(i, list):
      print("list found!")
      print(i)
      flat_list = flatten(i)
      result += flat_list
    else:
      result.append(i)
  return result

# Test
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', ['saturn']]], 'uranus', ['neptune', 'pluto']]
print(flatten(planets))


### Recursion <Tree>

def build_bst(my_list):
    if len(my_list) == 0:
        return "No Child"

    middle_idx = len(my_list) // 2
    middle_value = my_list[middle_idx]
  
    print("Middle index: {0}".format(middle_idx))
    print("Middle value: {0}".format(middle_value))
  
    tree_node = {"data": middle_value}
    tree_node["left_child"] = build_bst(my_list[ : middle_idx])
    tree_node["right_child"] = build_bst(my_list[middle_idx + 1 : ])

    return tree_node

# Testing
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)

runtime = "N*logN"