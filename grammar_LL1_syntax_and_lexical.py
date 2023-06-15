#local application imports
from Análisis_Léxico.Analizador.AnalizadorLexico import AnalizadorLexico
from Gramática.GLC import GLC
from Análisis_Sintáctico_LL1.syntax_chart import * 

#lexico
codigo = '''🜉
dum ☾🝳nombre🝳 🜗 -20☽
🜚
🝳var🝳 🝑 🝳var🝳 🜂 10 
🜚'''
try:
    analizador = AnalizadorLexico()
    tokens = analizador.analizar(codigo)

except Exception: 
    print("Encountered a lexical error.")

codeasastring = ""
for token in tokens:
    codeasastring += " " + token[0]
#region Grammar declaration
print("Análisis para la Gramática - LL1")
grammar = GLC('Start')
grammar.add_production("Start", "🜉 s Program 🝓")
grammar.add_production("Program", "Statement s Program")
grammar.add_production("Program", "λ")
grammar.add_production("Statement", "Assignment")
grammar.add_production("Statement", "IfStatement")
grammar.add_production("Assignment", "🝳 identifier 🝳 🝑 Expression")
grammar.add_production("Expression", "Term Expression\'")
grammar.add_production("Expression\'", "🜂 Term")
grammar.add_production("Expression\'", "🜃 Term")
grammar.add_production("Expression\'", "🜁 Term")
grammar.add_production("Expression\'", "🜄 Term")
grammar.add_production("Expression\'", "λ")
grammar.add_production("Term", "🝳 identifier 🝳")
grammar.add_production("Term", "constant")
grammar.add_production("IfStatement", "se ☾ Condition ☽ s 🜚 s Program 🜚")
grammar.add_production("Condition", "Expression 🜎 Expression")
grammar.add_production("Condition", "Expression 🜍 Expression")
grammar.add_production("Condition", "Expression 🜕 Expression")
grammar.add_production("Condition", "Expression 🜔 Expression")
grammar.add_production("Condition", "Expression 🜗 Expression")
grammar.add_production("Condition", "Expression 🜖 Expression")
grammar.add_production("Statement", "WhileLoop")
grammar.add_production("WhileLoop", "dum ☾ Condition ☽ s 🜚 s Program 🜚")
grammar.add_production("Statement", "ForLoop")
grammar.add_production("ForLoop", "por ☾ Assignment ; Condition ; Assignment ☽ s 🜚 s Program 🜚")
grammar.add_production("Statement", "Print")
grammar.add_production("Print", "presi ☾ Term ☽")
#endregion

grammar.firstPhase()
grammar.second_phase()
grammar.left_factoring()
grammar.eliminate_left_recursion()

grammar.terminals = grammar.remove_duplicates(grammar.terminals)
grammar.get_first()
grammar.get_following()

if(differentFirstandFollowing(grammar.firstS, grammar.followingS) == False):
    print("Firsts and Followings have elements in common, not LL1.")
else:
    chart = createChart(grammar)
    parse(tokens, chart, grammar)

