from google.appengine.ext import db

class Poll(db.Model):
	country = db.StringProperty()
	clockwise = db.IntegerProperty()
	counter_clockwise = db.IntegerProperty()

class RecordBook(db.Model):
	date = db.StringProperty()