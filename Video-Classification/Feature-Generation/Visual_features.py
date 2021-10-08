#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
import os

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


from google.colab import drive
drive.mount('/content/drive', force_remount=True)


# In[1]:


import pandas as pd
data = {'filename': ['File1.mp4', 'File2.mp4', 'File3.mp4'], 'video_b':[22,22,22], 'video_g':[22,22,22], 'video_r':[22,22,22], 'video_h':[22,22,22], 'video_s':[22,22,22],'video_v':[22,22,22],
        'contrast':[22,22,22],'dissimilarity':[22,22,22],'homogeneity':[22,22,22],'energy':[22,22,22],'correlation':[22,22,22],'ASM':[22,22,22]}
# Create DataFrame.
df = pd.DataFrame(data)


# In[2]:


df


# In[5]:


countr=0
avg_v_b = []
avg_v_g = []
avg_v_r = []
avg_v_h = []
avg_v_s = []
avg_v_v = []
energy = []
contrast = []
dissimilarity = []
homogeneity = []
energy = []
correlation = []
ASM = []
from skimage.feature import greycomatrix, greycoprops
from skimage import io, color, img_as_ubyte
import numpy as np
directory=r'drive/My Drive/remain/five'
for filename in os.listdir(directory):
    #print(filename)
    temp_dir=os.path.join(directory, filename)
    print(temp_dir)
    #print((directory + "\\" + str(i)))
    #temp_dir = directory + "\\" + str(i)
    for filename in os.listdir(temp_dir):
       if filename.endswith(".jpg"):
        temp_namee=os.path.join(temp_dir, filename)
        print(filename)
        myimg = cv2.imread(temp_namee)
        #print(type(myimg))
        #file=filename
        img = io.imread(temp_namee)
        gray = color.rgb2gray(img)
        image = img_as_ubyte(gray)
        GLCM = greycomatrix(image, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4])
        energy.append(greycoprops(GLCM, 'energy')[0, 0])
        contrast.append(greycoprops(GLCM, 'contrast')[0, 0])
        dissimilarity.append(greycoprops(GLCM, 'dissimilarity')[0, 0])
        homogeneity.append(greycoprops(GLCM, 'homogeneity')[0, 0])
        energy.append(greycoprops(GLCM, 'energy')[0, 0])
        correlation.append(greycoprops(GLCM, 'correlation')[0, 0])
        ASM.append(greycoprops(GLCM, 'ASM')[0, 0])
        hsv_img = cv2.cvtColor(myimg, cv2.COLOR_BGR2HSV)
        avg_color_per_row = np.average(myimg, axis=0)
        avg_color = np.average(avg_color_per_row, axis=0)
        avg_hsvcolor_per_row = np.average(hsv_img, axis=0)
        avg_hsvcolor = np.average(avg_hsvcolor_per_row, axis=0)
        avg_v_b.append(avg_color[0])
        avg_v_g.append(avg_color[1])
        avg_v_r.append(avg_color[2])
        avg_v_h.append(avg_hsvcolor[0])
        avg_v_s.append(avg_hsvcolor[1])
        avg_v_v.append(avg_hsvcolor[2])
      else:
        continue
    video_b = sum(avg_v_b) / len(avg_v_b)
    video_g = sum(avg_v_g) / len(avg_v_g)
    video_r = sum(avg_v_r) / len(avg_v_r)
    video_h = sum(avg_v_h) / len(avg_v_h)
    video_s = sum(avg_v_s) / len(avg_v_s)
    video_v = sum(avg_v_v) / len(avg_v_v)
    avg_contrast = sum(contrast) / len(contrast)
    avg_dissimilarity = sum(dissimilarity) / len(dissimilarity)
    avg_homogeneity = sum(homogeneity) / len(homogeneity)
    avg_energy = sum(energy) / len(energy)
    avg_correlation = sum(correlation) / len(correlation)
    avg_ASM = sum(ASM) / len(ASM)
    avg_v_b = []
    avg_v_g = []
    avg_v_r = []
    avg_v_h = []
    avg_v_s = []
    avg_v_v = []
    energy = []
    contrast = []
    dissimilarity = []
    homogeneity = []
    energy = []
    correlation = []
    ASM = []
    #print(video_b)
    #print(video_g)
    #print(video_r)
    #print(video_h)
    #print(video_s)
    #print(video_v)
    df.loc[len(df.index)] = [temp_dir, video_b,video_g,video_r,video_h,video_s,video_v,avg_contrast,avg_dissimilarity,avg_homogeneity,avg_energy,avg_correlation,avg_ASM]
    '''myimg = cv2.imread(filename)
        hsv_img = cv2.cvtColor(myimg, cv2.COLOR_BGR2HSV) #np.float32(imgUMat)
        avg_color_per_row = np.average(myimg, axis=0)
        avg_color = np.average(avg_color_per_row, axis=0)
        avg_hsvcolor_per_row = np.average(hsv_img, axis=0)
        avg_hsvcolor = np.average(avg_hsvcolor_per_row, axis=0)
        avg_v_b.append(avg_color[0])
        avg_v_g.append(avg_color[1])
        avg_v_r.append(avg_color[2])
        avg_v_h.append(avg_hsvcolor[0])
        avg_v_s.append(avg_hsvcolor[1])
        avg_v_v.append(avg_hsvcolor[2])
      else:
        continue
    video_b = sum(avg_v_b) / len(avg_v_b)
    video_g = sum(avg_v_g) / len(avg_v_g)
    video_r = sum(avg_v_r) / len(avg_v_r)
    video_h = sum(avg_v_h) / len(avg_v_h)
    video_s = sum(avg_v_s) / len(avg_v_s)
    video_v = sum(avg_v_v) / len(avg_v_v)
#print(video_b)
#print(video_g)
#print(video_r)
#print(video_h)
#print(video_s)
#print(video_v)
    #countr=0
    avg_v_b = []
    avg_v_g = []
    avg_v_r = []
    avg_v_h = []
    avg_v_s = []
    avg_v_v = []
    energy = []
    contrast = []
    dissimilarity = []
    homogeneity = []
    energy = []
    correlation = []
    ASM = []

    df.loc[len(df.index)] = [temp_dir, video_b,video_g,video_r,video_h,video_s,video_v]



# In[6]:


#df


# In[7]:


df = df.iloc[3:]


# In[8]:


df.to_csv( "drive/My Drive/df_visual_non_remain_five.csv", encoding='utf-8') #saving various features from a video files


# In[ ]:




