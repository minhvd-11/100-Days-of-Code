def print_door_mat(n, m):
    # Top half of the mat
    for i in range(1, n, 2):
        print(('.|.' * i).center(m, '-'))
    
    # Center of the mat
    print('WELCOME'.center(m, '-'))
    
    # Bottom half of the mat
    for i in range(n-2, 0, -2):
        print(('.|.' * i).center(m, '-'))

if __name__ == '__main__':
    n, m = map(int, input().split())
    print_door_mat(n, m)
