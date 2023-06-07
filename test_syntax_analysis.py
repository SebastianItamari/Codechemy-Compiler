from Gramática.GLC import GLC
from Análisis_Sintáctico import syntax_chart

glc = GLC('A')
glc.add_production('A', "B C'")
glc.add_production("C'", "+ B C'")
glc.add_production("C'", "λ")
glc.add_production('B', "F G")
glc.add_production('G', "* F G")
glc.add_production('G', "λ")
glc.add_production('F', "a")
glc.add_production('F', "( A )")

#glc.get_first()
#glc.get_following()

glc.firstS = {
    'A': ['a', '('], 
    "C'": ['+', 'λ'], 
    'B': ['a', '('],
    'G': ['*', 'λ'],
    'F': ['a', '('] 
    }

glc.followingS = {
    'A': ['$', ')'], 
    "C'": ['$', ')'], 
    'B': ['+', '$', ')'],
    'G': ['+', '$', ')'],
    'F': ['*', '+', '$', ')'] 
    }



chart = syntax_chart.createChart(glc)
syntax_chart.printChart(glc.terminals, glc.nonTerminals, chart)
#syntaxtchart.parse("(a+a)*a", chart, glc)
syntax_chart.parse("( a ) * ( a + a )", chart, glc)
#syntaxtchart.parse("a", chart, glc)
