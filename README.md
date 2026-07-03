# lcs-analyzer
# 🧬 LCS Analyzer

A Python desktop application for comparing biological sequences using the **Longest Common Subsequence (LCS)** algorithm. The application provides sequence comparison, similarity analysis, motif discovery, and a simple dot matrix visualization through an interactive graphical user interface.

---

## Features

- Select two biological sequences from a predefined dataset.
- Calculate the length of each sequence.
- Compute the Longest Common Subsequence (LCS) length.
- Generate the LCS string.
- Calculate similarity percentage between two sequences.
- Predict possible evolutionary relationship based on similarity.
- Find common motifs of a user-defined length.
- Display motif occurrence counts in both sequences.
- Visualize sequence matches using a miniature dot matrix.
- User-friendly graphical interface built with Tkinter.

---

## Technologies Used

- Python 3
- Tkinter
- Dynamic Programming
- Collections (Counter)

---

## Algorithm

The application uses the **Dynamic Programming** approach to solve the Longest Common Subsequence (LCS) problem.

### LCS Algorithm Steps

1. Read two selected biological sequences.
2. Construct a dynamic programming table.
3. Compare characters from both sequences.
4. Store the maximum LCS length at each position.
5. Backtrack through the table to reconstruct the LCS.
6. Calculate similarity percentage.
7. Search for common motifs.
8. Display the results through the graphical interface.

---

## Similarity Formula

```
Similarity (%) = (2 × LCS Length) / (Length of Sequence 1 + Length of Sequence 2) × 100
```

---

## Similarity Interpretation

| Similarity | Prediction |
|------------|------------|
| ≥ 80% | Likely shared a recent common ancestor |
| 50% – 79% | Possibly a distant common ancestor |
| < 50% | Unlikely to share a common ancestor |

---

## Input Format

The program reads biological sequences from an `input.txt` file.

Example:

```text
Human=ATGCTAGCTAGCTA
Chimpanzee=ATGCTGGCTAGCTA
Mouse=GTACCTAGGCTAAC
```

---

## Project Structure

```
LCS-Analyzer/
│
├── main.py
├── input.txt
├── README.md
└── screenshots/
```

---

## How to Run

1. Clone this repository.

```bash
git clone https://github.com/RokshanaARubi/LCS-Analyzer.git
```

2. Navigate to the project directory.

```bash
cd LCS-Analyzer
```

3. Run the application.

```bash
python lcs_app.py
```

---

## Application Workflow

1. Launch the application.
2. Select two sequences.
3. Calculate sequence lengths.
4. Calculate the LCS length.
5. Generate the LCS string.
6. Calculate similarity percentage.
7. View the evolutionary prediction.
8. Enter a motif length to identify common motifs.
9. View the dot matrix visualization.

---

## Screenshots

<img width="1617" height="1012" alt="image" src="https://github.com/user-attachments/assets/255bdbd1-7ba7-4d03-8f5b-9bdd7d65bbff" />


Example:

- Home Screen
- LCS Result
- Similarity Analysis
- Motif Finder
- Dot Matrix Visualization

---

## Learning Objectives

This project demonstrates the practical implementation of:

- Longest Common Subsequence (LCS)
- Dynamic Programming
- Sequence Comparison
- Motif Detection
- Similarity Analysis
- Bioinformatics Concepts
- GUI Development using Tkinter

---

## Author

Rokshana Akter Rubi

Bioinformatics Engineering
