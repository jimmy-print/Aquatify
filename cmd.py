import nlp

'''
Command line interface to experiment on nlp
'''

if __name__ == '__main__':
    s = input('s: ')
    action_type, num, unit = nlp.get_type_num_unit(s)
    optimal = nlp.get_optimal(action_type, unit)

    print('Action type: {}\nNumber: {}\nUnit: {}\nOptimal: {}'
          .format(action_type, num, unit, optimal))
    if num <= optimal:
        print('Feedback: good')
    else:
        print('Feedback: Reduce by {} {}'.format(str(float(num) - float(optimal)), unit))