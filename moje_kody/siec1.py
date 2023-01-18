weights = [0.1, 0.2, 0]
toes = [8.5, 9.5, 10, 9]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]
input = [toes[0], wlrec[0], nfans[0]]

def neural_network(input, weights):
    ''' (num, num) -> str?

    Na podstawie danych wejściowych zwraca przewidywanie zwycięstwa

    >>> neural_network([0.1, 0.2, 0, 4], [8.5, 9.5, 10, 9])
    zwyciężył
    '''
    
    prediction = w_sum(input, weights)
    return prediction

def w_sum(input, weights): #Suma ważona
    ''' (list, list) -> float

    Pobiera dane z obu list i oblicza sumę iloczynów w każdym indeksie
    na obu listach

    >>> w_sum(input, weights)
    0.98
    
    '''

    assert(len(input) == len(weights))
    output = 0
    for i in range (len(input)):
        output += (input[i] * weights[i])
    return output


    
pred = neural_network(input, weights)
print(pred)

def elementwise_multiplication(vec_a, vec_b):
    ''' (list, list) -> float

    Pobiera elementy z obu list i mnoży je według elementów, zwraca wynik.

    >>> elementwise_multiplication([1,2,4], [2, 0.4, 3])
    [2, 0.8, 12]
    
    '''

    assert(len(vec_a) == len(vec_b)) , 'Liczba elementów wektorów nie jest równa'
    output = []
    for i in range (len(vec_a)):
        mul = vec_a[i] * vec_b[i]
        output.append(mul)
    return output


