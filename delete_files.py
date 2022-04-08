import os
import main
import time

def delete():
  time.sleep(60)
  if os.path.exists(f"{main.main_ro()}.{main.main_ro()}" and f"{main.main_hu()}.{main.main_hu()}"):
    os.remove(f"{main.main_ro()}.{main.main_ro()}" and f"{main.main_hu()}.{main.main_hu()}")
  else:
    print("The file does not exist")



