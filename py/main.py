import webapp2
import json
import logging
from datetime import datetime
from py.models import *

class ToDoListHandler(webapp2.RequestHandler):
    def get(self):
        dict1=taskItems.getItem()
        self.response.out.write(json.dumps(dict1))
    	

    def put(self):
        json_input = json.loads(self.request.body)
        logging.info(json_input)
        logging.info("osjndcsn")
        datetime_object = datetime.strptime(json_input["dateTime"], '%b %d %Y %I:%M%p')
    	taskItems.addItem(json_input["name"], json_input["category"], json_input["description"],json_input["dateTime"] )


    def delete(self):
    	taskItems.deleteItem(self.request.get("name"),self.request.get("category"),self.request.get("description"),self.request.get("completed"),self.request.get("dateTime"))


class CategoryListHandler(webapp2.RequestHandler):
    def get(self):
        dict1=categoryItems.getCategoryItem()
        self.response.out.write(json.dumps(dict1))

    def post(self):
        categoryItems.addItem(self.request.get("categoryName"))

    def delete(self):
        logging.info("In delete call")
        categoryItems.deleteItem(self.request.get("categoryName"))

