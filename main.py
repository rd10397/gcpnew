import webapp2


class arun(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('THIS IS MODIFIED BY BLACKHAT')


app = webapp2.WSGIApplication([
    ('/', arun),
], debug=True)
