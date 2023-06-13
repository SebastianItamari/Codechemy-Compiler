import re

class AnalizadorLexico:
    def __init__(self):
        self.patron_numero = r'[-+]?\d+'
        self.patron_identificador = r'\w+'
        self.patron_operador_logico_and = r'🜓'
        self.patron_operador_logico_or = r'🝘'
        self.patron_simbolo_variable = r'🝳'
        self.patron_simbolo_funcion = r'🜛'
        self.patron_nombre = r'\w+'
        self.patron_operador_mas = r'🜂'
        self.patron_operador_menos = r'🜄'
        self.patron_operador_por = r'🜁'
        self.patron_operador_entre = r'🜃'
        self.patron_Operador_mayor = r'🜔' 
        self.patron_Operador_menor = r'🜕' 
        self.patron_Operador_mayor_Igual = r'🜖'  
        self.patron_Operador_menor_Igual = r'🜗' 
        self.patron_Operador_Igual_A = r'🜎'
        self.patron_Operador_Diferente_A = r'🜍'  
        self.patron_Operador_Asignacion= r'🝑'   
        self.patron_int = r'🝰'
        self.patron_bool = r'🝯'
        self.patron_char = r'🝮'
        self.patron_Boolean_vera= r'vera'
        self.patron_Boolean_malvera= r'malvera'
        self.patron_alie = r'alie'
        self.patron_comment = r'🜌'
        self.patron_se = r'se'
        self.patron_For = r'por'
        self.patron_While = r'dum'
        self.patron_Delimitador = r'🜚'
        self.patron_Break = r'rompi'
        self.patron_Return = r'reveni'
        self.patron_funkcio= r'funkcio'
        self.patron_Parentesis_Apertura = r'☾'
        self.patron_Parentesis_Cierre = r'☽'
        self.patron_Salto_Linea = r'\n'
        self.patron_Espacio_Blanco = r'([\t\r\f\v\s])'
        self.patron_inicio_programa = r'🜉'#
        self.patron_fin_programa = r'🝓'#
        self.patron_bloque = r'🜸'#
        self.patron_negacion_bool = r'🝱'#
        self.patron_parentesis_inicio = r'☾'#
        self.patron_parentesis_fin = r'☽'#
        self.tokens = []
        self.linea = 1

    def analizar(self,codigo_fuente):
        while codigo_fuente:
            #codigo_fuente = codigo_fuente.strip()  # Eliminar espacios en blanco al inicio y al final
            if re.match(self.patron_alie, codigo_fuente):
                keyWord = re.match(self.patron_alie, codigo_fuente).group()
                self.tokens.append(('alie', keyWord, self.linea))
                codigo_fuente = re.sub(self.patron_alie, '', codigo_fuente, count=1)
            elif re.match(self.patron_comment, codigo_fuente):
                keyWord = re.match(self.patron_comment, codigo_fuente).group()
                self.tokens.append(('🜌', keyWord, self.linea))
                codigo_fuente = re.sub(self.patron_comment, '', codigo_fuente, count=1) 
            elif re.match(self.patron_se, codigo_fuente):
                keyWord = re.match(self.patron_se, codigo_fuente).group()
                self.tokens.append(('se', keyWord, self.linea))
                codigo_fuente = re.sub(self.patron_se, '', codigo_fuente, count=1)     
            elif re.match(self.patron_funkcio, codigo_fuente):
                keyWord = re.match(self.patron_funkcio, codigo_fuente).group()
                self.tokens.append(('funkcio', keyWord, self.linea))
                codigo_fuente = re.sub(self.patron_funkcio, '', codigo_fuente, count=1)       
            elif re.match(self.patron_numero, codigo_fuente):
                numero = re.match(self.patron_numero, codigo_fuente).group()
                self.tokens.append(('NUMERO', numero, self.linea))
                codigo_fuente = re.sub(self.patron_numero, '', codigo_fuente, count=1)
            elif re.match(self.patron_simbolo_variable, codigo_fuente):
                identificador = re.match(self.patron_simbolo_variable, codigo_fuente).group()
                self.tokens.append(('🝳', identificador, self.linea))
                codigo_fuente = re.sub(self.patron_simbolo_variable, '', codigo_fuente, count=1)
            elif re.match(self.patron_simbolo_funcion, codigo_fuente):
                identificador = re.match(self.patron_simbolo_funcion, codigo_fuente).group()
                self.tokens.append(('🜛', identificador, self.linea))
                codigo_fuente = re.sub(self.patron_simbolo_funcion, '', codigo_fuente, count=1)
            elif re.match(self.patron_For, codigo_fuente):
                por = re.match(self.patron_For, codigo_fuente).group()
                self.tokens.append(('por', por, self.linea))
                codigo_fuente = re.sub(self.patron_For, '', codigo_fuente, count=1)
            elif re.match(self.patron_While, codigo_fuente):
                dum = re.match(self.patron_While, codigo_fuente).group()
                self.tokens.append(('dum', dum, self.linea))
                codigo_fuente = re.sub(self.patron_While, '', codigo_fuente, count=1)
            elif re.match(self.patron_Delimitador, codigo_fuente):
                delimitador = re.match(self.patron_Delimitador, codigo_fuente).group()
                self.tokens.append(('🜚', delimitador, self.linea))
                codigo_fuente = re.sub(self.patron_Delimitador, '', codigo_fuente, count=1)
            elif re.match(self.patron_Break, codigo_fuente):
                rompi = re.match(self.patron_Break, codigo_fuente).group()
                self.tokens.append(('rompi', rompi, self.linea))
                codigo_fuente = re.sub(self.patron_Break, '', codigo_fuente, count=1)
            elif re.match(self.patron_Return, codigo_fuente):
                reveni = re.match(self.patron_Return, codigo_fuente).group()
                self.tokens.append(('reveni', reveni, self.linea))
                codigo_fuente = re.sub(self.patron_Return, '', codigo_fuente, count=1)
            elif re.match(self.patron_nombre, codigo_fuente):
                identificador = re.match(self.patron_nombre, codigo_fuente).group()
                self.tokens.append(('NOMBRE', identificador, self.linea))
                codigo_fuente = re.sub(self.patron_nombre, '', codigo_fuente, count=1)
            elif re.match(self.patron_operador_mas, codigo_fuente):
                operador = re.match(self.patron_operador_mas, codigo_fuente).group()
                self.tokens.append(('🜂', operador, self.linea))
                codigo_fuente = re.sub(self.patron_operador_mas, '', codigo_fuente, count=1)
            elif re.match(self.patron_operador_menos, codigo_fuente):
                operador = re.match(self.patron_operador_menos, codigo_fuente).group()
                self.tokens.append(('🜄', operador, self.linea))
                codigo_fuente = re.sub(self.patron_operador_menos, '', codigo_fuente, count=1)
            elif re.match(self.patron_operador_por, codigo_fuente):
                operador = re.match(self.patron_operador_por, codigo_fuente).group()
                self.tokens.append(('🜁', operador, self.linea))
                codigo_fuente = re.sub(self.patron_operador_por, '', codigo_fuente, count=1)
            elif re.match(self.patron_operador_entre, codigo_fuente):
                operador = re.match(self.patron_operador_entre, codigo_fuente).group()
                self.tokens.append(('🜃', operador, self.linea))
                codigo_fuente = re.sub(self.patron_operador_entre, '', codigo_fuente, count=1)
            elif re.match(self.patron_Operador_Asignacion, codigo_fuente):
                operador = re.match(self.patron_Operador_Asignacion, codigo_fuente).group()
                self.tokens.append(('🝑', operador, self.linea))
                codigo_fuente = re.sub(self.patron_Operador_Asignacion, '', codigo_fuente, count=1)
            elif re.match(self.patron_Operador_mayor, codigo_fuente):
                operador = re.match(self.patron_Operador_mayor, codigo_fuente).group()
                self.tokens.append(('🜔', operador, self.linea))
                codigo_fuente = re.sub(self.patron_Operador_mayor, '', codigo_fuente, count=1)
            elif re.match(self.patron_Operador_menor, codigo_fuente):
                operador = re.match(self.patron_Operador_menor, codigo_fuente).group()
                self.tokens.append(('🜕', operador, self.linea))
                codigo_fuente = re.sub(self.patron_Operador_menor, '', codigo_fuente, count=1)
            elif re.match(self.patron_Operador_mayor_Igual, codigo_fuente):
                operador = re.match(self.patron_Operador_mayor_Igual, codigo_fuente).group()
                self.tokens.append(('🜖', operador, self.linea))
                codigo_fuente = re.sub(self.patron_Operador_mayor_Igual, '', codigo_fuente, count=1)
            elif re.match(self.patron_Operador_menor_Igual, codigo_fuente):
                operador = re.match(self.patron_Operador_menor_Igual, codigo_fuente).group()
                self.tokens.append(('🜗', operador, self.linea))
                codigo_fuente = re.sub(self.patron_Operador_menor_Igual, '', codigo_fuente, count=1)
            elif re.match(self.patron_Operador_Diferente_A, codigo_fuente):
                operador = re.match(self.patron_Operador_Diferente_A, codigo_fuente).group()
                self.tokens.append(('🜍', operador, self.linea))
                codigo_fuente = re.sub(self.patron_Operador_Diferente_A, '', codigo_fuente, count=1)
            elif re.match(self.patron_Operador_Igual_A , codigo_fuente):
                operador = re.match(self.patron_Operador_Igual_A , codigo_fuente).group()
                self.tokens.append(('🜎', operador, self.linea))
                codigo_fuente = re.sub(self.patron_Operador_Igual_A , '', codigo_fuente, count=1)
            elif re.match(self.patron_Boolean_vera, codigo_fuente):
                tipo = re.match(self.patron_Boolean_vera, codigo_fuente).group()
                self.tokens.append(('vera', tipo, self.linea))
                codigo_fuente = re.sub(self.patron_Boolean_vera, '', codigo_fuente, count=1)
            elif re.match(self.patron_Boolean_malvera, codigo_fuente):
                tipo = re.match(self.patron_Boolean_malvera, codigo_fuente).group()
                self.tokens.append(('malvera', tipo, self.linea))
                codigo_fuente = re.sub(self.patron_Boolean_malvera, '', codigo_fuente, count=1)
            elif re.match(self.patron_int, codigo_fuente):
                tipo = re.match(self.patron_int, codigo_fuente).group()
                self.tokens.append(('🝰', tipo, self.linea))
                codigo_fuente = re.sub(self.patron_int, '', codigo_fuente, count=1)
            elif re.match(self.patron_bool, codigo_fuente):
                tipo = re.match(self.patron_bool, codigo_fuente).group()
                self.tokens.append(('🝯', tipo, self.linea))
                codigo_fuente = re.sub(self.patron_bool, '', codigo_fuente, count=1)
            elif re.match(self.patron_char, codigo_fuente):
                tipo = re.match(self.patron_char, codigo_fuente).group()
                self.tokens.append(('🝮', tipo, self.linea))
                codigo_fuente = re.sub(self.patron_char, '', codigo_fuente, count=1)
            elif re.match(self.patron_Parentesis_Apertura, codigo_fuente):
                parentesis = re.match(self.patron_Parentesis_Apertura, codigo_fuente).group()
                self.tokens.append(('☾', parentesis, self.linea))
                codigo_fuente = re.sub(self.patron_Parentesis_Apertura, '', codigo_fuente, count=1)
            elif re.match(self.patron_Parentesis_Cierre, codigo_fuente):
                parentesis = re.match(self.patron_Parentesis_Cierre, codigo_fuente).group()
                self.tokens.append(('☽', parentesis, self.linea))
                codigo_fuente = re.sub(self.patron_Parentesis_Cierre, '', codigo_fuente, count=1)
            elif re.match(self.patron_Salto_Linea, codigo_fuente):
                saltoLinea = re.match(self.patron_Salto_Linea, codigo_fuente).group()
                self.tokens.append(('\n', saltoLinea, self.linea))
                codigo_fuente = re.sub(self.patron_Salto_Linea, '', codigo_fuente, count=1)
                self.linea += 1
            elif re.match(self.patron_Espacio_Blanco, codigo_fuente):
                espacioBlanco = re.match(self.patron_Espacio_Blanco, codigo_fuente).group()
                self.tokens.append(('_', espacioBlanco, self.linea))
                codigo_fuente = re.sub(self.patron_Espacio_Blanco, '', codigo_fuente, count=1)
            elif re.match(self.patron_identificador, codigo_fuente):
                identificador = re.match(self.patron_identificador, codigo_fuente).group()
                self.tokens.append(('IDENTIFICADOR', identificador, self.linea))
                codigo_fuente = re.sub(self.patron_identificador, '', codigo_fuente, count=1)
            elif re.match(self.patron_operador_logico_and, codigo_fuente):
                operador = re.match(self.patron_operador_logico_and, codigo_fuente).group()
                self.tokens.append(('🜓', operador, self.linea))
                codigo_fuente = re.sub(self.patron_operador_logico_and, '', codigo_fuente, count=1)
            elif re.match(self.patron_operador_logico_or, codigo_fuente):
                operador = re.match(self.patron_operador_logico_or, codigo_fuente).group()
                self.tokens.append(('🝘', operador, self.linea))
                codigo_fuente = re.sub(self.patron_operador_logico_or, '', codigo_fuente, count=1)
            elif re.match(self.patron_inicio_programa, codigo_fuente):
                inicio_programa = re.match(self.patron_inicio_programa, codigo_fuente).group()
                self.tokens.append(('🜉', inicio_programa, self.linea))
                codigo_fuente = re.sub(self.patron_inicio_programa, '', codigo_fuente, count=1) 
            elif re.match(self.patron_fin_programa, codigo_fuente):
                fin_programa = re.match(self.patron_fin_programa, codigo_fuente).group()
                self.tokens.append(('🝓', fin_programa, self.linea))
                codigo_fuente = re.sub(self.patron_fin_programa, '', codigo_fuente, count=1) 
            elif re.match(self.patron_bloque, codigo_fuente):
                bloque = re.match(self.patron_bloque, codigo_fuente).group()
                self.tokens.append(('🜸', bloque, self.linea))
                codigo_fuente = re.sub(self.patron_bloque, '', codigo_fuente, count=1)
            elif re.match(self.patron_negacion_bool, codigo_fuente):
                negacion_bool = re.match(self.patron_negacion_bool, codigo_fuente).group()
                self.tokens.append(('🝱', negacion_bool, self.linea))
                codigo_fuente = re.sub(self.patron_negacion_bool, '', codigo_fuente, count=1) 
            elif re.match(self.patron_parentesis_inicio, codigo_fuente):
                parentesis_inicio = re.match(self.patron_parentesis_inicio, codigo_fuente).group()
                self.tokens.append(('☾', parentesis_inicio, self.linea))
                codigo_fuente = re.sub(self.patron_parentesis_inicio, '', codigo_fuente, count=1) 
            elif re.match(self.patron_parentesis_fin, codigo_fuente):
                parentesis_fin = re.match(self.patron_parentesis_fin, codigo_fuente).group()
                self.tokens.append(('☽', parentesis_fin, self.linea))
                codigo_fuente = re.sub(self.patron_parentesis_fin, '', codigo_fuente, count=1) 
            else:
                print('Error: Carácter no válido encontrado')
                return

        return self.tokens
    
# Ejemplo de uso
codigo = '''
🝰 🝳a🝳 
🝳a🝳 🝑 2 🜄 3
🝰 🝳b🝳 
🝳b🝳 🝑 vera
3 🜔 2
🝳id🝳 🜕 3
🝳pos🝳 🜖 🝳len🝳
🝳hola🝳 🜗 12
1 🜎 1
🝳bebe🝳 🜍 🝳baba🝳

    🝰 🝳b🝳
    🝯 🝳lola🝳
    🝮 🝳v🝳

alie 🝳id🝳 🜔 2

alie 🝳id🝳 🜓 2
alie 🝳id🝳 🝘 2

🜌 se 🝳papa🝳 alie
🜛 se
por ☾ ☽
🜚
    rompi
🜚
dum ☾ ☽
🜚
    reveni
🜚

'''
analizador = AnalizadorLexico()
tokens = analizador.analizar(codigo)
for token in tokens:
    print(token)

