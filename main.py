from fusion import should_alert
import random
import time

def fake_pir():
  return random.choice([True,False])

def fake_motion():
  return random.choice([True,False])

def fake_distance():
  return round(random.uniform(0.3, 2.0), 2)

while True:
  pir = fake_pir()
  motion = fake_motion()
  distance = fake_distance()
  
  alert = should_alert(distance,motion,pir)
  
  print(f"PIR: {pir} | Motion: {motion} | Distance: {distance}m")
  
  if alert:
    print("alert is triggered")
  
  time.sleep(1)
