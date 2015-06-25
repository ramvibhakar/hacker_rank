__author__ = 'ramvibhakar'
T = input()

def choose_enemy1(data,min_req):
    min = 1001
    min_power = 0
    min_bullet = 0
    for arr in data:
        if arr[1] >= min_req:
            return arr[0],arr[1]
        elif arr[1] < min:
            min = arr[1]
            min_power = arr[0]
            min_bullet = arr[1]
    return min_power,min_bullet

def choose_enemy2(data,min_req):
    diff_arr = [bullets - power for power,bullets in data]
    max = -1001
    min_power = 0
    min_bullet = 0
    for i in xrange(0,len(data)):
        if max <= diff_arr[i]:
            max = diff_arr[i]
            min_power = data[i][0]
            min_bullet = data[i][1]
    return  min_power,min_bullet
while T > 0:
    game_start_bullets = 0
    n_levels,n_enemies =[int(num) for num in raw_input().split()]
    powers = []
    data_set = []
    for i in xrange(0,n_levels):
        power = [int(num) for num in raw_input().split()]
        powers.append(power)
    for i in xrange(0,n_levels):
        bullet = raw_input().split()
        data_row = []
        for j in xrange(0,len(bullet)):
            item = [powers[i][j],int(bullet[j])]
            data_row.append(item)
        data_set.append(data_row)
    arr = sorted(data_set[len(data_set)-1])
    required = arr[0][0]
    for i in xrange(len(data_set)-2,-1,-1):
        #chosen_enemy, enemy_bullets, criteria_met = choose_enemy(data_set[i],required)
        chosen_enemy, enemy_bullets = choose_enemy1(data_set[i],required)
        if not enemy_bullets < required:
            required = chosen_enemy
        else:
            game_start_bullets += required - enemy_bullets
            required = chosen_enemy
    game_start_bullets += chosen_enemy
    game_start_bullets2 = 0
    arr = sorted(data_set[len(data_set)-1])
    required = arr[0][0]
    for i in xrange(len(data_set)-2,-1,-1):
        #chosen_enemy, enemy_bullets, criteria_met = choose_enemy(data_set[i],required)
        chosen_enemy, enemy_bullets = choose_enemy2(data_set[i],required)
        if not enemy_bullets < required:
            required = chosen_enemy
        else:
            game_start_bullets2 += required - enemy_bullets
            required = chosen_enemy
    game_start_bullets2 += chosen_enemy
    print(min(game_start_bullets,game_start_bullets2))
    T -= 1


