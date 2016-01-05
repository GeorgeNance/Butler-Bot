from .plugin import Plugin
import time
import datetime,math


class Time(Plugin):
    """
    Plugin template class

    API reference here:
        http://rapptz.github.io/discord.py/api.html#
    """

    title = "Time"
    desc = "What is my purpose?"
    commands = ["!time","!ld"]

    def __init__(self): pass



    def on_message(self, client, message):
        if message.content.startswith(self.commands[0]) :
            yield from client.send_message(message.channel,time.time())
        if message.content.startswith(self.commands[1]):


            #
            # Ludum Dare
            #


            if (datetime.datetime.now() < datetime.datetime(2015,12,11,20,0,0,0)):

                diff = datetime.datetime(2015,12,11,20,0) - datetime.datetime.now()

                days, seconds = diff.days, diff.seconds
                hours = (days * 24) + seconds // 3600
                minutes = (seconds % 3600) // 60
                yield from client.send_message(message.channel,"The compo begins in %s hours and  %s minutes\n\nhttp://ludumdare.com/compo/"% (hours,minutes))
            else:
                diff = datetime.datetime(2015,12,14,20,0) - datetime.datetime.now()
                days, seconds = diff.days, diff.seconds
                hours = (days * 24) + seconds // 3600
                minutes = (seconds % 3600) // 60
                yield from client.send_message(message.channel,"The compo ends in %s hours and  %s minutes\n\nhttp://ludumdare.com/compo/"% (hours,minutes))



