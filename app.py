from extractor import Extractor
urls = [
    "https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vSfE0gPooz0EUmOJJZzt3GmQBdIuWOlWI_GH2hPbw4T4K50xHO3LVVoLnvqCg2qsqPuU1kX6NFWs60b/pubhtml#",
    "https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vTrxONoMmcTtVlClmRiRCXlM75d168dFsX1HYAaV19R6tgYE7p1ax4HX8l9worNKILG-4a2hMtC3t7C/pubhtml#",
    "https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vQ2EGqyQJNWHH5fTSjGhsG3_rAOYQWZRVR_xacbMet1uWa-3aE89Sw4hpUvYGfYuPfqYISAqRnGhcWQ/pubhtml",
    "https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vTHprPSV1gC6_PBl5rxXCW5ijxtOCLSFz_JiFHq21SZfWDZ19OseRfzHD49h9yZd2auY0GbHM2I54q3/pubhtml"
        ]
for url in urls:
    extractor = Extractor(url)
    extractor.handleContent()

