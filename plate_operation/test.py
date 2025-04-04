import cv2
import pytesseract
import numpy as np

# Load image
image_path = "/home/nazar/PycharmProjects/CoderOfSnake_Data/uploads/1cb7d56bc3e34d03ad83a20c06a889ab_Cars3.png"  # Update path
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")
    exit()

# Load the Haar Cascade for license plate detection
cascade_path = "car_number.xml"  # Update with correct path to your cascade
cascade = cv2.CascadeClassifier(cascade_path)

if cascade.empty():
    print("Error: Cascade not found!")
    exit()

# Convert to grayscale for cascade detection
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect plates using the Haar Cascade
plates = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# If no plate is detected, exit
if len(plates) == 0:
    print("No license plate detected.")
    exit()

# Process each detected plate (usually there will be only one)
for (x, y, w, h) in plates:
    # Draw a rectangle around the detected plate
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Crop the detected plate region
    cropped_plate = image[y:y + h, x:x + w]

    # Convert to grayscale for OCR
    gray_plate = cv2.cvtColor(cropped_plate, cv2.COLOR_BGR2GRAY)

    # Apply median blur (removes noise while keeping edges)
    denoised = cv2.medianBlur(gray_plate, 3)

    # Gentle sharpening (less aggressive than before)
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]], dtype=np.float32)
    sharpened = cv2.filter2D(denoised, -1, kernel)

    # Adaptive thresholding (less harsh, keeps more details)
    binary = cv2.adaptiveThreshold(sharpened, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                   cv2.THRESH_BINARY, 15, 5)

    # Run OCR with improved settings
    custom_config = "--psm 7 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 tessedit_char_blacklist=6"
    text = pytesseract.image_to_string(binary, config=custom_config).strip()

    print("Recognized Text:", text)

# Show the processed image for debugging
cv2.imshow("Detected Plate", image)
cv2.imshow("Cropped Plate", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()