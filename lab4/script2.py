from moviepy.editor import *
from PIL import Image
from argparse import ArgumentParser

if __name__ == "__main__":
    argumentParser = ArgumentParser()
    argumentParser.add_argument("file_name")
    argumentParser.add_argument("start_time")
    argumentParser.add_argument("end_time")
    argumentParser.add_argument("save_path")
    argumentParser.add_argument("-step", default=10, required=False)
    clip = VideoFileClip(argumentParser.parse_args().file_name)
    startTime, endTime = float(argumentParser.parse_args().start_time), float(argumentParser.parse_args().end_time)
    if (startTime >= endTime) or (startTime < 0) or (endTime > clip.duration):
        print("Incorrect fragment boundaries")
    else:
        subClip = clip.subclip(startTime, endTime)
        curFrame, step = 0, int(argumentParser.parse_args().step)
        savePath = argumentParser.parse_args().save_path
        while curFrame / subClip.fps < subClip.duration:
            img = Image.fromarray(clip.get_frame(curFrame / subClip.fps)).resize((250, 250))
            img.save(f'{savePath}/{curFrame}.jpg')
            curFrame += step    