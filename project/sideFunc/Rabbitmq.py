import pika


class logInRabbit:
    def __init__(self):
        self.ip = None
        self.connection = None

    def setServerIp(self, ip):
        """
        :param ip: set server's ip.
        """
        self.ip = ip

    def getServerIp(self):
        """
        return server's ip.
        """
        return self.ip

    def connect(self):
        """ create a database connection to a SQLite database """
        try:
            self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.ip))
            print ("connected!")
        except Exception as error:
            print ("connect() - error - {}".format(error))

    def getConnectObject(self):
        """
        get connection object.
        """
        return self.connection

    def disconnect(self):
        """
        disconnect from the server.
        :return:
        """
        try:
            self.connection.close()
            print ("disconnected!")
        except Exception as error:
            print ("disconnect() - error - {}".format(error))

#################################################################

class call:
    def __init__(self):
        self.channel = None

    def setChannel(self, connection):
        """set channel object"""
        self.channel = connection.channel()

    def getChannel(self):
        """get the channel object"""
        return self.channel
