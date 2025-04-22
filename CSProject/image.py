import math
from PIL import Image
from CSProject.matrix import matrix_multiplication


def image_to_matrix(image_path):
    img = Image.open(image_path)
    width, height = img.size

    matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            pixel = img.getpixel((x, y))
            row.append(pixel)
        matrix.append(row)

    return matrix

def matrix_to_image(matrix, output_path):
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0
    mode = "L" if isinstance(matrix[0][0], int) else "RGB"

    img = Image.new(mode, (width, height))

    for y in range(height):
        for x in range(width):
            img.putpixel((x, y), matrix[y][x])  # Manually set pixel values

    img.save(output_path)

def rotate_matrix(matrix, angle):
    rotated = []
    function = [[math.cos(angle), math.sin(angle)], [-(math.sin(angle), math.cos(angle))]]
    matrix_multiplication(function*matrix)