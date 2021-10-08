#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data = {'filename': ['File1.mp4', 'File2.mp4', 'File3.mp4'], 'bit_rate_mode':[22,22,22],
 'channel_layout':[22,22,22],
 'channel_positions':[22,22,22],
 'channel_s':[22,22,22],
 'frame_count':[22,22,22],
 'proportion_of_this_stream':[22,22,22],
 'stream_size':[22,22,22],
 'codec_id':[22,22,22],
 'other_bit_rate_mode':[22,22,22],
 'samples_per_frame':[22,22,22]}
# Create DataFrame.
df = pd.DataFrame(data)
from pprint import pprint
from pymediainfo import MediaInfo
#mediainfo = MediaInfo.parse(r'H:\Thesis_data\non-animated\Testing\44_nonanimatedtesting.mp4')


# In[2]:



import os
from pprint import pprint
from pymediainfo import MediaInfo
directory = r'/Data/My Drive/video_file'
i=0
import subprocess 
import re
for filename in os.listdir(directory):
    if filename.endswith(".mp4"):
        temp_name=os.path.join(directory, filename)
        #print(temp_name)
        mediainfo = MediaInfo.parse(temp_name)
        #print(mediainfo.to_data())
        for track in mediainfo.tracks:
            if track.track_type == "Video":
                print("Bit rate: {t.bit_rate}, Frame rate: {t.frame_rate}, "
                      "Format: {t.format}".format(t=track))
                #pprint(track.to_data())
        #for track in mediainfo.tracks:
        #    if track.track_type == "Video":
                #print("Bit rate: {t.bit_rate}, Frame rate: {t.frame_rate}, "
              #"Format: {t.format}".format(t=track))
                #track.to_data()
            res = dict((k, (track.to_data()[k])) for k in ['bit_rate_mode','channel_layout','channel_positions','channel_s','sample_count','stream_size','codec_id',
                                  'other_bit_rate_mode','frame_count','proportion_of_this_stream','channel_positions','channel_layout','samples_per_frame'] if k in (track.to_data()))
            channel_s = res.get('channel_s')
                #print(channel_s)
            #print(res)
            bit_rate_mode = res.get('bit_rate_mode'),
            channel_layout = res.get('channel_layout'),
            channel_positions = res.get('channel_positions'),
            frame_count = res.get('frame_count'),
            proportion_of_this_stream = res.get('proportion_of_this_stream'),
            stream_size = res.get('stream_size'),
            codec_id = res.get('codec_id'),
            other_bit_rate_mode = res.get('other_bit_rate_mode'),
            samples_per_frame = res.get('samples_per_frame')
        df.loc[len(df.index)] = [filename,bit_rate_mode,channel_layout,channel_positions,channel_s,frame_count,proportion_of_this_stream,stream_size,codec_id,other_bit_rate_mode,samples_per_frame]
        #pprint(track.to_data())
        print(filename)
        #print(len(i_frame))
        #print(len(b_frame))
        #print(len(p_frame))
        #df.loc[len(df.index)] = [filename,bit_rate_mode,channel_layout,channel_positions,channel_s,frame_count,proportion_of_this_stream,stream_size,codec_id,other_bit_rate_mode,samples_per_frame]
        
        #ffprobe -show_frames H:\Thesis_data\test\33_nonanimatedvalidation.mp4 > H:\Thesis_data\test\33_nonanimatedvalidation_outputfile.txt


# In[3]:


df


# In[4]:


df = df.iloc[3:]


# In[5]:


df.reset_index(inplace=True,drop=True)


# In[6]:


#df.drop()
df.drop(['codec_id','samples_per_frame'], axis=1, inplace=True)

#df["samples_per_frame"].nunique()


# In[7]:


df


# In[8]:


df['bit_rate_mode']=df['bit_rate_mode'].map(lambda x: str(x)[:-2])
df['channel_layout']=df['channel_layout'].map(lambda x: str(x)[:-2])
df['channel_positions']=df['channel_positions'].map(lambda x: str(x)[:-2])
df['frame_count']=df['frame_count'].map(lambda x: str(x)[:-2])
df['proportion_of_this_stream']=df['proportion_of_this_stream'].map(lambda x: str(x)[:-2])
df['stream_size']=df['stream_size'].map(lambda x: str(x)[:-2])
df['other_bit_rate_mode']=df['other_bit_rate_mode'].map(lambda x: str(x)[:-3])


# In[9]:


#df['frame_count'] = df['frame_count'].map(lambda x: str(x)[1:])

df['bit_rate_mode']=df['bit_rate_mode'].map(lambda x: str(x)[1:])
df['channel_layout']=df['channel_layout'].map(lambda x: str(x)[1:])
df['channel_positions']=df['channel_positions'].map(lambda x: str(x)[1:])
df['frame_count']=df['frame_count'].map(lambda x: str(x)[1:])
df['proportion_of_this_stream']=df['proportion_of_this_stream'].map(lambda x: str(x)[1:])
df['stream_size']=df['stream_size'].map(lambda x: str(x)[1:])
df['other_bit_rate_mode']=df['other_bit_rate_mode'].map(lambda x: str(x)[2:])


# In[10]:


df


# In[11]:


#df['frame_count']=df['frame_count'].astype(int)
df['frame_count'] = df['frame_count'].str.replace("'", '').astype(int)
df['bit_rate_mode'] = df['bit_rate_mode'].str.replace("'", '').astype(str)
df['channel_layout'] = df['channel_layout'].str.replace("'", '').astype(str)
df['channel_positions'] = df['channel_positions'].str.replace("'", '').astype(str)
df['proportion_of_this_stream'] = df['proportion_of_this_stream'].str.replace("'", '').astype(float)
df['other_bit_rate_mode'] = df['other_bit_rate_mode'].str.replace("'", '').astype(str)


# In[12]:


df


# In[13]:


#df['frame_count']


# In[14]:


df.to_csv(r"C:\Users\neel-\Downloads\df_bitrate.csv")


# In[ ]:




