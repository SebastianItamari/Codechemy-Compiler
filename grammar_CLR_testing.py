from AnalisisSintacticoCLR.GLC import GLC
from AnalisisSintacticoCSLR.Item import Item
from AnalisisSintacticoCLR.CLR import CLR 
from AnalisisSintacticoCLR.GrammarCLR import GrammarCRL

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