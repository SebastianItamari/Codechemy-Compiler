#standard library imports
import sys

#local application imports
from Análisis_Léxico.Analizador.AnalizadorLexico import AnalizadorLexico
from Gramática.GLC import GLC
from Análisis_Sintáctico_LL1.syntax_chart import * 

class LL1:
    def __init__(self, grammar):
        #region grammar LL1
        #'''
        grammarLL1 = GLC('Start')
        grammarLL1.add_production("Start", "🜉 s Program 🝓")
        grammarLL1.add_production("Program", "Statement s")
        grammarLL1.add_production("Program", "Statement s Program")
        grammarLL1.add_production("Statement", "Assignment")
        grammarLL1.add_production("Statement", "IfStatement")
        grammarLL1.add_production("Statement", "WhileLoop")
        grammarLL1.add_production("Statement", "ForLoop")
        grammarLL1.add_production("Statement", "Print")
        grammarLL1.add_production("Assignment", "🝳 identifier 🝳 🝑 Expression")
        grammarLL1.add_production("Expression", "Term Expression'")
        grammarLL1.add_production("Expression", "Term")
        grammarLL1.add_production("Expression'", "🜂 Term")
        grammarLL1.add_production("Expression'", "🜃 Term")
        grammarLL1.add_production("Expression'", "🜁 Term")
        grammarLL1.add_production("Expression'", "🜄 Term")
        grammarLL1.add_production("Term", "🝳 identifier 🝳")
        grammarLL1.add_production("Term", "constant")
        grammarLL1.add_production("IfStatement", "se ☾ Condition ☽ s 🜚 s Program 🜚")
        grammarLL1.add_production("Condition", "Expression 🜎 Expression")
        grammarLL1.add_production("Condition", "Expression 🜍 Expression")
        grammarLL1.add_production("Condition", "Expression 🜕 Expression")
        grammarLL1.add_production("Condition", "Expression 🜔 Expression")
        grammarLL1.add_production("Condition", "Expression 🜗 Expression")
        grammarLL1.add_production("Condition", "Expression 🜖 Expression")
        grammarLL1.add_production("WhileLoop", "dum ☾ Condition ☽ s 🜚 s Program 🜚")
        grammarLL1.add_production("ForLoop", "por ☾ Assignment ; Condition ; Assignment ☽ s 🜚 s Program 🜚")
        grammarLL1.add_production("Print", "presi ☾ Term ☽")
        #'''
        grammarLL1.firstPhase()
        grammarLL1.second_phase()
        grammarLL1.left_factoring()
        grammarLL1.eliminate_left_recursion()
        grammarLL1.get_first()
        grammarLL1.get_following()
        #endregion
        self.grammar = grammarLL1 
        self.chart = {}

    def buildTable(self):
        if(differentFirstandFollowing(self.grammar.firstS, self.grammar.followingS) == False):
            print("Firsts and Followings have elements in common, not LL1.")
        else:
            self.chart = createChart(self.grammar)

    def analyze(self, tokens):
        parse(tokens, self.chart, self.grammar)

def analyze(codigo):
    #lexico
    analizador = AnalizadorLexico()
    tokens = analizador.analizar(codigo)

    #sintáctico
    #region Grammar declaration
    print("Análisis para la Gramática - LL1")
    grammar = GLC('Start')
    grammar.add_production("Start", "🜉 s Program 🝓")
    grammar.add_production("Program", "Statement s")
    grammar.add_production("Program", "Statement s Program")
    grammar.add_production("Statement", "Assignment")
    grammar.add_production("Statement", "IfStatement")
    grammar.add_production("Statement", "WhileLoop")
    grammar.add_production("Statement", "ForLoop")
    grammar.add_production("Statement", "Print")
    grammar.add_production("Assignment", "🝳 identifier 🝳 🝑 Expression")
    grammar.add_production("Expression", "Term Expression'")
    grammar.add_production("Expression", "Term")
    grammar.add_production("Expression'", "🜂 Term")
    grammar.add_production("Expression'", "🜃 Term")
    grammar.add_production("Expression'", "🜁 Term")
    grammar.add_production("Expression'", "🜄 Term")
    grammar.add_production("Term", "🝳 identifier 🝳")
    grammar.add_production("Term", "constant")
    grammar.add_production("IfStatement", "se ☾ Condition ☽ s 🜚 s Program 🜚")
    grammar.add_production("Condition", "Expression 🜎 Expression")
    grammar.add_production("Condition", "Expression 🜍 Expression")
    grammar.add_production("Condition", "Expression 🜕 Expression")
    grammar.add_production("Condition", "Expression 🜔 Expression")
    grammar.add_production("Condition", "Expression 🜗 Expression")
    grammar.add_production("Condition", "Expression 🜖 Expression")
    grammar.add_production("WhileLoop", "dum ☾ Condition ☽ s 🜚 s Program 🜚")
    grammar.add_production("ForLoop", "por ☾ Assignment ; Condition ; Assignment ☽ s 🜚 s Program 🜚")
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

