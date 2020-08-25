"""
REQUIREMENT
FIRST
- ask a client name
- handle the client name in roboko's conversation

SECOND(when csv file is not written anything)
- ask a restaurant name
- write restaurant name in csv file
  - the restaurant name should be Camel case format by separated spaces.
  - count how many times client said like the restaurant.

SECOND(when csv file is already written)
- ask whether client likes the restaurants written in csv
  - ask all restaurants written in csv.
- when client says YES or Yes or yes or y or Y
  - update count of liker.
- after asking all restaurants, ask the client original restaurant he likes.
  - when the restaurant is already written in csv, just update count of liker.

THIRD
- finish the conversation, with last some words.
"""

import csv
import os

client_name = input('Hello! I am Roboko.\n''What\'s your name?')
recommended_restaurants = []

if os.path.isfile('ranking.csv'):
    with open('ranking.csv', 'r') as read_file:
        reader = csv.DictReader(read_file)
        for row in reader:
            recommended_restaurants.append(row)

restaurant_name = ''
liked_restaurants = []
for recommended_restaurant in recommended_restaurants:
    is_like = None
    while is_like is None:
        client_reply = input('Do you like {}?'.format(recommended_restaurant['restaurant_name']))
        yes_word = 'yes'
        omitted_yes_word = 'y'
        no_word = 'no'
        omitted_no_word = 'n'
        yes_word_list = [yes_word, yes_word.capitalize(), yes_word.title(), omitted_yes_word, omitted_yes_word.capitalize()]
        no_word_list = [no_word, no_word.capitalize(), no_word.title(), omitted_no_word, omitted_no_word.capitalize()]
        if client_reply in yes_word_list:
            is_like = True
        elif client_reply in no_word_list:
            is_like = False
    if is_like:
        liked_restaurants.append(recommended_restaurant['restaurant_name'])
    # like_num = recommended_restaurant.values()
    # like_num += 1 if is_like else like_num
    # new_recommended_restaurants.append({'restaurant_name': recommended_restaurant['restaurant_name'], 'like_count': like_num})

else:
    restaurant_name = input('hi {client_name}, which restaurant do you like?'.format(client_name=client_name))
    restaurant_name = restaurant_name.title()

    if not (restaurant_name in liked_restaurants):
        liked_restaurants.append(restaurant_name)
    for liked_restaurant in liked_restaurants:
        is_new_restaurant = True
        for recommended_restaurant in recommended_restaurants:
            if recommended_restaurant['restaurant_name'] == liked_restaurant:
                is_new_restaurant = False
                recommended_restaurant['like_count'] = int(recommended_restaurant['like_count']) + 1
        if is_new_restaurant:
            recommended_restaurants.append({'restaurant_name': restaurant_name, 'like_count': 1})
    if len(recommended_restaurants) < 1:
        recommended_restaurants.append({'restaurant_name': restaurant_name, 'like_count': 1})

with open('ranking.csv', 'w', newline='') as write_file:
    writer = csv.DictWriter(write_file, fieldnames=recommended_restaurants[0].keys())
    writer.writeheader()
    for recommended_restaurant in recommended_restaurants:
        writer.writerow(recommended_restaurant)

print('{client_name}, Thank you for talking with me.\n'.format(client_name=client_name) + 'Have a nice day!')


