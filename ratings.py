"""Restaurant rating lister."""
import random


def generate_ratings_dict(): 

    doc = open('scores.txt')
    rating = {}
    
    for line in doc:
        line = line.rstrip().split(":")
        restaurant, score = line
        rating[restaurant] = score
    
    doc.close()
    return rating
    

def sort_restaurants(rating):
    # rating[user_restaurant] = user_rating
    sorted_restaurants = sorted(rating)
    for sorted_restaurant in sorted_restaurants:
        print(f'{sorted_restaurant} is rated at {rating[sorted_restaurant]}')

        
def user_ratings(rating):
    
    user_restuarant = input("Please rate your fav restaurant!")

    while True:
        user_rating = int(input("Rating>>>  "))
        if user_rating >=1 and user_rating <=5:
            rating[user_restuarant] = user_rating
            return rating
        else:
            print("Rating must be between 1 and 5.")
            continue
def update_rand_restaurant(ratings):
   ratings = generate_ratings_dict()
   restaurants = ratings.keys()
   random_resaturant = random.choice(list(restaurants))
   print(random_resaturant) 

def choose_options():
    rating = generate_ratings_dict()

    while True:

        selection = input("What do you want to do?\n1)Print restaurant ratings\n2)Add a new restaurant rating\n3)Update random restaurant rating\n4)quit\n")
        if selection == '1':
            sort_restaurants(rating)
            continue

        elif selection == '2':
            rating = user_ratings(rating)
            continue
        elif selection == '3':
            update_rand_restaurant(rating)

        elif selection == '4':
            break





