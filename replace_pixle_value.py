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
            # Replace pixel value with red color (255, 0, 0)
            img_array[y, x] = [255, 0, 0]  # RGB color format
            # Update image plot
            ax.imshow(img_array)
            fig.canvas.draw()
    
    # Connect the onclick function to the figure
    fig.canvas.mpl_connect('button_press_event', onclick)
    
    # Display the plot
    plt.show()

if __name__ == "__main__":
    image_path = "/Users/yousifalani/Desktop/Screenshot 2024-07-02 at 1.23.39 PM.png" 
    display_image(image_path)

