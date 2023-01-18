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

def elementwise_addition(vec_a, vec_b):
    ''' (list, list) -> float

    Pobiera elementy z obu list i dodaje je według elementów, zwraca wynik.

    >>> elementwise_multiplication([1,2,4], [2, 0.4, 3])
    [3, 2.4, 7]
    
    '''

    assert(len(vec_a) == len(vec_b)) , 'Liczba elementów wektorów nie jest równa'
    output = []
    for i in range (len(vec_a)):
        mul = vec_a[i] + vec_b[i]
        output.append(mul)
    return output

def vector_sum(vector):
    ''' list -> num

    Zwraca sumę elementów listy.

    >>>vector_sum([3, 2, 1, 34])40
    40
    '''
    
    output = 0
    for i in range(len(vector)):
        output += vector[i]
    return output

def vector_avg(vector):
    ''' list -> float

    Zwraca średnią elementów listy.

    >>>vector_avg([3, 2, 1, 34])40
    10.0
    '''
    output = vector_sum(vector)/len(vector)
    return output

def iloraz_skalarny(vec_a,vec_b):
    ''' (list, list) -> float

    Oblicza średnią ważoną obu list i zwraca float.

    >>> iloraz_skalarny([3, 2, 1, 34], [0, 5,0.3,-2])
    -57.7
    '''
    return vector_sum(elementwise_multiplication(vec_a,vec_b))

def ele_mul(number, vector):
    ''' (num, list) -> list0

    Mnoży każdy element vector'a przez number i wstawia do nowej listy,
    którą zwraca.

    >>> ele_mul(2, [1,0,-1])
    [2,0,-2]
    '''
    
    output =[]
    for i in range(len(vector)):
        output.append(0)
    assert(len(output) == len(vector))
    for i in range(len(vector)):
        output[i] = number * vector[i]
    return output

def ele_add(number, vector):
    ''' (num, list) -> list

    Sumuje każdy element vector'a z number i wstawia do nowej listy,
    którą zwraca.

    >>> ele_add(2, [1,0,-1])
    [3,2,1]
    '''
    output =[]
    for i in range(len(vector)):
        output.append(0)
    assert(len(output) == len(vector))
    for i in range(len(vector)):
        output[i] = number + vector[i]
    return output

def vect_mat_mul(vector, matrix):
    ''' (list, list of list) -> list

    Zwraca listę ilorazów skalarnych (średnich ważonych) dla vectora
    z każdym elementem macierzy.

    >>> vect_mal_mul([0,3,7], [[0.2,0.6,0.9],[1,2,4],[10,14,16]])
    [8.1, 34, 154]

    '''
    assert(len(vector) == len(matrix))
    output =[]
    for i in range(len(vector)):
        output.append(0)
    for i in range(len(vector)):
        output[i] = iloraz_skalarny(vector, matrix[i])
    return output

def neural_network(input, weights):
    ''' (list, list of lists) -> list

    Na podstawie danych wejściowych zwraca przewidywanie.

    >>> neural_network([0,3,7], [[0.2,0.6,0.9],[1,2,4],[10,14,16]])
    [8.1, 34, 154]
    '''
    prediction = vect_mat_mul(input, weights)
    return prediction
