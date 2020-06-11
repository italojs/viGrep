import re
import cv2
import pytesseract 

class Video(object):
    def __init__(self, url, regex):
        self.cap = cv2.VideoCapture(url)
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.cts = 0.0
        self.regex = re.compile(regex)

    def __matchRegex(self, frame):
        text = pytesseract.image_to_string(frame)
        text = text.replace('\n', '')
        return text, re.findall(self.regex, text)

    def __getFrameSeconds(self):
        ts = self.cap.get(cv2.CAP_PROP_POS_MSEC) #timestamp
        self.cts = self.cts + 1000/self.fps

        return abs(ts - self.cts)/1000
    
    def process(self, callback = None):
        frames = []
        while(self.cap.isOpened()):
            done, frame = self.cap.read()
            if not done:
                break
            text, matches = self.__matchRegex(frame)
            if len(matches) == 0:
                continue

            sec = self.__getFrameSeconds()
            frameId = self.cap.get(cv2.CAP_PROP_POS_FRAMES)

            data = {"id": int(frameId),
                "second": sec,
                "matches": matches,
                "text": text}

            frames.append(data)
            yield data

        self.cap.release()
        if callback:
            callback(frames)

        

    