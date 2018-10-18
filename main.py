from random import randint

N = 1000
def pick_door_to_open(my_door, prize_door):
    if my_door == prize_door:
        # 2 = two choices to open
        return 2
    else:
        # 1 = only one choice for door to open
        return 1

def simulate(N):
    K = 0
    for _ in range(0, N):
        my_door = randint(1, 3)
        prize_door = randint(1, 3)
        opened_door = pick_door_to_open(my_door, prize_door)
        if opened_door == 1:
            K += 1
    return float(K) / float(N)

print(simulate(N))