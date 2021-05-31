# AWS_DeepRacer
The fastest way to get rolling with machine learning! AWS DeepRacer challenges! 

> Machine learning is the way for machines to beat humans in achieving something! The best way for them to achieve greatness, is by using the full power of reinforcement learning. 

Rather than to invent the wheel myself, a solution was found to have the AI teach itself how to get he best result possible. The model is based on the following thought process: 

1) The more progress made, 
2) In the least amount of steps, 
3) All wheels on the track,
4) Result: a quick laptime!


## Results
This model is currently in training for 2 hours and updates will be posted after. 

## Reward Function

```python
def reward_function(params):

    if params["all_wheels_on_track"] and params["steps"] > 0:
        reward = ((params["progress"] / params["steps"]) * 100) + (params["speed"]**2)
    else:
        reward = 0.01
        
    return float(reward)
```
