import cv2

# Read image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found")

else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply histogram equalization
    equalized = cv2.equalizeHist(gray)

    # Display images
    cv2.imshow("Original Image", gray)
    cv2.imshow("Equalized Image", equalized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()