
import web

# url映射
urls = (
    '/index','index',
    '/blog/\d+','blog',
    '/(.*)','hello'
)

app = web.application(urls, globals())

class index:
# 请求路径比如http://localhost:8080/index?name=yubajin&sex=female
    def GET(self):
        data = web.input()
        return data

class blog:
    # def GET(self):
    #     data = web.input()
    #     return data

    def GET(self):
            return web.ctx.env

    def POST(self):
        data = web.input()
        return data

# 请求路径比如http://localhost:8080
class hello:
    def GET(self,name):
        result = open(r'htmlfile/2.html','r').read()
        return result

if __name__ == '__main__':
    app.run()