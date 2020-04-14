def desencriptarCadena(mix_string):
    if not 'WUB' in mix_string:
        return mix_string
    result_song = ''

    while mix_string[ : 3 ] == 'WUB': # Remove WUB at beginning
        mix_string = mix_string[ 3 : ]
    while mix_string[ -3 : ] == 'WUB': # Remove WUB at end
        mix_string = mix_string[ : -3 ]
    while 'WUB' in mix_string:  # Remove internal WUB
        indice_siguiente_ocurrencia = mix_string.find('WUB')
        if indice_siguiente_ocurrencia is not 0: # Only append if WUB is not at beginning
            result_song += mix_string[: indice_siguiente_ocurrencia]
            result_song += ' '
        mix_string = mix_string[indice_siguiente_ocurrencia + 3: ]
    if mix_string is not '':  # Append the remaining string without WUB
        result_song += mix_string
    return result_song

cancion_cifrada = input()

print(desencriptarCadena(cancion_cifrada))
