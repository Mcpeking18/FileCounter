# 📂 Recursive File Finder

Ever had a folder containing dozens of subfolders, which contain even more subfolders, and somewhere deep inside are the files you actually care about? 🔍

This repository is a small journey through solving exactly that problem.

The scripts recursively scan directories, search for files with a chosen extension (currently configured for `.dwg`), and record their locations. While the project originated from organizing AutoCAD drawings, the same logic can be adapted to search for virtually any file type by changing the extension check.

Rather than presenting only the "best" solution, this repository documents the evolution of the code—from manually walking the directory tree to using Python's higher-level tools for cleaner and more maintainable implementations.

---

# 🛠️ The Files

### 1. `dwgcunt.py`

**The "let's build it ourselves" approach.** 🚶

No shortcuts. Uses only `os` and `os.path` along with a custom recursive function to navigate the directory tree. It's a great way to understand what actually happens behind the scenes when searching through nested folders. Results are written to separate text files.

---

### 2. `oswalk.py`

**Let Python do the walking.** 🚶‍♂️

Replaces the custom recursion with Python's built-in `os.walk()`. The code becomes noticeably shorter while producing the same results, allowing you to focus on processing files instead of traversing directories.

---

### 3. `oswalkpath.py`

**Paths become objects.** 🧩

Introduces `pathlib`, where file paths stop being plain strings and become proper objects. Using `Path.rglob()` makes recursive searching concise and removes much of the manual path manipulation required in earlier versions.

---

### 4. `pandaspath.py`

**Turning file paths into data.** 📊

Combines `pathlib` with `pandas` to generate a structured spreadsheet. Instead of dumping raw text, the script splits each path into useful metadata (Project, Department, Remaining Path, Filename) and exports everything into a CSV that's ready for filtering, sorting, or further analysis in Excel.

---

# 🚀 How to Use

1. Place the scripts in the directory containing your project folders.
2. Change the target file extension inside the script if needed (default is `.dwg`).
3. Run whichever implementation you'd like to explore.
4. If using `pandaspath.py`, install pandas first:

```bash
pip install pandas
```

---

# 💡 Why Four Versions?

Because sometimes the most valuable part of a project isn't just the final script—it's seeing how the solution evolves.

Each file demonstrates a different way to solve the same problem, showing the progression from manual recursion to modern Python tools. Whether you're learning recursion, comparing Python's filesystem APIs, or just looking for a quick file finder, there's something to take away from each version.

Happy exploring! 🎉
