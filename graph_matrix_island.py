'''Given a non-empty array of ones and zeroes where ones represent islands and zeroes represent water, find the width and the height of the island if there can only be one island.'''

ocean =[
[0, 0, 0, 0,],
[0, 1, 1, 0,],
[0, 1, 1, 0,],
[0, 1, 1, 0 ],
]

'''width: 2
length: 3'''

'''Knowns:
Islands are rectangular.
The island can have at most 8 neighbors.'''

'''Gameplan:
Traverse through each row checking for a 1.
The first one you find will be the uppermost leftmost corner of the island.
Keep traversing for the bottom_right_corner variable.
This number should keep updating until there are no more 1s and which will denote the bottom right hand corner.
Now that you have two corners, you can find out the area of the island using indexing.
'''

top_left_corner = []
bottom_right_corner = []
# for c in 0 < ocean.count {
#   for r in 0 < ocean.count {
#     print()
#   }
# }