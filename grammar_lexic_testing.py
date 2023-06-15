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
dum ☾🝳nombre🝳 🜗 -20☽ @@@2
🜚
🝳var🝳 🝑 🝳var🝳 🜂 10 🜄 🝳nombre🝳
🜚
🝓'''


codigo3 = '''🜉
🝳var🝳 🝑 0;
por ☾🝳nombre🝳 🝑 0; 🝳nombre🝳 🜗 -20; 🝳nombre🝳 🝑 🝳nombre🝳 🜂 1☽
🜚
🝳var🝳 🝑 🝳var🝳 🜂 10;
se ☾🝳id🝳 🜎 10☽
🜚
🝳id🝳 🝑 -5;
🜚
alie
🜚
🝳var🝳 🝑 🝳var🝳 🜂 10;
🜚
🜚
dum ☾🝳nombre🝳 🜗 -20☽
🜚
🝳var🝳 🝑 🝳var🝳 🜂 10 🜄 🝳nombre🝳;
🜚
🝓'''


analizador = AnalizadorLexico()
tokens = analizador.analizar(codigo2)

try:
    for token in tokens:
        print(token)

    str = ""
    for token in tokens:
        str += " " + token[0]

    print(str)
except Exception:
    print("Encountered a lexical error.")