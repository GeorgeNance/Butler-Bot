from .plugin import Plugin
import random


class Info(Plugin):
    """
    Plugin template class

    API reference here:
        http://rapptz.github.io/discord.py/api.html#
    """

    title = "Name of my plugin"
    desc = "What is my purpose?"
    commands = ["!id"]

    def __init__(self): pass


    def on_message(self, client, message):
        client.send_message(client,str(message.channel.id))


