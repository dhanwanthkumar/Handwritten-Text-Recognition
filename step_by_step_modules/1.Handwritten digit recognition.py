# if u run this module it will capture the screen in the top left conner and save it in the respective folders mentioned in line 5
# change the folder name inside the "captured images each time or else the captured screen will overwrite the existing photos"
import pyscreenshot as ImageGrab 
import time
images_folder="captured_images/0/" # this message is for folder 0
  
for i in range(0,5):
   time.sleep(8)
   im=ImageGrab.grab(bbox=(60,170,400,550)) # ( x1=60 ,y1=170 ,x2=400 ,y2=550 ).
   print("saved......",i)
   im.save(images_folder+str(i)+'.png')