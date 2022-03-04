from Linked_list import LinkedList
from Runtime_1 import find_max


def sort_linked_list(linked_list):
    print("\n---------------------------")
    print("The original linked list is:\n{0}".format(linked_list.stringify_list()))
    new_linked_list = LinkedList()
    while linked_list.get_head_node() != None:
        maximum = find_max(linked_list)
        new_linked_list.insert_beginning(maximum)
        linked_list.remove_node(maximum)
    return new_linked_list

  

#Test Cases
ll = LinkedList("Z")
ll.insert_beginning("C")
ll.insert_beginning("Q")
ll.insert_beginning("A")
print("The sorted linked list is:\n{0}".format(sort_linked_list(ll).stringify_list()))

ll_2 = LinkedList(1)
ll_2.insert_beginning(4)
ll_2.insert_beginning(18)
ll_2.insert_beginning(2)
ll_2.insert_beginning(3)
ll_2.insert_beginning(7)
print("The sorted linked list is:\n{0}".format(sort_linked_list(ll_2).stringify_list()))

ll_3 = LinkedList(-11)
ll_3.insert_beginning(44)
ll_3.insert_beginning(118)
ll_3.insert_beginning(1000)
ll_3.insert_beginning(23)
ll_3.insert_beginning(-92)
print("The sorted linked list is:\n{0}".format(sort_linked_list(ll_3).stringify_list()))

#Runtime
runtime = "N^2"
print("The runtime of sort_linked_list is O({0})\n\n".format(runtime))