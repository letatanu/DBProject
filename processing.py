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
            if ' & ' in r:
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


def createClassInstance():
    count = 0
    with CursorConnectionFromPool() as cursor:
        function = "Select sec, crn, time, instructor, course, title, term from project.classmetadata"
        cursor.execute(function)
        result = cursor.fetchall()
        for re in result:
            section, crn, date, instructor, course, title, quarter = re

            # getting day, time
            dates = []
            try:
                day, time = date.split(", ")
                if " " in day:
                    d, t = day.split(" ")
                    # adding day time to table
                    dates.append((d,t))

                elif " " in time:
                    d, t = day.split(" ")
                    # adding day time to table
                    dates.append((d, t))
                else:
                    # adding day time to table
                    dates.append((day, time))
            except:
                try:
                    day, time = date.split(" ")
                    # adding day time to table
                    # adding day time to table
                    dates.append((day, time))
                except:
                    print(date)

            #getting instructors
            instructors = []
            instructor2 = None
            if '&' in instructor:
                instructor1, instructor2 = instructor.split(' & ')
            if instructor2 is None and ' and ' in instructor:
                instructor1, instructor2 = instructor.split(' and ')
            if instructor2 is not None:
                instructors.append(instructor1)
                instructors.append(instructor2)
            else:
                instructors.append(instructor)

            #getting term and year
            term, year = quarter.split(" ")
            # print(dates, instructors, term, year, section, crn,  course, title)

            # getting course id
            courseQuery = "Select id from project.course where course_number='%s' and title='%s'"%(course, title)
            cursor.execute(courseQuery)
            course_id = cursor.fetchone()
            course_id = course_id[0] if course_id else -1
            # print(course_id)


            #getting quarter id
            termQuery = "Select id from project.quarter where term='%s' and year=%d" % (term, int(year))
            cursor.execute(termQuery)
            term_id = cursor.fetchone()
            term_id = term_id[0] if term_id else -1
            # print(term_id)

            for (d, t) in dates:
                dateTimeQuery = "Select id from project.schedule where day='%s' and time='%s'"%(d, t)
                cursor.execute(dateTimeQuery)
                schedule_id = cursor.fetchone()
                schedule_id = schedule_id[0] if schedule_id else -1
                # print(dateID)
                for instructor in instructors:
                    instructorQuery = "Select id from project.instructor where name=lower('%s')"%(instructor)
                    cursor.execute(instructorQuery)
                    instructor_id = cursor.fetchone()
                    instructor_id = instructor_id[0] if instructor_id else -1
                    # print(instructorID)

                    insertQuery = "INSERT INTO project.class_instance(id, section, crn, schedule_id, course_id, instructor_id, term_id) VALUES({},'{}','{}',{},{},{},{})".format(count, section, crn, schedule_id, course_id, instructor_id, term_id)
                    print(insertQuery)
                    cursor.execute(insertQuery)
                    count += 1

def createStudentInClassTable():
    classInstanceIDs = np.arange(993)
    insertQuery = "INSERT INTO project.student_in_class(student_id, class_instance_id) VALUES"
    with CursorConnectionFromPool() as cursor:
        for classInstanceID in classInstanceIDs:
            numberOfStudent = np.random.randint(10,30)
            studentIDs = np.random.choice(98, numberOfStudent, replace=False)
            for studentID in studentIDs:
                value = "(%d, %d)"%(studentID, classInstanceID)
                insert = insertQuery + value
                print(insert)
                cursor.execute(insert)



# createInstructorTable()
# createScheduleTable()
# createCourseTable()
# createQuarterTable()
# createStudentTable()
# createClassInstance()
# createStudentInClassTable()