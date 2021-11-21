# -*- coding: utf-8 -*-


!pip install SpeechRecognition

from google.colab import drive
drive.mount('/content/drive')

import os
import speech_recognition as sr




import pandas as pd
data = {'filename': ['File1.mp3', 'File2.mp3', 'File3.mp3'], 'text': ["Sample output output","sSample output output","Sample output output"]}
# Create DataFrame.
df = pd.DataFrame(data)

#currently working on
results = []
i = 1
import os



directory=r'drive/My Drive/video_file'
for filename in os.listdir(directory):
    #print(filename)
    if not len(filename.split('.'))>1:
        temp_dir=os.path.join(directory, filename)
        print(temp_dir)
    #print((directory + "\\" + str(i)))
    #temp_dir = directory + "\\" + str(i)
    
    for file in os.listdir(temp_dir):
        #print(file)
        if file.endswith(".wav"):
            temp_namee=os.path.join(temp_dir, file)
            print(temp_namee)
            r = sr.Recognizer()
            audio = sr.AudioFile(temp_namee)
            try:
              with audio as source:
                audio = r.record(source)
                texts = r.recognize_google(audio)
                results.append(texts)
            except:
              results.append("null")
            #    
             #   results.append(res)
                
    #print(results)
    #results=[]
    str_text=' '.join(results)
    #text = []
    #for file in results:
    #    for result in file['results']:
    #        text.append(result['alternatives'][0]['transcript'].rstrip() + '.\n ')
    #print(text)
    df.loc[len(df.index)] = [temp_dir, str_text]
    results=[]        
    #i += 1

#df

df = df.iloc[3:]

df.shape

df.to_csv( "drive/My Drive/df_restemp10.csv", encoding='utf-8')

