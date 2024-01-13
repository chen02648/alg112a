def permutations(arr):
    result = []
    generate_permutations(arr, 0, result)
    return result

def generate_permutations(arr, index, result):
    if index == len(arr):
        result.append(arr.copy())
        return

    for i in range(index, len(arr)):
        arr[index], arr[i] = arr[i], arr[index]  
        generate_permutations(arr, index + 1, result)
        arr[index], arr[i] = arr[i], arr[index]  

my_list = [1, 2, 3]
all_permutations = permutations(my_list)
print(all_permutations)
