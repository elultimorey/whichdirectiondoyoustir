from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app


class MainPage(webapp.RequestHandler):
        
    def get(self, arg):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('404')

application = webapp.WSGIApplication([('/(.*)', MainPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
