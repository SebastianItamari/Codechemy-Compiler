#local application imports
from Gramática.GLC import GLC
from AnalisisSintacticoSLR.Item import Item
from AnalisisSintacticoSLR.SLR import SLR 
"""
grammar = GLC("Start")

grammar.add_production("Start", "🜉 Program 🝓")
grammar.add_production("Program", "Statement")
grammar.add_production("Program", "Statement Program")
grammar.add_production("Statement", "Assignment ;")
grammar.add_production("Statement", "IfStatement")
grammar.add_production("Statement", "WhileLoop")
grammar.add_production("Statement", "ForLoop")   #
grammar.add_production("Assignment", "🝳 i 🝳 _ 🝑 _ Expression")
grammar.add_production("IfStatement", "se _ ☾ Condition ☽ 🜚 Program 🜚")
grammar.add_production("IfStatement", "se _ ☾ Condition ☽ 🜚 Program 🜚 alie 🜚 Program 🜚")
grammar.add_production("WhileLoop", "dum _ ☾ Condition ☽ 🜚 Program 🜚")
grammar.add_production("ForLoop", "por _ ☾ Assignment ; _ Condition ; _ Assignment ☽ 🜚 Program 🜚")  #
grammar.add_production("Expression", "🝳 i 🝳")
grammar.add_production("Expression", "c")
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

#analisis.analyze("🜉 🝳 i 🝳 _ 🝑 _ c ; por _ ☾ 🝳 i 🝳 _ 🝑 _ c ; _ 🝳 i 🝳 _ 🜗 _ c ; _ 🝳 i 🝳 _ 🝑 _ 🝳 i 🝳 _ 🜂 _ c ☽ 🜚 🝳 i 🝳 _ 🝑 _ 🝳 i 🝳 _ 🜂 _ c ; se _ ☾ 🝳 i 🝳 _ 🜎 _ c ☽ 🜚 🝳 i 🝳 _ 🝑 _ c ; 🜚 alie 🜚 🝳 i 🝳 _ 🝑 _ 🝳 i 🝳 _ 🜂 _ c ; 🜚 🜚 dum _ ☾ 🝳 i 🝳 _ 🜂 _ 🝳 i 🝳 _ 🜔 _ c _ 🜂 _ 🝳 i 🝳 ☽ 🜚 🝳 i 🝳 _ 🝑 _ 🝳 i 🝳 _ 🜂 _ c _ 🜄 _ 🝳 i 🝳 ; 🜚 🝓")
#analisis.analyze("🜉 dum _ ☾ c _ 🜂 _ c _ 🜔 _ c ☽ 🜚 por _ ☾ 🝳 i 🝳 _ 🝑 _ c ; _ c _ 🜗 _ c ; _ 🝳 i 🝳 _ 🝑 _ c ☽ 🜚 🝳 i 🝳 _ 🝑 _ c ; 🜚 🜚 🝓")
"""

grammar = GLC('Start')
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

grammar.print_productions()

analisis = SLR(grammar)
analisis.buildTable()
#analisis.printTable()
#analisis.analyze("🜉 s 🝳 identifier 🝳 🝑 constant s 🝳 identifier 🝳 🝑 constant s 🝓")
#analisis.analyze("🜉 s se ☾ 🝳 identifier 🝳 🜕 constant ☽ s 🜚 s 🝳 identifier 🝳 🝑 constant s 🜚 s 🝓")
#analisis.analyze("🜉 s dum ☾ constant 🜍 constant ☽ s 🜚 s 🝳 identifier 🝳 🝑 constant 🜁 constant s 🜚 s 🝓")
#analisis.analyze("🜉 s 🝳 identifier 🝳 🝑 constant s 🝳 identifier 🝳 🝑 constant s 🝓")
#analisis.analyze("🜉 s por ☾ 🝳 identifier 🝳 🝑 constant ; 🝳 identifier 🝳 🜔 constant ; 🝳 identifier 🝳 🝑 🝳 identifier 🝳 🜂 constant ☽ s 🜚 s 🝳 identifier 🝳 🝑 constant 🜁 constant s 🜚 s 🝓")
#analisis.analyze("🜉 s por ☾ 🝳 identifier 🝳 🝑 constant ; 🝳 identifier 🝳 🜔 constant ; 🝳 identifier 🝳 🝑 🝳 identifier 🝳 🜂 constant ☽ s 🜚 s se ☾ 🝳 identifier 🝳 🜕 constant ☽ s 🜚 s dum ☾ constant 🜍 constant ☽ s 🜚 s 🝳 identifier 🝳 🝑 constant 🜁 constant s 🜚 s 🜚 s 🜚 s 🝓")

