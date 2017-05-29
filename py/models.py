from google.appengine.ext import ndb
import logging

class taskItems(ndb.Model):
	name = ndb.StringProperty()
	category = ndb.StringProperty()
	description = ndb.StringProperty()
	completed = ndb.BooleanProperty(default=False)
	dateTime = ndb.DateTimeProperty(auto_now=True)

	@classmethod
	def addItem(self, name, category, description, completed, dateTime):
		obj=self(name=name, category=category, description=description, completed=completed, dateTime=dateTime)
		obj.put()

	@classmethod
	def deleteItem(self, name, category, description, completed, dateTime):
		obj=self.query(ndb.AND(name=name, category=category, description=description, completed=completed, dateTime=dateTime)).order(-dateTime)
		obj.delete()

	@classmethod#select/deselect items completed
	def completeItem(self, name, category, description, completed, dateTime):
		obj=self.query(ndb.AND(name=name, category=category, description=description, dateTime=dateTime))
		
		if obj.completed:
			obj.completed=False
		else:
			obj.completed=True
		obj.put()

	@classmethod
	def getItem(self, category):
		obj=self.query(category=category).order(-dateTime)
		return obj

class categoryItems(ndb.Model):
	categoryName= ndb.StringProperty()
	isSelected = ndb.BooleanProperty(default=True)

	@classmethod#select/deselect items completed
	def completeItem(self, name, category, description, completed, dateTime):
		obj=self.query(categoryName=categoryName)
		
		if obj.isSelected:
			obj.isSelected=False
		else:
			obj.isSelected=True
		obj.put()

	@classmethod
	def getCategoryItem(self):
		obj=self.query()
		return obj

	@classmethod
	def getSelectedCategoryItem(self):
		obj=self.query(isSelected=True).fetch()
		return obj
