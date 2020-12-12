import numpy as np
import matplotlib.pyplot as plt
import random
from typing import List, Any, Dict, Tuple
import os
from PIL import Image
import pandas as pd

exp = 0
num_images = 15
radius = 0.05 
epsilon = 2/255
bg_start = [150.0/255.0, 0.0, 150.0/255.0]
c_start = [150.0/255.0, 0.0, 150.0/255.0]
if exp == 0:
    expt_type = "pbg_bu"
    channel = 3
    
elif exp == 1:
    expt_type = "pbg_ru"
    channel = 1

bg_base = "images/{}_0.png".format(expt_type)

base = []
def plot_test(radius: float, colour_c: List, colour_bg: List, 
              epsilon: int, num_graphs: int, file_name: str, channel: int):
    names = []
    quadrant = []
    color_change = []
    if not os.path.exists("images"):
        os.makedirs("images")
    for i in range(0,num_graphs):
        centers = [(0.5, 0.85), (0.15, 0.5), (0.5, 0.15), (0.85, 0.5)]
        quad = random.choice([0, 1, 2, 3])
        quadrant.append(quad)
        circle = plt.Circle(centers[quad], radius, color=colour_c)
        color_change.append(round(colour_c[channel-1]*255,4))
        colour_c[channel-1] = colour_c[channel-1]+epsilon
        print(round(colour_c[channel-1]*255,4))
        fig, ax = plt.subplots(figsize = [8,8])
        ax.set_facecolor(colour_bg)
        ax.add_artist(circle)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        plt.tight_layout()
        img_name = "images/{}_{}.png".format(file_name,i)
        plt.savefig(img_name)
        plt.close()
        im = Image.open(img_name)
        im_crop = im.crop((15, 15, 555, 555))
        im_crop.save(img_name)
        names.append(img_name)
    return names,quadrant,color_change
        
names,quadrant,color_change = plot_test(radius, c_start, 
                                        bg_start,epsilon,
                                        num_images,expt_type,channel)
CorrAns = []
for i,n in enumerate(quadrant):
    if quadrant[i] == 0: CorrAns.append("up")
    elif quadrant[i] == 1: CorrAns.append("left")
    elif quadrant[i] == 2: CorrAns.append("down")
    elif quadrant[i] == 3: CorrAns.append("right")
    base.append(bg_base)
    # print(quadrant[i],CorrAns[i])
data = pd.DataFrame({'File':names,'BGbase':base,'Color_change':color_change,'CorrAns':CorrAns})
data.to_csv("{}.csv".format(expt_type),index=False)