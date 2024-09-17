calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    a = len(string)
    b = string.upper()
    c = string.lower()
    tup = (a, b, c)
    print(tup)
    return string


def is_contains(string, list_to_search):
    count_calls()
    a = []
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string.lower():
            a.append(True)
        elif str(list_to_search[i]).lower() != string.lower():
            a.append(False)
    if True in a:
        print(True)
    else:
        print(False)
    return string, list_to_search


string_info('AdCdEfG#456')
string_info('FDDDSSS23')
string_info('qwerty123')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('ZcGFDNTD', ['eww', '122dddfffcsjhbsmdb', 'ZcgfdNTD', 'ddshdh', 'urBeeeeAN'])
is_contains('cycle', ['recycling', 'cyclic'])
is_contains('1', ['2', 'c'])
print(calls)
