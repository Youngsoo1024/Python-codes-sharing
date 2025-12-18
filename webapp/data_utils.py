import DBcm

##db_details = "CoachDB.sqlite3"

import platform

if "aws" in platform.uname().release:
    db_details = {
        "host": "Youngsoo82.mysql.pythonanywhere-services.com",
        "database": "Youngsoo82$default",
        "user": "Youngsoo82",
        "password": "Kysp5448**",   
    }
else:
    # Running locally.
    db_details = {
        "host": "localhost",
        "database": "swimDB",
        "user": "swimuser",
        "password": "swimpasswd"
    }

db_details = {
    "host": "localhost",
    "database": "swimDB",
    "user": "swimuser",
    "password": "swimpasswd"
}

from queries import *

def get_swim_sessions():
    """Return a tuple-list of unique session timestamps."""
    with DBcm.UseDatabase(db_details) as db:
        db.execute(SQL_SESSIONS)
        results = db.fetchall()
    return results

def get_session_swimmers(date):
    """When given a date (YYYY-MM-DD), return a tuple-list of swimmers
    and their associated age (filtered by data)"""
    with DBcm.UseDatabase(db_details) as db:
        db.execute(SQL_SWIMMERS_BY_SESSION, (date,))
        results = db.fetchall()
    return results

def get_swimmers_events(name, age, date):
    """When gibven a date (YYYY-MM-DD), swimmer name, and age, return a tuple-list of events
    the swimmer swam on that date."""
    with DBcm.UseDatabase(db_details) as db:
        db.execute(SQL_SWIMMERS_EVENTS_BY_SESSION, (name, age, date,))
        results = db.fetchall()
    return results

def get_swimmers_times(name, age, distance, stroke, date):
    """When given a date (YYYY-MM-DD), swimmer name, age, distance, and stroke,
    return a tuple-list of times the swimmer swam on that date over the identified
    distance/stroke combination."""
    with DBcm.UseDatabase(db_details) as db:
        db.execute(SQL_CHART_DATA_BY_SWIMMER_EVENT_SESSION, (name, age, distance, stroke, date,))
        results = db.fetchall()
    return results