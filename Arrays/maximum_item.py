
array = [10, 42, 55, 2, 1, 0]

# linear search O(N) - ordo N linear running time complexity

# Random indexing is an O(1) constant running time complexity

_max = array[0]   # ordo 1 running time complexity

for num in array:
    if num > _max:
        _max = num

print(_max)

_min = array[0]

for num in array:
    if num < _min:
        _min = num

print(_min)
