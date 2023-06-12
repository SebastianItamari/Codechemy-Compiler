import re
from colorama import init, Fore, Style

# Inicializar colorama
init()

# Definir los patrones de búsqueda y sus correspondientes colores
patterns = [
    (r'🝰', Fore.GREEN),  # int
    (r'🝯', Fore.GREEN),  # bool
    (r'🝮', Fore.GREEN),  # char
    (r'♒︎', Fore.GREEN),  # string
    (r'♈︎', Fore.GREEN),  # double
    (r'♋︎', Fore.GREEN),  # float
    (r'♊︎', Fore.GREEN),  # array
    (r'se', Fore.BLUE),  # if
    (r'alie', Fore.BLUE),  # else
    (r'por', Fore.BLUE),  # for
    (r'dum', Fore.BLUE),  # while
    (r'rompi', Fore.BLUE),  # break
    (r'reveni', Fore.BLUE),  # return
    (r'🜂', Fore.YELLOW),  # +
    (r'🜄', Fore.YELLOW),  # -
    (r'🜁', Fore.YELLOW),  # *
    (r'🜃', Fore.YELLOW),  # /
    (r'🜅', Fore.YELLOW),  # %
    (r'malvera', Fore.RED),  # false
    (r'vera', Fore.RED),  # true
    (r'🜓', Fore.YELLOW),  # &&
    (r'🝘', Fore.YELLOW),  # ||
    (r'🜎', Fore.YELLOW),  # ==
    (r'🜔', Fore.YELLOW),  # >
    (r'🜕', Fore.YELLOW),  # <
    (r'🜖', Fore.YELLOW),  # >=
    (r'🜗', Fore.YELLOW),  # <=
    (r'🜍', Fore.YELLOW),  # !=
    (r'🝱', Fore.RED),  # !
    (r'☾', Fore.MAGENTA),  # (
    (r'☽', Fore.MAGENTA),  # )
    (r'🝳', Fore.GREEN),  # declaración (nombreVariable)
    (r'🝑', Fore.GREEN),  # asignación (variable = valor)
    (r'🜌', Fore.CYAN),  # //
    (r'🜋🜋', Fore.CYAN),  # /**/
    (r'null', Fore.GREEN)  # null
]

# Función para resaltar los patrones encontrados en el texto
def highlight_text(text):
    for pattern, color in patterns:
        text = re.sub(pattern, f"{color}{pattern}{Style.RESET_ALL}", text)
    return text

# Ejemplo de código
codigo = '''
3 🜔 2
id 🜕 3
pos 🜖 len
hola 🜗 12
1 🜎 1
bebe 🜍 baba

    🝰 b
    🝯 lola
    🝮 v

alie id 🜔 2
🜌 papa alie
'''

# Resaltar los patrones en el código
codigo_resaltado = highlight_text(codigo)

# Imprimir el código resaltado
print(codigo_resaltado)
