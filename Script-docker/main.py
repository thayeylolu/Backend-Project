def multiple(number, steps):
    if (number == 0) and (steps == 0):
        print('Error occured: {} and {} in imposible (I think!)'.format(number, steps))
    for num in range (1, steps+1):
        
        print("{} * {} =  {} ". format(number, num, num * number))

input_1 = eval(input('Enter a Number you would like to multiple : '))
input_2 = eval(input('Enter what you would like to multipel with  : '))

multiple(input_1, input_2)
