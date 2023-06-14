from Análisis_Léxico.Analizador.AnalizadorLexico import AnalizadorLexico

# Ejemplo de uso
codigo = '''
🝰 🝳a🝳 
🝳a🝳 🝑 2 🜄 3
🝰 🝳b🝳 
🝳b🝳 🝑 vera
3 🜔 2
🝳id🝳 🜕 3
🝳pos🝳 🜖 🝳len🝳
🝳hola🝳 🜗 12
1 🜎 1
🝳bebe🝳 🜍 🝳baba🝳

    🝰 🝳b🝳
    🝯 🝳lola🝳
    🝮 🝳v🝳

alie 🝳id🝳 🜔 2

alie 🝳id🝳 🜓 2
alie 🝳id🝳 🝘 2

🜌 se 🝳papa🝳 alie
🜛 se
por ☾ ☽
🜚
    rompi
🜚
dum ☾ ☽
🜚
    reveni
🜚
'''

codigo1 = '''🜉
se ☾🝳id🝳 🜎 10☽
🜚
🝳id🝳 🝑 -5
🜚
alie
🜚
🝳var🝳 🝑 🝳var🝳 🜂 10
🜚
🝓'''

codigo2 = '''🜉
dum ☾🝳nombre🝳 🜗 -20☽
🜚
🝳var🝳 🝑 🝳var🝳 🜂 10 🜄 🝳nombre🝳
🜚
🝓'''

codigo3 = '''🜉
🝳var🝳 🝑 0
por ☾🝳nombre🝳 🝑 0; 🝳nombre🝳 🜗 -20; 🝳nombre🝳 🝑 🝳nombre🝳 🜂 1☽
🜚
🝳var🝳 🝑 🝳var🝳 🜂 10
🜚
🝓'''

analizador = AnalizadorLexico()
tokens = analizador.analizar(codigo3)
for token in tokens:
    print(token)
