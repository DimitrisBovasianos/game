import web
import map

urls = (
  '/game', 'GameEngine',
  '/', 'Login',
)

app = web.application(urls, globals())

# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store,
                                  initializer={'room': None,})
    web.config._session = session
else:
    session = web.config._session

render = web.template.render('templates/', base="layout")

data = (
    ('dimi','1234'),
    ('mar','1234')
)

class Login(object):
    def GET(self):
        if session.get('logged_in',True):
             return render.login()
        else:
            session.room = map.START
            web.seeother('/game')


    def POST(self):
        name,passwd = web.input().user,web.input().passwd
        if (name,passwd) in data:
            session.room = map.START
            web.seeother('/game')
            session.logged_in = False
        else:
            session.logged_in = True
            web.seeother('/')



class GameEngine(object):

    def GET(self):
        if session.room:
            return render.showroom(room=session.room)
        else:
            # why is there here? do you need it?
            return render.you_died()

    def POST(self):
        form = web.input(action=None)

        # there is a bug here, can you fix it?
        if session.room and form.action:
            session.room = session.room.go(form.action)

        web.seeother("/game")

if __name__ == "__main__":
    app.run()
