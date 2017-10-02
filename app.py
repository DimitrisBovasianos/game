
import web
import map
import re
import base64

urls = (
  '/', 'Index',
  '/login','Login',
  '/game','gameengine'
)

app = web.application(urls, globals())

# little hack so the debug mode works with session
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app,store,
                                  initializer={'room': None})
    web.config._session = session
else:
    session = web.config._session

render = web.template.render('templates/', base="layout")

allowed = (
      ('jon','pass1'),
      ('tom','pass2')
)

class Index(object):

     def GET(self):
        if web.ctx.env.get('HTTP_AUTHORIZATION') is not None:
            return 'this is the index page'

        else:
          raise web.seeother('/login')

class Login(object):
    def GET(self):
        auth = web.ctx.env.get('HTTP_AUTHORIZATION')
        authreq = False
        if auth is None:
            authreq = True
        else:
            auth = re.sub('^Basic','',auth)
            username,password = base64.decodestring(auth).split(':')
            if (username,password) in allowed:
                session.room = map.START
                web.seeother('/game')

            else:
                authreq = True
        if authreq:
            web.header('www-Authenticate', 'Basic realm = "Auth example"')
            web.ctx.status = '401 Unauthorized'
            return


class gameengine(object):

  def GET(self):

    if session.room:
        return render.showroom(room=session.room)
    else:
        #why is there?do you need it?
        return render.you_died()

  def POST(self):
        form = web.input(action=None)

        #there is a bug here
        if session.room and form.action:
            session.room = session.room.go(form.action)

        web.seeother("/game")

if __name__ == "__main__":
    app.run()
