# Codechemy Compiler

**Codechemy Compiler** is designed to process programs written in *Codechemy*, a custom-built programming language. It first receives the language's grammar and simplifies it as needed. Then, it analyzes the source code using lexical and syntactic stages to verify its correctness or identify the exact location of any errors. The compiler supports three types of syntactic analysis: **LL1**, **SLR**, and **CLR**, allowing flexible parsing strategies.

<p align="center">
  <img width="750" alt="image" src="https://github.com/user-attachments/assets/3672b75b-6be7-4378-a1bf-56a369279d25" />
</p>

## How to Run the Project 🧩

To compile and test Codechemy programs, follow these steps:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/SebastianItamari/Codechemy-Compiler.git
cd Codechemy-Compiler
```

### 2️⃣ Choose a Grammar and Analyzer
Open the file `grammar_IDE_testing.py` and scroll to the last line:
```python
IDE = CodechemyIDE(grammar, "CLR")
```

You can replace `"CLR"` with any of the following supported parsers:
- `"LL1"` for top-down analysis
- `"SLR"` for simple LR parsing
- `"CLR"` for canonical LR parsing

### 3️⃣ Run the Compiler
From the root directory, execute:
```bash
python grammar_IDE_testing.py
```

If your system has multiple Python versions, you may need to use:
```bash
python3 grammar_IDE_testing.py
```

This will open the Codechemy IDE, where you can enter your code and analyze it using the compiler.

## Codechemy Syntax Guide 🧪

Codechemy is a symbolic language inspired by alchemy. Each instruction uses unique Unicode symbols to reflect its purpose. Below is a reference of core syntax elements:

### 🔰 Program Structure
| Symbol          | Meaning                   |
|----------------|----------------------------|
| 🜉<br>🝓           | Start and End of Program   |
| 🝳identifier🝳 🝑 Expression | Variable declaration         |

### 🔁 Control Structures
| Symbol Sequence               | Meaning         |
|------------------------------|-----------------|
| se ☾ Condition ☽<br>🜚<br>…<br>🜚         | `if` statement   |
| dum ☾ Condition ☽<br>🜚<br>…<br>🜚       | `while` loop     |
| por ☾ Assignment; Condition; Assignment ☽<br>🜚<br>…<br>🜚 | `for` loop       |

### 🖨️ Output Instruction
| Symbol          | Meaning           |
|----------------|--------------------|
| presi ☾ Term ☽     | Print to console   |

### ➗ Operators
**Arithmetic**:
| Symbol | Operation        |
|--------|------------------|
| 🜂     | Addition (`+`) |
| 🜄     | Subtraction (`-`)       |
| 🜁     | Multiplication (`*`)            |
| 🜃     | Division (`/`)    |

**Logical**:
| Symbol | Operation        |
|--------|------------------|
| �     | Equality (`==`)     |
| 🜍     | Inequality (`!=`)          |
| 🜕     | Less Than (`<`)        |
| 🜔     | Greater Than (`>`)          |
| 🜗     | Less or Equal (`<=`)       |
| 🜖     | Greater or Equal (`>=`)     |

## Result 📊
<p align="center">
  <img width="550" height="758" alt="image" src="https://github.com/user-attachments/assets/32c9f947-23db-404d-93a4-4d8c44296eba" />
</p>

## Authors 🧑‍💻
- [@GiulianaD](https://github.com/GiulianaD)
- [@delgadillolaura](https://github.com/delgadillolaura)
- [@SebastianItamari](https://github.com/SebastianItamari)
- [@gracetorrico](https://github.com/gracetorrico)
- [@Selwab](https://github.com/Selwab)
- [@ax8888](https://github.com/ax8888)
