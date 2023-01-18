
def neural_network(input, weight):
    ''' (list, list of lists) -> list

    Na podstawie danych wejściowych zwraca przewidywanie.

    >>> neural_network([0,3,7], [[0.2,0.6,0.9],[1,2,4],[10,14,16]])
    [8.1, 34, 154]
    '''
    prediction = input * weight
    return prediction

'''number_of_toes = [8.5]
weight = 0.1
alpha = 0.01
win_or_lose_binary = [1] # (zwycięstwo!!!)
input = number_of_toes[0]
goal_pred = win_or_lose_binary[0]
pred = neural_network(input, weight)
error = (pred - goal_pred) ** 2
delta = pred - goal_pred
weight_delta = input * delta
weight -= weight_delta * alpha'''

#weight, goal_pred, input = (0.0, 0.8, 0.5)
'''for iteration in range(4):
    pred = input * weight
    error = (pred - goal_pred) ** 2
    delta = pred - goal_pred
    weight_delta = input * delta
    weight -= weight_delta
    print("Error:" + str(error) + " Prediction:" + str(pred))'''


'''for iteration in range(4):
    pred = input * weight
    error = ((0.5*weight) - 0.8) ** 2
    delta = pred - goal_pred
    weight_delta = input * delta
    weight -= weight_delta
    print("Error:" + str(error) + " Prediction:" + str(pred))'''
weight, goal_pred, input = (0.0, 0.8, 1.1)
for iteration in range(4):
    print("----\nWeight:" + str(weight))
    pred = input * weight
    error = (pred - goal_pred) ** 2
    delta = pred - goal_pred
    weight_delta = input * delta
    weight -= weight_delta
    print("Error:" + str(error) + " Prediction:" + str(pred))
    print("Delta:" + str(delta) + " Weight Delta:" + str(weight_delta))

def my_function(x):
    return x *2
