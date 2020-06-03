from database import CursorConnectionFromPool
class Query:
    def __init__(self, query):
        self.query = query

    def submit(self):
        with CursorConnectionFromPool() as cursor:
            cursor.execute(self.query)
            queryResults = cursor.fetchall()
            for sch in queryResults:
                print(sch)
