from objects.hazards import *
from objects.player import Player
from objects.static import *
from objects.object_with_goals import *
from objects.movable import *

from core.state_manger import State


#lvl01
w=1+2
h=5+2

objects = []

#left and right walls
for i in range(0,h):
    wall = Wall(0,i)
    objects.append(wall)
    wall = Wall(w-1,i)
    objects.append(wall)
#top and bottom walls
for i in range(0,w):
    wall = Wall(i,0)
    objects.append(wall)
    wall = Wall(i,h-1)
    objects.append(wall)




objects.append(Player(1,5))
objects.append(TopOfPillarObject(1,4,color="yellow"))


goal_objects = [
    TopOfPillarObject(1,1,color="yellow"),
]


state = State(
    w,
    h,
    objects,
    goal_objects
)



from collections import deque
from core.enums import PushDirection
import os

def bfs_solve(initial_state: State):
    queue = deque()
    visited = set()

    queue.append((initial_state, []))
    visited.add(initial_state)

    while queue:
        state, path = queue.popleft()
        # os.system("cls")
        print(" ".join(PushDirection._names[d] for d in path))

        if state.is_completed():
            return path

        for d in [
            PushDirection.UP,
            PushDirection.DOWN,
            PushDirection.LEFT,
            PushDirection.RIGHT,
        ]:
            next_state = state.step(d)
            if next_state is None:
                continue

            if next_state in visited:
                continue

            visited.add(next_state)
            queue.append((next_state, path + [d]))

    return None




solution = bfs_solve(state)

if solution is None:
    print("No solution found")
else:
    print("Solution:", solution)
    print(" ".join(PushDirection._names[d] for d in solution))