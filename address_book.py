import json


def enter_info(new_list):
    name = input('Give me name: ')
    number = int(input('Give me number: '))

    try:
        number = int(number)
    except ValueError:
        print('You gave wrong number')
    else:
        registration = {'name': name, 'number': number}
        new_list.append(registration)
        return new_list


def load_registration():
    try:
        book_address = 'number_list.json'
        with open(book_address, 'r') as f:
            book_numbers = json.load(f)
            print(f'You added {len(book_numbers)} items.')
            return book_numbers
    except FileNotFoundError:
        return []


if __name__ == '__main__':
    book_numbers = load_registration()
    while True:
        answer = input('Do you want to add new registration?\nAnswer t or n : ')
        if answer == 't':
            enter_info(book_numbers)
            continue
        elif answer == 'n':
            print(book_numbers)
            break
        else:
            continue
    with open('number_list.json', mode='w') as packet:
        json.dump(book_numbers, packet)

number_list = []
registration = {'name': 'Mark', 'number': 67823}

# number_list.append(registration)

# print(enter_info(number_list))
# print(load_registration())

# with open('number_list.json', mode='w') as packet:
#     json.dump(number_list, packet)
