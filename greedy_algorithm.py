class Box:
    def __init__(self, height, width, depth):
        self.height = height
        self.width = width
        self.depth = depth

    def get_area(self):
        return self.width * self.depth

def box_stacking(boxes):
    box_possibilities = []

    for i in range(len(boxes)):
        current_box = boxes[i]
        box_1 = Box(current_box.height, current_box.width, current_box.depth)
        box_2 = Box(current_box.depth, current_box.width, current_box.height)
        box_3 = Box(current_box.width, current_box.height, current_box.depth)
        box_possibilities.extend([box_1, box_2, box_3])

    box_possibilities.sort(key=lambda box: box.get_area(), reverse=True)

    stacked_boxes = []
    for i in range(len(box_possibilities)):
        if stacked_boxes == []:
            stacked_boxes.append(box_possibilities[i])

        else:
            if box_possibilities[i].width < stacked_boxes[-1].width and box_possibilities[i].depth < stacked_boxes[-1].depth:
                stacked_boxes.append(box_possibilities[i])

    print(sum(box.height for box in stacked_boxes))

box_stacking([Box(2, 7, 5), Box(7, 6, 3), Box(10, 20, 5), Box(3, 4, 5)])