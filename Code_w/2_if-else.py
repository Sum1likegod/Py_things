# use of if else and elif
room_temp = float(input('Enter The Current Temperature '))

if 26 >= room_temp >= 22:
    print('The temperature is good')
elif 22 > room_temp >= 15:
    print('its cold in here')
elif 26 < room_temp < 35:
    print('hot in here')
else:
    print('not suitable temperature')
