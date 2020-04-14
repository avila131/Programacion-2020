def obtenerOcurrencias(base, key):
    contador_ocurrencias = 0
    while key in base:
        contador_ocurrencias += 1
        indice_siguiente_ocurrencia = base.find(key)
        nuevo_inicio = indice_siguiente_ocurrencia + len(key)
        base = base[nuevo_inicio: ]
    return contador_ocurrencias

def print_result(number_case, result):
    print('Caso {}: {}'.format(number_case, result))

number_of_bases = int(input())
input_key = input()
input_base = input()

result_case = obtenerOcurrencias(input_base, input_key)
print_result(1, result_case)

for i in range(number_of_bases - 1):
    aditional_base = input()
    result_case = obtenerOcurrencias(aditional_base, input_key)
    print_result(i + 2, result_case)
