from Box import Box

def box_stacking(boxes):
    box_possibilities = []

    for i in range(len(boxes)):
        current_box = boxes[i]
        box_1 = Box(current_box.height, min(current_box.width, current_box.depth), max(current_box.width, current_box.depth))
        box_2 = Box(current_box.width, min(current_box.height, current_box.depth), max(current_box.height, current_box.depth))
        box_3 = Box(current_box.depth, min(current_box.width, current_box.height), max(current_box.width, current_box.height))
        box_possibilities.extend([box_1, box_2, box_3])

    box_possibilities.sort(key=lambda box: box.get_area(), reverse=True)

    max_height = [box.height for box in box_possibilities]

    # print(max_height[11])

    n = len(box_possibilities)

    for i in range(1, n):
        stacked_boxes = [box_possibilities[0]]
        for j in range(0, i):
            if box_possibilities[i].width < box_possibilities[j].width and box_possibilities[i].depth < box_possibilities[j].depth:
                if max_height[i] < max_height[j] + box_possibilities[i].height:
                    max_height[i] = max_height[j] + box_possibilities[i].height
                    if (box_possibilities[j].width == stacked_boxes[-1].width and box_possibilities[j].depth < stacked_boxes[-1].depth) or (box_possibilities[j].depth == stacked_boxes[-1].depth and box_possibilities[j].width < stacked_boxes[-1].width):
                        stacked_boxes.pop()
                    stacked_boxes.append(box_possibilities[j])
        stacked_boxes.append(box_possibilities[i])
        if max_height[i] == max(max_height):
            max_stack = stacked_boxes

    print(max(max_height))
    
    for i in range(len(max_stack)):
        print(max_stack[i].height, 'x', max_stack[i].width, 'x', max_stack[i].depth)

def refractor(file):
    boxes = open(f'{file}', 'r')
    Lines = boxes.readlines()
    count = 0
    boxList = []
    for line in Lines:
        boxList.append(Box([*map(lambda x: int(x), line.split())][0], [*map(lambda x: int(x), line.split())][1], [*map(lambda x: int(x), line.split())][2]))
        count += 1

    return boxList

box_stacking(refractor("boxes.txt"))