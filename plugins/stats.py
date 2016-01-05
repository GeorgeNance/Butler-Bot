from .plugin import Plugin
import os,time
from nltk.corpus import stopwords
import collections
import asyncio


class Stats(Plugin):
    """
    Plugin template class

    API reference here:
        http://rapptz.github.io/discord.py/api.html#
    """

    title = "Name of my plugin"
    desc = "What is my purpose?"
    commands = ["!top"]

    def __init__(self): pass

    def on_message(self, client, message):

        if message.content.startswith('!top'):
            authors = []
            words = []
            for message in client.logs_from(message.channel,limit=2000):
                if message.author.name != "ButlerBot":
                    authors.append(str(message.author))
                if message.author != client.user and not message.content.startswith("!"):
                    for word in str(message.content).split():
                            words.append(str(word))
            yield from client.send_message(message.channel,"__Most Popular Words:__ \n\n"+self.popularWords(words))
            yield from client.send_message(message.channel,"__Most Spammy Users:__ \n\n"+self.popularWords(authors))


    def popularWords(self,words):
        filtered_words = [word for word in words if word.lower() not in stopwords.words('english')]
        counter = collections.Counter(filtered_words).most_common(10)
        message = ""
        count = 1
        for key,value in (counter):
            message+="**"+str(count)+"**. "+str(key)+" : *"+str(value)+"*\n"
            count+=1
        return message
