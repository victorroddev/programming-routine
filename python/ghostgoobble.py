#Excercise from exercism.org

#Define a function that takes two parameters, 
#If Pac-Man has a power pellect activate and if Pac- Man is touching a ghost.
#Return a boolean value if Pac-Man is able to ear a ghost.
#The function should return True only if Pac-Man has a power pellet and is touching a ghost.
def eat_ghost(power_pellet_activate, touching_ghost):
    """Verify that pac man can eat a ghost if he is empowered by a power pellet.
    
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - can a ghost be eaten?
    """
    
    return power_pellet_activate and touching_ghost

#Define a function that takes two parameters (if Pac Man is touching a power pellet
#and if Pac Man is touching a dot) and return a Boolean if Pac Man scored.
#The function should return True if Pacman is touching a power pellet or a dot.
def score(touching_power_pellet, touching_dot):
    """Verify if Pac Man Is touching a power pellet or a dot
    :param touching_dot: bool - is the player touching a dot?
    :return: bool - has the player scored or not?
    """

    return touching_power_pellet or touching_dot

"""Define if Pac Man loses, function that takes two parameters(if PacMan has a power pellet
activate and if Pac Man is touching a ghost) and return a Boolean value if Pac-Man loses.
Should return True if Pac Man is touching a ghost and does not have a power pellet active
"""
def loser(power_pellet_active, touching_ghost):
    """Trigger the game loop to end (game over) when Pac-Man touches a ghost witout his power pellet
    
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player lost the game?
    """

    return not power_pellet_active and touching_ghost

"""Function that takes three parameter (if pac-man has eaten all of the dots, if pac-man has a power pellet active, and if Pac-Man
is touching a ghost) return a boolean value if Pac-Man wins. Should return True if Pac-Man has eaten all of the dots and has not lost
based on the parameter of the past function
"""
def win(has_eaten_all_dots, power_pellet_active, touching_ghost):  
    """Trigger the victory event when all dots have been eaten.

    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player won the game?
    """
    
    return has_eaten_all_dots and power_pellet_active or not power_pellet_active and not touching_ghost