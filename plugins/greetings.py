from .plugin import Plugin





class GreetingPlugin(Plugin):
    """
	Plugin template class

	API reference here:
		http://rapptz.github.io/discord.py/api.html#
	"""

    title = "Greeting plugin"
    desc = "Greet people that enter the channel"
    def __init__(self):
        pass


    def on_member_join(self, client, member):
        # get the default text-channel
        channel = yield from member.server.get_default_channel()

        yield from client.send_message(channel, "Welcome, %s!" % member.name)

    def on_member_remove(self, client, member):
        # get the default text-channel
        channel = yield from member.server.get_default_channel()

        yield from client.send_message(channel, "You lill shit you think u can leave like that, %s" % member.name)
