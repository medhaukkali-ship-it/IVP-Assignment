import cv2

# Read image
img = cv2.imread("image.jpg")

# Check whether image is loaded
if img is None:
    print("Image not found")
else:
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Display original image
    cv2.imshow("Original Image", img)

    # Display grayscale image
    cv2.imshow("Grayscale Image", gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()