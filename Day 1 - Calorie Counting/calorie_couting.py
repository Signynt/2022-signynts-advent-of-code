def load_calories_file(calories_file):
    with open(calories_file) as f:
        calories_string = f.read()
    return calories_string

def convert_list_to_int(list):
    int_list = [int(item) for item in list if item]
    return int_list

def sum_calories_for_each_elf(list):
    list_of_summed_calories = []
    for item in list:
        calories_of_one_elf = item.split('\n')
        int_list = convert_list_to_int(calories_of_one_elf)
        summed_calories = sum(int_list)
        list_of_summed_calories.append(summed_calories)
    return list_of_summed_calories

def output_result_top_x_elves(list, top_x_elves):
    sorted_list = sorted(list, reverse=True)[:top_x_elves]
    result_calories = sum(sorted_list)
    result_index = [list.index(item) for item in sorted_list]
    print("The top " + str(top_x_elves) + " elves are " + str(result_index) + " and are carrying " + str(result_calories) + " calories total.")

list_split_up_by_elf = load_calories_file('calories.txt').split('\n\n')

output_result_top_x_elves(sum_calories_for_each_elf(list_split_up_by_elf), 3)
