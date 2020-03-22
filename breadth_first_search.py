from collections import deque

graph = {}
graph['first_iteration'] = ['first_one', 'first_two', 'first_three']
graph['first_one'] = ['first_one_one', 'first_one_two']
graph['first_two'] = ['first_two_onE', 'repeating_element']
graph['first_three'] = ['repeating_element']
graph['first_one_one'] = []
graph['first_one_two'] = []
graph['first_two_one'] = []
graph['repeating_element'] = []

def number_is_true(name):
    return name[-1] == 'E'

def search(name):
    desearch = deque()
    desearch += graph[name]
    desearched = []
    while desearch:
        number = desearch.popleft()
        if not number in desearched:
            if number_is_true(number):
                print(number + " is true! ")
                return True
            else:
                desearch += graph[number]
                desearched.append(number)
    return False
search('first_iteration')