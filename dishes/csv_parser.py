import csv
import json
from django.conf import settings
from dishes.models import *

# This script is used to parse csv file and save the data in db.sqlite3 file
# for running the script, you have to run the command below in your terminal, you should replace the file path with your own file path in the command below.
# ./manage.py shell < /home/salohiddin/Workspace/search_dish/dishes/csv_parser.py
# Open file
my_file_path = "/home/salohiddin/Workspace/search_dish/restaurants_small.csv"
with open(my_file_path) as file_obj:
    # Create reader object by passing the file
    # object to reader method
    reader_obj = csv.reader(file_obj)
    # Iterate over each row in the csv
    # file using reader object
    for row in reader_obj:
        if row[0] == 'id':
            continue
        try:
            location = Location.objects.get(name=row[2])
        except Location.DoesNotExist:
            location = Location.objects.create(name=row[2])

        lat_long = row[4].split(",")
        restaurant = Restaurant.objects.create(name=row[1], location=location, full_details=row[5],
                                               latitude=lat_long[0],
                                               longitude=lat_long[1])
        item_dict = json.loads(row[3])
        for dish, price in item_dict.items():
            try:
                item = Item.objects.get(name=dish)
            except Item.DoesNotExist:
                item = Item.objects.create(name=dish)
            RestaurantItem.objects.create(item=item, restaurant=restaurant, price=price)
print('Success')
