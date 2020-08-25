# PerturbedDLIB
This is the implementation of the face landmarks detection of DLIB. <br>
It's the implementation of Disney landmarks perturbation
# Requirements
No required version
* DLib 
> pip install dlib
* OpenCV
> pip install opencv-python
* Numpy
> pip install numpy

## Steps
1. CLone the project
2. Download the shape predictor of dlib from this link [drive](https://drive.google.com/file/d/1Vu2eHpnjdCRulUDaDUPFzBtfFfOiw2IW/view?usp=sharing), next save it under the folder data with the name shapePredictor.dat
3. execute the main.py if you want to test the code
## Possible inputs
The main function inputs:<br>
* one image (.png, .jpg, .jpeg)
* folder of images
* a video (.avi, .mp4, .mpeg)
## template command line
1. One image
> python main.py -i ./test/face.png -o ./test/face_landmarks.jpg
or
> python main.py -i ./test/face.png -o ./test

2. Folder of images
> python main.py -i ./test -o ./test

3. Folder of images
> python main.py -i ./test/video.mp4 -o ./test/frames