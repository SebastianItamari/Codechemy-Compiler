#standard library imports
import tkinter as tk
from tkinter import scrolledtext, Menu, ttk, BOTTOM
from tkinter.filedialog import asksaveasfilename, askopenfilename
import re

#local application imports
from AnalisisSintacticoSLR.SLR import SLR, SLRError
from AnalisisSintacticoCLR.CLR import CLR, CLRError
from Análisis_Léxico.Analizador.AnalizadorLexico import AnalizadorLexico, LexicalError

class CodechemyIDE:
    def __init__(self, grammar, analyzer="SLR"):
        self.window = tk.Tk()
        self.window.title("IDE CODECHEMY")
        #self.grammar = grammar
        self.lexical_analyzer = AnalizadorLexico()
        self.file_path = ''
        self.patterns = [
            (r'🝰', 'green'),  # int
            (r'🝯', 'green'),  # bool
            (r'🝮', 'green'),  # char
            (r'♒︎', 'green'),  # string
            (r'♈︎', 'green'),  # double
            (r'♋︎', 'green'),  # float
            (r'♊︎', 'green'),  # array
            (r'se', 'blue'),  # if
            (r'alie', 'blue'),  # else
            (r'por', 'blue'),  # for
            (r'dum', 'blue'),  # while
            (r'rompi', 'blue'),  # break
            (r'reveni', 'blue'),  # return
            (r'🜂', 'yellow'),  # +
            (r'🜄', 'yellow'),  # -
            (r'🜁', 'yellow'),  # *
            (r'🜃', 'yellow'),  # /
            (r'🜅', 'yellow'),  # %
            (r'malvera', 'red'),  # false
            (r'vera', 'red'),  # true
            (r'🜓', 'yellow'),  # &&
            (r'🝘', 'yellow'),  # ||
            (r'🜎', 'yellow'),  # ==
            (r'🜔', 'yellow'),  # >
            (r'🜕', 'yellow'),  # <
            (r'🜖', 'yellow'),  # >=
            (r'🜗', 'yellow'),  # <=
            (r'🜍', 'yellow'),  # !=
            (r'🝱', 'red'),  # !
            (r'☾', 'magenta'),  # (
            (r'☽', 'magenta'),  # )
            (r'🝳', 'green'),  # declaración (nombreVariable)
            (r'🝑', 'green'),  # asignación (variable = valor)
            (r'🜌', 'cyan'),  # //
            (r'🜋🜋', 'cyan'),  # /**/
            (r'null', 'green')  # null
        ]

        if analyzer == "SLR":
            self.syntax_analyzer = SLR(grammar)
            self.syntax_analyzer.buildTable()
        elif analyzer == "CLR":
            self.syntax_analyzer = CLR(grammar)
            self.syntax_analyzer.buildTable()

        self.create_menu()
        self.create_editor()
        self.create_output()
        self.create_words_bar()
        self.bind_events()
    
        # Mostrar la ventana
        self.window.mainloop()

    def create_menu(self):
        # Crear y configurar menú
        menu = Menu(self.window)
        self.window.config(menu=menu)

        # Crear submenús y añadirlos al menú principal
        file_menu = Menu(menu, tearoff=0)
        output_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file_menu)
        menu.add_cascade(label="Output", menu=output_menu)

        # Configurar file_menu
        file_menu.add_command(label="Open", accelerator="Ctrl+O", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Save", accelerator="Ctrl+S", command=self.save_file)
        file_menu.add_command(label="Save as", accelerator="Ctrl+A", command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", accelerator="Ctrl+Q", command=self.close)

        # Configurar output_menu
        output_menu.add_command(label="Execute", accelerator="F5", command=self.execute_code)
        output_menu.add_separator()
        output_menu.add_command(label="Clean", accelerator="F4", command=self.clean_output)

    def create_editor(self):
        self.editor = scrolledtext.ScrolledText(self.window, width=80, height=20, font=("Courier New", 12))
        self.editor.pack(expand=True, fill=tk.BOTH)
        self.editor.bind("<KeyRelease>", self.highlight_syntax)
        self.editor.bind("<<Modified>>", self.change_word)
    
    def create_output(self):
        self.output = scrolledtext.ScrolledText(self.window, height=8)
        self.output.pack(expand=True, fill=tk.BOTH)
        self.output.config(state="disabled")

    def create_words_bar(self):
        self.words_bar = ttk.Label(self.window, text="\t\t\t\t\t\tt\t\t\t\t\t\t\t characters: 0 words: 0")
        self.words_bar.pack(side=BOTTOM)

    def bind_events(self):
        self.window.bind("<Control-q>", self.close)
        self.window.bind("<Control-Q>", self.close)
        self.window.bind("<Control-o>", self.open_file)
        self.window.bind("<Control-O>", self.open_file)
        self.window.bind("<Control-s>", self.save_file)
        self.window.bind("<Control-S>", self.save_file)
        self.window.bind("<Control-a>", self.save_as)
        self.window.bind("<Control-A>", self.save_as)
        self.window.bind("<F5>", self.execute_code)
        self.window.bind("<F4>", self.clean_output)

    # Función para pintar en tiempo real las palabras reservadas
    def highlight_syntax(self, event=None):
        #if event.keysym == "space" or event.keysym == "Return":
            text = self.editor.get("1.0", "end-1c")
            self.editor.tag_remove("highlight", "1.0", "end")  # Eliminar todas las etiquetas de resaltado existentes
            
            for i, (pattern, color) in enumerate(self.patterns):
                matches = re.finditer(pattern, text)
                for match in matches:
                    start = f"1.0+{match.start()}c"
                    end = f"1.0+{match.end()}c"
                    tag_name = f"highlight_{i}"  # Etiqueta única para cada patrón
                    self.editor.tag_add(tag_name, start, end)
                    self.editor.tag_config(tag_name, foreground=color)

    # Función para actualizar la cantidad de palabras y caractéres
    def change_word(self, event=None):
        if self.editor.edit_modified():
            word = len(self.editor.get("1.0", "end-1c").split())
            text = self.editor.get("1.0", "end-1c").replace(" ", "")
            text = text.replace("\n","")
            chararcter = len(text)
            self.words_bar.config(text=f"\t\t\t\t\t\tt\t\t\t\t\t\t\t characters: {chararcter} words: {word}")
        self.editor.edit_modified(False)

    # Función para cerrar la ventana
    def close(self, event=None):
        self.window.destroy()

    # Función para abrir archivos
    def open_file(self, event=None):
        open_path = askopenfilename(filetypes=[("CHEMY File", "*.chemy")])
        if open_path != '':
            self.file_path = open_path
            with open(open_path, "r") as file:
                code = file.read()
                self.editor.delete("1.0", "end")
                self.editor.insert("1.0", code)
                self.highlight_syntax()

    # Función para guardar archivos
    def save_file(self, event=None):
        if self.file_path == '':
            save_path = asksaveasfilename(defaultextension=".chemy", filetypes=[("CHEMY File", "*.chemy")])
            self.file_path = save_path
        else:
            save_path = self.file_path
        if save_path != '':
            with open(save_path, "w") as file:
                code = self.editor.get("1.0", "end-1c")
                file.write(code)

    # function para guardar archivos con un nombre específico
    def save_as(self, event=None):
        save_path = asksaveasfilename(defaultextension=".chemy", filetypes=[("CHEMY File", "*.chemy")])
        self.file_path = save_path
        if save_path != '':
            with open(save_path, "w") as file:
                code = self.editor.get("1.0", "end-1c")
                file.write(code)

    # function para compilar el código del IDE
    def execute_code(self, event=None):
        execution = "Compiling..."
        print(execution)
        self.output.config(state="normal")
        #aca agregar el resultado de los análisis
        try:
            tokens = self.lexical_analyzer.analizar(self.editor.get("1.0", "end-1c"))
            self.syntax_analyzer.analyze(tokens)
            print("------------------------")
            print("¡Instrucción válida!")
            print("------------------------")
            execution = execution + "\n¡Instrucción válida!"
        except LexicalError as lexicalError:
            print("------------------------")
            print(lexicalError.mensaje)
            print("------------------------")
            execution = execution + "\n" + lexicalError.mensaje
        except SLRError as syntaxError:
            print("------------------------")
            print("Error en analizador sintáctico SLR")
            print(syntaxError.mensaje)
            print("------------------------")
            execution = execution + "\n" + "Error en analizador sintáctico SLR" + "\n" + syntaxError.mensaje
        except CLRError as syntaxError:
            print("------------------------")
            print("Error en analizador sintáctico CLR")
            print(syntaxError.mensaje)
            print("------------------------")
            execution = execution + "\n" + "Error en analizador sintáctico CLR" + "\n" + syntaxError.mensaje

        self.output.delete("1.0", "end")
        self.output.insert("1.0", execution)
        self.output.config(state="disabled")

    # function para limpiar la salida del IDE
    def clean_output(self, event=None):
        self.output.config(state="normal")
        self.output.delete("1.0", "end")
        self.output.config(state="disabled")