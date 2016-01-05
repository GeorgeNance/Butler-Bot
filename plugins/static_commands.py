from .plugin import Plugin
import csv


class StaticCommands(Plugin):
    """
    Plugin template class

    API reference here:
        http://rapptz.github.io/discord.py/api.html#
    """

    title = "Custom Commands"
    desc = "Simple Text Commands"

    commands = ["!addcommand", "!removecommand"]

    custom_commands = {}

    def __init__(self):
        pass


    def on_message(self, client, message):
        # #Create a new command
        # if message.content.startswith(self.commands[0]):
        #     if len(message.content) > 13:
        #        split_msg=message.content[12:].split(" ")
        #        if (split_msg[0].startswith("!")):
        #            key=split_msg[0]
        #            val = ''.join(split_msg[1:])
        #            self.custom_commands["!"+key]=val;
        #            client.send_message(message.channel,"Command added. Use "+key+" to use it")
        #            self.save_commands()
        #            self.add_customcommands_to_commands()
        #     else:
        #         client.send_message(message.channel,"Enter a new command seperated by spaces like this "
        #                                             "\n!addcommand !CommandName MyResponse")
        self.reload_commands()
        # Remove a command
        if message.content.startswith(self.commands[1]): pass

        for command in self.custom_commands.keys():
            if command in message.content:
                yield from client.send_message(message.channel, self.custom_commands[command])

    def save_commands(self):
        with open("customcommands.csv", "wb") as csvfile:
            writer = csv.DictWriter(csvfile, self.custom_commands.items())
            for key, value in self.custom_commands.items():
                writer.writerow([key, value])

    def reload_commands(self):
        with open("customcommands.csv") as csvfile:
            csvReader = csv.reader
            for line in csvReader(csvfile):
                self.custom_commands[line[0]] = line[1]
            for command in self.custom_commands:
                self.commands.append(command)
