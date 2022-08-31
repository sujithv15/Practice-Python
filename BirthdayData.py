import json
from collections import Counter

def get_bday_from_json():
    # create new dictionary
    bday_dictionary = {'Amy': '03/23/86',
                       'Bob': '06/01/76',
                       'Jen': '10/02/94',
                       'Tom': '09/22/93'
                       }
    # Whose name user wants to find birthday
    user_request_name = input("Whose birthday would you like to look up?")

    print(bday_dictionary.get(user_request_name, 'Name not found'))

    with open('info.json', 'r') as bday_json:
        bday_info = json.load(bday_json)

    if user_request_name in bday_info:
        print('{}\'s nirthday: {}'.format(user_request_name, bday_json[user_request_name]))


def add_bday_to_json():
    name = input('What is the name of the employee?')
    bday = input('What is their birthday?(XX/XX/XXXX)')
    bday_info = {name: bday}
    with open('info.json', 'r') as file:
        bday_list_from_json = json.load(file)

    bday_list_from_json.update({name: bday})

    with open('info.json', 'w') as file:
        json.dump(bday_list_from_json, file)

def make_sample_json():
    bday_info = {
        'Amy': '03/23/86', 'Bob': '06/01/76', 'Jen': '10/02/94', 'Tom': '09/22/93'
    }
    with open('info.json', 'w') as file:
        json.dump(bday_info, file)

#FIXME
def count_bdays_per_month():
    with open('info.json', 'r') as file:
        bday_dict = json.load(file)

    print(bday_dict)
    print(Counter.bday_dict)

count_bdays_per_month()