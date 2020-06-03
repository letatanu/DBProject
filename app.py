from database import CursorConnectionFromPool

class App:
    @classmethod
    #all classes are available at term and year
    def classAvailableAtTerm(cls, term, year):
        with CursorConnectionFromPool() as cursor:
            query = "Select distinct c.course_number " \
                    "FROM project.course c, project.class_instance ci, project.quarter q " \
                    "WHERE ci.course_id = c.id " \
                    "AND ci.term_id = q.id " \
                    "AND lower(q.term)=lower('%s') " \
                    "AND q.year=%d"%(term, year)

            cursor.execute(query)
            r = cursor.fetchall()
            result = [i[0] for i in r]
            print(result)

    @classmethod
    def classTaughtBy(cls, instructor, term, year):
        with CursorConnectionFromPool() as cursor:
            query = "Select distinct c.course_number " \
                    "FROM project.course c, project.class_instance ci, project.quarter q, project.instructor it " \
                    "WHERE ci.course_id = c.id " \
                    "AND ci.term_id = q.id " \
                    "AND ci.instructor_id = it.id " \
                    "AND lower(it.name) LIKE lower('%{}%') " \
                    "AND lower(q.term)=lower('{}') " \
                    "AND q.year={}".format(instructor, term, year)
            # print(query)
            cursor.execute(query)
            r = cursor.fetchall()
            result = [i[0] for i in r]
            print(result)
    @classmethod
    def classTaughtBy2Instructors(cls, instructor1, instructor2, term, year):
        with CursorConnectionFromPool() as cursor:
            query = "Select distinct c.course_number "\
                    "FROM project.course c, project.class_instance ci, project.quarter q, project.instructor it "\
                    "WHERE ci.course_id = c.id "\
                    "AND ci.term_id = q.id "\
                    "AND ci.instructor_id = it.id "\
                    "AND lower(it.name) LIKE lower('%{0}%') "\
                    "AND lower(q.term) = lower('{2}') "\
                    "AND q.year = {3} "\
            "intersect " \
                    "Select distinct c.course_number " \
                    "FROM project.course c, project.class_instance ci, project.quarter q, project.instructor it " \
                    "WHERE ci.course_id = c.id " \
                    "AND ci.term_id = q.id " \
                    "AND ci.instructor_id = it.id " \
                    "AND lower(it.name) LIKE lower('%{1}%') " \
                    "AND lower(q.term) = lower('{2}') " \
                    "AND q.year = {3} ".format(instructor1, instructor2, term, year)
                # print(query)
            cursor.execute(query)
            r = cursor.fetchall()
            result = [i[0] for i in r]
            print(result)
    @classmethod
    def listStudentInClassAtTerm(cls, courseNumber, term, year):
        with CursorConnectionFromPool() as cursor:
            query = "Select st.id, st.first_name, st.last_name, c.course_number "\
                    "FROM " \
                    "project.student st, project.course c, project.class_instance ci, project.quarter q, project.student_in_class sc " \
                    "WHERE ci.course_id = c.id " \
                    "AND ci.term_id = q.id " \
                    "AND sc.class_instance_id = ci.id " \
                    "AND sc.student_id = st.id " \
                    "AND lower(c.course_number) LIKE lower('%{}%') " \
                    "AND lower(q.term)=lower('{}') AND q.year={}".format(courseNumber, term, year)
            # print(query)
            cursor.execute(query)
            r = cursor.fetchall()
            print(r)
if __name__ == '__main__':
    selection = input("Input the task number you want to do. \n"
                      "1. See all available courses at a specific term.\n"
                      "2. See all available courses taught by a certain instructor at a specific term, year.\n"
                      "3. Which classes are taught by 2-3 specific instructors?\n"
                      "4. List all the students in a specific course.\n"
                      "Otherwise, exit.\n")
    try :
        if int(selection) == 1:
            term = input("Please input the term.")
            term = term.replace(" ", "")
            year = int(input("Please input the year."))
            print("All classes which are available at %s, %d are:"%(term, year))
            App.classAvailableAtTerm(term, year)
        elif int(selection) == 2:
            term = input("Please input the term.")
            term = term.replace(" ", "")
            year = int(input("Please input the year."))
            instructor = input("Please input the name of instructor.")
            instructor.strip() #remove leading and trailing space
            App.classTaughtBy(instructor, term, year)
        elif int(selection) == 3:
            term = input("Please input the term.")
            term = term.replace(" ", "")
            year = int(input("Please input the year."))
            instructor1 = input("Please input the name of instructor 1.")
            instructor1.strip()  # remove leading and trailing space
            instructor2 = input("Please input the name of instructor 2.")
            instructor2.strip()  # remove leading and trailing space
            App.classTaughtBy2Instructors(instructor1, instructor2, term, year)
        elif int(selection) == 4:
            term = input("Please input the term.")
            term = term.replace(" ", "")
            year = int(input("Please input the year."))
            courseNumber = input("Please input the course number.")
            courseNumber.strip()  # remove leading and trailing space
            App.listStudentInClassAtTerm(courseNumber, term, year)
        else:
            exit()
    except:
        exit()

