import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, UnidentifiedImageError
import os
import subprocess
import glob

# Path to the detect.py file
DETECT_PATH = "C:/yolovo5/yolov5/detect.py"

# Function to run YOLOv5 detection
def run_detection(file_path, file_type):
    # Create a unique identifier for the current run
    output_dir = f"runs/detect/exp_{os.path.basename(file_path).split('.')[0]}"
    
    # Set the command based on file type
    command = [
        "python", DETECT_PATH,
        "--weights", "C:/yolovo5/yolov5/runs/train/exp2/weights/best.pt",
        "--source", file_path,
        "--img-size", "640",
        "--conf-thres", "0.25",
        "--iou-thres", "0.45",
        "--save-txt",
        "--save-conf",
        "--project", "runs/detect",
        "--name", os.path.basename(file_path).split('.')[0]
    ]
    
    # Run the YOLOv5 detection
    subprocess.run(command)
    
    # Handle the output based on file type
    if file_type == "image":
        result_file_path = os.path.join(output_dir, os.path.basename(file_path))
        if os.path.exists(result_file_path):
            display_image(result_file_path, processed_image_label)
        else:
            messagebox.showerror("Error", "Processed image not found.")
    else:
        # Just show a message with the video location
        messagebox.showinfo("Info", f"Video processed and saved in: {output_dir}")

# Function to display images in the GUI
def display_image(image_path, label):
    try:
        # Load and resize the image
        img = Image.open(image_path)
        img = img.resize((400, 400), Image.LANCZOS)
        
        # Convert to Tkinter format
        img_tk = ImageTk.PhotoImage(img)
        
        # Update the label with the image
        label.config(image=img_tk)
        label.image = img_tk
    except UnidentifiedImageError:
        messagebox.showerror("Error", "Selected file is not a valid image.")

# Function to select a file and run detection
def select_file(file_type):
    # Set file types based on the file_type argument
    if file_type == "image":
        file_types = [("Image Files", "*.jpg *.jpeg *.png *.bmp *.jfif *.tiff")]
    elif file_type == "video":
        file_types = [("Video Files", "*.mp4 *.avi *.mov *.mkv *.wmv")]
    
    # Open a file dialog to select a file
    file_path = filedialog.askopenfilename(filetypes=file_types)
    
    if file_path:
        # Display the selected image (only for images)
        if file_type == "image":
            display_image(file_path, selected_image_label)
        
        # Run detection on the selected file
        run_detection(file_path, file_type)

# Create the main Tkinter window
root = tk.Tk()
root.title("YOLOv5 Detector")

# Create a frame for the images
image_frame = tk.Frame(root)
image_frame.pack()

# Create labels to display the selected and processed images
selected_image_label = tk.Label(image_frame)
selected_image_label.pack(side=tk.LEFT, padx=10)

processed_image_label = tk.Label(image_frame)
processed_image_label.pack(side=tk.RIGHT, padx=10)

# Create buttons for selecting an image or video
img_btn = tk.Button(root, text="Select Image", command=lambda: select_file("image"), width=25, height=2)
vid_btn = tk.Button(root, text="Select Video", command=lambda: select_file("video"), width=25, height=2)

# Place buttons in the window
img_btn.pack(pady=10)
vid_btn.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
