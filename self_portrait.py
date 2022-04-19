import imageio as iio
import numpy as np
from matplotlib import pyplot as plt
import os

img_source = iio.imread(os.path.join(os.getcwd(), "image_files//self_0.jpg"))
img_source = np.array(img_source)

# print(img_source)


# get greyscaled image
def get_surrounding(image, x, y, size_x = 5, size_y = 5):
    x_start = max(x - size_x, 0)
    x_end = min(x + size_x + 1, image.shape[0])
    y_start = max(y - size_y, 0)
    y_end = min(y + size_y + 1, image.shape[1])
    background = np.zeros(3)
    counter = 0
    for image_x in range(x_start, x_end, 1):
        for image_y in range(y_start, y_end, 1):
            background += image[image_x, image_y]
            counter += 1
    background = np.divide(background, counter)
    return background

target_image = np.zeros(img_source.shape)
for image_x in range(target_image.shape[0]):
    print(image_x)
    for image_y in range(target_image.shape[1]):
        background = get_surrounding(img_source, image_x, image_y, size_x = 5, size_y = 5)
        # print(background)

        # # horizontal boundary
        # if abs(np.sum(img_source[image_x, image_y, :] - background)) > 15:
        #     target_image[image_x, image_y] = (1, 1, 1)


        # blurred greyscale
        if image_x < 440 or image_y < 520:
            if np.sum(background) > 250:
                target_image[image_x, image_y] = (1, 1, 1)
            elif np.sum(background) > 200:
                target_image[image_x, image_y] = (.8, .8, .8)
            elif np.sum(background) > 150:
                target_image[image_x, image_y] = (.6, .6, .6)
            elif np.sum(background) > 100:
                target_image[image_x, image_y] = (.4, .4, .4)
            elif np.sum(background) > 50:
                target_image[image_x, image_y] = (.3, .3, .3)
        else:
            target_image[image_x, image_y] = (1, 1, 1)


np.save(os.path.join(os.getcwd(), "target_image"), target_image)
plt.imshow(target_image)
plt.show()