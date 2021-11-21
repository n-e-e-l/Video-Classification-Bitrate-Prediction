import os
import moviepy.editor as mp

directory = r'location\Video_Data\'
for filename in os.listdir(directory):
    if filename.endswith(".mp4") or filename.endswith(".mpg"):
        full_file = os.path.join(directory, filename)
        print(full_file)
        my_clip = mp.VideoFileClip(full_file)
        full_file = full_file.replace(".mp4",'')
        full_file = full_file.replace(".mpg",'')
        my_clip.audio.write_audiofile(full_file+"_result"+".mp3")
        #print(os.path.join(directory, filename))
    else:
        continue