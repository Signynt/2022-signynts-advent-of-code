def load_calories_file(calories_file):
    with open(calories_file) as f:
        calories_string = f.read()
    return calories_string

def convert_list_to_int(list):
    int_list = [int(item) for item in list if item]
    return int_list

def find_max_calories(list):
    max_value = max(list)
    index = list.index(max_value)
    return index, max_value

def sum_calories_for_each_elf(list):
    list_of_summed_calories = []
    for item in list:
        calories_of_one_elf = item.split('\n')
        int_list = convert_list_to_int(calories_of_one_elf)
        summed_calories = sum(int_list)
        list_of_summed_calories.append(summed_calories)
    return list_of_summed_calories

def output_result(list):
    result_index = find_index_of_max(list)[0]
    result_calories = find_index_of_max(list)[1]
    print("The elf carrying the most calories is elf number " + str(result_index) + ", who is carrying " + str(result_calories) + " calories.")

list_split_up_by_elf = load_calories_file('calories.txt').split('\n\n')
output_result(sum_calories_for_each_elf(list_split_up_by_elf))
