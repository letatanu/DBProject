from bs4 import BeautifulSoup as BS
import urllib.request as reader
from database import CursorConnectionFromPool
class Extractor:
    def __init__(self, src):
        self.Error = False
        try:
            response = reader.urlopen(src)
            self.content = response.read().decode("utf8")
        except:
            self.Error = True

    def handleContent(self):
        if not self.Error:
            data = BS(self.content, "html.parser").select('tbody tr')
            term = ""
            for id, d in enumerate(data):
                # print(d.contents)
                if len(d.contents) >= 7:
                    row = []
                    # if id >= 6:
                    for i, content in enumerate(d.contents):
                        tmp = content.text if len(content.contents) else " "
                        if i:
                            if i == 1 and 'CS ' not in tmp:
                                t = content.select("td.s0.softmerge > div")
                                if len(t):
                                    term = t[0].text
                                break
                            tmp = tmp.replace("\'", "\"")
                            row.append(tmp)
                            if len(row) == 7:
                                row.append(term)
                                print(row)
                                self.insertTable(row)
                                row = []

                else:

                    tmp = d.select('td.s0')
                    if len(tmp):
                        term = tmp[0].text
                    else:
                        tmp = d.select('td.s22')
                        if len(tmp):
                            term = tmp[0].text if len(tmp[0].text) < 13 else term


    def insertTable(self, row):
        if len(row) >= 8:
            with CursorConnectionFromPool() as cursor:
                function = "INSERT INTO project.classmetadata(course, sec ,crn ,title ,instructor ,time, notes, term ) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                print(function)
                cursor.execute(function)
                # print(row)
                # connection_pool.putconn(connection)
        else:
            print("Row is not valid")

urls = [
    "https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vSfE0gPooz0EUmOJJZzt3GmQBdIuWOlWI_GH2hPbw4T4K50xHO3LVVoLnvqCg2qsqPuU1kX6NFWs60b/pubhtml#",
    "https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vTrxONoMmcTtVlClmRiRCXlM75d168dFsX1HYAaV19R6tgYE7p1ax4HX8l9worNKILG-4a2hMtC3t7C/pubhtml#",
    "https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vQ2EGqyQJNWHH5fTSjGhsG3_rAOYQWZRVR_xacbMet1uWa-3aE89Sw4hpUvYGfYuPfqYISAqRnGhcWQ/pubhtml",
    "https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vTHprPSV1gC6_PBl5rxXCW5ijxtOCLSFz_JiFHq21SZfWDZ19OseRfzHD49h9yZd2auY0GbHM2I54q3/pubhtml"
        ]
for url in urls:
    extractor = Extractor(url)
    extractor.handleContent()


