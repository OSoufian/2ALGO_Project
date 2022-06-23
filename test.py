from Box import Box


test = [Box(2, 7, 5), Box(7, 6, 3), Box(10, 20, 5), Box(3, 4, 5)]
max_height = [box.height for box in test]


print(max_height)
