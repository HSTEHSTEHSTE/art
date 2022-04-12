import imageio as iio
import numpy as np
from matplotlib import pyplot as plt
import os

img_source = iio.imread(os.path.join(os.getcwd(), "image_files//shanghai.jpg"))
img_source = np.array(img_source)

# find base colour
base_colour_0 = np.zeros(3)
counter = 0
for column in range(img_source.shape[1]):
    for pixel_x in range(30):
        base_colour_0 += img_source[pixel_x, column]
        counter += 1
base_colour_0 = np.divide(base_colour_0, counter)

base_colour_1 = np.zeros(3)
counter = 0
for column in range(img_source.shape[1]):
    for pixel_x in range(-30, 0, 1):
        base_colour_1 += img_source[pixel_x, column]
        counter += 1
base_colour_1 = np.divide(base_colour_1, counter)

base_colours = [base_colour_0, base_colour_1]
print(base_colours)

boundary = np.zeros(img_source.shape)
for column in range(img_source.shape[1]):
    for pixel_x in range(img_source.shape[0]):
        if np.sum(np.abs(img_source[pixel_x, column, :] - base_colour_0)) > 80 and np.sum(np.abs(img_source[pixel_x, column, :] - base_colour_1)) > 40:
            boundary[pixel_x, column] = np.array([1, 1, 1])

for column in range(img_source.shape[1]):
    for pixel_x in range(img_source.shape[0]):
        if np.divide(column, img_source.shape[1]) + np.divide(pixel_x, img_source.shape[0]) <= 1:
            if boundary[pixel_x, column, 0] == 0:
                boundary[pixel_x, column] = np.array([1, 0, 0])

# print(boundary)
img = plt.imshow(boundary, interpolation='nearest')
img.set_cmap('hot')
plt.axis('off')
# plt.show()
plt.savefig(os.path.join(os.getcwd(), "image_files//shanghai_0.jpg"), bbox_inches='tight', pad_inches = 0.0)