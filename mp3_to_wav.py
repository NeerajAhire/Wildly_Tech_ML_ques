import os
from pydub import AudioSegment

def mp3_to_wav(source, destination):
    dir_list = os.listdir(source)
    for i in dir_list:
        path = source + "\\" + i
        sound = AudioSegment.from_mp3(path)
        output_file = os.path.basename(path).split(".")[0] + ".wav"
        sound.export(destination + "\\" + output_file, format="wav")
