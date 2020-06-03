from database import CursorConnectionFromPool

def createInstructorTable():
    with CursorConnectionFromPool() as cursor:
        function = "SELECT distinct lower(instructor) from project.classmetadata"
        cursor.execute(function)
        result = cursor.fetchall()
        count = 0
        for re in result:
            r = re[0]
            instructor2 = None
            if '&' in r:
                instructor1, instructor2 = r.split(' & ')
            if instructor2 is None and ' and ' in r:
                instructor1, instructor2 = r.split(' and ')
            if instructor2 is not None:
                insertQuery = "INSERT INTO project.instructor(id, name) VALUES ({},'{}')".format(count,instructor1)
                cursor.execute(insertQuery)
                count += 1
                insertQuery = "INSERT INTO project.instructor(id,name) VALUES ({},'{}')".format(count, instructor2)
                cursor.execute(insertQuery)
                count += 1
                print(insertQuery)
            else:
                insertQuery = "INSERT INTO project.instructor(id,name) VALUES ({}, '{}')".format(count, r)
                print(insertQuery)
                cursor.execute(insertQuery)
                count += 1


def createScheduleTable():
    with CursorConnectionFromPool() as cursor:
        function = "Select distinct time from project.classmetadata"
        cursor.execute(function)
        result = cursor.fetchall()
        for r in result:
            day, time = r.split(" ")


createInstructorTable()
# createScheduleTable()