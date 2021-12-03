import cv2
import dropbox
import time
import random
start_time = time.time()
def take_snapshot():
    number = random.randint(1,100)
    videoCaptureObject = cv2.VideoCapture(0)
    # above line starts camera, 0 indicates  the camera of our sytem
    result = True
    while (result):
        ret ,frame = videoCaptureObject.read()
        img_name = 'img'+str(number)+'.png'
        cv2.imwrite(img_name,frame)
        result = False
    return img_name
    print('snapshot taken')
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = '1S9L4qWqWBcAAAAAAAAAAVtNdlP7zsvr-uSgT7nNdAbg3CEd4MbrmKuYyXAp8PdN'
    file = img_name
    file_from = file 
    file_to = '/NewFolder2/'+(img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print('file uploaded')
def main():
    while(True):
        if((time.time()-start_time)>= 15):
            name = take_snapshot()
            upload_file(name)
main()


