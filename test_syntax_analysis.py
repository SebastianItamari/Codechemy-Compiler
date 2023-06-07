from Gramática.GLC import GLC
from Análisis_Sintáctico import syntax_chart

#Grammar to test in simplified form
glc = GLC('A')
glc.add_production('A', "B C'")
glc.add_production("C'", "+ B C'")
glc.add_production("C'", "λ")
glc.add_production('B', "F G")
glc.add_production('G', "* F G")
glc.add_production('G', "λ")
glc.add_production('F', "a")
glc.add_production('F', "( A )")
######

glc.get_first()
print("Firsts:", glc.firstS)
glc.get_following()
print("Followings:", glc.followingS)
print("Firsts:", glc.firstS)

chart = syntax_chart.createChart(glc)
syntax_chart.printChart(glc.terminals, glc.nonTerminals, chart)
syntax_chart.parse("( a + a ) * a", chart, glc)
syntax_chart.parse("( a ) * ( a + a )", chart, glc)
syntax_chart.parse("a", chart, glc)
