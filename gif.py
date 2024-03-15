import os
import imageio

file_list = sorted(os.listdir("img"))

IMAGES = []
for file_name in file_list:
    file_path = "img/" + file_name
    image = imageio.imread(file_path)
    IMAGES.append(image)

imageio.mimsave("my_output.gif", IMAGES)