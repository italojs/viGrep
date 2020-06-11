import re
import cv2
import numpy as np
from frame import Frame
from multiprocessing import Pool
from multiprocessing import cpu_count



def processFrames(params):
    batchId, batch, callback = params
    print(batchId)
    for frame in batch:
        frame.process()
        if callback is not None:
            callback(batchId, frame)

class Video(object):
    def __init__(self, url, regex):
        self.cap = cv2.VideoCapture(url)
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.cts = 0.0
        self.regex = re.compile(regex)
        self.frames = []

    def __getFrameTime(self):
        ts = self.cap.get(cv2.CAP_PROP_POS_MSEC) #timestamp
        self.cts = self.cts + 1000/self.fps

        return abs(ts - self.cts)/1000
    
    def loadFrames(self):
        while(self.cap.isOpened()):
            done, img = self.cap.read()
            if not done:
                break

            frame = Frame(
                img, 
                float(self.__getFrameTime()),
                int(self.cap.get(cv2.CAP_PROP_POS_FRAMES)),
                self.regex
            )

            self.frames.append(frame)
        self.cap.release()
    
    def __divideFramesInBatchs(self, batchsQuantity):
        batchSize = len(self.frames) / float(batchsQuantity)
        batchSize = int(np.ceil(batchSize))

        for i in range(0, len(self.frames), batchSize):
            yield self.frames[i: i + batchSize]

    def process(self, callback = None, pools = 1):
        if len(self.frames) == 0:
            self.loadFrames()

        batches = list(self.__divideFramesInBatchs(pools))

        params = []
        for i, batch in enumerate(batches):
            params.append((i, batch, callback))

        pool = Pool(processes=pools)
        pool.map_async(processFrames, params)

        del batches
        del params
        del self.frames
        del self.cap

        pool.close()
        pool.join()

        

    