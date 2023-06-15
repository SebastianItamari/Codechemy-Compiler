import re

class LexicalError(Exception):
    pass

class AnalizadorLexico:
    def __init__(self):

        self.patron_While = r'dum'
        self.patron_se = r'se'
        self.patron_For = r'por'
        self.patron_pcoma = r';'
        self.patron_operador_mas = r'🜂'
        self.patron_operador_menos = r'🜄'
        self.patron_operador_por = r'🜁'
        self.patron_operador_entre = r'🜃'
        self.patron_Delimitador = r'🜚'
        self.patron_Operador_mayor = r'🜔' 
        self.patron_Operador_menor = r'🜕' 
        self.patron_Operador_mayor_Igual = r'🜖'  
        self.patron_Operador_menor_Igual = r'🜗' 
        self.patron_Operador_Igual_A = r'🜎'
        self.patron_Operador_Diferente_A = r'🜍'  
        self.patron_Operador_Asignacion= r'🝑'
        self.patron_parentesis_inicio = r'☾'#
        self.patron_parentesis_fin = r'☽'#
        self.patron_numero = r'[-+]?\d+'
        self.patron_inicio_programa = r'🜉'#
        self.patron_fin_programa = r'🝓'#
        self.patron_Salto_Linea = r'\n'
        self.patron_simbolo_variable = r'🝳'
        self.patron_nombre = r'\w+'

        """ 
        self.patron_Espacio_Blanco = r'([\t\r\f\v\s])'
        self.patron_alie = r'alie'
        self.patron_identificador = r'\w+'
        self.patron_operador_logico_and = r'🜓'
        self.patron_operador_logico_or = r'🝘'
        self.patron_simbolo_funcion = r'🜛'        
        self.patron_int = r'🝰'
        self.patron_bool = r'🝯'
        self.patron_char = r'🝮'
        self.patron_Boolean_vera= r'vera'
        self.patron_Boolean_malvera= r'malvera'
        self.patron_comment = r'🜌'
        self.patron_Break = r'rompi'
        self.patron_Return = r'reveni'
        self.patron_funkcio= r'funkcio'
        self.patron_Parentesis_Apertura = r'☾'
        self.patron_Parentesis_Cierre = r'☽'  
        self.patron_bloque = r'🜸'#
        self.patron_negacion_bool = r'🝱'#
        """

        self.tokens = []
        self.linea = 1
        self.columna = 1

    def analizar(self,codigo_fuente):
        while codigo_fuente:
            #codigo_fuente = codigo_fuente.strip()  # Eliminar espacios en blanco al inicio y al final
            #if re.match(self.patron_alie, codigo_fuente):
            #    codigo_fuente = self.matchPattern(self.patron_alie, codigo_fuente, 'alie')
            #elif re.match(self.patron_comment, codigo_fuente):
            #    codigo_fuente = self.matchPattern(self.patron_comment, codigo_fuente, '🜌')
            if re.match(self.patron_se, codigo_fuente):
                codigo_fuente = self.matchPattern(self.patron_se, codigo_fuente, 'se') 
            elif re.match(self.patron_pcoma, codigo_fuente):
                codigo_fuente = self.matchPattern(self.patron_pcoma, codigo_fuente, ';')

            #elif re.match(self.patron_funkcio, codigo_fuente):
            #    codigo_fuente = self.matchPattern(self.patron_funkcio, codigo_fuente, 'funkcio')  
            elif re.match(self.patron_numero, codigo_fuente):
                codigo_fuente = self.matchPattern(self.patron_numero, codigo_fuente, 'NUMERO') 
            elif re.match(self.patron_simbolo_variable, codigo_fuente):
                codigo_fuente = self.matchPattern(self.patron_simbolo_variable, codigo_fuente, '🝳')
            #elif re.match(self.patron_simbolo_funcion, codigo_fuente):
            #   codigo_fuente = self.matchPattern(self.patron_simbolo_funcion, codigo_fuente, '🜛')
            elif re.match(self.patron_For, codigo_fuente):
                codigo_fuente = self.matchPattern(self.patron_For, codigo_fuente, 'por')
            elif re.match(self.patron_While, codigo_fuente):
                codigo_fuente = self.matchPattern(self.patron_While, codigo_fuente, 'dum')
            elif re.match(self.patron_Delimitador, codigo_fuente):
                codigo_fuente = self.matchPattern(self.patron_Delimitador, codigo_fuente, '🜚')
            #elif re.match(self.patron_Break, codigo_fuente):
            #    codigo_fuente = self.matchPattern(self.patron_Break, codigo_fuente, 'rompi')
            #elif re.match(self.patron_Return, codigo_fuente):
            #    codigo_fuente = self.matchPattern(self.patron_Return, codigo_fuente, 'reveni')
            elif re.match(self.patron_nombre, codigo_fuente):
                codigo_fuente = self.matchPattern(self.patron_nombre, codigo_fuente, 'NOMBRE')
            elif re.match(self.patron_operador_mas, codigo_fuente):
                codigo_fuente = self.matchPattern(self.patron_operador_mas, codigo_fuente, '🜂')
            elif re.match(self.patron_operador_menos, codigo_fuente):
                codigo_fuente = self.matchPattern(self.patron_operador_menos, codigo_fuente, '🜄')
            elif re.match(self.patron_operador_por, codigo_fuente):
                codigo_fuente = self.matchPattern(self.patron_operador_por, codigo_fuente, '🜁')
            elif re.match(self.patron_operador_entre, codigo_fuente):
                codigo_fuente = self.matchPattern(self.patron_operador_entre, codigo_fuente, '🜃')
            elif re.match(self.patron_Operador_Asignacion, codigo_fuente):
                codigo_fuente = self.matchPattern(self.patron_Operador_Asignacion, codigo_fuente, '🝑')
            elif re.match(self.patron_Operador_mayor, codigo_fuente):
                codigo_fuente = self.matchPattern(self.patron_Operador_mayor, codigo_fuente, '🜔')
            elif re.match(self.patron_Operador_menor, codigo_fuente):
                codigo_fuente = self.matchPattern(self.patron_Operador_menor, codigo_fuente, '🜕')
            elif re.match(self.patron_Operador_mayor_Igual, codigo_fuente):
                codigo_fuente = self.matchPattern(self.patron_Operador_mayor_Igual, codigo_fuente, '🜖')
            elif re.match(self.patron_Operador_menor_Igual, codigo_fuente):
                codigo_fuente = self.matchPattern(self.patron_Operador_menor_Igual, codigo_fuente, '🜗')
            elif re.match(self.patron_Operador_Diferente_A, codigo_fuente):
                codigo_fuente = self.matchPattern(self.patron_Operador_Diferente_A, codigo_fuente, '🜍')
            elif re.match(self.patron_Operador_Igual_A , codigo_fuente):
                codigo_fuente = self.matchPattern(self.patron_Operador_Igual_A, codigo_fuente, '🜎')
            #elif re.match(self.patron_Boolean_vera, codigo_fuente):
            #    codigo_fuente = self.matchPattern(self.patron_Boolean_vera, codigo_fuente, 'vera')
            #elif re.match(self.patron_Boolean_malvera, codigo_fuente):
            #   codigo_fuente = self.matchPattern(self.patron_Boolean_malvera, codigo_fuente, 'malvera')
            #elif re.match(self.patron_int, codigo_fuente):
            #codigo_fuente = self.matchPattern(self.patron_int, codigo_fuente, '🝰')
            #elif re.match(self.patron_bool, codigo_fuente):
            #    codigo_fuente = self.matchPattern(self.patron_bool, codigo_fuente, '🝯')
            #elif re.match(self.patron_char, codigo_fuente):
            #    codigo_fuente = self.matchPattern(self.patron_char, codigo_fuente, '🝮')
            elif re.match(self.patron_parentesis_inicio, codigo_fuente):
                codigo_fuente = self.matchPattern(self.patron_parentesis_inicio, codigo_fuente, '☾')
            elif re.match(self.patron_parentesis_fin, codigo_fuente):
                codigo_fuente = self.matchPattern(self.patron_parentesis_fin, codigo_fuente, '☽')
            elif re.match(self.patron_Salto_Linea, codigo_fuente):
                codigo_fuente = self.matchPattern(self.patron_Salto_Linea, codigo_fuente, 's')
                self.columna = 1
                self.linea += 1
            
            #elif re.match(self.patron_Espacio_Blanco, codigo_fuente):
            #    codigo_fuente = self.matchPattern(self.patron_Espacio_Blanco, codigo_fuente, '_')
            #elif re.match(self.patron_identificador, codigo_fuente):
            #    codigo_fuente = self.matchPattern(self.patron_identificador, codigo_fuente, 'IDENTIFICADOR')
            #elif re.match(self.patron_operador_logico_and, codigo_fuente):
            #    codigo_fuente = self.matchPattern(self.patron_operador_logico_and, codigo_fuente, '🜓')
            #elif re.match(self.patron_operador_logico_or, codigo_fuente):
            #   codigo_fuente = self.matchPattern(self.patron_operador_logico_or, codigo_fuente, '🝘')
            elif re.match(self.patron_inicio_programa, codigo_fuente):
                codigo_fuente = self.matchPattern(self.patron_inicio_programa, codigo_fuente, '🜉')
            elif re.match(self.patron_fin_programa, codigo_fuente):
                codigo_fuente = self.matchPattern(self.patron_fin_programa, codigo_fuente, '🝓')
            #elif re.match(self.patron_bloque, codigo_fuente):
            #    codigo_fuente = self.matchPattern(self.patron_bloque, codigo_fuente, '🜸')
            #elif re.match(self.patron_negacion_bool, codigo_fuente):
            #    codigo_fuente = self.matchPattern(self.patron_negacion_bool, codigo_fuente, '🝱') 
            else:
                raise LexicalError("Error Léxico: Carácter no válido " + codigo_fuente[0] + " encontrado en la fila " + str(self.linea))

        return self.tokens
    
    def matchPattern(self, pattern, codigo_fuente, token):
        matchedPattern = re.match(pattern, codigo_fuente).group()
        finColumna = self.columna + len(matchedPattern)
        self.tokens.append((token, matchedPattern, self.linea, (self.columna, finColumna)))
        self.columna = finColumna
        return re.sub(pattern, '', codigo_fuente, count=1)


