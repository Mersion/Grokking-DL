weight = 0.3
goal_pred = 0.8
input = 2
alpha = 0.1

for iteration in range(20):
    pred = input * weight
    error = (pred - goal_pred) ** 2
    #delta = pred - goal_pred
    #weight_delta = input * delta
    derivative = input * (pred - goal_pred)
    weight = weight - (alpha * derivative)
    print("Error:" +str(error) + " Prediction:" + str(pred))
    
