def one_time():
    import pyscreenshot as ImageGrab 
    import time
    images_folder="captured_images/0/"
    for i in range(0,5):
        time.sleep(8)
        im=ImageGrab.grab(bbox=(60,170,400,550)) # 
        print("saved......",i)
        im.save(images_folder+str(i)+'.png')