from database import CursorConnectionFromPool
import numpy as np

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
        count = 0
        for re in result:
            r = re[0]
            insertQuery = "INSERT INTO project.schedule(id, day, time) VALUES "

            try:
                day, time = r.split(", ")
                if " " in day:
                    d, t = day.split(" ")
                    # adding day time to table
                    data = "({}, '{}', '{}')".format(count,d,t)
                    insert = insertQuery + data
                    print(insert)
                    cursor.execute(insert)
                    count += 1

                elif " " in time:
                    d, t = day.split(" ")
                    # adding day time to table
                    data = "({}, '{}', '{}')".format(count, d, t)
                    insert = insertQuery + data
                    print(insert)
                    cursor.execute(insert)
                    count += 1
                else:
                    # adding day time to table
                    data = "({}, '{}', '{}')".format(count, day, time)
                    insert = insertQuery + data
                    print(insert)
                    cursor.execute(insert)
                    count += 1
            except:
                try:
                    day, time = r.split(" ")
                    # adding day time to table
                    # adding day time to table
                    data = "({}, '{}', '{}')".format(count, day, time)
                    insert = insertQuery + data
                    print(insert)
                    cursor.execute(insert)
                    count += 1
                except:
                    print(r)

def createCourseTable():
    with CursorConnectionFromPool() as cursor:
        function = "Select distinct course, title from project.classmetadata"
        cursor.execute(function)
        result = cursor.fetchall()
        for index, re in enumerate(result):
            course, title = re
            insertQuery = "INSERT INTO project.course(id, course_number, title) VALUES ({},'{}','{}')".format(index, course, title)
            print(insertQuery)
            cursor.execute(insertQuery)

def createQuarterTable():
    with CursorConnectionFromPool() as cursor:
        function = "Select distinct term from project.classmetadata"
        cursor.execute(function)
        result = cursor.fetchall()
        for index, re in enumerate(result):
            content = re[0]
            term, year  = content.split(" ")
            insertQuery = "INSERT INTO project.quarter(id, term, year) VALUES ({},'{}',{})".format(index,term,int(year))
            print(insertQuery)
            cursor.execute(insertQuery)

def createStudentTable():
    first_name = np.array([
        "Mary",
        "Geogre",
        "Lucy",
        "Tim",
        "Jennifer",
        "Jerry",
        "Wendy",
        "Larry"
        "Candy",
        "Andrew"

    ])
    last_name = np.array([
        "Hamilton",
        "Ng",
        "Li",
        "Le",
        "Smith",
        "Johnson",
        "Davis",
        "Rodriguez",
        "Lopez",
        "Nguyen",
        "Chan",
    ])

    genders = np.array([
        "male", "female", "other"
    ])

    day = np.arange(1,32)
    month = np.arange(1,13)

    birthday_year = np.arange(1989,2003)
    count = 0
    for first in first_name:
        for last in last_name:
            bd = day[np.random.randint(0,len(day))]
            bdm = month[np.random.randint(0,len(month))]
            bdy = birthday_year[np.random.randint(0,len(birthday_year))]

            ad = day[np.random.randint(0,len(day))]
            am = month[np.random.randint(0,len(month))]
            ay = bdy + 18
            gender = genders[np.random.randint(0,len(genders))]
            birthday = "{}/{}/{}".format(bdm, bd, bdy)
            admisionDay = "{}/{}/{}".format(am, ad, ay)
            # print(first, last, birthday, admisionDay)
            with CursorConnectionFromPool() as cursor:
                function = "INSERT INTO project.student(id, first_name, last_name, birthday, gender, admission_date) VALUES ({},'{}','{}','{}','{}','{}')".format(count, first, last, birthday, gender, admisionDay)
                print(function)
                cursor.execute(function)
            count+=1

# createInstructorTable()
# createScheduleTable()
# createCourseTable()
# createQuarterTable()
# createStudentTable()