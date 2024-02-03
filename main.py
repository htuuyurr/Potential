def decode(ship_info):
    '''

    :param ship_info: broken string in format of ShipName*planet*coord_place*direction
    :return: fixed string
    '''
    result = ''
    coords_pos = [0, 0]
    counter = 0
    n = int(ship_info[5])
    m = int(ship_info[6])
    x = 0
    xd = 0
    y = 0
    yd = 0
    speed_vector0 = ''
    speed_vector1 = ''
    t = 0
    i = 9
    while ship_info[i] != '*':
        t += 1
        i += 1
    i = 0
    while ship_info[len(ship_info) - i - 1] != '*':
        speed_vector0 += ship_info[len(ship_info) - i - 1]
        i += 1
    for i in range(len(speed_vector0) - 1, -1, -1):
        speed_vector1 += speed_vector0[i]
    speed_vector1 = speed_vector1.replace('\n', '')
    xd = int(speed_vector1[0:speed_vector1.index(' ')])
    yd = int(speed_vector1[speed_vector1.index(' '):len(speed_vector1)])
    if n > 5:
        x = n + xd
    else:
        x = -(n + xd) * 4 + t
    if m > 3:
        y = m + t + yd
    else:
        y = -(n + yd) * m
    for i in range(len(ship_info)):
        if ship_info[i] == '*':
            counter += 1
        if counter == 1:
            coords_pos[0] = i
        elif counter == 2:
            coords_pos[1] = i
    return (ship_info[0:coords_pos[0] + 2] + str(x) + ' ' + str(y) + ship_info[coords_pos[1]:len(ship_info)])


file = list(open(r'space.txt', encoding='utf-8'))
output = open(r'space_new.txt', 'w', encoding='utf-8')
ship_string = ''
for i in range(1, len(file)):
    ship_string = file[i]
    if ship_string[3]=='V':
        output.write(decode(ship_string))
