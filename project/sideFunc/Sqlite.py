import sqlite3

class logInSqlite:
    def __init__(self):
        self.dataBase = None
        self.connection = None

    def setDataBase(self, dataBase):
        """
        set the database.
        :param dataBase: database name.
        :return:
        """
        self.dataBase = dataBase

    def getDataBase(self):
        """
        get the database
        :return: database.
        """
        return self.dataBase

    def connect(self):
        """ create a database connection to a SQLite database """
        try:
            self.connection = sqlite3.connect(self.dataBase)
            print ("connected!")
        except Exception as error:
            print ("connect() - error - {}".format(error))

    def getConnection(self):
        """
        get the connection object.
        :return: connection object.
        """
        return self.connection

    def disconnect(self):
        """
        disconnect from the database.
        """
        try:
            self.connection.close()
            print ("disconnected!")
        except Exception as error:
            print ("disconnect() - error - {}".format(error))

############################################################

class create:
    def __init__(self):
        self.cursor = None

    def setCursor(self, connection):
        """
        set a cursor object.
        :param connection: connection object.
        """
        self.cursor = connection.cursor()

    def getCursor(self):
        """
        get the cursor object.
        :return: cursor object.
        """
        return self.cursor

    def addIntoTable(self, country, table, subjects):#todo
        """
        Create a new project into the table
        :param country: country that we will add.
        :param table: table name
        :return:
        """

        if len(subjects) == 5:
            sql = ''' INSERT INTO {}{}
                      VALUES(?,?,?,?,?) '''.format(table,subjects)
        else:
            sql = ''' INSERT INTO {}{}
                                  VALUES(?,?,?,?) '''.format(table, subjects)
        self.cursor.execute(sql, country)  # add to the table

    def selectAllTasks(self, sql):
        """
        return rows from the database
        :param sql: the command.
        :return: rows
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def deleteTask(self, id, table):
        """
        Delete a task by task id
        :param table: table name.
        :param id: id of the task
        """
        sql = 'DELETE FROM {} WHERE id=?'.format(table)
        self.cursor.execute(sql, (id,))

    def deleteAllTasks(self, table):
        """
        Delete all rows in the table
        :param table: table name.
        :return:
        """
        sql = 'DELETE FROM {}'.format(table)
        self.cursor.execute(sql)
