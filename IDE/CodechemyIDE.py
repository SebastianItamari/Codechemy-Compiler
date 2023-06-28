#standard library imports
import tkinter as tk
from tkinter import scrolledtext, Menu, ttk, BOTTOM
from tkinter.filedialog import asksaveasfilename, askopenfilename
import re

#local application imports
from Análisis_Sintáctico_LL1.LL1 import LL1 
from Análisis_Sintáctico_LL1.syntax_chart import * 
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
        
        self.lightpattern = [
            (r'🝰', 'Dark green'),  # int
            (r'🝯', 'Dark green'),  # bool
            (r'🝮', 'Dark green'),  # char
            (r'♒︎', 'Dark green'),  # string
            (r'♈︎', 'Dark green'),  # double
            (r'♋︎', 'Dark green'),  # float
            (r'♊︎', 'Dark green'),  # array
            (r'se', 'orange'),  # if
            (r'alie', 'orange'),  # else
            (r'por', 'orange'),  # for
            (r'dum', 'orange'),  # while
            (r'rompi', 'orange'),  # break
            (r'reveni', 'orange'),  # return
            (r'🜂', 'purple'),  # +
            (r'🜄', 'purple'),  # -
            (r'🜁', 'purple'),  # *
            (r'🜃', 'purple'),  # /
            (r'🜅', 'purple'),  # %
            (r'malvera', 'red'),  # false
            (r'vera', 'red'),  # true
            (r'🜓', 'purple'),  # &&
            (r'🝘', 'purple'),  # ||
            (r'🜎', 'purple'),  # ==
            (r'🜔', 'purple'),  # >
            (r'🜕', 'purple'),  # <
            (r'🜖', 'purple'),  # >=
            (r'🜗', 'purple'),  # <=
            (r'🜍', 'purple'),  # !=
            (r'🝱', 'red'),  # !
            (r'☾', 'magenta'),  # (
            (r'☽', 'magenta'),  # )
            (r'🝳', '#151715'),  # declaración (nombreVariable)
            (r'🝑', '#151715'),  # asignación (variable = valor)
            (r'🜌', 'cyan'),  # //
            (r'🜋🜋', 'cyan'),  # /**/
            (r'null', '#151715')  # null
        ]
        self.darkpattern = [
            (r'🝰', '#f58442'),  # int
            (r'🝯', '#f58442'),  # bool
            (r'🝮', '#f58442'),  # char
            (r'♒︎', '#f58442'),  # string
            (r'♈︎', '#f58442'),  # double
            (r'♋︎', '#f58442'),  # float
            (r'♊︎', '#f58442'),  # array
            (r'se', 'magenta'),  # if
            (r'alie', 'magenta'),  # else
            (r'por', 'magenta'),  # for
            (r'dum', 'magenta'),  # while
            (r'rompi', 'magenta'),  # break
            (r'reveni', 'magenta'),  # return
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
            (r'🝳', '#03fc4e'),  # declaración (nombreVariable)
            (r'🝑', '#03fc4e'),  # asignación (variable = valor)
            (r'🜌', 'cyan'),  # //
            (r'🜋🜋', 'cyan'),  # /**/
            (r'null', 'yellow')  # null
        ]
        self.patternUsed=self.lightpattern
        if analyzer == "SLR":
            self.syntax_analyzer = SLR(grammar)
            self.syntax_analyzer.buildTable()
        elif analyzer == "CLR":
            self.syntax_analyzer = CLR(grammar)
            self.syntax_analyzer.buildTable()
        elif analyzer == "LL1":
            self.syntax_analyzer = LL1(grammar)
            self.syntax_analyzer.buildTable()

        self.create_menu()
        self.create_editor()
        self.create_output()
        self.create_words_bar()
        self.bind_events()
    
        # Mostrar la ventana
        self.window.mainloop()
    
    # function for light mode window
    def light(self):
        self.editor.config(fg="black",bg="white")
        self.window.config(bg="white")
        self.patternUsed=self.lightpattern
        self.output.config(fg="black",bg="white")
        self.highlight_syntax()


    # function for dark mode window
    def dark(self):
        self.editor.config(fg="white", bg="black", insertbackground="white")
        self.window.config(bg="black")
        self.output.config(bg="black", fg="white")
        self.patternUsed=self.darkpattern
        self.highlight_syntax()

    def create_menu(self):
        # Crear y configurar menú
        menu = Menu(self.window)
        self.window.config(menu=menu)

        # Crear submenús y añadirlos al menú principal
        file_menu = Menu(menu, tearoff=0)
        output_menu = Menu(menu, tearoff=0)
        theme_menu = Menu(menu, tearoff=0)
        symbol_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file_menu)
        menu.add_cascade(label="Output", menu=output_menu)
        menu.add_cascade(label="Theme", menu=theme_menu)
        menu.add_cascade(label="Dictionary", menu=symbol_menu)

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

        # Comando para cambiar theme
        theme_menu.add_command(label="Light", command= self.light)
        theme_menu.add_command(label="Dark", command= self.dark)

        #Comando para insertar simbolos
        #symbol_menu.add_command(label="🝰 int", accelerator="Ctrl-B", command=lambda: self.insert_symbol("🝰"))
        #symbol_menu.add_command(label="🝯 bool", accelerator="Ctrl-D", command=lambda: self.insert_symbol("🝯"))
        #symbol_menu.add_command(label="🝮 char", accelerator="Ctrl-E", command=lambda: self.insert_symbol("🝮"))
        #symbol_menu.add_command(label="♒︎ string", accelerator="Ctrl-F", command=lambda: self.insert_symbol("♒︎"))
        #symbol_menu.add_command(label="♈︎ double", accelerator="Ctrl-G", command=lambda: self.insert_symbol("♈︎"))
        #symbol_menu.add_command(label="♋︎ float", accelerator="Ctrl-H", command=lambda: self.insert_symbol("♋︎"))
        #symbol_menu.add_command(label="♊︎ array", accelerator="Ctrl-I", command=lambda: self.insert_symbol("♊︎"))
        symbol_menu.add_command(label="🜂 +", accelerator="Ctrl-J", command=lambda: self.insert_symbol("🜂"))
        symbol_menu.add_command(label="🜄 -", accelerator="Ctrl-K", command=lambda: self.insert_symbol("🜄"))
        symbol_menu.add_command(label="🜁 *", accelerator="Ctrl-L", command=lambda: self.insert_symbol("🜁"))
        symbol_menu.add_command(label="🜃 /", accelerator="Ctrl-M", command=lambda: self.insert_symbol("🜃"))
        symbol_menu.add_command(label="🜅 %", accelerator="Ctrl-N", command=lambda: self.insert_symbol("🜅"))
        symbol_menu.add_command(label="🜓 &&", accelerator="Ctrl-P", command=lambda: self.insert_symbol("🜓"))
        symbol_menu.add_command(label="🝘 ||", accelerator="Ctrl-R", command=lambda: self.insert_symbol("🝘"))
        symbol_menu.add_command(label="🜎 ==", accelerator="Ctrl-T", command=lambda: self.insert_symbol("🜎"))
        symbol_menu.add_command(label="🜔 >", accelerator="Ctrl-U", command=lambda: self.insert_symbol("🜔"))
        symbol_menu.add_command(label="🜕 <", accelerator="Ctrl-W", command=lambda: self.insert_symbol("🜕"))
        symbol_menu.add_command(label="🜖 >=", accelerator="F1", command=lambda: self.insert_symbol("🜖"))
        symbol_menu.add_command(label="🜗 <=", accelerator="F2", command=lambda: self.insert_symbol("🜗"))
        symbol_menu.add_command(label="🜍 !=", accelerator="F3", command=lambda: self.insert_symbol("🜍"))
        symbol_menu.add_command(label="🝱 !", accelerator="F6", command=lambda: self.insert_symbol("🝱"))
        symbol_menu.add_command(label="☾ (", accelerator="F7", command=lambda: self.insert_symbol("☾"))
        symbol_menu.add_command(label="☽ )", accelerator="F8", command=lambda: self.insert_symbol("☽"))
        symbol_menu.add_command(label="🝳 Declaracion", accelerator="F9", command=lambda: self.insert_symbol("🝳"))
        symbol_menu.add_command(label="🝑 Asignacion", accelerator="F10", command=lambda: self.insert_symbol("🝑"))
        symbol_menu.add_command(label="🜌 //", accelerator="F11", command=lambda: self.insert_symbol("🜌"))
        symbol_menu.add_command(label="🜋🜋 /**/", accelerator="F12", command=lambda: self.insert_symbol("🜋🜋"))

        # Insert column break after every 10 commands
        for i in range(1, 10):
            symbol_menu.entryconfigure(i * 5, columnbreak=tk.TRUE)

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
        #self.window.bind("<Control-B>", lambda event: self.insert_symbol("🝰"))
        #self.window.bind("<Control-b>", lambda event: self.insert_symbol("🝰"))
        #self.window.bind("<Control-D>", lambda event: self.insert_symbol("🝯"))
        #self.window.bind("<Control-d>", lambda event: self.insert_symbol("🝯"))
        #self.window.bind("<Control-E>", lambda event: self.insert_symbol("🝮"))
        #self.window.bind("<Control-e>", lambda event: self.insert_symbol("🝮"))
        #self.window.bind("<Control-F>", lambda event: self.insert_symbol("♒︎"))        
        #self.window.bind("<Control-f>", lambda event: self.insert_symbol("♒︎"))
        #self.window.bind("<Control-G>", lambda event: self.insert_symbol("♈︎"))        
        #self.window.bind("<Control-g>", lambda event: self.insert_symbol("♈︎"))
        #self.window.bind("<Control-H>", lambda event: self.insert_symbol("♋︎"))        
        #self.window.bind("<Control-h>", lambda event: self.insert_symbol("♋︎"))
        #self.window.bind("<Control-I>", lambda event: self.insert_symbol("♊︎"))        
        #self.window.bind("<Control-i>", lambda event: self.insert_symbol("♊︎"))
        self.window.bind("<Control-J>", lambda event: self.insert_symbol("🜂"))
        self.window.bind("<Control-j>", lambda event: self.insert_symbol("🜂"))
        self.window.bind("<Control-K>", lambda event: self.insert_symbol("🜄"))
        self.window.bind("<Control-k>", lambda event: self.insert_symbol("🜄"))
        self.window.bind("<Control-L>", lambda event: self.insert_symbol("🜁"))
        self.window.bind("<Control-l>", lambda event: self.insert_symbol("🜁"))
        self.window.bind("<Control-M>", lambda event: self.insert_symbol("🜃"))
        self.window.bind("<Control-m>", lambda event: self.insert_symbol("🜃"))
        self.window.bind("<Control-N>", lambda event: self.insert_symbol("🜅"))
        self.window.bind("<Control-n>", lambda event: self.insert_symbol("🜅"))
        self.window.bind("<Control-P>", lambda event: self.insert_symbol("🜓"))
        self.window.bind("<Control-p>", lambda event: self.insert_symbol("🜓"))
        self.window.bind("<Control-R>", lambda event: self.insert_symbol("🝘"))
        self.window.bind("<Control-r>", lambda event: self.insert_symbol("🝘"))
        self.window.bind("<Control-T>", lambda event: self.insert_symbol("🜎"))
        self.window.bind("<Control-t>", lambda event: self.insert_symbol("🜎"))
        self.window.bind("<Control-U>", lambda event: self.insert_symbol("🜔"))
        self.window.bind("<Control-u>", lambda event: self.insert_symbol("🜔"))
        self.window.bind("<Control-W>", lambda event: self.insert_symbol("🜕"))
        self.window.bind("<Control-w>", lambda event: self.insert_symbol("🜕"))
        self.window.bind("<F1>", lambda event: self.insert_symbol("🜖"))
        self.window.bind("<F2>", lambda event: self.insert_symbol("🜗"))
        self.window.bind("<F3>", lambda event: self.insert_symbol("🜍"))
        self.window.bind("<F6>", lambda event: self.insert_symbol("🝱"))
        self.window.bind("<F7>", lambda event: self.insert_symbol("☾"))
        self.window.bind("<F8>", lambda event: self.insert_symbol("☽"))
        self.window.bind("<F9>", lambda event: self.insert_symbol("🝳"))
        self.window.bind("<F10>", lambda event: self.insert_symbol("🝑"))
        self.window.bind("<F11>", lambda event: self.insert_symbol("🜌"))
        self.window.bind("<F12>", lambda event: self.insert_symbol("🜋🜋"))




    # Función para pintar en tiempo real las palabras reservadas
    def highlight_syntax(self, event=None):
        #if event.keysym == "space" or event.keysym == "Return":
            text = self.editor.get("1.0", "end-1c")
            self.editor.tag_remove("highlight", "1.0", "end")  # Eliminar todas las etiquetas de resaltado existentes

            for i, (pattern, color) in enumerate(self.patternUsed):
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
            with open(open_path, "r", encoding="utf-8") as file:
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
            with open(save_path, "w", encoding="utf-8") as file:
                code = self.editor.get("1.0", "end-1c")
                file.write(code)

    # function para guardar archivos con un nombre específico
    def save_as(self, event=None):
        save_path = asksaveasfilename(defaultextension=".chemy", filetypes=[("CHEMY File", "*.chemy")])
        self.file_path = save_path
        if save_path != '':
            with open(save_path, "w", encoding="utf-8") as file:
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
            print("------------  ------------")
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

        except LL1Error as syntaxError:
            print("------------------------")
            print("Error en analizador sintáctico LL1")
            print(syntaxError.mensaje)
            print("------------------------")
            execution = execution + "\n" + "Error en analizador sintáctico LL1" + "\n" + syntaxError.mensaje


        self.output.delete("1.0", "end")
        self.output.insert("1.0", execution)
        self.output.config(state="disabled")

    # function para limpiar la salida del IDE
    def clean_output(self, event=None):
        self.output.config(state="normal")
        self.output.delete("1.0", "end")
        self.output.config(state="disabled")

    def insert_symbol(self, symbol):
        # Insert the symbol at the current cursor position in the editor
        cursor_pos = self.editor.index(tk.INSERT)
        self.editor.insert(cursor_pos, symbol)
        self.highlight_syntax()

    


    