# my_bad_list=['b','a','d']
# print(bool(my_bad_list))
year= input('year of birth:')
if not bool(year.rstrip()):
    print('you must write year of birth')