from exif import Image
from datetime import datetime


def get_time(image):
    with open(image, 'rb') as image_file:
        img = Image(image_file)
        time_str = img.get("datetime_original")
        time = datetime.strptime(time_str, '%Y:%m:%d %H:%M:%S')
        return time
    
test = get_time("ExamplePhotos/atlas_photo_012.jpg")
test2 = get_time("ExamplePhotos/atlas_photo_013.jpg")
print("time of image 1:",test)
print("time of image 2:",test2)