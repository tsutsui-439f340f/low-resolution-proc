import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser() 
parser.add_argument('src', help='入力画像パス')
parser.add_argument('dst', help='出力画像名')  
parser.add_argument('particle', help='粒度(奇数で設定)') 
parser.add_argument('n_color', help='色の数') 
args = parser.parse_args()

def low_resolution(img,n,n_color):
    h,w,c=img.shape
    color=[]
    for i in range(n_color+1):
        color.append(int((255/n_color)*i))
    color=np.array(color)
    d=img.copy()
    for i in range(n//2,h+n,n-1):
        for j in range(n//2,w+n,n-1):

            if  (i-n//2>=0) and (i+n//2<h):
                if (j-n//2>=0) and (j+n//2<w): 
                    trans_color=[]
                    for l in d[i-n//2:(i+n//2)+1,j-n//2:(j+n//2)+1].T.mean(axis=1).mean(axis=1):
                        a=np.argmin(np.abs(color-l))
                        trans_color.append(color[a])
                    k=np.zeros((n,n,3))+np.array(trans_color)

                    d[i-n//2:(i+n//2)+1,j-n//2:(j+n//2)+1]=k

                else:
                    if w-(j-n//2)>0:                  
                        trans_color=[]
                        for l in d[i-n//2:(i+n//2)+1,j-n//2:w].T.mean(axis=1).mean(axis=1):
                            a=np.argmin(np.abs(color-l))
                            trans_color.append(color[a])
                        k=np.zeros((n,w-(j-n//2),3))+np.array(trans_color)

                        d[i-n//2:(i+n//2)+1,j-n//2:w]=k
            else:
                if (j-n//2>=0) and (j+n//2<w): 
                    if h-(i-n//2)>0:
                        trans_color=[]
                        for l in d[i-n//2:h,j-n//2:(j+n//2)+1].T.mean(axis=1).mean(axis=1):
                            a=np.argmin(np.abs(color-l))
                            trans_color.append(color[a])
                        k=np.zeros((h-(i-n//2),n,3))+np.array(trans_color)

                        d[i-n//2:h,j-n//2:(j+n//2)+1]=k
    return d

img=cv2.imread(args.src)
low_img=low_resolution(img,n=int(args.particle),n_color=int(args.n_color))
cv2.imwrite(args.dst,low_img)
print("Finish")