from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app


class MainPage(webapp.RequestHandler):
        
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('/* TEAM */\n')
        self.response.out.write('\tJose Joaquin Pastor Martinez\n')
        self.response.out.write('\tSite: http://www.elultimorey.es\n')
        self.response.out.write('\tBlog: http://www.urlfalsa.com\n')
        self.response.out.write('\tTwitter: @elultimorey\n')
        self.response.out.write('\tLocation: Murcia, Spain\n')
        self.response.out.write('\n')
        self.response.out.write('/* THANKS */\n')
        self.response.out.write('\tName: ~peachystarfish [http://peachystarfish.deviantart.com/]\n')
        self.response.out.write('\n')
        self.response.out.write('/* Site */\n')
        self.response.out.write('\tLast update: 2012/06/19\n')
        self.response.out.write('\tComponents: Google App Engine, Google Charts, python-geoip, Foundation\n')
        self.response.out.write('\tSoftware: Eclipse\n')
        
application = webapp.WSGIApplication([('/humans.txt', MainPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
