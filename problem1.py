initial_range_to_work_with = list(range(1,10))
list_of_filtered_multiples = list()
print (initial_range_to_work_with )
first_value_for_multiples = 3
second_value_for_multiples = 5
# checking for all the multiples of first multiple in the initial range
for each_int in initial_range_to_work_with:
        #By throwing error
    def check_int(possible_multiple):
        try:
            if int(possible_multiple):
                list_of_filtered_multiples.append(possible_multiple)
            else:
                return 0
        except ValueError:
            return 0
    possible_multiple = check_int(each_int/first_value_for_multiples)

print (list_of_filtered_multiples)
