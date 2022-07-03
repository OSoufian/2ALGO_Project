from Box import Box

def box_stacking_r(boxes):
    box_possibilities = []

    for i in range(len(boxes)):
        current_box = boxes[i]
        box_1 = Box(current_box.height, min(current_box.width, current_box.depth), max(current_box.width, current_box.depth))
        box_2 = Box(current_box.width, min(current_box.height, current_box.depth), max(current_box.height, current_box.depth))
        box_3 = Box(current_box.depth, min(current_box.width, current_box.height), max(current_box.width, current_box.height))
        box_possibilities.extend([box_1, box_2, box_3])

    box_possibilities.sort(key=lambda box: box.get_area(), reverse=True)    

    H = [box.height for box in box_possibilities]
    max_height = find_highest(box_possibilities, H, 1)
    print("La hauteur maximale :", max_height)

def find_highest(boxes, H, i):
    for j in range(0, i):
        if boxes[i].width < boxes[j].width and boxes[i].depth < boxes[j].depth:
                if H[i] < H[j] + boxes[i].height:
                    H[i] = H[j] + boxes[i].height

    if i == (len(boxes) - 1):
        return max(H)

    return find_highest(boxes, H, i+1)