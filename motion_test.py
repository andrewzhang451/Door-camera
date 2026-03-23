#import module
import cv2
import numpy

#passing frame into parameters. frame[row,column] = [B,G,R] or frame[row,column] = [brightness level] 
def detection_motion(prev_frame, curr_frame):
  #make both curr and prev to greyscale
  prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
  curr_frame_gray = cv2.cvtColor(curr_frame, cv2.COLOR_BGR2GRAY)
  
  #make both blur
  prev_blur = ""
  curr_blur = ""
  
  #find what changed in pixel between the two frames
  #keep only strong changes and store it in a variable (white = change, black = unchange)
  #make the white areas bigger so the white motion blobs are easier to detect
  #find seperate moving areas
    
    
  return False

#start camera

#loop: 
#-get frame
#-call detection_motion()
#-print result
