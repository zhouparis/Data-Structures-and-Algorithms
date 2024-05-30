def feedDog(hunger_level, biscuit_size):
    hunger_level.sort()
    biscuit_size.sort()

    hunger_index, biscuit_index = 0, 0
    dogs_satisfied = 0
    hunger_length = len(hunger_level)
    biscuit_length = len(biscuit_size)
    
    while hunger_index < hunger_length and biscuit_index < biscuit_length :
        if biscuit_size[biscuit_index] >= hunger_level[hunger_index]:
            dogs_satisfied += 1
            hunger_index += 1
        biscuit_index += 1

    return dogs_satisfied
