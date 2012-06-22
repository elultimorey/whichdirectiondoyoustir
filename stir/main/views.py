from django.shortcuts import render_to_response

from stir.main.models import Poll

MEMCACHE_POLL = 'poll'

def main(request):
	response = render_to_response('index.html',{})
	return response
	
def stats(request, arg=None):
	country = ''
	data = {}
	# Alert-box type
	if str(request.get_full_path()).endswith('?v'):
		data['type'] = 'success'
		data['alert_info'] = 'Vote counted correctly'
	if str(request.get_full_path()).endswith('?d'):
		data['type'] = 'error'
		data['alert_info'] = 'Vote unaccounted'
	if str(arg) == '':
		country = 'all'
	else:
		country = str(arg).replace('/', '')
	poll = Poll.get_by_key_name(country)
	if poll == None:
		# The country not exits
		data['type'] = 'warning'
		data['alert_info'] = 'No data for that country'
		poll = Poll.get_by_key_name('all')
	data['country']=poll.country
	total = poll.clockwise + poll.counter_clockwise
	data['clockwise'] = poll.clockwise*100/total
	data['counter_clockwise'] = poll.counter_clockwise*100/total
	countries = []
	for p in Poll.all():
		countries.append(p.country)
	data['countries']=countries
	response = render_to_response('countries.html',data)
	return response
