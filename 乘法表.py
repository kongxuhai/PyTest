print('\n'.join([' '.join([f"{j}x{i}={i*j}" for j in range(1, i + 1)]) for i in range(1, 10)]))

for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()

    i = 1
while i <= 9:
    j = 1
    while(j <= i):    # j的大小是由i来控制的
        print('%d*%d=%-3d' % (i, j, i*j), end='\t')
        j += 1
    print('')
    i += 1
