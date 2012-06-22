from datetime import datetime

from google.appengine.api.labs import taskqueue
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import pygeoip

from stir.main.models import Poll, RecordBook

class CounterHandler(webapp.RequestHandler):
	def get(self):
		self.response.out.write(";)")

	def post(self):
		def addVote(self):
			choice = self.request.get('choice')
			choice = choice.lower()
			geo = self.request.get('geo', 'off')
			if geo != 'off':
				GEOIP = pygeoip.Database('GeoIP.dat')
				info = GEOIP.lookup(self.request.remote_addr)
				if not info.country:
					country = 'neverland'
				else:
					country = info.country
			else:
				country = 'neverland'
			country = country.lower()
			# Add the task to the default queue.
			taskqueue.add(url='/worker', params={'choice': choice, 'country': country, 'ip': self.request.remote_addr})
			
			self.redirect('/stats/?v')
			
		record = RecordBook.get_by_key_name(self.request.remote_addr)
		if record is None:
			addVote(self)
		else:
			recordDate = datetime.strptime(record.date, "%d/%m/%Y")
			nowDate = datetime.now()
			gap = nowDate-recordDate
			if gap.days >= 1:
				addVote(self)
			else:
				self.redirect('/stats/?d')
			

class CounterWorker(webapp.RequestHandler):
	
	def post(self): # should run at most 1/s
		choice = self.request.get('choice')
		country = self.request.get('country')
		ip = self.request.get('ip')
		def countryVote():
			poll = Poll.get_by_key_name(country)
			if poll is None:
				poll = Poll(key_name=country)
				poll.country = country
				poll.clockwise = 0
				poll.counter_clockwise = 0
			if choice == 'clockwise':
				poll.clockwise += 1
			else:
				poll.counter_clockwise += 1
			poll.put()
		def allVote():
			poll = Poll.get_by_key_name('all')
			if poll is None:
				poll = Poll(key_name='all')
				poll.country = 'all'
				poll.clockwise = 0
				poll.counter_clockwise = 0
			if choice == 'clockwise':
				poll.clockwise += 1
			else:
				poll.counter_clockwise += 1
			poll.put()
		def addIP():
			record = RecordBook(key_name=ip)
			record.date = datetime.now().strftime("%d/%m/%Y") 
			record.put()
		
		db.run_in_transaction(countryVote)
		db.run_in_transaction(allVote)
		db.run_in_transaction(addIP)

def main():
	run_wsgi_app(webapp.WSGIApplication([
		('/vote/', CounterHandler),
		('/worker', CounterWorker),
	]))

if __name__ == '__main__':
	main()
