from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def display_image(image_path):
    # Open image using Pillow (PIL)
    img = Image.open(image_path)
    
    # Convert image to numpy array
    img_array = np.array(img)
    
    # Display image using matplotlib
    fig, ax = plt.subplots()
    ax.imshow(img_array)
    
    # Define a function to handle mouse click events
    def onclick(event):
        if event.xdata is not None and event.ydata is not None:
            x = int(event.xdata)
            y = int(event.ydata)
            pixel_value = img_array[y, x]  # Access pixel value (row, column)
            print(f"Clicked on pixel ({x}, {y}) with value: {pixel_value}")
    
    # Connect the onclick function to the figure
    fig.canvas.mpl_connect('button_press_event', onclick)
    
    # Display the plot
    plt.show()

if __name__ == "__main__":
    image_path = "/Users/yousifalani/Desktop/Screenshot 2024-07-02 at 1.23.39 PM.png"  # Replace with your image file path
    display_image(image_path)
