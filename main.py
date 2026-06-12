import cv2
import numpy as np

# Load image
image = cv2.imread('gb_la_midfield.png')

# Convert to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define Green-White Range
lower_broad = np.array([30, 0, 120])
upper_broad = np.array([90, 80, 255])

# Create mask
mask = cv2.inRange(hsv, lower_broad, upper_broad)

# Apply mask
result = cv2.bitwise_and(image, image, mask=mask)

# Save results
cv2.imwrite('mask.jpg', mask)
cv2.imwrite('result.jpg', result)