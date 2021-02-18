# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).

# Tower block is represented as *

[
  '     *     ', 
  '    ***    ', 
  '   *****   ', 
  '  *******  ', 
  ' ********* ', 
  '***********'
]

def tower_builder(n_floors):
    height = 0
    building = []
    floor = ''
    while height < n_floors:
        height = height + 1
        stars = (((height*2)-1)*'*')
        white_space = ' ' * (n_floors - height)
        floor = white_space + stars + white_space
        building.append(floor)
    return building
