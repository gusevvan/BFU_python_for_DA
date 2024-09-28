from moviepy.editor import *
from argparse import ArgumentParser

if __name__ == "__main__":
    argumentParser = ArgumentParser()
    argumentParser.add_argument("file_name")
    argumentParser.add_argument("start_time")
    argumentParser.add_argument("end_time")
    clip = VideoFileClip(argumentParser.parse_args().file_name)
    startTime, endTime = float(argumentParser.parse_args().start_time), float(argumentParser.parse_args().end_time)
    if (startTime >= endTime) or (startTime < 0) or (endTime > clip.duration):
        print("Incorrect fragment boundaries")
    else:
        clip.subclip(startTime, endTime).write_videofile('subclip.mp4')
