#local application imports
from Gramática.GLC import GLC
from AnalisisSintacticoSLR.Item import Item
from AnalisisSintacticoSLR.SLR import SLR 
from Análisis_Léxico.Analizador.AnalizadorLexico import AnalizadorLexico
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

#grammar.print_productions()

analisis = SLR(grammar)
analisis.buildTable()
#analisis.printGoto()
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

codigo0 = '''🜉
🝳var🝳 🝑 -10
🝳nombre🝳 🝑 1
🝓'''

codigo1 = '''🜉
se ☾ 🝳var🝳 🜕 -2 ☽
🜚
🝳var🝳 🝑 🝳var🝳 🜂 2
🜚
🝓'''

codigo2 = '''🜉
dum ☾🝳id🝳 🜍 200☽
🜚
🝳id🝳 🝑 12 🜁 1
🜚
🝓'''

codigo3 = '''🜉
🝳identifier🝳 🝑 23
🝳identifier🝳 🝑 -2
🝓'''

codigo4 = '''🜉
por ☾🝳len🝳 🝑 0; 🝳len🝳 🜔 12; 🝳len🝳 🝑 🝳len🝳 🜂 1☽
🜚
🝳len🝳 🝑 12 🜁 23
🜚
🝓'''

codigo5 = '''🜉
por ☾🝳identifier🝳 🝑 0; 🝳identifier🝳 🜔 23; 🝳identifier🝳 🝑 🝳identifier🝳 🜂 2☽
🜚
se ☾🝳identifier🝳 🜕 3☽
🜚
dum ☾🝳identifier🝳 🜍 0☽
🜚
🝳identifier🝳 🝑 2 🜁 3
🜚
🜚
🜚
🝳identifier🝳 🝑 -1
🝓'''

codigo6 = '''🜉
presi ☾ 🝳 identifier 🝳 ☽
🝓'''

codigo7 = '''🜉
🝳identifier🝳 2
🝳identifier🝳 🝑 -5
🝓'''

codigo8 = '''🜉
🝓

'''

codigo9 = '''🜉
se ☾🝳🝳 🜕 10 ☽
🜚
🝳identifier🝳 🝑 -5
🜚
🝓'''

codigo10 = '''🜉
dum ☾15 🜍 12☽
🜚
🝳identifier🝳 🝑 t
🜚
🝓'''

codigo11 = '''🜉
dum ☾🝳nombre🝳 🜗 -20☽
🜚
por ☾🝳identifier🝳 🝑 5; 🝳identifier🝳 🜔 8; 🝳identifier🝳 🝑 🝳identifier🝳 🜂 5☽ 
🜚 
se ☾🝳identifier🝳 🜕 9☽ 
🜚
🝳identifier🝳 🝑 -7 🜁 8
presi ☾6☽
🜚
se ☾🝳identifier🝳 🜕 6☽ 
🜚 
🝳identifier🝳 🝑 5 
🜚
🜚
🝳var🝳 🝑 🝳var🝳 🜂 10
🜚
🝓'''

codigo12 = '''🜉
🝳identifier🝳 🝑 12 
🝳identifier🝳 🝑 -2
🝳identifier🝳 🝑 12
se ☾🝳identifier🝳 🜗 🝳identifier🝳☽
🜚
🝳identifier🝳 🝑 🝳identifier🝳
🜚
se ☾🝳identifier🝳 🜗 🝳identifier🝳☽
🜚
🝳identifier🝳 🝑 🝳identifier🝳
🜚
se ☾🝳identifier🝳 🜗 🝳identifier🝳☽
🜚
🝳identifier🝳 🝑 🝳identifier🝳
🜚
🝓'''

codigo13 = '''🜉
🝳var🝳 🝑 2 🜂 3 🜂 4
🝓'''

analizador = AnalizadorLexico()
tokens = analizador.analizar(codigo12)
analisis.analyze(tokens)
