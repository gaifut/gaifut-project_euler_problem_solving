initial_range_to_work_with = list(range(1,1000))
list_of_filtered_multiples = list()
first_value_for_multiples = 3
second_value_for_multiples = 5
# checking for all the multiples of first multiple in the initial range
for each_int in initial_range_to_work_with:
    def check_int(each_int):
        muliple_check_first_value = each_int/first_value_for_multiples
        multiple_check_second_value = each_int/second_value_for_multiples
        whole_number_check = (muliple_check_first_value).is_integer() or (multiple_check_second_value).is_integer()
        if whole_number_check == True:
                list_of_filtered_multiples.append(each_int)
        else:
                return 0
    check_int(each_int)
sum_of_multiples = sum(list_of_filtered_multiples,0)
print(sum_of_multiples)
