from astro_pi_orbit import ISS
from picamzero import Camera


def get_gps_coordinates(iss):
    """
    Returns a tuple of latitude and longitude coordinates expressed
    in signed degrees minutes seconds.
    """
    point = iss.coordinates()
    return (point.latitude.signed_dms(), point.longitude.signed_dms())


cam = Camera()
iss = ISS()

cam.take_photo("gps_image1.jpg", gps_coordinates=get_gps_coordinates(iss))

estimate_kmps = 7.1234567890

estimate_kmps_formatted = "{:.4f}".format(estimate_kmps)

output_string = estimate_kmps_formatted

file_path = "result.txt"
with open(file_path, 'w') as file:
    file.write(output_string)

print("Data written to", file_path)
