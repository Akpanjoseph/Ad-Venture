# import ffmpy
import os
import ffpyplayer
import cv2
from moviepy.editor import VideoFileClip,concatenate_videoclips
import random

# paths
Ad_path = './files/Ad'
vidoe_path = './files/Videos'

# getting vidoes in the folder path
get_ads =os.listdir(Ad_path)
get_videos =os.listdir(vidoe_path)

# storing extracted paths
video_list = []
ad_list = []


# extracting file datas

def get_data():
    for i in get_ads:
        link = f'{Ad_path}/{i}' # contructing ad path
        duration = VideoFileClip(link).duration #get video durations
        name = i.replace('.mp4','') # get video name

        ad_list.append({
            'name' : name,
            'link' : link,
            'duration' : duration
        })

    # videos
    for i in get_videos:
        link = f'{vidoe_path}/{i}' # contructing video path
        duration = VideoFileClip(link).duration #get video durations
        name = i.replace('mp4','') # get video name

        # saving the data
        video_list.append({
            'name' : name,
            'link' : link,
            'duration' : duration
        })


get_data()






# adding ads to video
def add_ad_to_vidoe():
  
    # generating ads 
    ads1 = ad_list[random.randint(0,len(ad_list))-1]
    ads2 = ad_list[random.randint(0,len(ad_list))-1]
    vd = video_list[random.randint(0,len(video_list))-1]

   
    clip1 = VideoFileClip(ads1.get('link')).subclip(0,ads1.get('duration'))
    clip2 = VideoFileClip(vd.get('link')).subclip(0,vd.get('duration'))
    clip3 = VideoFileClip(ads2.get('link')).subclip(0,ads2.get('duration'))
    
    combine = concatenate_videoclips([clip1,clip2,clip3])
    combine.write_videofile("test1.mp4")


add_ad_to_vidoe()
