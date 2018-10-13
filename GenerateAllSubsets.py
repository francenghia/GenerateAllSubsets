def subsets(array):
    if array == []:
        return [[]]

    x = subsets(array[1:])

    return x + [[array[0]] + y for y in x]
	
print (subsets(["A", "B", "C"]))
