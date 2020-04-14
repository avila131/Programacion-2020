def get_key_in_base(key_characters, base_characters):
    result = ''
    for i in range(len(base_characters)):
        result += key_characters[i % len(key_characters)]
    return result

def print_case(number_case, base, result):
    print('Caso {}:'.format(number_case))
    print(base)
    print(result)

number_of_keys = int(input())
key = input()
base_string = input()

# Delete blank spaces
base_string = base_string.replace(' ', '')
key = key.replace(' ', '')

result_string = get_key_in_base(key, base_string)
print_case(1, base_string, result_string)
if number_of_keys is not 1:
    print("")

for i in range(number_of_keys - 1):  # -1 porque ya se recibió un parámetro
    aditional_base = input()
    aditional_base = aditional_base.replace(' ', '')
    result_string = get_key_in_base(key, aditional_base)
    print_case(i+2, aditional_base, result_string)
    if number_of_keys != i + 2: # si es el último caso
        print("")
