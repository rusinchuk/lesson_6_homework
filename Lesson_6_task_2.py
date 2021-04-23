import time


def la_la_song(how_strings, la_in_string, number=0):
    song = ''
    string = ''
    for count_la in range(la_in_string):
        string += 'la '
    for count_str in range(how_strings):
        song += string + '\n'
    if number == 0:
        song = song[:-2] + '.'
    if number == 1:
        song = song[:-2] + '!'
    return song


my_song = la_la_song(3, 4, 1)
filew = open('La_la_la.txt', 'w')
filew.write(my_song)
filew.close()

filewp = open('La_la_la_song.txt', 'w')
print(my_song, file=filewp)

with open('La_la_la.txt', 'w') as file:
    file.write(la_la_song(3, 4, 1))



