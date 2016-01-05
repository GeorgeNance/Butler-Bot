from .plugin import Plugin
from wikipedia import *


class Wikipedia(Plugin):
    """
    Plugin template class

    API reference here:
        http://rapptz.github.io/discord.py/api.html#
    """

    title = "Wikipedia"
    desc = "What is my purpose?"
    commands = ["!wiki"]

    def __init__(self): pass


    def on_message(self, client, message):
        if (message.content.startswith(self.commands[0])):
            try:
                w = wikipedia.page(message.content[6:])
                return client.send_message(message.channel, w.url)


            except PageError:
                 yield from client.send_message(message.channel, "I could not find that page")
            except DisambiguationError as e:
                yield from client.send_message(message.channel, "Do you mean \n"+str(e.options))
