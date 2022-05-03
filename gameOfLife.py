import numpy


def compute_number_neighbors(padded_frame, index_line, index_column):
    number_neighbors = 0
    if padded_frame[index_line + 1][index_column] == 1:
        number_neighbors += 1
    if padded_frame[index_line - 1][index_column] == 1:
        number_neighbors += 1
    if padded_frame[index_line][index_column + 1] == 1:
        number_neighbors += 1
    if padded_frame[index_line][index_column - 1] == 1:
        number_neighbors += 1
    if padded_frame[index_line + 1][index_column + 1] == 1:
        number_neighbors += 1
    if padded_frame[index_line - 1][index_column - 1] == 1:
        number_neighbors += 1
    if padded_frame[index_line - 1][index_column + 1] == 1:
        number_neighbors += 1
    if padded_frame[index_line + 1][index_column - 1] == 1:
        number_neighbors += 1
    return number_neighbors


def live_or_die(number_neighbors, cell, frame, index_line, index_column):
    if cell == 0 and number_neighbors == 3:
        frame[index_line - 1][index_column - 1] = 1
    elif cell == 1 and (number_neighbors != 3 and number_neighbors != 2):
        frame[index_line - 1][index_column - 1] = 0
    return frame


def compute_next_frame(frame):

    padded_frame = numpy.pad(frame, 1, mode="constant")

    for index_line in range(1, len(padded_frame) - 1):
        for index_column in range(1, len(padded_frame[0]) - 1):
            number_neighbors = compute_number_neighbors(
                padded_frame, index_line, index_column)
            cell = padded_frame[index_line][index_column]
            frame = live_or_die(number_neighbors, cell,
                                frame, index_line, index_column)
    return frame
