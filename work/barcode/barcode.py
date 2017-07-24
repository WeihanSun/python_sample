# barcode can be used to connect images with their IDs
import numpy as np
import cv2

# barcode setting
BIT_SIZE_BARCODE = 32
BIT_SIZE_SCENE_ID = 14
BIT_SIZE_FRAME_ID = 18
CELL_SIZE = 4
OFFSET_X = 10
OFFSET_Y = 10


# read barcode
def read_barcode(infile):
    img = cv2.imread(infile, cv2.IMREAD_COLOR)
    w = img.shape[1]
    barcode_left = w - OFFSET_X - CELL_SIZE
    barcode_top = OFFSET_Y
    scene_id, frame_id = 0, 0
    threshold = 30
    for b in range(0, BIT_SIZE_SCENE_ID):
        x = barcode_left - CELL_SIZE * b
        y = barcode_top
        if np.all(img[y:y + CELL_SIZE, x:x + CELL_SIZE, :] < threshold):
            scene_id += (0x1 << b)

    for b in range(0, BIT_SIZE_FRAME_ID):
        x = barcode_left - CELL_SIZE * BIT_SIZE_SCENE_ID - CELL_SIZE * b
        y = barcode_top
        if np.all(img[y:y + CELL_SIZE, x:x + CELL_SIZE, :] < threshold):
            frame_id += (0x1 << b)

    return scene_id, frame_id


# add barcode
def add_barcode(infile, outfile, scene_id, frame_id):
    img = cv2.imread(infile, cv2.IMREAD_COLOR)
    w = img.shape[1]
    barcode_left = w - OFFSET_X - CELL_SIZE
    barcode_top = OFFSET_Y
    for b in range(0, BIT_SIZE_SCENE_ID):
        x = barcode_left - CELL_SIZE * b
        y = barcode_top
        if ((scene_id >> b) & 0x1) == 1:
            img[y:y + CELL_SIZE, x:x + CELL_SIZE, :] = 0
        else:
            img[y:y + CELL_SIZE, x:x + CELL_SIZE, :] = 255

    for b in range(0, BIT_SIZE_FRAME_ID):
        x = barcode_left - CELL_SIZE * BIT_SIZE_SCENE_ID - CELL_SIZE * b
        y = barcode_top
        if ((frame_id >> b) & 0x1) == 1:
            img[y:y + CELL_SIZE, x:x + CELL_SIZE, :] = 0
        else:
            img[y:y + CELL_SIZE, x:x + CELL_SIZE, :] = 255

    cv2.imwrite(outfile, img)
