#this file decides whether to alert or not 
import time

last_alert_time = 0 #stores when alert was last triggered

def should_alert(distance_m: float, motion: bool, pir: bool) -> bool:
  global last_alert_time
  
  DISTANCE_THRESHOLD = 1.0
  COOLDOWN = 5 #seconds
  
  now = time.time() #current time in seconds
  
  if pir and motion and (distance_m < DISTANCE_THRESHOLD): #if pir and motion is true, and distance_m is less than Distance_threshhold
    if now - last_alert_time > COOLDOWN:
      last_alert_time = now
      return True
  
  return False