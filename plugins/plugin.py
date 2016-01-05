# a simple Python plugin loading system
# see https://gist.github.com/will-hart/5899567

import asyncio


class PluginMount(type):
    """
    A plugin mount point derived from:
        http://martyalchin.com/2008/jan/10/simple-plugin-framework/

    Acts as a metaclass which creates anything inheriting from Plugin
    """

    def __init__(cls, name, bases, attrs):
        if not hasattr(cls, "plugins"):
            cls.plugins = []
        else:
            cls.register_plugin(cls)

    def register_plugin(cls, plugin):
        instance = plugin()
        cls.plugins.append(instance)


class Plugin(metaclass=PluginMount):
    """
    Plugin template class

    API reference here:
        http://rapptz.github.io/discord.py/api.html#
    """

    title = "Name of my plugin"
    desc = "What is my purpose?"
    commands = []

    @asyncio.coroutine
    def on_ready(self, client): pass

    @asyncio.coroutine
    def on_message(self, client, message): pass

    @asyncio.coroutine
    def on_socket_closed(self, client): pass

    @asyncio.coroutine
    def on_message_delete(self, client, message): pass

    @asyncio.coroutine
    def on_message_edit(self, client, before, after): pass

    @asyncio.coroutine
    def on_status(self, client, member): pass

    @asyncio.coroutine
    def on_channel_delete(self, client, channel): pass

    @asyncio.coroutine
    def on_channel_create(self, client, channel): pass

    @asyncio.coroutine
    def on_channel_update(self, client, channel): pass

    @asyncio.coroutine
    def on_member_join(self, client, member): pass

    @asyncio.coroutine
    def on_member_remove(self, client, member): pass

    @asyncio.coroutine
    def on_member_update(self, client, member): pass

    @asyncio.coroutine
    def on_server_create(self, client, server): pass

    @asyncio.coroutine
    def on_server_delete(self, client, server): pass

    @asyncio.coroutine
    def on_server_role_create(self, client, server, role): pass

    @asyncio.coroutine
    def on_server_role_delete(self, client, server, role): pass

    @asyncio.coroutine
    def on_server_role_update(self, client, role): pass

    @asyncio.coroutine
    def on_voice_state_update(self, client, member): pass
