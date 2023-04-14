a = [1, 3, 4, 5, 6]
b = []

def recursive_count(array):

    if not array:
        return 0
    else:
        return 1 + recursive_count(array[1:])
        
print(recursive_count(b))



    

