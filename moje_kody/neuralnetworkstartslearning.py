weight = 0.1
lr = 0.01
def neural_network(input, weight):
    prediction = input * weight
    return prediction

number_of_toes = [8.5]
win_or_lose_binary = [1] # (zwycięstwo!!!)
input = number_of_toes[0]
true = win_or_lose_binary[0]
pred = neural_network(input, weight)
error = (pred - true) ** 2
print(error)

p_up = neural_network(input,weight+lr) #p od pred, e od error
e_up = (p_up - true) ** 2
print(e_up)

p_dn = neural_network(input,weight-lr) #p od pred, e od error
e_dn = (p_dn - true) ** 2
print(e_dn)

if error > e_dn or error > e_up:
    if e_dn < e_up:
        weight -= lr
    if e_up < e_dn:
        weight += lr
