weight = 0.5
input = 0.5
goal_prediction = 0.8
step_amount = 0.001
reach = 0
while reach < 1:
    prediction = input * weight
    error = (prediction - goal_prediction) ** 2

    print("Error:" + str(error) + " Prediction:" + str(prediction))

    up_prediction = input * (weight + step_amount)
    up_error = (up_prediction - goal_prediction) ** 2

    down_prediction = input * (weight - step_amount)
    down_error = (down_prediction - goal_prediction) ** 2

    if down_error < up_error:
        weight -= step_amount
    if up_error < down_error:
        weight += step_amount
    
    if down_prediction > goal_prediction or up_prediction > goal_prediction:
        reach += 1

