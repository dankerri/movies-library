#coding:utf-8
import web

db = web.database(dbn='sqlite', db="movies.db")

class Movies(object):
    @staticmethod
    def get_all():
        return db.select('movies')
