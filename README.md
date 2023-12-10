# Find the wrong picture and create the wrong picture with OpenCV

---

1. **Create an image that we will use to find the wrong picture.**

<img width="1621" alt="스크린샷 2023-12-10 18 49 15" src="https://github.com/devjaeseung/opensw_team70/assets/100324690/d434a4ca-1cb4-4878-8691-1553af297607">

2. **Use OpenCV to find the wrong picture and recognize the object.**
   
![스크린샷 2023-12-10 18 21 07](https://github.com/devjaeseung/opensw_team70/assets/100324690/ea21d6d4-9da0-432d-aad1-2f98b8f23d49)

![스크린샷 2023-12-10 18 51 37](https://github.com/devjaeseung/opensw_team70/assets/100324690/3378a8aa-ef37-4ea5-a4f5-4128a954a096)


- VirtualEnv install
    
    ```jsx
    python3 -m venv myenv
    ```
    
- VirtualEnv run
    
    ```jsx
    source myenv/bin/activate
    ```
    
- Installing a library with pip
    - Update pip before installing
        
        ```jsx
        pip install --upgrade pip
        ```
        
    - Installing OpenCV
        
        ```jsx
        pip install opencv-python
        ```
        
    - Installing imutils 
        
        ```jsx
        pip install imutils
        ```

- Installing Library Links
  
      Pre-trained model weights :  https://pjreddie.com/media/files/yolov3.weights
      Model configuration file (text file) :  https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg
      COCO class names (text file):  https://github.com/pjreddie/darknet/blob/master/data/coco.names
      haarcascade_frontalface_alt(.xml file):  https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_alt.xml

- Run makeDiffImg.py File 

    ```jsx
    python makeDiffImg.py
    ```

- Run diffimage.py File 

    ```jsx
    python diffimage.py
    ```
- Reference Link 

  https://www.youtube.com/watch?v=Ph4lI-LxzDg

  Gachon University OpenSW Lecture - Lab 12, 13, 14
  
  

