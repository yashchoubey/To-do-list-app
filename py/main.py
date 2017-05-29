#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import json
import logging

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.write('Hello world! Blah blah')
		
		try:
			todo_lists = [
				{
					"title":"List 1"
				},
				{
					"title":"List 2"
				},
				{
					"title":"List 3"
				},
				{
					"title":"List 4"
				}
			]
			logging.info(todo_lists)
			response_json = {"success":"true", "items":todo_lists}
		except Exception,e:
			logging.info(e)
			response_json = {"success":"false"}
			
		self.response.out.write(json.dumps(response_json))

class ToDoListHandler(webapp2.RequestHandler):
    def get(self):
    	todolist=[]
    	list1=categoryItems.getSelectedCategoryItem()
    	for obj in list1:
    		todolist.append(taskItems.getItem(obj))
    		return todolist

    def put(self,**kwargs):
    	taskItems.addItem(self.request.get("name"),self.request.get("category"),self.request.get("description"),self.request.get("completed"),self.request.get("dateTime"))

		

app = webapp2.WSGIApplication([
    ('/todo-list', MainHandler)
], debug=True)
