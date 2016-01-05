from .plugin import Plugin


class Mod(Plugin):
    """
    Plugin template class

    API reference here:
        http://rapptz.github.io/discord.py/api.html#
    """

    title = "Name of my plugin"
    desc = "What is my purpose?"
    commands = ["!delete", "!mute", "!unmute"]
    mods = ["BudaDude"]

    def __init__(self):
        self.muted_members = ["kyle_crafty"]

    def on_message(self, client, message):
        if message.author.name in self.mods:
            if message.content.startswith(self.commands[0]):
                number = int(message.content[8:])
                messege_log = yield from client.logs_from(message.channel, before=message, limit=number);
                for msg in messege_log:
                    yield from client.delete_message(msg)

                yield from client.delete_message(message)
                #
                # move a person to a role of mute
                #
