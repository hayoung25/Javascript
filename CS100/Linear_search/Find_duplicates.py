# Search list and target value
tour_locations = [ "New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto"]
target_city = "New York City"

#Linear Search Algorithm
def linear_search(search_list, target_value):

    # Create array which takes indices
    matches = []

    # Iterate through the whole list
    for idx in range(len(search_list)):
        if search_list[idx] == target_value:

            # If there are idx corresponding to the target_value, add into matches array
            matches.append(idx)

    # Returning matches        
    if matches:
        return matches
    else:
        raise ValueError("{0} not in list".format(target_value))


# Testing
tour_stops = linear_search(tour_locations, target_city)
print(tour_stops)
