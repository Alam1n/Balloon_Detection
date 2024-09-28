# Balloon Detection Project

## Overview

This is a simple image detection project designed to detect balloons in images or videos using the YOLOv5 model. The project utilizes pre-trained weights and a detection script (detect.py) to analyze and identify balloons within the provided media.

## Installation
### Requirements
To run this project, you'll need to install the necessary Python dependencies. Here's how you can get started:

#### Clone the repository to your local machine:
```
git clone https://github.com/yourusername/balloon-detection.git
cd balloon-detection
```
#### Create a virtual environment (optional but recommended):
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
#### Install the dependencies:
```
pip install -r requirements.txt
Download the YOLOv5 model weights:
```

Ensure that the `best.pt` file is located in the weights/ directory (or adjust the path in the code accordingly).
Ensure the following important folders and files are present:

`detect.py`: The main detection script.

`weights/best.pt`: The model weights file.

`data/`: (Optional) A folder containing sample images/videos.

`runs/detect/`: The folder where the output (detected images/videos) will be saved.

#### How to Run the Detection
To run the detection on an image or video, execute the following command:

bash
```python image_detection.py```

This will launch the GUI where you can select an image or video for balloon detection. The detected balloons will be highlighted in the output, and for videos, the location of the saved video will be displayed.

Example Usage
You can try the detection by selecting an image or video from your local machine. The results will be displayed in the GUI or saved in the runs/detect/ directory.







