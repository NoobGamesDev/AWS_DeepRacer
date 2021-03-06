# AWS_DeepRacer
The fastest way to get rolling with machine learning! AWS DeepRacer challenges! 

> Machine learning is the way for machines to beat humans in achieving something! The best way for them to achieve greatness, is by using the full power of reinforcement learning. 

This repo is build to provide the community with Machine Learning Algorithms that can be used both in the AWS DeepRacer challange, and beyond! Feel free to use any (parts or full) of the codes, and try to beat my results! I'll be happy to contribute to your success! :) 


## ML_Learner
Rather than to invent the wheel myself, a solution was found to have the AI teach itself how to get he best result possible. The model is based on the following thought process: 

1) The more progress made, 
2) In the least amount of steps, 
3) All wheels on the track,
4) Result: a quick laptime!


### Reward Function

```python
def reward_function(params):

    if params["all_wheels_on_track"] and params["steps"] > 0:
        reward = ((params["progress"] / params["steps"]) * 100) + (params["speed"]**2)
    else:
        reward = 0.01
        
    return float(reward)
```
### Results - Cosmic Loop

This model has been **trained for 10 hours** and provided the following results: 

![image](https://user-images.githubusercontent.com/20015201/120315536-61869f80-c2d4-11eb-9b45-9e88b22ab9ee.png)



#### Evaluation Results 

| Trial | Time (MM:SS.mmm)  | Trial results (% track completed) | Status       |
|-------|-------------------|-----------------------------------|--------------|
|1	    | 01:06.001         | 100%	                            | Lap Complete |
|2	    | 01:02.732	        | 100%	                            | Lap Complete |
|3	    | 00:27.229	        | 40%	                            | Off track    |



### Results - Kuei Raceway
This model has been **trained for 2 hours** and provided the following results: 

![image](https://user-images.githubusercontent.com/20015201/120245416-08cbee00-c265-11eb-9eb7-4f63981138e5.png)

The model seems to progress the learning curve in a smooth way up. 
Therefore I conclude that the agent learns on a steady pace, though, with only 2 hours of training it's not all conclusive. 
More training will be needed. 

#### Evaluation Results 

| Trial | Time (MM:SS.mmm)  | Trial results (% track completed) | Status    |
|-------|-------------------|-----------------------------------|-----------|
|1	    | 00:30.580         | 52%	                            | Off track |
|2	    | 00:22.734	        | 30%	                            | Off track |
|3	    | 00:30.670	        | 52%	                            | Off track |


****


## ML_Racer
This algorithm checks various variables in order to achieve the best laptime around a racetrack. For the full source code, see [ML_Racer.py][1] 

The first part is to check if the car is on the track. 
```python
def on_track_reward(current_reward, on_track):
    if not on_track:
        current_reward = MIN_REWARD
    else:
        current_reward = MAX_REWARD
```

After that the car will be rewarded for being near the center line. 
The more distance from center, the lesser it's reward will be.
```python
    def distance_from_center_reward(current_reward, track_width, distance_from_center):
        # Calculate 3 marks that are farther and father away from the center line
        marker_1 = 0.1 * track_width
        marker_2 = 0.25 * track_width
        marker_3 = 0.5 * track_width

        # Give higher reward if the car is closer to center line and vice versa
        if distance_from_center <= marker_1:
            current_reward *= 1.2
        elif distance_from_center <= marker_2:
            current_reward *= 0.8
        elif distance_from_center <= marker_3:
            current_reward += 0.5
        else:
            current_reward = MIN_REWARD  # likely crashed/ close to off track
```

As it's a racer, speed is also an important factor. Positive reward if the car is in a straight line going fast.
```python
    if abs(steering) < 0.1 and speed > 3:
        current_reward *= 1.2
```

To make sure the car isn't making too many meters, the algorithm verifies the distance between waypoints and the direction the car is heading. 
```python
        next_point = waypoints[closest_waypoints[1]]
        prev_point = waypoints[closest_waypoints[0]]

        # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
        direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0]) 
        # Convert to degrees
        direction = math.degrees(direction)

        # Cacluate difference between track direction and car heading angle
        direction_diff = abs(direction - heading)

        # Penalize if the difference is too large
        if direction_diff > DIRECTION_THRESHOLD:
            current_reward *= 0.5
```

As steering and acceleration ain't the best combination for a succesful racer, the model is rewarded when the speed is reduced while steering. 
```python
    def throttle_reward(current_reward, speed, steering):
        # Decrease throttle while steering
        if speed > 2.5 - (0.4 * abs(steering)):
            current_reward *= 0.8
```

### Results - Kuei Raceway
This model has been **trained for 5 hours** and provided the following results: 
  
![image](https://user-images.githubusercontent.com/20015201/120240864-825ddf00-c259-11eb-8d2c-494cd8fff7fa.png)
Rewards quickly jumped to around 32k, dropped a little and stayed around the same value.. 
Track completion stalled at 50% after a 5 hours training session.. 

#### AWS Virtual Race

![image](https://user-images.githubusercontent.com/20015201/120240382-51c97580-c258-11eb-8e61-d69d64a23648.png)


Ranking : **195**/562 

3 Laps Race : 03:38.631

Nr.1 Race : 01:06.983

#### Evaluation Results

| Trial | Time (MM:SS.mmm)  | Trial results (% track completed) | Status    |
|-------|-------------------|-----------------------------------|-----------|
|1	    | 00:34.790         | 56%	                            | Off track |
|2	    | 00:33.540	        | 55%	                            | Off track |
|3	    | 00:33.856	        | 54%	                            | Off track |




### Reward Function
For the full source code, see [ML_Racer.py][1] 

****


## Hyperparameters
|Hyperparameter                 |   Value    |
|:------------------------------|:-----------|
|Gradient descent batch size    |	64       |
|Entropy                        |	0.01     |
|Discount factor                |	0.999    |
|Loss type                      |	Huber    |
|Learning rate                  |	0.0003   |
|Number of experience episodes between each policy-updating iteration   |	20  |
|Number of epochs	            |   10       |


[1]: https://github.com/CheapWebdesign/AWS_DeepRacer/blob/main/ML_Racer.py
