import cv2
import glob

# filenames = glob.glob("/home/n1m4/Desktop/yolov3-tf2/extracted/2019-11-30_19-13/*.jpg")
# filenames.sort()
# images = [cv2.imread(img) for img in filenames]
# imageName = [print(imgg) for imgg in filenames]

# for img in images:
#     # print(images)
#     cv2.circle(img, (100,100), 2, (0, 0, 255), -1)
#     # f = open("/home/n1m4/Desktop/yolov3-tf2/extracted/2019-11-30_19-13/"+  +".txt", "r")
#     # print(f.read())
#     cv2.imshow('result',img)
#     key = cv2.waitKey(0)
#     if key == 27:
#         cv2.destroyAllWindows()         # It's escape button to exit
#         exit()

path = ("/home/n1m4/Desktop/yolov3-tf2/extracted/2019-11-30_19-13/*.jpg")
for file in glob.glob(path):
    print(file)
    img = cv2.imread(file)
    cv2.circle(img, (100,100), 2, (0, 0, 255), -1)
    cv2.imshow(file, img)
    key = cv2.waitKey(0)
    if key == 27:
        cv2.destroyAllWindows() # It's escape button to exit
        exit()
    cv2.destroyAllWindows()
