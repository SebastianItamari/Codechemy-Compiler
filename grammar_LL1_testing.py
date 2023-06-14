from Gramática.GLC import GLC
from Análisis_Sintáctico_LL1.syntax_chart import * 

print("Análisis para la Gramática - LL1")
grammar = GLC('Start')

grammar.add_production("Start", "🜉 s")
grammar.add_production("Start", "Program s")
grammar.add_production("Start", "🝓")

grammar.add_production("Program", "Statement")
grammar.add_production("Program", "Statement s")
grammar.add_production("Program", "Program")

grammar.add_production("Statement", "Assignment")
grammar.add_production("Statement", "IfStatement")
grammar.add_production("Statement", "WhileLoop")
grammar.add_production("Statement", "ForLoop")

grammar.add_production("Assignment", "🝳 identifier 🝳 _ 🝑 _ Expression")

grammar.add_production("IfStatement", "se _ ☾ Condition ☽ s")
grammar.add_production("IfStatement", "🜚 s")
grammar.add_production("IfStatement", "Program s")
grammar.add_production("IfStatement", "🜚")
#grammar.add_production("IfStatement", "se _ ☾ Condition ☽  s")
grammar.add_production("IfStatement", "🜚  s")
#grammar.add_production("IfStatement", "Program s")
#grammar.add_production("IfStatement", "🜚  s")
grammar.add_production("IfStatement", " alie s")
#grammar.add_production("IfStatement", " 🜚 s")
#grammar.add_production("IfStatement", "Program s")
#grammar.add_production("IfStatement", "🜚")

grammar.add_production("WhileLoop", "dum _ ☾ Condition ☽ s")
grammar.add_production("WhileLoop", "🜚 s")
grammar.add_production("WhileLoop", "Program s")
grammar.add_production("WhileLoop", "🜚")

grammar.add_production("ForLoop", "por _ ☾ Assignment ; _ Condition ; _  Assignment ☽ s")
grammar.add_production("ForLoop", "🜚 s")
grammar.add_production("ForLoop", "Program s")
grammar.add_production("ForLoop", "🜚")

grammar.add_production("Expression", "🝳 identifier 🝳")
grammar.add_production("Expression", "constant")
grammar.add_production("Expression", "Expression _ 🜂 _ Expression")
grammar.add_production("Expression", "Expression _ 🜃 _ Expression")
grammar.add_production("Expression", "Expression _ 🜁 _ Expression")
grammar.add_production("Expression", "Expression _ 🜄 _ Expression")

grammar.add_production("Condition", "Expression _ 🜎 _ Expression")
grammar.add_production("Condition", "Expression _ 🜍 _ Expression")
grammar.add_production("Condition", "Expression _ 🜕 _ Expression")
grammar.add_production("Condition", "Expression _ 🜔 _ Expression")
grammar.add_production("Condition", "Expression _ 🜗 _ Expression")
grammar.add_production("Condition", "Expression _ 🜖 _ Expression")

grammar.print_productions()

print("----------------------------------")

#grammar.firstPhase()
#grammar.second_phase()
#grammar.left_factoring()
#grammar.eliminate_left_recursion()
#grammar.print_productions()

print("PRIMEROS")
print(grammar.get_first())
print("SIGUIENTES")
print(grammar.get_following())

if(differentFirstandFollowing(grammar.firstS, grammar.followingS) == False):
    print("Firsts and Followings have elements in common, not LL1.")
else:
    chart = createChart(grammar)
    printChart(grammar.terminals, grammar.nonTerminals, chart)
    parse("🝳 a 🝳 🝑 2 🜄 3", chart, grammar)

'''
print("--------------------------------------")
print("NUESTRA GRAMÁTICA")
grammar = GLC('A')
grammar = GLC("Program")
grammar.add_production("Program", "Statement")
grammar.add_production("Program", "Statement Program")
grammar.add_production("Statement", "Assignment")
grammar.add_production("Statement", "IfStatement")
grammar.add_production("Statement", "WhileLoop")
grammar.add_production("Assignment", "identifier = Expression ;")
grammar.add_production("IfStatement", "if ( Condition ) { Program }")
grammar.add_production("IfStatement", "if ( Condition ) { Program } else { Program }")
grammar.add_production("WhileLoop", "while ( Condition ) { Program }")
grammar.add_production("Expression", "identifier")
grammar.add_production("Expression", "constant")
#grammar.add_production("Expression", "Expression + Expression")
#grammar.add_production("Expression", "Expression / Expression")
#grammar.add_production("Expression", "Expression * Expression")
#grammar.add_production("Expression", "Expression - Expression")
grammar.add_production("Expression", "Term Expression'")
grammar.add_production("Expression'", "+ Term Expression'")
grammar.add_production("Expression'", "- Term Expression'")
grammar.add_production("Expression'", "λ")
grammar.add_production("Term", "Factor Term'")
grammar.add_production("Term'", "* Factor Term'")
grammar.add_production("Term'", "/ Factor Term'")
grammar.add_production("Term'", "λ")
grammar.add_production("Factor", "identifier")
grammar.add_production("Factor", "constant")
grammar.add_production("Factor", "( Expression )")
grammar.add_production("Condition", "Expression == Expression")
grammar.add_production("Condition", "Expression != Expression")
grammar.add_production("Condition", "Expression < Expression")
grammar.add_production("Condition", "Expression > Expression")
grammar.add_production("Condition", "Expression b= Expression")
grammar.add_production("Condition", "Expression >= Expression")

grammar.print_productions()


print("----------------------------------")

grammar.firstPhase()
grammar.second_phase()
grammar.left_factoring()
grammar.eliminate_left_recursion()
grammar.print_productions()

print("PRIMEROS")
print(grammar.get_first())
print("SIGUIENTES")
print(grammar.get_following())

if(differentFirstandFollowing(grammar.firstS, grammar.followingS) == False):
    print("Firsts and Followings have elements in common, not LL1.")
else:
    chart = createChart(grammar)
    printChart(grammar.terminals, grammar.nonTerminals, chart)
    parse("🝳 a 🝳 🝑 2 🜄 3", chart, grammar)
'''