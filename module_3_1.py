calls = 0
def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    string = str(string)
    lenght = len(string)
    UP = string.upper()
    low = string.lower()
    tuple = (lenght, UP, low)
    count_calls()
    return tuple

def is_contains(string,list_to_search):
    lower_string = str(string).lower()
    list_to_search = list(list_to_search)
    lower_list_to_search = [word.lower() for word in list_to_search]
    answer_ = 0
    if lower_string in lower_list_to_search:
        answer_ = True
    elif lower_string not in lower_list_to_search:
        answer_ = False
    count_calls()
    return answer_

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)


