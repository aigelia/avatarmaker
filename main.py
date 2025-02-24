from PIL import Image

image = Image.open("example.jpg")
red, green, blue = image.split()

red_coordinates_1 = (50, 0, red.width, red.height)
red_cropped_1 = red.crop(red_coordinates_1)
red_coordinates_2 = (25, 0, red.width - 25, red.height)
red_cropped_2 = red.crop(red_coordinates_2)
red_cropped = Image.blend(red_cropped_1, red_cropped_2, 0.5)

blue_coordinates_1 = (0, 0, blue.width - 50, blue.height)
blue_cropped_1 = blue.crop(blue_coordinates_1)
blue_coordinates_2 = (25, 0, blue.width - 25, blue.height)
blue_cropped_2 = blue.crop(blue_coordinates_2)
blue_cropped = Image.blend(blue_cropped_1, blue_cropped_2, 0.5)

green_coordinates = (25, 0, green.width - 25, green.height)
green_cropped = green.crop(green_coordinates)

new_image = Image.merge("RGB", (red_cropped, green_cropped, blue_cropped))
# new_image.thumbnail(80, 80)

new_image.save("new_image.jpg")