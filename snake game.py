usergboard = input("Enter the game board size ")
gboard = int(usergboard) * int(usergboard)
snakepell = 1
snakesize = 1
while snakesize < gboard :
    snakesize = snakesize * 2
    snakepell += 1
print(f"The final snake size is :{snakesize}")
print(f"The final pellet count is :{snakepell}")