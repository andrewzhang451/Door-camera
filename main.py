from fusion import should_alert
import time

test_data = [
  {"pir":False, "motion":False, "distance":2.0}, #nobody
  {"pir":True, "motion":True, "distance":0.9}, #person arrive
  {"pir":True, "motion":True, "distance":0.5}, #still there
  {"pir":True, "motion":True, "distance":0.3}, #still there
  {"pir":False, "motion":False, "distance":2.0} #left
]
  
while True:
  for reading in test_data:
    pir = reading["pir"]
    motion = reading["motion"]
    distance = reading["distance"]
    
    alert = should_alert(distance,motion,pir)
    
    print(f"PIR: {pir} | Motion: {motion} | Distance: {distance}m")
  
    if alert:
      print("alert is triggered")
  
    time.sleep(1)

  print("\n--- Loop Restart ---\n")