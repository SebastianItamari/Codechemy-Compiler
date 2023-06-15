#local application imports
from Análisis_Sintáctico_LL1.grammar_LL1_syntax_and_lexical import analyze

codigo = '''🜉
dum ☾🝳nombre🝳 🜗 -20☽
🜚
🝳var🝳 🝑 🝳var🝳 🜂 10 🜂 10
🜚
🝓'''

analysis = analyze(codigo)