import discord, threading, sys, asyncio
from plugins import Plugin

client = discord.Client()

f = open("auth.txt", "r").read().splitlines()



@client.async_event
def on_message(message):
    for plugin in Plugin.plugins:
        if hasattr(plugin, "on_message"):
            yield from plugin.on_message(client, message)


@client.async_event
def on_member_join(self, member):
    for plugin in Plugin.plugins:
        if hasattr(plugin, "on_member_join"):
            yield from plugin.on_member_join(client, member)


@client.async_event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    for plugin in Plugin.plugins:
        if hasattr(plugin, "on_ready"):
            yield from plugin.on_ready(client)


def main_task():
    yield from client.login(f[0], f[1])
    yield from client.connect()


loop = asyncio.get_event_loop()
loop.run_until_complete(main_task())
loop.close()
