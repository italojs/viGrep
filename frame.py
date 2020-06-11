import pytesseract 
import re

class Frame(object):
    def __init__(self, image, time, id, regex):
        self.image = image
        self.time = time
        self.id = id
        self.regex = regex
        self.text = ""
        self.matches = []

    def process(self):
        text = pytesseract.image_to_string(self.image)
        self.text = text.replace('\n', '')
        self.matches = re.findall(self.regex, text)
        return self.text, self.matches