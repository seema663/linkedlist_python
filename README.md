# Codon to Amino Acid Mapping Using Linked List with Visualization

## Project Overview
This project is a Python program that maps an **mRNA codon** to its corresponding **amino acid** using a **linked list data structure**. It also provides a **visual representation** of how the linked list is traversed to find the amino acid. This helps in understanding both **bioinformatics concepts** and **data structures** in computer science.

---

## Features
- Input a **3-letter mRNA codon** (A, U, G, C only).  
- **Validation** for correct codon format.  
- **Linked list traversal** to find the amino acid.  
- **GUI visualization** using Tkinter:
  - Nodes representing amino acids and their codons.
  - Highlights nodes sequentially during traversal.
  - Shows which node matches the input codon (green) or displays "not found" (red).

---

## How it Works
1. Each amino acid is stored as a **node** with its corresponding codons.  
2. The program **traverses the linked list**, checking if the input codon exists in any node.  
3. Visualization highlights nodes to show the **internal working of traversal**.  
4. Outputs the amino acid if found or an error message if the codon is invalid or not present.

---

## Requirements
- Python 3.x
- Tkinter (usually included with Python)
- IDE or terminal for running Python scripts

---

## How to Run
1. Clone or download the repository.  
2. Open terminal or command prompt in the project folder.  
3. Run the Python script:

```bash
python codon_visual.py
