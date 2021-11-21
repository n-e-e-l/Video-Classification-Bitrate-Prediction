#make folder  for each mp3 file and then divide the mp3 file into 30secs chunck
import os
import subprocess 

i = 0
directory = r'location\Video_Data\'
for filename in os.listdir(directory):
    if filename.endswith(".wav"):
        temp_name=os.path.join(directory, filename)
        fold_name = temp_name.replace(".wav",'')
        print(fold_name)
        os.makedirs(fold_name)
        #i = i + 1
        temp_name=os.path.join(directory, filename)
        command = "ffmpeg -i " + temp_name + " -c copy -map 0 -segment_time 00:00:30 -f segment "+ fold_name + "\\" + "%03d.wav"
        #print(command)
        subprocess.call(command, shell=True)
    else:
        continue