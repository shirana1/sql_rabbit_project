from sideFunc.Sqlite import *
from sideFunc.tools import *
from sideFunc.dataBase2_1 import countries1
from sideFunc.dataBase2_3 import countries3
import xml.etree.cElementTree as etree
import os
import datetime
"""
Description = open a server , get your information and return a csv, json and xml files.

"""

baseFolder = ""
countryData = """ CREATE TABLE IF NOT EXISTS countryData (
                                       id integer PRIMARY KEY,
                                       name text NOT NULL,
                                       date integer,
                                       numberOfBuying integer,
                                       listOfAlbums text
                                   ); """
countryData3 = """ CREATE TABLE IF NOT EXISTS countryData3 (
                                       id integer PRIMARY KEY,
                                       name text NOT NULL,
                                       date integer,
                                       numberOfsells integer,
                                       diskNames text,
                                       type text
                                   ); """

def createDataBase2_1(cursor, createObject): #todo
    """
    create a new table every time its run.
    :param cursor: the cursor object
    :param createObject: the createObject object
    :return:
    """
    try:  # try to do the command
        dropTableStatement = "DROP TABLE countryData"  # command
        cursor.execute(dropTableStatement)  # execute the command.
    except Exception :  # pass if fail (happens when there is no table in the first place).
        pass
    cursor.execute(countryData)  # create the table.
    subjects = ("name", "date", "numberOfBuying", "listOfAlbums")
    for country in countries1 :
        project_id = createObject.addIntoTable(country, "countryData", subjects) # add the rows into the table.

def createDataBase2_3(cursor, createObject):#todo
    """
        create a new table every time its run.
        :param cursor: the cursor object
        :param createObject: the createObject object
        :return:
        """
    try:  # try to do the command
        dropTableStatement = "DROP TABLE countryData3"  # command
        cursor.execute(dropTableStatement)  # execute the command.
    except Exception:  # pass if fail (happens when there is no table in the first place).
        pass
    cursor.execute(countryData3)  # create the table.
    subjects = ("name","date","numberOfsells","diskNames","type")
    for country in countries3:
        project_id = createObject.addIntoTable(country, "countryData3", subjects)  # add the rows into the table.


def main(results):  # the main func
    now = datetime.datetime.now()
    timeFormat = now.strftime("%d_%m_%y-%H_%M_%S")
    location = createDirectory(baseFolder+"results")
    connectSqlite = logInSqlite()  # call  the sqlite class
    if os.path.isfile(results["location"]):  # check if you gave the right location and file.
        connectSqlite.setDataBase(results["location"])  # set the database
        connectSqlite.connect()  # connect to the database.
        connection = connectSqlite.getConnection()  # get the connection object.
        createObject = create()  # call the sqlite create class (sqlite tools).
        createObject.setCursor(connection)  # set a cursor as our command tool.
        cursor = createObject.getCursor()  # get the cursor object.

        createDataBase2_1(cursor, createObject)  # update the database. (if the user changed the database)
        #get the rows with the same country and date that the user gave us.
        sql = """SELECT * FROM countryData WHERE date = '{}' AND name = '{}';""".format(results["date"],results["country"])
        found = createObject.selectAllTasks(sql)

        if found:  # check if we found some results
            path = createDirectory("{}{}".format(location,timeFormat))
            subjects = (list(map(lambda x: x[0], cursor.description)))  # get the subjects of the database
            subjectsToPutIn = ["name", "numberOfBuying"]  # the subjects we need for the csv.
            writeToCSV(path=path, rows=found, subject=subjects, subjectsToPutIn=subjectsToPutIn)  # write to csv.
            subjectsToPutIn = ["name", "listOfAlbums"]  # the subjects we need for the json file.
            writeDictToFile(path + "result.json", rows=found, subject=subjects, subjectsToPutIn=subjectsToPutIn)  # write to json file.
            connection.commit()  # save the actions we did (if we did any).
            print(found)
            print ("done!")  # print if the program finished.


        else:  # if we didnt find a results print error and finish.
            print ("couldn't find a results for your search database: 2_1. please try again.")

        createDataBase2_3(cursor, createObject)  # create the 2_3 database
        # get the higher seller from the chosen country (try israel , 2005 . )
        sql = """SELECT * FROM countryData3 WHERE date >= '{0}' AND name = '{1}' AND numberOfsells=(SELECT MAX(numberOfsells) FROM countryData3 WHERE name = '{1}' AND type = 'ROCK') ;""".format(
            results["date"], results["country"])
        found = createObject.selectAllTasks(sql)  # found

        if found:
            path = createDirectory("{}{}".format(location, timeFormat))
            writeToXml(path+"result.xml",found)  # write to xml file.
            print (found)
        else:  # if we didnt find a results print error and finish.
            print("couldn't find a results for your search database: 2_3. please try again.")
        connectSqlite.disconnect()  # disconnect from the database.

    else:  # if the user didnt put the right path print error and finish.
        print ("invalid location! please try again...")
