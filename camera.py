import cv2 as cv 
import os
from PIL import Image, ImageDraw
import pyvirtualcam
import numpy

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

rodando = 0
with pyvirtualcam.Camera(width=800, height=600, fps=30) as cam:
    print(f'Using virtual camera: {cam.device}')
    while True:
        new_frame = []
        status, frame = camera.read()
        dim = (120, 60)
        frame = cv.resize(frame, dim, interpolation=cv.INTER_AREA)
        frame = numpy.flip(frame, axis=1)

        for i in frame:
            new_line = ''
            for j in i:
                new_line += get_ascii(sum(j)/3)
            new_frame.append(new_line)
        # os.system('cls' if os.name == 'nt' else 'clear')
        im = Image.new(mode="RGB", size=(800, 600))
        I1 = ImageDraw.Draw(im)
        line_counter = 0
        line_spacing = 600/len(new_frame)
        for x in new_frame:
            stroke_counter = 0
            pixel_stroke = 800/len(x)
            for stroke in x:
                I1.text((stroke_counter * pixel_stroke, line_counter * line_spacing), stroke, fill=(255, 255, 255))
                stroke_counter += 1
            line_counter += 1
            # print(x)
        # im.show()
        open_cv_image = numpy.array(im)
        open_cv_image = numpy.flip(open_cv_image, axis=1)
        # Convert RGB to BGR
        open_cv_image = open_cv_image[:, :, ::-1].copy()
        cam.send(open_cv_image)
        cam.sleep_until_next_frame()
        rodando += 1
    