import json
import requests
import time
from pymongo import MongoClient
client = MongoClient()  # connects to default host and port to run Mongod instance
mydb = client.hn_database  # names a database

running_item_id = 14421055

while running_item_id >= 1:
    request = requests.get('https://hacker-news.firebaseio.com/v0/item/{0}.json'.format(running_item_id))
    time.sleep(0.07)
    json_type = request.text
    try:
        returned_dict = json.loads(json_type)  # a dictionary data structure
        if returned_dict is None:  # sometimes we get a null string so the post doesn't exist anymore
            # we can't add this string to Mongo because it's not an iterable object
            print("returned dict returned a None object")
        else:
            # mytable is the name of our collection
            returned_dict['_id'] = returned_dict.pop('id')
            print(returned_dict)
            mydb.hn_collections.insert(returned_dict)  # this inserts the 'document' of the HN post into our collection
    except ValueError as value_exception_object:
        print("there was an error converting JSON object to Python object")
    running_item_id -= 1

