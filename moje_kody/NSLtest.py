weight = 0.3
goal_pred = 0.8
alpha = 0.1
input = 2

for iteration in range(20):
    pred = weight * input
    error = (pred - goal_pred) ** 2
    derivative = input * (pred - goal_pred)
    weight = weight - (derivative * alpha)
    print("Error:" +str(error) + " Prediction:" + str(pred))
