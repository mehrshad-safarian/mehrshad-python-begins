health = 10 
while health > 0:
    print(health)
    health -= 1 # forgetting this line will result infinite loop 

# infinite loop
game_over = False
while not game_over:
    print(game_over)
    game_over -= 1