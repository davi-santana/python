import random
def linear_search(my_list, key):
    for item in my_list:
        if key == item:
            return True
    return False

main_key = 345
my_list = random.sample(range(1000), 100)
print(f'before{my_list}')
print(f' \nAfter {sorted(my_list)}')

answer = linear_search(my_list = my_list, key = main_key)
print(f'{main_key} {" is " if answer else "is not"} present in your data set')
