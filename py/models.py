from google.appengine.ext import ndb
import logging
from datetime import datetime

class taskItems(ndb.Model):
	name = ndb.StringProperty()
	category = ndb.StringProperty()
	description = ndb.StringProperty()
	completed = ndb.BooleanProperty(default=False)
	dateTime = ndb.DateTimeProperty(auto_now=True)

	@classmethod
	def addItem(self, name, category, description, dateTime):
		logging.info(category,name,description)
		obj=self(name=name, category=category, description=description, dateTime=dateTime)
		obj.put()

	@classmethod
	def deleteItem(self, name, category, description, completed, dateTime):
		obj=self.query(ndb.AND(name==name, category==category, description==description, completed==completed, dateTime==dateTime)).order(-dateTime)
		obj.key.delete()

	@classmethod#select/deselect items completed
	def completeItem(self, name, category, description, completed, dateTime):
		obj=self.query(ndb.AND(name==name, category==category, description==description, dateTime==dateTime))
		
		if obj.completed:
			obj.completed=False
		else:
			obj.completed=True
		obj.put()

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
			#dict_obj["dateTime"] = string(obj.dateTime)
			returnList.append(dict_obj)
		return returnList
	
class categoryItems(ndb.Model):
	categoryName= ndb.StringProperty()
	isSelected = ndb.BooleanProperty(default=True)

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
		logging.info(categoryName)
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
