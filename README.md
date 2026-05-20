# 🧮 Python Calculator — CLI + Web App
**Assignment:** Python Project  
**Name:** Jammala Saitagore  
**App No:** 1406  
**Section:** 4

---

## 📌 Overview
A calculator built entirely in Python, available in **two versions**:
- **CLI Version** (`calculator.py`) — runs in the terminal using an infinite loop
- **Web Version** (`calculator_app.py`) — interactive browser UI built with **Streamlit**

Both versions share the same core logic: five arithmetic operations, custom input validation, calculation history, and the ability to reuse previous results.

---

## ✨ Features

| Feature | Description |
|---|---|
| ➕ Arithmetic Operations | Addition, Subtraction, Multiplication, Modulus, Exponentiation |
| 🔍 Input Validation | Custom `check()` function — handles decimals, negatives, empty input |
| 🔁 Reuse Previous Result | Type `p` instead of a number to use the last result |
| 📜 History Tracking | All results stored and viewable anytime |
| 🗑️ Clear History | Wipe history with a single click / command |
| 🌐 Web Interface | Streamlit UI with dropdowns, text inputs, and live result display |
| 🔂 Infinite Loop (CLI) | Keeps running until the user chooses to exit |
| 🚪 Graceful Exit (CLI) | Quit cleanly using `q` or `Q` |

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Web Framework:** Streamlit
- **Key Python Features Used:**
  - `match / case` — Python 3.10+ structural pattern matching
  - `st.session_state` — persistent state across Streamlit reruns
  - `input()` / `print()` — standard I/O (CLI version)
  - `list` — for dynamic history storage
  - Custom validation logic (no `float()` conversion before checking)

---

## 🚀 How to Run

### ▶ Web Version (Streamlit)
```bash
pip install streamlit
streamlit run calculator_app.py
```
Opens automatically at `http://localhost:8501`

### ▶ CLI Version (Terminal)
```bash
python calculator.py
```

> Requires Python 3.10 or higher (for `match/case` support).

---

## 📋 Commands

### Web Version
| UI Element | Description |
|---|---|
| Operator dropdown | Select `+` `−` `×` `%` `**` |
| First / Second number field | Enter a number or type `p` for previous result |
| CALCULATE button | Runs the operation and displays result |
| CLEAR button | Clears history and resets previous result |

### CLI Version
| Command | Where to Use | Description |
|---|---|---|
| `+` `-` `*` `%` `**` | Operator prompt | Choose arithmetic operation |
| `p` | Number prompt | Use the previous result as input |
| `h` | Operator prompt | View full calculation history |
| `c` | Operator prompt | Clear calculation history |
| `q` / `Q` | Operator prompt | Quit the calculator |

---

## 💻 Sample Output

### CLI
```
=== calculator ===
operations: +  -  *  %  **
type 'p' to use previous result while entering numbers
type 'h' to view history
type 'c' to clear history
type 'q' to quit
enter operator: +
enter first number: 45
enter second number: 55
Result: 100.0
enter operator: **
enter first number: p
enter second number: 3
Result: 1000000.0
enter operator: h
history: [100.0, 1000000.0]
enter operator: q
exit
```

### Web Version
- Select operator from dropdown (e.g. `×`)
- Enter numbers or type `p` to reuse previous result
- Click **CALCULATE** → result appears at top
- History panel shows all past calculations with expressions (e.g. `5 × prev(100) = 500`)

---

## 🔐 Input Validation Logic

The custom `check(n)` function validates user input **without** relying on `float()` or `try/except`. It:
- Rejects empty strings
- Allows one leading `-` for negative numbers
- Allows at most one `.` for decimal numbers
- Rejects any non-numeric characters

```python
def check(n):
    if n == "":
        return False
    dot = 0
    i = 0
    if n[0] == "-":
        if len(n) == 1:
            return False
        i = 1
    for j in range(i, len(n)):
        if n[j] == ".":
            dot += 1
            if dot > 1:
                return False
        elif n[j] < "0" or n[j] > "9":
            return False
    return True
```

---

## ⚠️ Edge Cases Handled

- Division / modulus by zero → shows error, continues
- Invalid operator → shows error, re-prompts
- Invalid number input → shows error, re-prompts
- `p` used before any calculation exists → shows error
- Single `-` entered as number → rejected as invalid
- Empty input → rejected as invalid

---

## 📁 Project Structure

```
📦 Python_project_Assignment
 ┣ 📄 calculator.py          # CLI version (terminal-based)
 ┣ 📄 calculator_app.py      # Web version (Streamlit)
 ┗ 📄 README.md              # Project documentation
```

---

## 👤 Author
**Jammala Saitagore**  
App No: `1406` | Section: `4`  
Python Programming Assignment — CSE Department
