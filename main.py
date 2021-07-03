IMG_RES = 416

piece_to_index = {
    'Black_bishop': 0,
    'Black_king': 1,
    'Black_knight': 2,
    'Black_pawn': 3,
    'Black_queen': 4,
    'Black_rook': 5,
    'White_bishop': 6,
    'White_king': 7,
    'White_knight': 8,
    'White_pawn': 9,
    'White_queen': 10,
    'White_rook': 11
}


def str_to_percent_to_str(n):
    return str(float(n) / IMG_RES)


def two_corners_to_center_and_sizes(four_coords):
    if True:
        return [str((float(four_coords[0]) + float(four_coords[2])) / 2),
                str((float(four_coords[1]) + float(four_coords[3])) / 2),
                str(abs(float(four_coords[0]) - float(four_coords[2]))),
                str(abs(float(four_coords[1]) - float(four_coords[3])))]
    else:
        return four_coords


# classes = ['Black_bishop',
#            'Black_king',
#            'Black_knight',
#            'Black_pawn',
#            'Black_queen',
#            'Black_rook',
#            'White_bishop',
#            'White_king',
#            'White_knight',
#            'White_pawn',
#            'White_queen',
#            'White_rook']

if __name__ == '__main__':
    with open('_annotations.txt') as f:
        content = f.readlines()

    content = [x.strip() for x in content]
    for line in content:
        line_list = line.split(' ')
        file_name = line_list.pop(0).split('.')
        file_name.pop()
        file_name.append('txt')
        new_file = '.'.join(file_name)
        print(new_file)
        f = open(new_file, 'w')
        for five in line_list:
            coords = five.split(',')
            # This line will put class name
            # class_id = classes[int(coords.pop())]
            # This line will put class ID
            class_id = coords.pop()
            coords = two_corners_to_center_and_sizes(coords)
            coords = list(map(str_to_percent_to_str, coords))
            coords.insert(0, class_id)
            output = ' '.join(coords)
            print(output)

            f.write(output + '\n')
        f.close()
        print('\n')
