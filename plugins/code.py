from .plugin import Plugin
import random


class Code(Plugin):
    """
    Plugin template class

    API reference here:
        http://rapptz.github.io/discord.py/api.html#
    """

    title = "Code!"
    desc = "What is my purpose?"
    commands = ["!code"]

    def __init__(self): pass


    def on_message(self, client, message):
        if (message.content.startswith(self.commands[0])):
            yield from client.send_message(message.channel,message.author.name+":\n```"+message.content[5:]+"```" )
            yield from client.delete_message(message)