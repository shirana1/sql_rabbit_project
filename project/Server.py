
from sideFunc.Rabbitmq import logInRabbit , call
import json
from main import main
"""
get a message from the client and active the main func .
after that the server disconnect.
"""
def server():
    connectRabbit = logInRabbit()  # call the rabbit class
    connectRabbit.setServerIp("localhost")  # set the ip
    connectRabbit.connect()  # create connection
    connection = connectRabbit.getConnectObject()  # get the connection object.

    callCommands = call()  # call the rabbit's tools class.
    callCommands.setChannel(connection)  # set the channel object.
    channel = callCommands.getChannel()  # get the channel onject.
    channel.queue_declare(queue='dataBase')  # declare the queue name.

    def callback(ch, method, properties, body):  # catch the message.
        print ("received :{}".format(body))  # print what it got.
        results = json.loads(body)  # translate the str message to dict.
        main(results)  # active the main func with the message.

    channel.basic_consume('dataBase',callback,True)  #say to the program to catch all the messages with the name 'database'.
    print(' [*] Waiting for messages. To exit press CTRL+C')  # writing to the 'admin'.
    channel.start_consuming()  # start to consum the messages.
    #connectRabbit.disconnect()  # disconnect.

server()