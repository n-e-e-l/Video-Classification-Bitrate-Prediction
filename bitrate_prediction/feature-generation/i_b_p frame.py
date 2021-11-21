#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
data = {'filename': ['File1.mp4', 'File2.mp4', 'File3.mp4'], 'i_frame':[22,22,22],'b_frame':[22,22,22],'p_frame':[22,22,22]}
# Create DataFrame.
df = pd.DataFrame(data)


# In[ ]:


#H:\Thesis_data\test\test
import os
directory = r'H:\Thesis_data\animated\Training'
i=0
import subprocess 
import re
for filename in os.listdir(directory):
    if filename.endswith(".mp4"):
        temp_name=os.path.join(directory, filename)
        command = "ffprobe -show_frames " + str(temp_name)
        ress=subprocess.run(command, shell=True, stdout=subprocess.PIPE)
        #print(type(ress))
        i_frame=re.findall(r'pict_type=I', str(ress.stdout))
        b_frame=re.findall(r'pict_type=B', str(ress.stdout))
        p_frame=re.findall(r'pict_type=P', str(ress.stdout))
        print(filename)
        #print(len(i_frame))
        #print(len(b_frame))
        #print(len(p_frame))
        df.loc[len(df.index)] = [filename,len(i_frame),len(b_frame),len(p_frame)]
        
        #ffprobe -show_frames H:\Thesis_data\test\33_nonanimatedvalidation.mp4 > H:\Thesis_data\test\33_nonanimatedvalidation_outputfile.txt


# In[ ]:


df = df.iloc[3:]


# In[ ]:


#df


# In[ ]:


df.to_csv(r'C:\Users\neel-\Downloads\bitrate_animated_frame_training.csv',encoding='utf-8')


# In[1]:


#This is bitrate

import pandas as pd
data = {'filename': ['Tom', 'Joseph', 'Krish'], 'i_frame':[22,22,22],'b_frame':[22,22,22],'p_frame':[22,22,22]}
# Create DataFrame.
dff = pd.DataFrame(data)


# In[2]:


#H:\Thesis_data\test\test
import os
directory = r'H:\Thesis_data\non-animated\Training'
i=0
import subprocess 
import re
for filename in os.listdir(directory):
    if filename.endswith(".mp4"):
        temp_name=os.path.join(directory, filename)
        command = "ffprobe -show_frames " + str(temp_name)
        ress=subprocess.run(command, shell=True, stdout=subprocess.PIPE)
        #print(type(ress))
        i_frame=re.findall(r'pict_type=I', str(ress.stdout))
        b_frame=re.findall(r'pict_type=B', str(ress.stdout))
        p_frame=re.findall(r'pict_type=P', str(ress.stdout))
        print(filename)
        #print(len(i_frame))
        #print(len(b_frame))
        #print(len(p_frame))
        dff.loc[len(dff.index)] = [filename,len(i_frame),len(b_frame),len(p_frame)]
        
        #ffprobe -show_frames H:\Thesis_data\test\33_nonanimatedvalidation.mp4 > H:\Thesis_data\test\33_nonanimatedvalidation_outputfile.txt


# In[3]:


dff = dff.iloc[3:]
dff.to_csv(r'C:\Users\neel-\Downloads\bitrate_non_animated_frame_training.csv',encoding='utf-8')


# In[4]:


#This is bitrate


dff1 = pd.DataFrame(data)


# In[5]:


#H:\Thesis_data\test\test
import os
directory = r'/location/video_file'
i=0
import subprocess 
import re
for filename in os.listdir(directory):
    if filename.endswith(".mp4"):
        temp_name=os.path.join(directory, filename)
        command = "ffprobe -show_frames " + str(temp_name)
        ress=subprocess.run(command, shell=True, stdout=subprocess.PIPE)
        #print(type(ress))
        i_frame=re.findall(r'pict_type=I', str(ress.stdout))
        b_frame=re.findall(r'pict_type=B', str(ress.stdout))
        p_frame=re.findall(r'pict_type=P', str(ress.stdout))
        print(filename)
        #print(len(i_frame))
        #print(len(b_frame))
        #print(len(p_frame))
        dff1.loc[len(dff1.index)] = [filename,len(i_frame),len(b_frame),len(p_frame)]
        
        #ffprobe -show_frames H:\Thesis_data\test\33_nonanimatedvalidation.mp4 > H:\Thesis_data\test\33_nonanimatedvalidation_outputfile.txt


# In[6]:


dff1 = dff1.iloc[3:]
dff1.to_csv(r'C:\Users\neel-\Downloads\bitrate_non_animated_frame_testing.csv',encoding='utf-8')


