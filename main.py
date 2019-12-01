import cv2
import glob
import csv


path = ("/home/n1m4/Desktop/yolov3-tf2/extracted/2019-11-30_19-13/*.jpg")
pathtxt = ("/home/n1m4/Desktop/yolov3-tf2/extracted/2019-11-30_19-13/0.txt")

def imageToTxt(pathJPG):
    pathJPG = pathJPG.strip('.jpg')
    pathJPG = pathJPG + ".txt"
    return pathJPG

def readTxt(pathTxt):
    with open(pathTxt, newline = '') as games:                                                                                          
        game_reader = csv.reader(games, delimiter='\t')
        for game in game_reader:
            return game

for file in glob.glob(path):
    x = readTxt(imageToTxt(file))
    print(x)
    center = (x[1],x[2])
    print(center[0])
    radious = 5
    color = (0, 0, 255)
    thicknes = -1
    img = cv2.imread(file)
    cv2.circle(img, (int(center[0]),int(center[1])), radious, color, thicknes)
    cv2.imshow(file, img)
    key = cv2.waitKey(0)
    if key == 27:
        cv2.destroyAllWindows() # It's escape button to exit
        exit()
    cv2.destroyAllWindows()
