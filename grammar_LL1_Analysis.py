#local application imports
from Análisis_Sintáctico_LL1.grammar_LL1_syntax_and_lexical import analyze

codigo = '''🜉
🝳 a 🝳 🝑 3
🝳 b 🝳 🝑 45
🝳 c 🝳 🝑 10
se ☾ 🝳 a 🝳 🜗 🝳 b 🝳 ☽ 
🜚
🝳 c 🝳 🝑 100
🜚
se ☾ 🝳 a 🝳 🜗 🝳 b 🝳 ☽ 
🜚
🝳 c 🝳 🝑 201
🜚
se ☾ 🝳 a 🝳 🜗 🝳 c 🝳 ☽ 
🜚
🝳 a 🝳 🝑 🝳 b 🝳
🜚
🝓'''

analysis = analyze(codigo)