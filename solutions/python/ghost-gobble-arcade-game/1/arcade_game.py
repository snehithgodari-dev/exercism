def eat_ghost(power_pellet_active, touching_a_ghost):
    return power_pellet_active and touching_a_ghost


def score(touching_power_pallet, touching_a_dot):
    return touching_power_pallet or touching_a_dot


def lose(power_pellet_active, touching_a_ghost):
    return touching_a_ghost and not power_pellet_active


def win(eaten_all_dots, power_pallet_active, touching_ghost):
    return eaten_all_dots and not lose(power_pallet_active, touching_ghost)