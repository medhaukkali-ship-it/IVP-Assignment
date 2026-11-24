import cv2

img = cv2.imread("image.jpg")

if img is None:
    print("Image not found")
else:
    print("Original Image Size:", img.shape)

    rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    print("Rotated Image Size:", rotated.shape)

    cv2.imshow("Original Image", img)
    cv2.imshow("Rotated Image", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()