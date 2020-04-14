def get_encrypted_password(key_string, base_string):
    indice_base = 0
    indice_key = 0
    result_string = ''

    for i in range(2 * len(base_string) - 1):
        if i % 2 is 0:
            result_string += base_string[indice_base % len(base_string)]
            indice_base += 1
        else:
            result_string += key_string[indice_key % len(key_string)]
            indice_key += 1
    return result_string

def print_result(number_case, result):
    print('Caso {}: {}'.format(number_case, result))

number_of_passwords = int(input())
key = input()
password = input()

# Delete blank spaces
password = password.replace(' ', '')
key = key.replace(' ', '')

result_string = get_encrypted_password(key, password)
print_result(1, result_string)

for i in range(number_of_passwords - 1):
    aditional_password = input()
    aditional_password = aditional_password.replace(' ', '')
    result_string = get_encrypted_password(key, aditional_password)
    print_result(i + 2, result_string)
