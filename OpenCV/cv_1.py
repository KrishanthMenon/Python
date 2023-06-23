import cv2

img = cv2.imread("C:/Users/Krishanth/Desktop/highway.jpg")

print("Dimensions of the image: ",img.shape)

cv2.imshow("window" , img)

cv2.waitKey(0)

cv2.destroyAllWindows()
