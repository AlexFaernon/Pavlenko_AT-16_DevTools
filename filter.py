from PIL import Image
import numpy as np

CELL_X_OFFSET = 10
CELL_Y_OFFSET = 10
GREY_GRADATION = 50


def try_image_from_path(path):
    try:
        Image.open(path)
        return True
    except FileNotFoundError:
        return False


def try_save(res, path):
    try:
        res.save(path)
        return True
    except FileNotFoundError:
        return False


def filtering():
    path = input()
    while True:
        if try_image_from_path(path):
            img = Image.open(path)
            break

    img_matrix = np.array(img)
    len_x = len(img_matrix)
    len_y = len(img_matrix[1])
    cell_x = 0
    while cell_x < len_x:
        cell_y = 0
        while cell_y < len_y:
            sum_rgb = 0
            sum_rgb += np.sum(img_matrix[cell_x:cell_x + CELL_X_OFFSET, cell_y:cell_y + CELL_Y_OFFSET]) // 3
            sum_rgb = int(sum_rgb // 100)
            grey_matrix = np.zeros((CELL_X_OFFSET, CELL_Y_OFFSET, 3))
            grey_matrix[:] = int(sum_rgb // GREY_GRADATION) * GREY_GRADATION
            img_matrix[cell_x:cell_x + CELL_X_OFFSET, cell_y:cell_y + CELL_Y_OFFSET] = grey_matrix
            cell_y = cell_y + CELL_Y_OFFSET
        cell_x = cell_x + CELL_X_OFFSET
    res = Image.fromarray(img_matrix)

    while True:
        path = input()
        if try_save(res, path):
            break


filtering()
