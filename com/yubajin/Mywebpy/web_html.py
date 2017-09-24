import web

urls = (
    '/(.*)','hello'
)

app = web.application(urls, globals())

class hello:
    def GET(self,name):
        result = open(r'htmlfile/1.html','r').read()
        return result

if __name__ == '__main__':
    app.run()