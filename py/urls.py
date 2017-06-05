import webapp2
from py import main

url_patterns = [
    webapp2.Route('/todo/todolist', main.ToDoListHandler),
    webapp2.Route('/todo/category', main.CategoryListHandler),
    webapp2.Route('/todo/main', main.WebPageHandler),
    ]
application = webapp2.WSGIApplication(url_patterns, debug=True)