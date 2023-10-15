def flatten_list(nested_list):
    flattened_list = []
    for item in nested_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list

input_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output_list = flatten_list(input_list)

print(output_list)

def reverse_nested_list(input_list):
    reversed_list = []
    for item in input_list:
        if isinstance(item, list):
            reversed_list.append(reverse_nested_list(item)[::-1])
        else:
            reversed_list.append(item)
    return reversed_list

input_list = [[1, 2], [3, 4], [5, 6, 7]]
output_list = reverse_nested_list(input_list)[::-1]

print(output_list)
