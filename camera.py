import cv2 as cv 
import os

camera = cv.VideoCapture(0)
rodando = True

ascii_color = '.,:;i!1j?23498$W#@Ñ'
color_dict = {}
inte = 255/len(ascii_color)

y = 0
for x in ascii_color:
    y += inte
    color_dict[y] = x

def get_ascii(int_color):
    for x in color_dict.keys():
        if int_color <= x:
            return color_dict[x]

while rodando < 100:
    new_frame = []
    status, frame = camera.read()
    dim = (120, 60)
    frame = cv.resize(frame, dim, interpolation=cv.INTER_AREA)

    for i in frame:
        new_line = []
        for j in i:
            new_line.append(sum(j)/3)
        new_frame.append(''.join([get_ascii(x) for x in new_line]))
    os.system('cls' if os.name == 'nt' else 'clear')
    for x in new_frame:
        print(x)
