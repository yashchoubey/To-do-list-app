import webapp2
import json
import logging
from datetime import datetime
import os
import jinja2
from py.models import *

class BaseRequestHandler(webapp2.RequestHandler):
    def dispatch(self):
        # Get a session store for this request.
        # self.session_store = sessions.get_store(request=self.request)
        
        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            # self.session_store.save_sessions(self.response)
            pass
    
    @webapp2.cached_property
    def jinja2(self):
        """Returns a Jinja2 renderer cached in the app registry"""
        return jinja2.get_jinja2(app=self.app)
    
    def render(self, template_name, template_vars={}):
        logging.info("HEree1")
        path, filename = os.path.split(tpl_path)
        logging.info("HEree2")
        return jinja2.Environment(loader=jinja2.FileSystemLoader(path or './')).get_template(filename).render(context)
        logging.info("HEree3")

        try:
            logging.info("HEree")
        except:
            logging.info("HEree")
            self.abort(404)

class WebPageHandler(BaseRequestHandler):
    def get(self):
        logging.info("In main call")
        logging.info(self.request.get("userEmail"))
        self.response.out.write(self.render('../index.html'))#, self.request.get("userEmail")

class ToDoListHandler(webapp2.RequestHandler):
    def get(self):
        dict1=taskItems.getItem()
        self.response.out.write(json.dumps(dict1))
    	

    def put(self):
        json_input = json.loads(self.request.body)
        logging.info(json_input)
        date_object = datetime.strptime(json_input["dueDate"].split("T")[0],'%Y-%m-%d')
        logging.info(date_object)
        taskItems.addItem(json_input["name"], json_input["category"], json_input["description"],date_object)
        
    def post(self):#delete
        json_input = json.loads(self.request.body)
        logging.info(json_input)
        date_object = datetime.strptime(json_input["dueDate"].split("T")[0],'%Y-%m-%d')
        logging.info(date_object)
    	taskItems.deleteItem(json_input["name"], json_input["category"], json_input["description"],date_object,json_input["completed"])


class CategoryListHandler(webapp2.RequestHandler):
    def get(self):
        dict1=categoryItems.getCategoryItem()
        self.response.out.write(json.dumps(dict1))

    def post(self):
        categoryItems.addItem(self.request.get("categoryName"))

    def delete(self):
        logging.info("In delete call")
        categoryItems.deleteItem(self.request.get("categoryName"))

