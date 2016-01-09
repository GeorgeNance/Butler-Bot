from .plugin import Plugin
import random
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

class TextImage(Plugin):
    """
    Plugin template class

    API reference here:
        http://rapptz.github.io/discord.py/api.html#
    """

    title = "Text Image"
    desc = "What is my purpose?"
    commands = ["!rip"]

    def __init__(self): pass


    def on_message(self, client, message):
        if (message.content.startswith(self.commands[0])):
            self.create_text_image(str(message.content)[5:],"grave.png")
            with open("output.jpg","r",) as image:
                yield from client.send_file(message.channel,"output.jpg")


    def create_text_image(self,text,image):
        img = Image.open("images/"+image)

        font = ImageFont.truetype("OpenSans-Regular.ttf", 64)

        # make a blank image for the text, initialized to transparent text color
        draw = ImageDraw.Draw(img)
        draw.text((img.width/2 - draw.textsize(text, font)[0], img.height/2),text,(50,50,50),font=font)

        img.save('output.jpg')
        print("saved file")