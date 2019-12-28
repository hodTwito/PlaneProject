from Engine import Engine
import time

engine = Engine()

precent = 0

while(precent != 999 and precent != 777):
    try:
        precent = float(raw_input())
        #print(precent)
        engine.rotate(precent)
    except Exception as e:
        engine.stop(e)
        precent=777

if precent == 999:
    engine.stop()


"""
engine.rotate(30)
time.sleep(1)
engine.rotate(50)
time.sleep(1)
engine.rotate(70)
time.sleep(1)
engine.rotate(90)
time.sleep(1)
engine.rotate(0)
time.sleep(1)
engine.stop()
"""
"""
engine.drive(1500)
time.sleep(3)
engine.stop()
"""