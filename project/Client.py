from sideFunc.Rabbitmq import logInRabbit, call
import json
"""
send a message to the server.
"""
def client():
    connectRabbit = logInRabbit()  # call the rabbit class
    connectRabbit.setServerIp("localhost")  # set the ip
    connectRabbit.connect()  # create connection
    connection = connectRabbit.getConnectObject()  # get the connection object.
    callCommands = call()  # call the rabbit's tools class.
    callCommands.setChannel(connection)  # set the channel object.
    channel = callCommands.getChannel()  # get the channel onject.
    channel.queue_declare(queue='dataBase')  # declare the queue name.
    location = input("the location of the dataBase:")  # ask for the location and the name of the database.
    country = input ("the country you want to get:")  # ask for the country name.
    date = input("the date:")  # ask for the date.
    body = {'location':location,'country':country,'date':date}  # build the body.
    channel.basic_publish(exchange='',
                          routing_key='dataBase',
                          body=json.dumps(body))  # build the message.
    print(" [x] Sent '{}'".format(body))  # print for the user what he sent.

    connectRabbit.disconnect()  # dissconect.


client()  # active the client func.
