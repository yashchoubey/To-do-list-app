from google.appengine.ext import ndb
import logging
from datetime import datetime

class taskItems(ndb.Model):
	
	name = ndb.StringProperty()
	category = ndb.StringProperty()
	description = ndb.StringProperty()
	completed = ndb.BooleanProperty(default=False)
	dueDate = ndb.DateProperty(auto_now=False)
	userEmail=ndb.StringProperty(default="yashchoubey@gmail.com")

	@classmethod
	def getItem(self):
		objs=self.query()
		returnList=[]
		for obj in objs:
			dict_obj={}
			dict_obj["name"]=obj.name
			dict_obj["category"] = obj.category
			dict_obj["description"] = obj.description
			dict_obj["completed"] = obj.completed
			dict_obj["dueDate"] = str(obj.dueDate)
			returnList.append(dict_obj)
		return returnList

	@classmethod
	def addItem(self, name, category, description, dueDate):
		obj=self(name=name, category=category, description=description, dueDate=dueDate)
		obj.put()

	@classmethod
	def deleteItem(self, name, category, description,dueDate, completed):
		obj=taskItems.query(ndb.AND(taskItems.name==name, taskItems.category==category, taskItems.description==description,taskItems.dueDate==dueDate, taskItems.completed==completed)).get()
		
		if obj:
			obj.key.delete()

	@classmethod#select/deselect items completed
	def completeItem(self, name, category, description, dateTime, completed):
		obj=self.query(ndb.AND(name==name, category==category, description==description, dateTime==dateTime))
		if obj:
			if obj.completed:
				obj.completed=False
			else:
				obj.completed=True
			obj.put()

	
	
class categoryItems(ndb.Model):
	categoryName= ndb.StringProperty()
	isSelected = ndb.BooleanProperty(default=True)
	userEmail=ndb.StringProperty(default="yashchoubey@gmail.com")

	@classmethod
	def getCategoryItem(self):
		dict1={}
		objs=self.query().fetch()
		for obj in objs:
			dict1[obj.categoryName]=obj.isSelected
		logging.info(dict1)	
		return dict1

	@classmethod
	def addItem(self, categoryName):
		logging.info(categoryName)
		obj=self(categoryName=categoryName)
		obj.put()


	@classmethod
	def deleteItem(self, categoryName):
		obj=categoryItems.query(categoryItems.categoryName==categoryName).get()

		if obj:
			obj.key.delete()

	@classmethod#select/deselect items completed
	def completeItem(self, name, category, description, dateTime, completed):
		obj=self.query(categoryName==categoryName)
		
		if obj.isSelected:
			obj.isSelected=False
		else:
			obj.isSelected=True
		obj.put()

	
	@classmethod
	def getSelectedCategoryItem(self):
		obj=self.query(isSelected==True).fetch()
		return obj
