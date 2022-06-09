health = 90
damage = 90

health = health - damage
print(health)
if health == 0:
    print('game over')
health = health + 50
print(health)

health = health * 1.5
health = health / 2