def reward_function(params):
    '''
    In @params object:
    {
        "all_wheels_on_track": Boolean,    # flag to indicate if the vehicle is on the track
        "progress": float,                 # percentage of track completed
        "steps": int,                      # number steps completed
        "speed": float,                    # vehicle's speed in meters per second (m/s)
    }
    '''
    # ONLY 4 PARAMETERS ARE USED TO MAKE THE MOST OF REINFORCED LEARNING! 
    # LET THE MACHINE LEARN THE TRICK WIHTOUT HUMAN INTERFERENCE! 
    if params["all_wheels_on_track"] and params["steps"] > 0:
        reward = ((params["progress"] / params["steps"]) * 100) + (params["speed"]**2)
    else:
        reward = 0.01
        
    return float(reward)
