#import module
import cv2
import numpy


#count how many pixels changed
def count_changed_pixels (thresh):
  bw_difference = cv2.countNonZero(thresh)
  return bw_difference

#passing frame into parameters. frame[row,column] = [B,G,R] or frame[row,column] = [brightness level] 
def detection_motion(prev_frame, curr_frame):
  
  #absdiff() will calculate pixel value that changed between the prev and curr frame. then the value will be passed into threshold(). the difference will be the threshold minimum.
  
  #make both curr and prev to greyscale
  prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
  curr_frame_gray = cv2.cvtColor(curr_frame, cv2.COLOR_BGR2GRAY)
  
  #make both blur
  prev_blur = cv2.GaussianBlur(prev_gray, (5,5), 0)
  curr_blur = cv2.GaussianBlur(curr_frame_gray, (5,5), 0)
  
  #find what changed in pixel between the two frames
  difference = cv2.absdiff(prev_blur, curr_blur)
  
  #create a threshold for it. IMPORTANT becaue working with greyscale is messy. hard to tell what is real motion.
  #threshold converts difference image above into "motion or no motion" pixels.
  _, thresh = cv2.threshold(difference, 20,255, cv2.THRESH_BINARY) # "_" means we ignore the first returned value. (threshold used)
  
  #count how many pixels changed
  changed_pixels = count_changed_pixels(thresh)
  
  #keep only strong changes and store it in a variable (white = change, black = unchange)
  motion_pixel_threshold = 12000 #might change later based on testing
  
  if changed_pixels > motion_pixel_threshold:
    return True 
    
  return False

# def is_motion_strong_enough(changed_pixels:int, motion_pixel_threshold:int):
#   pass



#start camera
cap = cv2.VideoCapture(0)

ret, prev_frame = cap.read()

while True:
    ret, curr_frame = cap.read()
    
    if not ret:
      break
    
    motion = detection_motion(prev_frame, curr_frame)
    
    if motion:
      print("Motion detected!!")
    else: 
      print("no motion")
      
    prev_frame = curr_frame
    
    #press 'g; to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()



#loop: 
  #-get frame
  #-call detection_motion()
  #-print result
