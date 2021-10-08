#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display
import IPython.display as ipd
import os
import moviepy.editor as mp


# In[2]:


import pandas as pd
# assign data of lists.
#Sample dataframe
data = {'filename': ['file1.mp3', 'file2.mp3', 'file3.mp3'], 'chroma_stft': [[0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719], [0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719], [0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719]],'zero': [[0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719], [0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719], [0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719]],'chroma_cqt': [[0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719], [0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719], [0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719]],'chroma_cens': [[0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719], [0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719], [0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719]],'melspectrogram': [[0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719], [0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719], [0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719]],'mfcc': [[0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719], [0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719], [0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719]],'mfcc_sum':[122113,12324,1324],'rms': [[0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719], [0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719], [0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719]], 'spectral_centroid': [[0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719], [0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719], [0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719]],'spectral_bandwidth': [[0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719], [0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719], [0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719]],'spectral_contrast': [[0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719], [0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719], [0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719]],'spectral_flatness': [[0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719], [0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719], [0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719]],'spectral_rolloff': [[0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719], [0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719], [0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719]],'poly_features': [[0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719], [0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719], [0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719]],'tonnetz': [[0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719], [0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719], [0.03027344, 0.03027344, 0.03027344, 0.04003906, 0.02636719]],'label': ['animated', 'animated', 'animated']}
# Create DataFrame.
df_animated_validation = pd.DataFrame(data)
# Print the output.
print(df_animated_validation)
df_non_animated_validation = pd.DataFrame(data)


# In[3]:


from google.colab import drive
drive.mount('/content/drive')


# In[4]:



#import os
#import moviepy.editor as mp

directory = r'drive/My Drive/non-animated/five/five7'
i = 0
for filename in os.listdir(directory):
    if filename.endswith(".mp3"):
        i = i + 1
        temp_name=os.path.join(directory, filename)
        #print(type(temp_name))
        y, sr = librosa.load(temp_name)
        chroma_stft = librosa.feature.chroma_stft(y)
        zero = librosa.feature.zero_crossing_rate(y)
        chroma_cqt = librosa.feature.chroma_cqt(y)
        chroma_cens = librosa.feature.chroma_cens(y)
        melspectrogram = librosa.feature.melspectrogram(y)
        mfcc = librosa.feature.mfcc(y)
        mfcc_sum = mfcc.sum()
        rms = librosa.feature.rms(y)
        spectral_centroid = librosa.feature.spectral_centroid(y)
        spectral_bandwidth = librosa.feature.spectral_bandwidth(y)
        spectral_contrast = librosa.feature.spectral_contrast(y)
        spectral_flatness = librosa.feature.spectral_flatness(y)
        spectral_rolloff = librosa.feature.spectral_rolloff(y)
        poly_features = librosa.feature.poly_features(y)
        tonnetz = librosa.feature.tonnetz(y)
        label = 'animated'
        print(temp_name)
        #librosa.beat.tempo(y)
        #librosa.beat.plp(y)
        df_animated_validation.loc[len(df_animated_validation.index)] = [temp_name, chroma_stft,zero,chroma_cqt,chroma_cens,melspectrogram,mfcc,mfcc_sum,rms,spectral_centroid,spectral_bandwidth,spectral_contrast,spectral_flatness,spectral_rolloff,poly_features,tonnetz, label]
    else:
        continue


# In[5]:


df_animated_validation = df_animated_validation.iloc[3:]


# In[6]:


df_animated_validation.to_csv( "drive/My Drive/df_five.csv", encoding='utf-8')


# In[ ]:


from google.colab import files
df_animated_validation.to_csv('df_animated_training_two.csv',encoding='utf-8')
files.download('df_animated_training_two.csv')


# In[ ]:




