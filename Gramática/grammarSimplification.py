class CFG:
    def __init__(self,initial):
        self.terminalsVocabulary = {}
        self.nonTerminalsVocabulary = {}
        self.terminals = []
        self.nonTerminals = []
        self.productions = {}
        self.firstS = {}
        self.followingS = {}
        self.initial = self.findEquivalentLetter(initial)


    def addLetter(self, vocabulary):
        
        if vocabulary == "nonTerminal":
            start = 'A'
            vocabulary = self.nonTerminalsVocabulary
        else:
            start = 'a'
            vocabulary = self.terminalsVocabulary


        items = list(vocabulary.values())
        if items == []:
            return start
        
        last = items[-1]
        numberOfAlphabets = int(len(items) / 26)
        next_char = chr((ord(last[0]) - ord(start) + 1) % 26 + ord(start))
        newChar = ""

        for a in range(numberOfAlphabets+1):
            newChar += next_char

        return newChar


    def findEquivalentLetter(self, variable):
         if variable[0] == '<':
            if not variable in self.nonTerminalsVocabulary:
                self.nonTerminalsVocabulary[variable] = self.addLetter("nonTerminal")
            return self.nonTerminalsVocabulary[variable]
         else:
            """
             if not variable in self.terminalsVocabulary:
                self.terminalsVocabulary[variable] = self.addLetter("terminal")
             return self.terminalsVocabulary[variable]
            """
            return variable

    def simplifyGrammar(self, production):
        translated = ""

        for c in production.split():
            translated += self.findEquivalentLetter(c) + " "
        
        return translated
     
    def add_production(self, variable, production):
        
        equivalentVariable = self.findEquivalentLetter(variable)

        if equivalentVariable in self.productions:
            self.productions[equivalentVariable].append(self.simplifyGrammar(production))
        else:
            self.productions[equivalentVariable] = [self.simplifyGrammar(production)]
        
        self.addTerminalsAndNonTerminals(equivalentVariable, production)


    def addTerminalsAndNonTerminals(self, variable, production):
        if not variable in self.nonTerminals:
            self.nonTerminals.append(variable)

        for c in production.split():
            if c[0].isupper() and not c in self.nonTerminals:
                self.nonTerminals.append(c)
            else:
                self.terminals.append(c)

    def print_productions(self):
        for variable in self.productions.keys():
            print(variable + " -> " + " | ".join(self.productions[variable]))

print("NUESTRA GRAMÁTICA")
grammar4 = CFG('<program>')

grammar4.add_production("<program>", "🜉 <listaSentencia> 🝓")  #Reemplazar producción por DB si se quiere probar que si añade 'λ' a los primeros de S
grammar4.add_production("<type> ", "🝰")
grammar4.add_production("<type> ", "🝯")
grammar4.add_production("<type> ", "🝮")
grammar4.add_production("<returnType>", "<type>")
grammar4.add_production("<returnType>", "🜸")
grammar4.add_production("<identificadorVariable>", "🝳 <nombre> 🝳")
grammar4.add_production("<identificadorFuncion>", "🜛 <nombre> ☾ <argumentos> ☽ 🜛")
grammar4.add_production("<declaración>", "<type> e <identificadoVariable>")
grammar4.add_production("<asignar>", "<identificador> _ 🝑 _ <expresion> ")
grammar4.add_production("<expresion>", "<expresion_Aritmetica>")
grammar4.add_production("<expresion>", "<expresion_Booleana>")
grammar4.add_production("<operando_Aritmetico>", "<identificador>")
grammar4.add_production("<operando_Aritmetico>", "<número>")
grammar4.add_production("<operadorAritmetico>", "🜂")    
grammar4.add_production("<operadorAritmetico>", "🜄")
grammar4.add_production("<operadorAritmetico>", "🜁")
grammar4.add_production("<operadorAritmetico>", "🜃")
grammar4.add_production("<nombre>", "<letra> <nombre>")  
grammar4.add_production("<nombre>", "<número > <nombre>")
grammar4.add_production("<nombre>", "λ")
grammar4.add_production("<letra>", "'a'")  
grammar4.add_production("<letra>", "'b'")
grammar4.add_production("<letra>", "'c'")
grammar4.add_production("<letra>", "'d'")
grammar4.add_production("<letra>", "'A'")
grammar4.add_production("<letra>", "'B'")
grammar4.add_production("<letra>", "'C'")
grammar4.add_production("<letra>", "'D'")
grammar4.add_production("<número>", "<dígito>")
grammar4.add_production("<número>", "<dígito> <número>") 
grammar4.add_production("<dígito>", "0")  
grammar4.add_production("<dígito>", "1")  
grammar4.add_production("<dígito>", "2")  
grammar4.add_production("<dígito>", "3")  
grammar4.add_production("<dígito>", "4")  
grammar4.add_production("<dígito>", "5")  
grammar4.add_production("<dígito>", "6")  
grammar4.add_production("<dígito>", "7")  
grammar4.add_production("<dígito>", "8")
grammar4.add_production("<dígito>", "9")    
grammar4.add_production("<negacionLogica>", "🝱")
grammar4.add_production("<operadorLogico>", "🜓")
grammar4.add_production("<operadorLogico>", "🝘")
grammar4.add_production("<operador_Comparacion>", "🜔")
grammar4.add_production("<operador_Comparacion>", "🜕")
grammar4.add_production("<operador_Comparacion>", "🜖")
grammar4.add_production("<operador_Comparacion>", "🜗")
grammar4.add_production("<operador_Comparacion>", "🜎")
grammar4.add_production("<operador_Comparacion>", "🜍")
grammar4.add_production("<operando_Booleano>", "vera")
grammar4.add_production("<operando_Booleano>", "malvera")
grammar4.add_production("<operando_Booleano>", "<identificadorVariable>")
grammar4.add_production("<if_Condition>", "se _ ☾ <expresion_Booleana> ☽ \\n 🜚 \\n <listaSentencia> 🜚 \\n <else_Condition>")
grammar4.add_production("<else_Condition>", "alie \\n 🜚 \\n <listaSentencia> n 🜚")  
grammar4.add_production("<else_Condition>", "λ")

"""
grammar4.add_production("U", "d e ☾ E' ☽ n 🜚 n V n 🜚")
grammar4.add_production("V", "Y")
grammar4.add_production("V", "Y n V")
grammar4.add_production("V", "a n")
grammar4.add_production("W", "Y")
grammar4.add_production("W", "Y n W")
grammar4.add_production("W", "r e D n")
grammar4.add_production("X", "I Q I")
grammar4.add_production("Y", "Z")
grammar4.add_production("Y", "Z n Y")
grammar4.add_production("Z", "F") 
grammar4.add_production("Z", "A'")
grammar4.add_production("Z", "U")
grammar4.add_production("Z", "S")
grammar4.add_production("Z", "n")
grammar4.add_production("Z", "J'")
grammar4.add_production("Z", "H'")
grammar4.add_production("Z", "G")
grammar4.add_production("A'", "B'")
grammar4.add_production("A'", "E'")
grammar4.add_production("B'", "B' 🜂 C'")
grammar4.add_production("B'", "B' 🜄 C'")
grammar4.add_production("B'", "C'")
grammar4.add_production("C'", "C' 🜁 D'")
grammar4.add_production("C'", "C' 🜃 D'")
grammar4.add_production("C'", "D'")
grammar4.add_production("D'", "☾ B' ☽")
grammar4.add_production("D'", "I")
grammar4.add_production("E'", "E' 🝘 F'")
grammar4.add_production("E'", "F")
grammar4.add_production("E'", "X")
grammar4.add_production("F'", "F' 🜓  G'")
grammar4.add_production("F'", "G'")
grammar4.add_production("G'", "🝱 G'")
grammar4.add_production("G'", "G'")
grammar4.add_production("G'", "R")
grammar4.add_production("H'", "f e C e E ☾ I' ☽ n 🜚 n W n 🜚")
grammar4.add_production("I'", "F")
grammar4.add_production("I'", "F c I'")
grammar4.add_production("I'", "λ")
grammar4.add_production("J'", "K'")
grammar4.add_production("J'", "L'")
grammar4.add_production("K'", "🜌 Z n")
grammar4.add_production("K'", "🜌 a")
grammar4.add_production("K'", "🜌 r")
grammar4.add_production("L'", "🜋 W 🜋")
grammar4.add_production("L'", "🜋 V 🜋")

"""



grammar4.print_productions()