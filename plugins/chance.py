import logging
from .plugin import Plugin
import random,asyncio

log = logging.getLogger("discord")


class Chance(Plugin):


    title = "Chance"
    desc = "Luck Based Commands"
    commands = ["!flip", "!8ball","!dice"]
    def on_message(self, client, message):
        if message.content.startswith("!flip"):
            yield from client.send_message(message.channel,random.choice(["Heads","Tails"]))
        elif message.content.startswith("!8ball"):
            yield from client.send_message(message.channel,random.choice(["Yes","No","I wouldn't bet on it","Focus more on something else","Ask yourself, is that really what you want?"]))
        elif message.content.startswith("!dice"):
            yield from client.send_message(message.channel,random.randint(1,6))
        # client.logout()

