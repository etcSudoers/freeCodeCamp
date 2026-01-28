"""
Scaled Image

Given a string representing the width and height of an image, and a number to scale the image, return the scaled width and height.

    The input string is in the format "WxH". For example, "800x600".
    The scale is a number to multiply the width and height by.

Return the scaled dimensions in the same "WxH" format.
"""


def scale_image(size: str, scale: float):
    strSplit = size.split("x")
    w = int(int(strSplit[0]) * scale)
    h = int(int(strSplit[1]) * scale)
    return f"{w}x{h}"


assert scale_image("800x600", 2) == "1600x1200"
assert scale_image("100x100", 10) == "1000x1000"
assert scale_image("1024x768", 0.5) == "512x384"
assert scale_image("300x200", 1.5) == "450x300"
