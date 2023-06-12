import re

class AnalizadorLexico:
    def __init__(self):
        self.patron_numero = r'\d+'
        self.patron_identificador = r'\w+'
        self.patron_Operador_Comparacion = r'[🜔🜕🜖🜗🜎🜍]'   
        self.patron_Tipo = r'[🝰🝯🝮]'   
        self.patron_Key_Word = r'(alie|🜌)'
        self.patron_Salto_Linea = r'\n'
        self.patron_Espacio_Blanco = r'(\t| )'
        self.tokens = []
        self.linea = 1

    def analizar(self,codigo_fuente):
        while codigo_fuente:
            #codigo_fuente = codigo_fuente.strip()  # Eliminar espacios en blanco al inicio y al final
            if re.match(self.patron_Key_Word, codigo_fuente):
                keyWord = re.match(self.patron_Key_Word, codigo_fuente).group()
                self.tokens.append(('PALABRA RESERVADA', keyWord, self.linea))
                codigo_fuente = re.sub(self.patron_Key_Word, '', codigo_fuente, count=1)
            elif re.match(self.patron_numero, codigo_fuente):
                numero = re.match(self.patron_numero, codigo_fuente).group()
                self.tokens.append(('NUMERO', numero, self.linea))
                codigo_fuente = re.sub(self.patron_numero, '', codigo_fuente, count=1)
            elif re.match(self.patron_identificador, codigo_fuente):
                identificador = re.match(self.patron_identificador, codigo_fuente).group()
                self.tokens.append(('IDENTIFICADOR', identificador, self.linea))
                codigo_fuente = re.sub(self.patron_identificador, '', codigo_fuente, count=1)
            elif re.match(self.patron_Operador_Comparacion, codigo_fuente):
                operador = re.match(self.patron_Operador_Comparacion, codigo_fuente).group()
                self.tokens.append(('OPERADOR COMPARACION', operador, self.linea))
                codigo_fuente = re.sub(self.patron_Operador_Comparacion, '', codigo_fuente, count=1)
            elif re.match(self.patron_Tipo, codigo_fuente):
                tipo = re.match(self.patron_Tipo, codigo_fuente).group()
                self.tokens.append(('TIPO', tipo, self.linea))
                codigo_fuente = re.sub(self.patron_Tipo, '', codigo_fuente, count=1)
            elif re.match(self.patron_Salto_Linea, codigo_fuente):
                saltoLinea = re.match(self.patron_Salto_Linea, codigo_fuente).group()
                self.tokens.append(('SALTO DE LINEA', saltoLinea, self.linea))
                codigo_fuente = re.sub(self.patron_Salto_Linea, '', codigo_fuente, count=1)
                self.linea += 1
            elif re.match(self.patron_Espacio_Blanco, codigo_fuente):
                espacioBlanco = re.match(self.patron_Espacio_Blanco, codigo_fuente).group()
                self.tokens.append(('ESPACIO BLANCO', espacioBlanco, self.linea))
                codigo_fuente = re.sub(self.patron_Espacio_Blanco, '', codigo_fuente, count=1)
            else:
                print('Error: Carácter no válido encontrado')
                return

        return self.tokens
    
# Ejemplo de uso
codigo = '''
3 🜔 2
id 🜕 3
pos 🜖 len
hola 🜗 12
1 🜎 1
bebe 🜍 baba

    🝰 b
    🝯 lola
    🝮 v

alie id 🜔 2
🜌 papa alie
'''
analizador = AnalizadorLexico()
tokens = analizador.analizar(codigo)
for token in tokens:
    print(token)

