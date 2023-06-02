from ..Gramática import GLC
import syntaxchart

glc = GLC.GLC('A')
#glc.noTerminals = ['A', 'C', 'B', 'G', 'F']
glc.terminals = ['a', '+', '*', '(', ')']
glc.add_production('A', "BC")
glc.add_production('C', "+BC")
glc.add_production('C', "λ")
glc.add_production('B', "FG")
glc.add_production('G', "*FG")
glc.add_production('G', "λ")
glc.add_production('F', "a")
glc.add_production('F', "(A)")

glc.firstS = {
    'A': ['a', '('], 
    'C': ['+', 'λ'], 
    'B': ['a', '('],
    'G': ['*', 'λ'],
    'F': ['a', '('] 
    }
glc.nextS = {
    'A': ['$', ')'], 
    'C': ['$', ')'], 
    'B': ['+', '$', ')'],
    'G': ['+', '$', ')'],
    'F': ['*', '+', '$', ')'] 
    }

chart = syntaxchart.createChart(glc)
syntaxchart.printChart(glc.terminals, glc.noTerminals, chart)
#syntaxtchart.parse("(a+a)*a", chart, glc)
syntaxchart.parse("(a)+a", chart, glc)
#syntaxtchart.parse("a", chart, glc)
