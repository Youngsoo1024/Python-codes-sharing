import gazpacho
import json

URL = "https://en.wikipedia.org/wiki/List_of_world_records_in_swimming"
RECORDS = {0, 1, 3, 4}   
COURSES = ("LC Men", "LC Women", "SC Men", "SC Women")
WHERE = "/home/Youngsoo82/webapp"
## WHERE = ""
JSONDATA = "records.json"

html = gazpacho.get(URL)
soup = gazpacho.Soup(html)
tables = soup.find("table")
records = {}
for table, course in zip(RECORDS, COURSES):
    # each course name is a key in the "records" dictionary, which (initially) has a new empty dictionary
    # associated with it each time the outer loop iterates, the inner dictionary is set to empty
    records[course] = {}
    # The current value of "table" is used to index into the "Tables"
    # list to grab the world records table you need
    for row in tables[table].find("tr", mode = "all")[1:]:
        cols = row.find("td", mode = "all")
        event = cols[0].text
        time = cols[1].text
        # if the event contains the word "relay" ignore it.
        #only add a key/value pairing to the inner dictionary for nonrelay events.
        if "relay" not in event:
            records[course][event] = time

with open(WHERE+ JSONDATA, "w") as jf:
    json.dump(records, jf)
            