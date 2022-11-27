import cv2 as cv
import numpy as np
import yaml
import os
import glob2 as glob

corner_x=8
corner_y=6

criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER,30,0.01)

objp = np.zeros((corner_y*corner_x,3),np.float32)
objp[:,:2] = np.mgrid[0:corner_x,0:corner_y].T.reshape(-1,2)

objpoints = []

jpgpoints = []

source_path ="C:/Users/Selva Kumar E/Desktop/Assignment1"

print("image found :",len(os.listdir(source_path)))

images = [source_path + '/' + f for f in glob.glob("ass1.jpg")]

found = 0
for fname in images: 
    jpg = cv.imread(fname)
    cv.imshow('jpg',jpg)
    cv.waitKey(500)
    print(fname)
    gray = cv.cvtColor(jpg,cv.COLOR_BGRA2GRAY)
    
    ret,corners = cv.findChessboardCorners(gray,(corner_x,corner_y),None)
    
    if ret == True:
        
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray,corners,(25,5),(-1,-5),criteria)
        jpgpoints.append(corners2)
        
        jpg =cv.drawChessboardCorners(jpg,(corner_x,corner_y),corners2,ret)
        found+=1
        cv.imshow('chessboard',jpg)
        cv.waitKey(0)

print("number of imagesused for calibration:",found)

ret,mtx,dist,rvecs, tvecs =cv.calibrateCamera(objpoints,jpgpoints,gray.shape[::-1],None,None)
data = {"camera_matrix": np.asarray(mtx).tolist(),"dist_coeff": np.asarray(dist).tolist()}
print(mtx)
print(dist)

with open ("calibration_matrix.yaml","w")as f:
    yaml.dump(data,f)

for fname in images:
    jpg=cv.imread(fname)
    
    h,w = jpg.shape[:2]
    
    newcameramtx,roi=cv.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))
    dst =cv.undistort(jpg,mtx,dist,None,newcameramtx)
    cv.imshow("undistort",dist)
    cv.waitKey(500)
    
    x,y,w,h = roi
    dst=dst[y:y+h,x:x+w]
    cv.imshow('undistort2',dst)
    cv.waitKey(0)

