from .plugin import Plugin
import random


class Jokes(Plugin):
    """
    Plugin template class

    API reference here:
        http://rapptz.github.io/discord.py/api.html#
    """

    title = "Jokes"
    desc = "What is my purpose?"
    commands = ["!joke", "!tellmeajoke"]

    def __init__(self): pass


    def on_message(self, client, message):
        if (message.content.startswith(self.commands[0])):
            f = open("jokes.txt", "r").read().splitlines()
            joke = random.choice(f)
            yield from client.send_message(message.channel, str(joke))
