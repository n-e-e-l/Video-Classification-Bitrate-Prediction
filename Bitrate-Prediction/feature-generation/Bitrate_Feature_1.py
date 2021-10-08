# -*- coding: utf-8 -*-


from google.colab import drive
drive.mount('/content/drive', force_remount=True)

import pandas as pd
data = {'filename': ['File1.mp4', 'File2.mp4', 'File3.mp4'], 'size-bytes':[22,22,22], 'height':[22,22,22], 'width':[22,22,22], 'framespersecond':[22,22,22], 'duration':[22,22,22]}
# Create DataFrame.
df = pd.DataFrame(data)

# visual aspect: width,height,framerate, video codec,length,size
# need to derive: number of words basically text features.
# audio: Sampling rate,Channels,Bit depth, audio codec
import cv2
import os
directory = r'drive/My Drive/video_file'
for filename in os.listdir(directory):
  print(filename)
  temp_name = os.path.join(directory, filename)
  size = os.path.getsize(temp_name) 
  vid = cv2.VideoCapture(temp_name)
  height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
  width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
  framespersecond= int(vid.get(cv2.CAP_PROP_FPS))
  frame_count = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
  duration = frame_count/framespersecond
  df.loc[len(df.index)] = [filename, size,height,width,framespersecond,duration]

df = df.iloc[3:]

#df

df.to_csv( "drive/My Drive/df.csv", encoding='utf-8')

