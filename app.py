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

if __name__ == '__main__':
    selection = input("Input the task number you want to do. \n"
                      "1. See all available courses at a specific term.\n"
                      "2. See all available courses taught by a certain instructor at a specific term, year.\n"
                      "3. Which classes are taught by 2-3 specific instructors?\n"
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
        else:
            exit()
    except:
        exit()