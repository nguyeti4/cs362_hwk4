def calc_avg(elements):
    if len(elements)==0:
        raise ValueError("List should not be empty")
    for x in elements:
        if type(x) != type(1):
            raise ValueError("All elements should be ints")
            break
    total = 0
    for x in elements:
        total += x
    return total/len(elements)
    
#print(calc_avg(elements=[1,2,3,4,5]))
           