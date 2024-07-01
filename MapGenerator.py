import random

_ = False

def generate_dungeon_map():
    map_size = 64
    wall = 1
    textures = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    # Initialize map with walls
    dungeon_map = [[wall for _ in range(map_size)] for _ in range(map_size)]

    def add_room(x, y, width, height):
        for i in range(y, y + height):
            for j in range(x, x + width):
                if 1 <= i < map_size-1 and 1 <= j < map_size-1:
                    dungeon_map[i][j] = random.choice(textures)

    def add_corridor(x1, y1, x2, y2):
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                if 1 <= y < map_size-1:
                    dungeon_map[y][x1] = random.choice(textures)
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                if 1 <= x < map_size-1:
                    dungeon_map[y1][x] = random.choice(textures)

    # Add some rooms
    num_rooms = 10
    for _ in range(num_rooms):
        room_width = random.randint(5, 15)
        room_height = random.randint(5, 15)
        x = random.randint(1, map_size - room_width - 1)
        y = random.randint(1, map_size - room_height - 1)
        add_room(x, y, room_width, room_height)

    # Add some corridors
    for _ in range(num_rooms):
        x1 = random.randint(1, map_size - 2)
        y1 = random.randint(1, map_size - 2)
        x2 = random.randint(1, map_size - 2)
        y2 = random.randint(1, map_size - 2)
        add_corridor(x1, y1, x2, y2)

    return dungeon_map

MAP = generate_dungeon_map()

# Printing the map to check the structure
for row in MAP:
    print(row)