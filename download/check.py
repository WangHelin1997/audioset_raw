import librosa
import os
audio_path = '/home/helin.wang/audioset/audioset_raw/download/train'
listx=[]
for root, dirs, files in os.walk(audio_path):
    for x in files:
        audio = audio_path+ '/'+x
        time = librosa.get_duration(filename=audio)
        if(time>0):
            print(x)
            listx.append(x)
print(len(listx))