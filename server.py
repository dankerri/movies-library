#coding:utf-8

import web
import json
from models import Movies

urls = (
    '/', 'index',
    '/todo/', 'todo',
)
app = web.application(urls, globals())

render = web.template.render('')

class index:
    def GET(self):
        return render.index()


class todo:
    def GET(self):
        # movies = []
        # itermovies = Movies.get_all()
        # for movie in itermovies:
        #     movies.append({
        #         "name": movie.name,
        #         "actress": movie.actress,
        #         "buttonType": movie.type,
        #     })
        movies = [
        {
            "name": "ambi05",
            "time": "201708"+"/",
            "buttonType":"0",
            "videoFormat":"avi",
            "actress":"alice",
        }
        ]
        return json.dumps(movies)

if __name__ == "__main__":
    app.run()
