
from flask import Flask, request, send_file, render_template
from PIL import Image
import math
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def image_to_matrix(image_path):
    img = Image.open(image_path)
    w, h = img.size
    matrix = []
    for y in range(h):
        r = []
        for x in range(w):
            pixel = img.getpixel((x, y))
            r.append(pixel)
        matrix.append(r)
    return matrix


def matrix_to_image(A, output_path):
    h = len(A)
    w = len(A[0]) if h > 0 else 0
    img = Image.new("RGB", (w, h))
    for y in range(h):
        for x in range(w):
            img.putpixel((x, y), A[y][x])
    img.save(output_path)


def rotate_matrix_angle(A, a, bg=(255, 255, 255)):
    a_r = math.radians(a)
    h, w = len(A), len(A[0])
    cos_r, sin_r = math.cos(a_r), math.sin(a_r)
    new_w = int(abs(w * cos_r) + abs(h * sin_r))
    new_h = int(abs(w * sin_r) + abs(h * cos_r))
    new_m = [[bg for _ in range(new_w)] for _ in range(new_h)]
    xo, yo = w / 2, h / 2
    cx_new, cy_new = new_w / 2, new_h / 2
    for i in range(new_h):
        for j in range(new_w):
            x_old = (j - cx_new) * cos_r + (i - cy_new) * sin_r + xo
            y_old = -(j - cx_new) * sin_r + (i - cy_new) * cos_r + yo
            if 0 <= int(x_old) < w and 0 <= int(y_old) < h:
                new_m[i][j] = A[int(y_old)][int(x_old)]
    return new_m


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]
        angle = int(request.form["angle"])
        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(input_path)

        matrix = image_to_matrix(input_path)
        rotated = rotate_matrix_angle(matrix, angle)
        output_path = os.path.join(UPLOAD_FOLDER, "rotated_" + file.filename)
        matrix_to_image(rotated, output_path)
        return send_file(output_path, mimetype='image/png')

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
