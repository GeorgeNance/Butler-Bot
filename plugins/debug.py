from .plugin import Plugin
from datetime import datetime


class Debug(Plugin):
    """
    Plugin template class

    API reference here:
        http://rapptz.github.io/discord.py/api.html#
    """

    title = "Name of my plugin"
    desc = "What is my purpose?"
    commands = ["!debug","!reload"]
    mods = ["BudaDude"]

    def __init__(self):
        self.muted_members = ["kyle_crafty"]


    def on_message(self, client, message):
        if message.author.name  in self.mods:
            if message.content.startswith(self.commands[0]):
                try:
                    msg = eval(message.content[7:])
                    yield from client.send_message(message.channel,"``` %s ```" %msg)
                except (SyntaxError,NameError) as e:
                    yield from client.send_message(message.channel,"``` %s ```" %e)

