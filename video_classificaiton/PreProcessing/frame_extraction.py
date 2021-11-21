#Extract Frames from Video
import cv2
import os
i = 0
#Input the video location
directory = r'location\Video_Data\' 
for filename in os.listdir(directory):
    i = i + 1
    temp_name=os.path.join(directory, filename)
    #print(filename)
    temp_dic=os.path.join(directory,os.path.splitext(filename)[0])
    #print(ch)
    #print()
    try:
        if not os.path.exists(temp_dic):
            os.makedirs(temp_dic)
                # if not created then raise error
    except OSError:
        print ('Error: Creating directory of data')
    print(temp_dic)
    os.chdir(temp_dic)
    vidcap = cv2.VideoCapture(temp_name)
    #vidcap = cv2.VideoCapture(r'G:\Thesis_data\animated\test\55_animatedtesting.mp4') 
    #Capturing Frames Based on the duration 
    success = True
    count = 0 #success = True
    fps = int(vidcap.get(cv2.CAP_PROP_FPS))
    frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count/fps
    #print(fps)
    #print(duration)
    if duration>=600:
        while success:
            success,image = vidcap.read()
            if count%(60*fps) == 0 :
                cv2.imwrite('frame%d.jpg'%count,image)
            count+=1
    elif duration<600 and duration>90:
        while success:
            success,image = vidcap.read()
            if count%(45*fps) == 0 :
                cv2.imwrite('frame%d.jpg'%count,image)
            count+=1
    else:
        while success:
            success,image = vidcap.read()
            if count%(5*fps) == 0 :
                cv2.imwrite('frame%d.jpg'%count,image)
            count+=1
    vidcap.release()
    cv2.destroyAllWindows()