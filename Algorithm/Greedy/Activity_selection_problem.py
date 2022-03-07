"""Find maximum number of events. (Each events has start, finish time, start and all events should not overlap. """
start  =  [1, 0, 3, 5, 8, 5]
finish =  [2, 6, 4, 7, 9, 9]

def make_event_array(start, finish):
     start_finish = []
     for i in range(len(finish)):
          #make dictionary with 2 keys
          new_dic = {"start": int, "finish": int}

          #push in values into dictionary
          new_dic["start"] = start[i]
          new_dic["finish"] = finish[i]

          #push each dictionary into an array
          start_finish.append(new_dic)

     return start_finish

## Max events
def get_max_events(array):
     n = len(array)
     i = 0
     j = 1 
     max_event = []
     max_event.append(array[0])     
     while (j < n):
          if array[i]["finish"] <= array[j]["start"]:
               max_event.append(array[j])
               i = j
          j += 1
     return max_event

## Making event array
start_finish = make_event_array(start, finish)

## sorting from low to high according to finish
def get_finish(event):
     return event.get("finish")

start_finish.sort(key=get_finish)

## get max_array with the events which are not overlapping

max_events = get_max_events(start_finish)      

## Answer
answer = len(max_events)
print(answer)