class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_neighbours(self):
        return [Position(x=self.x - 1, y=self.y), Position(x=self.x + 1, y=self.y),
                Position(x=self.x, y=self.y - 1), Position(x=self.x, y=self.y + 1)]

    def is_equal(self, position):
        return self.y == position.y and self.x == position.x

    def __eq__(self, position):
        return self.is_equal(position)


def calculate_visions_dls(position, limit):
    limit += 1
    sentinel = Position(None, None)
    position_stack = [position]
    visited = []
    path = []

    while position_stack:
        current_position = position_stack.pop()

        if current_position == sentinel:

            # finished this level; go back up one level
            limit += 1

        elif limit > 0:

            # go one level deeper, push sentinel
            limit -= 1
            path.append(current_position)
            position_stack.append(sentinel)
            visited.append(current_position)

            if limit > 0:
                for neighbour in _get_valid_neighbours(current_position.get_neighbours()):
                    if neighbour not in visited:
                        position_stack.append(neighbour)
    return path


def _get_valid_neighbours(neighbours):
    valid_neighbours = []
    for neighbour in neighbours:
        if 0 <= neighbour.x < 24:
            if 0 <= neighbour.y < 24:
                valid_neighbours.append(neighbour)
    return valid_neighbours


def _join_visions(vision_positions):
    final_list = []
    for position in vision_positions:
        if any(position == new_pos for new_pos in final_list):
            continue
        else:
            final_list.append(position)
    return final_list


fog = _join_visions(calculate_visions_dls(Position(20, 22), 5))
for f in fog:
    print(f.y, '    ', f.x)
# a = [Position(1, 2), Position(2, 5), Position(1, 2), Position(1, 2), Position(2, 5), Position(1, 10)]
