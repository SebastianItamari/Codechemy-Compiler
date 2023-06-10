import re

def analizador_lexico(codigo_fuente):
    # Definir las expresiones regulares para los tokens
    patron_numero = r'\d+'
    patron_identificador = r'\w+'
    patron_operador = r'[+\-*/]'

    # Definir una lista de tuplas para almacenar los tokens encontrados
    tokens = []

    # Buscar los tokens en el código fuente utilizando expresiones regulares
    while codigo_fuente:
        codigo_fuente = codigo_fuente.strip()  # Eliminar espacios en blanco al inicio y al final
        if re.match(patron_numero, codigo_fuente):
            numero = re.match(patron_numero, codigo_fuente).group()
            tokens.append(('NUMERO', numero))
            codigo_fuente = re.sub(patron_numero, '', codigo_fuente, count=1)
        elif re.match(patron_identificador, codigo_fuente):
            identificador = re.match(patron_identificador, codigo_fuente).group()
            tokens.append(('IDENTIFICADOR', identificador))
            codigo_fuente = re.sub(patron_identificador, '', codigo_fuente, count=1)
        elif re.match(patron_operador, codigo_fuente):
            operador = re.match(patron_operador, codigo_fuente).group()
            tokens.append(('OPERADOR', operador))
            codigo_fuente = re.sub(patron_operador, '', codigo_fuente, count=1)
        else:
            print('Error: Carácter no válido encontrado')
            return

    return tokens

# Ejemplo de uso
codigo = '''
3 + 4 * id
1 + 1 * pos
    2+2
'''
print(codigo)
tokens = analizador_lexico(codigo)
for token in tokens:
    print(token)