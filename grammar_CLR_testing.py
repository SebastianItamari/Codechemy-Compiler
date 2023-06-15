#local application imports
from Gramática.GLC import GLC
from AnalisisSintacticoCLR.ItemCLR import ItemCLR
from AnalisisSintacticoCLR.CLR import CLR 
from AnalisisSintacticoCLR.GrammarCLR import GrammarCRL

"""
grammar = GLC("Program")
grammar.add_production("Program", "Statement")
grammar.add_production("Program", "Statement Program")
grammar.add_production("Statement", "Assignment")
grammar.add_production("Statement", "IfStatement")
grammar.add_production("Statement", "WhileLoop")
grammar.add_production("Statement", "ForLoop")   #
grammar.add_production("Assignment", "identifier = Expression ;")
grammar.add_production("IfStatement", "if ( Condition ) { Program }")
grammar.add_production("IfStatement", "if ( Condition ) { Program } else { Program }")
grammar.add_production("WhileLoop", "while ( Condition ) { Program }")
grammar.add_production("AssignmentFor", "identifier = Expression")   #
grammar.add_production("ForLoop", "for ( AssignmentFor ; Condition ; AssignmentFor ) { Program }")  #
grammar.add_production("Expression", "identifier")
grammar.add_production("Expression", "constant")
grammar.add_production("Expression", "Expression + Expression")
grammar.add_production("Expression", "Expression / Expression")
grammar.add_production("Expression", "Expression * Expression")
grammar.add_production("Expression", "Expression - Expression")
grammar.add_production("Condition", "Expression == Expression")
grammar.add_production("Condition", "Expression != Expression")
grammar.add_production("Condition", "Expression < Expression")
grammar.add_production("Condition", "Expression > Expression")
grammar.add_production("Condition", "Expression <= Expression")
grammar.add_production("Condition", "Expression >= Expression")

grammar.print_productions()

analisis = CLR(grammar)
analisis.buildTable()
analisis.printTable()
analisis.analyze("if ( identifier == constant ) { constant ; }")
analisis.analyze("if ( identifier == constant ) { identifier = constant ; }")
analisis.analyze("if ( identifier == constant ) { identifier = identifier * constant + constant ; }")
analisis.analyze("while ( identifier > constant ) { identifier = constant / constant - identifier ; identifier = constant ; }")
analisis.analyze("while ( identifier > constant ) { if ( identifier != constant ) { identifier = constant ; } }")
analisis.analyze("for ( identifier = constant ; identifier >= constant ; identifier = identifier + constant ) { if ( identifier != constant ) { identifier = constant ; } }")
"""

grammar = GLC("Start")
grammar.add_production("Start", "🜉 s Program 🝓")
grammar.add_production("Program", "Statement s")
grammar.add_production("Program", "Statement s Program")
grammar.add_production("Statement", "Assignment")
grammar.add_production("Statement", "IfStatement")
grammar.add_production("Statement", "WhileLoop")
grammar.add_production("Statement", "ForLoop")
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
grammar.add_production("Statement", "Print")
grammar.add_production("Print", "presi ☾ Term ☽")

grammar.print_productions()

analisis = CLR(grammar)
analisis.buildTable()
#analisis.printTable()

# INSTRUCCIONES VÁLIDAS #

#analisis.analyze("🜉 s 🝳 identifier 🝳 🝑 constant s 🝳 identifier 🝳 🝑 constant s 🝓")
#analisis.analyze("🜉 s se ☾ 🝳 identifier 🝳 🜕 constant ☽ s 🜚 s 🝳 identifier 🝳 🝑 constant s 🜚 s 🝓")
#analisis.analyze("🜉 s dum ☾ constant 🜍 constant ☽ s 🜚 s 🝳 identifier 🝳 🝑 constant 🜁 constant s 🜚 s 🝓")
#analisis.analyze("🜉 s 🝳 identifier 🝳 🝑 constant s 🝳 identifier 🝳 🝑 constant s 🝓")
#analisis.analyze("🜉 s por ☾ 🝳 identifier 🝳 🝑 constant ; 🝳 identifier 🝳 🜔 constant ; 🝳 identifier 🝳 🝑 🝳 identifier 🝳 🜂 constant ☽ s 🜚 s 🝳 identifier 🝳 🝑 constant 🜁 constant s 🜚 s 🝓")
#analisis.analyze("🜉 s por ☾ 🝳 identifier 🝳 🝑 constant ; 🝳 identifier 🝳 🜔 constant ; 🝳 identifier 🝳 🝑 🝳 identifier 🝳 🜂 constant ☽ s 🜚 s se ☾ 🝳 identifier 🝳 🜕 constant ☽ s 🜚 s dum ☾ constant 🜍 constant ☽ s 🜚 s 🝳 identifier 🝳 🝑 constant 🜁 constant s 🜚 s 🜚 s 🜚 s 🝳 identifier 🝳 🝑 constant s 🝓")
#analisis.analyze("🜉 s presi ☾ 🝳 identifier 🝳 ☽ s 🝓")

# INSTRUCCIONES VÁLIDAS #

#analisis.analyze("🜉 s 🝳 identifier 🝳 constant s 🝳 identifier 🝳 🝑 constant s 🝓")
#analisis.analyze("🜉 s 🝓 s s")
#analisis.analyze("🜉 s se ☾ 🝳 🝳 🜕 constant ☽ s 🜚 s 🝳 identifier 🝳 🝑 constant s 🜚 s 🝓")
#analisis.analyze("🜉 s dum ☾ constant 🜍 constant ☽ s 🜚 s 🝳 identifier 🝳 🝑 t s 🜚 s 🝓")