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
analizador = AnalizadorLexico()
tokens = analizador.analizar(codigo)
for token in tokens:
    print(token)
