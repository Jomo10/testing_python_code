import cv2
import numpy as np
import argparse

def display_and_edit_image(image_path):
    # Load the image using OpenCV
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if img is None:
        print(f"Failed to load image: {image_path}")
        return

    def draw_rectangle(event, x, y, flags, param):
        nonlocal ix, iy, drawing, img
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            ix, iy = x, y
        elif event == cv2.EVENT_MOUSEMOVE:
            if drawing:
                img_copy = img.copy()
                cv2.rectangle(img_copy, (ix, iy), (x, y), (0, 255, 0), 1)
                cv2.imshow('Image', img_copy)
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 1)
            roi = img[iy:y, ix:x]
            roi[:] = 255 - roi  # Invert colors in the selected area
            cv2.imshow('Image', img)

    ix, iy = -1, -1
    drawing = False
    cv2.namedWindow('Image')
    cv2.setMouseCallback('Image', draw_rectangle)

    while True:
        cv2.imshow('Image', img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:  # ESC key to exit
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Edit an image.')
    parser.add_argument('image_path', type=str, help='Path to the image file')
    args = parser.parse_args()

    display_and_edit_image(args.image_path)

