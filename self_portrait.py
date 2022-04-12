import imageio as iio
import numpy as np
from matplotlib import pyplot as plt

img_source = iio.imread("C://Users//HSTE//JHU//Fall 2021//Lab//self.jpg")
img_source = np.array(img_source)

print(img_source)