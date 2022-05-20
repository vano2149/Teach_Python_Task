"""
"""
'''
ONES = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 
        'eighteen', 'nineteen']

TENS = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def parse_int(string):
    numbers = []
    for token in string.replace('-', ' ').split(' '):
        if token in ONES:
            numbers.append(ONES.index(token))
        elif token in TENS:
            numbers.append((TENS.index(token) + 2) * 10)
        elif token == "hundred":
            numbers[-1] *= 100
        elif token == 'thousand':
            numbers == [x * 1000 for x in numbers]
        elif token == 'million':
            numbers = [x * 1000000 for x in numbers]
    return print(sum(numbers))
parse_int("")
'''

def parse_int(string):
    result = 0

    list = string.replace(' and', '').split(' ')

    dict1 = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
             'nine': 9,
             'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
             'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30,
             'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90}
    dict2 = {'hundred': 100, 'thousand': 1000, 'hundredthousand': 100000, 'million': 1000000}

    def hyphenator(list):
        list = list.split('-')
        return dict1[list[0]] + dict1[list[1]]

    list2 = []

    for element in list:
        if element.count('-') > 0:
            list2.append(hyphenator(element))
        elif element in dict1:
            list2.append(dict1[element])
        else:
            list2.append(element)

    for i in range(len(list2) - 1):
        if list2[i] == 'hundred' and i != len(list2) - 1:
            if list2[i + 1] == 'thousand':
                list2[i] = 'hundredthousand'
                list2.pop(i + 1)
                print(list2)

    if type(list2[-1]) == int:
        result += list2[-1]
        list2.pop(-1)

    def translator(list):
        new_list = []
        while len(list) > 1:
            new_list.append(list[0] * dict2[list[1]])
            list.pop(0)
            list.pop(0)
        return new_list

    list3 = translator(list2)

    while len(list3) > 1:
        if list3[0] > list3[1]:
            result += list3[0]
            list3.pop(0)
        else:
            if len(str(list3[0])) == 3 and str(list3[0])[1:3] == '00' and len(str(list3[1])) == 4:
                result += int(str(list3[0])[0:2] + str(list3[1]))
                list3.pop(0)
                list3.pop(0)
            else:
                result += int(str(list3[0])[0] + str(list3[1]))
                list3.pop(0)
                list3.pop(0)

    if len(list3) > 0:
        result += list3[0]

    return result