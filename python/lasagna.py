#Exercise from excercis.org

#TO DO Define a expected bake time constant
EXPECTED_BAKE_TIME = 40

#Calculate the remaining bake time in minutes
def bake_time_remaining(actual_time):
    """Calculate time remaining"""
    current_time = 40
    EXPECTED_BAKE_TIME = current_time - actual_time
    return EXPECTED_BAKE_TIME


#Calculate preparation time in minutes, by number of layers
def preparation_time_in_minutes(number_of_layers):
    """
    Calculate preparation time by multiply the number of layer by 2
    """
    time_per_layer = 2
    time_in_minutes = time_per_layer * number_of_layers
    return time_in_minutes

#Calculate the elapsed cooking time in minutes
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate elapsed bake time in minutes, multiply one parameter by 2 and sum this
    parameter with other parameter 
    """
    total_elapsed_time = elapsed_bake_time + number_of_layers * 2
    return total_elapsed_time