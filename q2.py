import statistics
def convert_to_matrix(user_list):
    temp = user_list.copy()

    while len(temp) < 9:
        temp.append(None)

    temp = temp[:9]

    matrix = [
        temp[0:3],
        temp[3:6],
        temp[6:9]
    ]

    return matrix
def tuple_statistics(user_list):
    user_tuple = tuple(user_list)

    mean_value = statistics.mean(user_tuple)
    median_value = statistics.median(user_tuple)
    try:
        mode_value = statistics.mode(user_tuple)
    except:
        mode_value = "No unique mode"

    return {
        "Tuple": user_tuple,
        "Mean": mean_value,
        "Median": median_value,
        "Mode": mode_value
    }
def iterate_functions(user_list):
    matrix_output = convert_to_matrix(user_list)
    stats_output = tuple_statistics(user_list)

    final_result = {
        "Matrix Function Output": matrix_output,
        "Statistics Function Output": stats_output
    }

    return final_result
user_list = list(map(int, input("Enter list elements separated by space: ").split()))
result = iterate_functions(user_list)
print(result)