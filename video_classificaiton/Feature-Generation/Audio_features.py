# -*- coding: utf-8 -*-
"""Audio_Feature.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fNuqpOFdu1FAeZQv4xoUy5gCjNgt3bmh
"""

import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display
import IPython.display as ipd
import os
import moviepy.editor as mp

import pandas as pd
# assign data of lists.
data = {'filename': ['Tom', 'Joseph', 'Krish'], "chroma_stft_sum": [2,2,2],"chroma_stft_min": [2,2,2],"chroma_stft_max": [2,2,2],"chroma_stft_mean": [2,2,2],"chroma_stft_std": [2,2,2],"chroma_stft_median": [2,2,2],"chroma_stft_len": [2,2,2],
        "zero_sum": [2,2,2],"zero_min": [2,2,2],"zero_max": [2,2,2],"zero_mean": [2,2,2],"zero_std": [2,2,2],"zero_median": [2,2,2],"zero_len": [2,2,2],"n_zeros":[2,2,2],
        "chroma_cqt_sum": [2,2,2],"chroma_cqt_min": [2,2,2],"chroma_cqt_max": [2,2,2],"chroma_cqt_mean": [2,2,2],"chroma_cqt_std": [2,2,2],"chroma_cqt_median": [2,2,2],"chroma_cqt_len": [2,2,2],
        "chroma_cens_sum": [2,2,2],"chroma_cens_min": [2,2,2],"chroma_cens_max": [2,2,2],"chroma_cens_mean": [2,2,2],"chroma_cens_std": [2,2,2],"chroma_cens_median": [2,2,2],"chroma_cens_len": [2,2,2],
        "melspectrogram_sum": [2,2,2],"melspectrogram_min": [2,2,2],"melspectrogram_max": [2,2,2],"melspectrogram_mean": [2,2,2],"melspectrogram_std": [2,2,2],"melspectrogram_median": [2,2,2],"melspectrogram_len": [2,2,2],
        "mfcc_sum": [2,2,2],"mfcc_min": [2,2,2],"mfcc_max": [2,2,2],"mfcc_mean": [2,2,2],"mfcc_std": [2,2,2],"mfcc_median": [2,2,2],"mfcc_len": [2,2,2],
        "rms_sum": [2,2,2],"rms_min": [2,2,2],"rms_max": [2,2,2],"rms_mean": [2,2,2],"rms_std": [2,2,2],"rms_median": [2,2,2],"rms_len": [2,2,2],
        "spectral_centroid_sum": [2,2,2],"spectral_centroid_min": [2,2,2],"spectral_centroid_max": [2,2,2],"spectral_centroid_mean": [2,2,2],"spectral_centroid_std": [2,2,2],"spectral_centroid_median": [2,2,2],"spectral_centroid_len": [2,2,2],
        "spectral_bandwidth_sum": [2,2,2],"spectral_bandwidth_min": [2,2,2],"spectral_bandwidth_max": [2,2,2],"spectral_bandwidth_mean": [2,2,2],"spectral_bandwidth_std": [2,2,2],"spectral_bandwidth_median": [2,2,2],"spectral_bandwidth_len": [2,2,2],
        "spectral_contrast_sum": [2,2,2],"spectral_contrast_min": [2,2,2],"spectral_contrast_max": [2,2,2],"spectral_contrast_mean": [2,2,2],"spectral_contrast_std": [2,2,2],"spectral_contrast_median": [2,2,2],"spectral_contrast_len": [2,2,2],
        "spectral_flatness_sum": [2,2,2],"spectral_flatness_min": [2,2,2],"spectral_flatness_max": [2,2,2],"spectral_flatness_mean": [2,2,2],"spectral_flatness_std": [2,2,2],"spectral_flatness_median": [2,2,2],"spectral_flatness_len": [2,2,2],
        "spectral_rolloff_sum": [2,2,2],"spectral_rolloff_min": [2,2,2],"spectral_rolloff_max": [2,2,2],"spectral_rolloff_mean": [2,2,2],"spectral_rolloff_std": [2,2,2],"spectral_rolloff_median": [2,2,2],"spectral_rolloff_len": [2,2,2],
        "poly_features_sum": [2,2,2],"poly_features_min": [2,2,2],"poly_features_max": [2,2,2],"poly_features_mean": [2,2,2],"poly_features_std": [2,2,2],"poly_features_median": [2,2,2],"poly_features_len": [2,2,2],
        "tonnetz_sum": [2,2,2],"tonnetz_min": [2,2,2],"tonnetz_max": [2,2,2],"tonnetz_mean": [2,2,2],"tonnetz_std": [2,2,2],"tonnetz_median": [2,2,2],"tonnetz_len": [2,2,2],
        "label":["jfnaeofn","finesoif","kfjbea"]}
# Create DataFrame. df_animated = pd.DataFrame(data)
# Print the output.
print(df_animated_validation)
df_non_animated_validation = pd.DataFrame(data)

from google.colab import drive
drive.mount('/content/drive')

#import os
#import moviepy.editor as mp

directory = r'drive/My Drive/audio_file'
i = 0
for filename in os.listdir(directory):
    if filename.endswith(".mp3"):
        i = i + 1
        temp_name=os.path.join(directory, filename)
        #print(type(temp_name))
        y, sr = librosa.load(temp_name)
        chroma_stft = librosa.feature.chroma_stft(y).ravel()
        chroma_stft_sum = chroma_stft.sum()
        chroma_stft_min = chroma_stft.min()
        chroma_stft_max = chroma_stft.max()
        chroma_stft_mean = chroma_stft.mean()
        chroma_stft_std = np.std(chroma_stft)
        chroma_stft_median = np.median(chroma_stft)
        chroma_stft_len = len(chroma_stft)
        zero = librosa.feature.zero_crossing_rate(y).ravel()
        zero_sum = zero.sum()
        zero_min = zero.min()
        zero_max = zero.max()
        zero_mean = zero.mean()
        zero_std = np.std(zero)
        zero_median = np.median(zero)
        zero_len = len(zero)
        n_zeros = np.count_nonzero(zero==0)
        chroma_cqt = librosa.feature.chroma_cqt(y).ravel()
        chroma_cqt_sum = chroma_cqt.sum()
        chroma_cqt_min = chroma_cqt.min()
        chroma_cqt_max = chroma_cqt.max()
        chroma_cqt_mean = chroma_cqt.mean()
        chroma_cqt_std = np.std(chroma_cqt)
        chroma_cqt_median = np.median(chroma_cqt)
        chroma_cqt_len = len(chroma_cqt)
        chroma_cens = librosa.feature.chroma_cens(y).ravel()
        chroma_cens_sum = chroma_cens.sum()
        chroma_cens_min = chroma_cens.min()
        chroma_cens_max = chroma_cens.max()
        chroma_cens_mean = chroma_cens.mean()
        chroma_cens_std = np.std(chroma_cens)
        chroma_cens_median = np.median(chroma_cens)
        chroma_cens_len = len(chroma_cens)
        melspectrogram = librosa.feature.melspectrogram(y).ravel()
        melspectrogram_sum = melspectrogram.sum()
        melspectrogram_min = melspectrogram.min()
        melspectrogram_max = melspectrogram.max()
        melspectrogram_mean = melspectrogram.mean()
        melspectrogram_std = np.std(melspectrogram)
        melspectrogram_median = np.median(melspectrogram)
        melspectrogram_len = len(melspectrogram)
        mfcc = librosa.feature.mfcc(y).ravel()
        mfcc_sum = mfcc.sum()
        mfcc_min = mfcc.min()
        mfcc_max = mfcc.max()
        mfcc_mean = mfcc.mean()
        mfcc_std = np.std(mfcc)
        mfcc_median = np.median(mfcc)
        mfcc_len = len(mfcc)
        #mfcc_sum = mfcc.sum()
        rms = librosa.feature.rms(y).ravel()
        rms_sum = rms.sum()
        rms_min = rms.min()
        rms_max = rms.max()
        rms_mean = rms.mean()
        rms_std = np.std(rms)
        rms_median = np.median(rms)
        rms_len = len(rms)
        spectral_centroid = librosa.feature.spectral_centroid(y).ravel()
        spectral_centroid_sum = spectral_centroid.sum()
        spectral_centroid_min = spectral_centroid.min()
        spectral_centroid_max = spectral_centroid.max()
        spectral_centroid_mean = spectral_centroid.mean()
        spectral_centroid_std = np.std(spectral_centroid)
        spectral_centroid_median = np.median(spectral_centroid)
        spectral_centroid_len = len(spectral_centroid)
        spectral_bandwidth = librosa.feature.spectral_bandwidth(y).ravel()
        spectral_bandwidth_sum = spectral_bandwidth.sum()
        spectral_bandwidth_min = spectral_bandwidth.min()
        spectral_bandwidth_max = spectral_bandwidth.max()
        spectral_bandwidth_mean = spectral_bandwidth.mean()
        spectral_bandwidth_std = np.std(spectral_bandwidth)
        spectral_bandwidth_median = np.median(spectral_bandwidth)
        spectral_bandwidth_len = len(spectral_bandwidth)
        spectral_contrast = librosa.feature.spectral_contrast(y).ravel()
        spectral_contrast_sum = spectral_contrast.sum()
        spectral_contrast_min = spectral_contrast.min()
        spectral_contrast_max = spectral_contrast.max()
        spectral_contrast_mean = spectral_contrast.mean()
        spectral_contrast_std = np.std(spectral_contrast)
        spectral_contrast_median = np.median(spectral_contrast)
        spectral_contrast_len = len(spectral_contrast)
        spectral_flatness = librosa.feature.spectral_flatness(y).ravel()
        spectral_flatness_sum = spectral_flatness.sum()
        spectral_flatness_min = spectral_flatness.min()
        spectral_flatness_max = spectral_flatness.max()
        spectral_flatness_mean = spectral_flatness.mean()
        spectral_flatness_std = np.std(spectral_flatness)
        spectral_flatness_median = np.median(spectral_flatness)
        spectral_flatness_len = len(spectral_flatness)
        spectral_rolloff = librosa.feature.spectral_rolloff(y).ravel()
        spectral_rolloff_sum = spectral_rolloff.sum()
        spectral_rolloff_min = spectral_rolloff.min()
        spectral_rolloff_max = spectral_rolloff.max()
        spectral_rolloff_mean = spectral_rolloff.mean()
        spectral_rolloff_std = np.std(spectral_rolloff)
        spectral_rolloff_median = np.median(spectral_rolloff)
        spectral_rolloff_len = len(spectral_rolloff)
        poly_features = librosa.feature.poly_features(y).ravel()
        poly_features_sum = poly_features.sum()
        poly_features_min = poly_features.min()
        poly_features_max = poly_features.max()
        poly_features_mean = poly_features.mean()
        poly_features_std = np.std(poly_features)
        poly_features_median = np.median(poly_features)
        poly_features_len = len(poly_features)
        tonnetz = librosa.feature.tonnetz(y).ravel()
        tonnetz_sum = tonnetz.sum()
        tonnetz_min = tonnetz.min()
        tonnetz_max = tonnetz.max()
        tonnetz_mean = tonnetz.mean()
        tonnetz_std = np.std(tonnetz)
        tonnetz_median = np.median(tonnetz)
        tonnetz_len = len(tonnetz)
        label = 'animated'
        print(filename)
        #librosa.beat.tempo(y)
        #librosa.beat.plp(y)
        df_animated_validation.loc[len(df_animated_validation.index)] = [filename, 
        chroma_stft_sum, 
        chroma_stft_min, 
        chroma_stft_max, 
        chroma_stft_mean, 
        chroma_stft_std,
        chroma_stft_median,
        chroma_stft_len,

        zero_sum,
        zero_min ,
        zero_max ,
        zero_mean ,
        zero_std ,
        zero_median, 
        zero_len,
        n_zeros,

        chroma_cqt_sum, 
        chroma_cqt_min ,
        chroma_cqt_max,
        chroma_cqt_mean, 
        chroma_cqt_std,
        chroma_cqt_median, 
        chroma_cqt_len ,

        chroma_cens_sum,
        chroma_cens_min ,
        chroma_cens_max ,
        chroma_cens_mean ,
        chroma_cens_std ,
        chroma_cens_median, 
        chroma_cens_len,

        melspectrogram_sum, 
        melspectrogram_min,
        melspectrogram_max,
        melspectrogram_mean, 
        melspectrogram_std ,
        melspectrogram_median,
        melspectrogram_len ,

        mfcc_sum,
        mfcc_min ,
        mfcc_max ,
        mfcc_mean ,
        mfcc_std ,
        mfcc_median,
        mfcc_len ,


        rms_sum,
        rms_min ,
        rms_max,
        rms_mean,
        rms_std ,
        rms_median, 
        rms_len,

        spectral_centroid_sum,
        spectral_centroid_min ,
        spectral_centroid_max,
        spectral_centroid_mean, 
        spectral_centroid_std ,
        spectral_centroid_median, 
        spectral_centroid_len,

        spectral_bandwidth_sum ,
        spectral_bandwidth_min ,
        spectral_bandwidth_max,
        spectral_bandwidth_mean,
        spectral_bandwidth_std ,
        spectral_bandwidth_median, 
        spectral_bandwidth_len,

        spectral_contrast_sum ,
        spectral_contrast_min,
        spectral_contrast_max ,
        spectral_contrast_mean ,
        spectral_contrast_std,
        spectral_contrast_median, 
        spectral_contrast_len,

        spectral_flatness_sum,
        spectral_flatness_min,
        spectral_flatness_max,
        spectral_flatness_mean,
        spectral_flatness_std,
        spectral_flatness_median, 
        spectral_flatness_len ,

        spectral_rolloff_sum ,
        spectral_rolloff_min ,
        spectral_rolloff_max ,
        spectral_rolloff_mean ,
        spectral_rolloff_std ,
        spectral_rolloff_median, 
        spectral_rolloff_len ,

        poly_features_sum ,
        poly_features_min ,
        poly_features_max ,
        poly_features_mean ,
        poly_features_std ,
        poly_features_median, 
        poly_features_len ,

        tonnetz_sum ,
        tonnetz_min ,
        tonnetz_max ,
        tonnetz_mean ,
        tonnetz_std ,
        tonnetz_median, 
        tonnetz_len ,label]
    else:
        continue
 df_animated = df_animated_validation.iloc[3:]
 df_animated.to_csv( "drive/My Drive/df_animated.csv", encoding='utf-8')