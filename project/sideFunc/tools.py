import os
import pandas as pd
import json

##################################################################
def createDirectory(fileName):  # create a directory.
    """
    create directory (if its doesnt exist) and return its location.
    :return: directory location
    """
    storeDir = "%s/" % fileName
    try:
        if not os.path.isdir(storeDir):  #check if the directory allready exist.
                os.mkdir(storeDir)  # create directory.

    except Exception as error:
        print ("createDirectory()-couldn't create your directory.")

    finally:
        return storeDir

##################################################################
def loadDictFromFile(fileName):  # load dict from file.
    """
    load the dict from the file.
    :return dict
    """
    dict = {}  # where we will put the dict.
    try:
        with open(fileName, "r") as read:
            dict = json.load(read)  #load dict
            read.close()
        #logger.info("loadDictFromFile()-ended without problems-loaded-{}" .format(fileName))
    except Exception as error:
        print ("loadDictFromFile - error - {}".format(error))
        #logger.error("loadDictFromFile() func:error-{}" .format(error))

    finally:
        return dict

##################################################################
def writeDictToFile(fileName, rows , subject, subjectsToPutIn):
    """
    write the dict from the file.
    :param fileName on the base folder, dictionary.
    :return None
    """
    try:
        dict = createDict(rows , subject, subjectsToPutIn)
        if "listOfAlbums" in dict:
            for index,album in enumerate(dict["listOfAlbums"]):
                if album is not list and "[" in album:
                    dict["listOfAlbums"][index] = json.loads(album)

        with open(fileName, "w") as writeFile:
            json.dump(dict,writeFile)
            writeFile.close()
    except Exception as error:
        print("writeDictToFile - error - {}".format(error))
        #logger.error("writeDictToFile() func:error-{}" .format(error))

def createDict(rows , subject, subjectsToPutIn):
    try:
        dict = {}
        for row in rows:  # run on the rows of the dataBase
            for index, data in enumerate(row):  # get data from row (name, id ...)
                if subject[
                    index] in subjectsToPutIn:  # check if subject == the subject we want (name or number of buying)
                    if subject[index] in dict:  # if the subject is already on the dict.
                        dict[subject[index]].append(data)  # add it (add the data)
                    else:  # if not
                        dict[subject[index]] = []  # create the subject
                        dict[subject[index]].append(data)  # add the data that created it.
        return dict
    except Exception as error:
        print("createDict - error - {}".format(error))
        # logger.error("writeToCSV() func:error-{}" .format(error))

def writeToCSV(path, rows , subject, subjectsToPutIn):
    try:
        dict = createDict(rows , subject, subjectsToPutIn)
        dataFrame = pd.DataFrame(dict) #create dataFrame
        dataFrame.to_csv(path+"output.csv",index=False) # put it on csv

    except Exception as error:
        print("writeToCSV - error - {}".format(error))
        # logger.error("writeToCSV() func:error-{}" .format(error))

def readFromCSV():#todo
    try:
        return 0
    except Exception as error:
        print("readFromCSV - error - {}".format(error))
        # logger.error("readFromCSV() func:error-{}" .format(error))

def writeToXml(outfileName,rows):
    """
    write to xml
    :param outfileName: file name
    :param rows: rows to write.
    :return:
    """
    try:
        outfile = open(outfileName, 'w')
        outfile.write('<?xml version="1.0" ?>\n')
        outfile.write('<mydata>\n')
        for row in rows:
            outfile.write('  <row>\n')
            outfile.write('    <name>%s</name>\n' % row[0])
            outfile.write('    <date>%s</date>\n' % row[1])
            outfile.write('    <numberOfsells>%s</numberOfsells>\n' % row[2])
            outfile.write('    <diskNames>%s</diskNames>\n' % row[3])
            outfile.write('  </row>\n')
        outfile.write('</mydata>\n')
        outfile.close()
    except Exception as error:
        print("writeToXml - error - {}".format(error))
        # logger.error("writeToXml() func:error-{}" .format(error))