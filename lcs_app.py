import tkinter as tk
from tkinter import ttk, messagebox, END
from collections import Counter

class LCSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LCS Algorithm")
        self.root.geometry("1000x600")
        self.root.configure(bg="lightblue") 
        
        self.title_label = tk.Label(
            self.root, 
            text="LCS ANALYZER", 
            font=("Arial", 20,"bold"), 
            bg="white"
        )
        self.title_label.place(relx=0.5, y=20, anchor='n') 

        self.organism_map = self.read_sequences("input.txt")
        self.create_layout_frames()
        self.create_widgets()

    def read_sequences(self, filename):
        organism_map = {}
        try:
            with open(filename, 'r') as file:
                for line in file:
                    parts = line.strip().split('=', 1)
                    if len(parts) == 2:
                        organism_map[parts[0].strip()] = parts[1].strip()
        except FileNotFoundError:
            messagebox.showerror("Error", f"File '{filename}' not found!")
        return organism_map

    def create_layout_frames(self):
        self.left_frame = tk.Frame(self.root, bg="lavender", bd=2, relief="groove")
        self.left_frame.place(relx=0.05, rely=0.15, relwidth=0.9, relheight=0.8)

        # Frame for the dot matrix visualization
        self.right_frame = tk.Frame(self.root, bg="white", bd=2, relief="groove")
        self.right_frame.place(relx=0.6, rely=0.15, relwidth=0.35, relheight=0.8)

        # Canvas for the mini dot matrix
        self.dot_matrix_canvas = tk.Canvas(self.right_frame, width=300, height=300, bg="white")
        self.dot_matrix_canvas.pack()

    def create_widgets(self):
        container = self.left_frame

        label_seq1 = tk.Label(container, text="Sequence 1", font=("Arial", 12, "bold"), bg="white")
        label_seq1.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.combo_seq1 = ttk.Combobox(container, values=list(self.organism_map.keys()), font=("Arial", 12))
        self.combo_seq1.grid(row=0, column=1, padx=10, pady=10)

        label_seq2 = tk.Label(container, text="Sequence 2", font=("Arial", 12, "bold"), bg="white")
        label_seq2.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.combo_seq2 = ttk.Combobox(container, values=list(self.organism_map.keys()), font=("Arial", 12))
        self.combo_seq2.grid(row=1, column=1, padx=10, pady=10)

        self.add_button_and_entry(container, "Length S1", self.calculate_length_s1, 2)
        self.add_button_and_entry(container, "Length S2", self.calculate_length_s2, 3)
        self.add_button_and_entry(container, "LCS Length", self.calculate_lcs_length, 4)
        self.add_button_and_entry(container, "LCS String", self.calculate_lcs_string, 5)
        self.add_button_and_entry(container, "Similarity", self.calculate_similarity, 6)

        label_motif = tk.Label(container, text="Motif Length", font=("Arial", 12, "bold"), bg="white")
        label_motif.grid(row=7, column=0, padx=10, pady=10, sticky="e")
        self.text_motif_length = tk.Entry(container, font=("Arial", 12))
        self.text_motif_length.grid(row=7, column=1, padx=10, pady=10)

        motif_button = tk.Button(container, text="Find Motifs", font=("Arial", 12), command=self.find_common_motifs)
        motif_button.grid(row=8, column=0, columnspan=2, pady=10)

        self.label_ancestor = tk.Label(container, text="", font=("Arial", 12, "italic"), bg="lavender", fg="darkgreen")
        self.label_ancestor.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

    def add_button_and_entry(self, container, text, command, row):
        button = tk.Button(container, text=text, font=("Arial", 12), command=command)
        button.grid(row=row, column=0, padx=10, pady=10, sticky="e")
        entry = tk.Entry(container, font=("Arial", 12))
        entry.grid(row=row, column=1, padx=10, pady=10)
        setattr(self, f"text_{text.lower().replace(' ', '_')}", entry)

    def get_selected_sequences(self):
        seq1 = self.organism_map.get(self.combo_seq1.get(), "")
        seq2 = self.organism_map.get(self.combo_seq2.get(), "")
        if not seq1 or not seq2:
            messagebox.showerror("Error", "Please select valid sequences!")
            return None, None
        return seq1, seq2

    def draw_mini_dot_matrix(self, canvas, seq1, seq2, grid_size=30):
        canvas.delete("all")
        step1 = max(1, len(seq1) // grid_size)
        step2 = max(1, len(seq2) // grid_size)
        
        # Create the dot matrix based on sequence matches
        for i in range(grid_size):
            for j in range(grid_size):
                c1 = seq1[i * step1] if i * step1 < len(seq1) else ""
                c2 = seq2[j * step2] if j * step2 < len(seq2) else ""
                if c1 == c2 and c1 != "":
                    x = j * 10
                    y = i * 10
                    canvas.create_rectangle(x, y, x+8, y+8, fill="black")

    def calculate_length_s1(self):
        seq1, _ = self.get_selected_sequences()
        if seq1:
            self.text_length_s1.delete(0, END)
            self.text_length_s1.insert(0, str(len(seq1)))

    def calculate_length_s2(self):
        _, seq2 = self.get_selected_sequences()
        if seq2:
            self.text_length_s2.delete(0, END)
            self.text_length_s2.insert(0, str(len(seq2)))

    def calculate_lcs_length(self):
        seq1, seq2 = self.get_selected_sequences()
        if not seq1 or not seq2:
            return
        m, n = len(seq1), len(seq2)
        lcs_table = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if seq1[i - 1] == seq2[j - 1]:
                    lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
                else:
                    lcs_table[i][j] = max(lcs_table[i - 1][j], lcs_table[i][j - 1])
        self.text_lcs_length.delete(0, END)
        self.text_lcs_length.insert(0, str(lcs_table[m][n]))

    def calculate_lcs_string(self):
        seq1, seq2 = self.get_selected_sequences()
        if not seq1 or not seq2:
            return
        m, n = len(seq1), len(seq2)
        lcs_table = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if seq1[i - 1] == seq2[j - 1]:
                    lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
                else:
                    lcs_table[i][j] = max(lcs_table[i - 1][j], lcs_table[i][j - 1])
        lcs_string = []
        i, j = m, n
        while i > 0 and j > 0:
            if seq1[i - 1] == seq2[j - 1]:
                lcs_string.append(seq1[i - 1])
                i -= 1
                j -= 1
            elif lcs_table[i - 1][j] > lcs_table[i][j - 1]:
                i -= 1
            else:
                j -= 1
        lcs_string.reverse()
        self.text_lcs_string.delete(0, END)
        self.text_lcs_string.insert(0, "".join(lcs_string))
        
        # Draw the mini dot matrix
        self.draw_mini_dot_matrix(self.dot_matrix_canvas, seq1, seq2)

    def calculate_similarity(self):
        seq1, seq2 = self.get_selected_sequences()
        if not seq1 or not seq2:
            return
        try:
            lcs_length = int(self.text_lcs_length.get())
        except ValueError:
            messagebox.showerror("Error", "Please calculate LCS length first!")
            return
        similarity = (2.0 * lcs_length / (len(seq1) + len(seq2))) * 100
        self.text_similarity.delete(0, END)
        self.text_similarity.insert(0, f"{similarity:.2f}%")

        if similarity >= 80:
            prediction = "✅ Likely shared a recent common ancestor."
        elif similarity >= 50:
            prediction = "🟡 Possibly a distant common ancestor."
        else:
            prediction = "❌ Unlikely to share a common ancestor."
        
        self.label_ancestor.config(text=prediction)

    def find_common_motifs(self):
        seq1, seq2 = self.get_selected_sequences()
        if not seq1 or not seq2:
            return
        try:
            motif_length = int(self.text_motif_length.get())
            if motif_length <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive integer for motif length!")
            return
        def extract_motifs(sequence, k):
            return [sequence[i:i+k] for i in range(len(sequence) - k + 1)]
        motifs_seq1 = extract_motifs(seq1, motif_length)
        motifs_seq2 = extract_motifs(seq2, motif_length)
        counter1 = Counter(motifs_seq1)
        counter2 = Counter(motifs_seq2)
        common = set(counter1.keys()) & set(counter2.keys())
        if not common:
            messagebox.showinfo("Motif Finder", "No common motifs found.")
            return
        result_text = "Motif | Count in Seq1 | Count in Seq2\n"
        result_text += "-" * 35 + "\n"
        for motif in sorted(common):
            result_text += f"{motif: <6} | {counter1[motif]:^13} | {counter2[motif]:^13}\n"
        result_window = tk.Toplevel(self.root)
        result_window.title("Common Motifs")
        text_box = tk.Text(result_window, font=("Courier", 11))
        text_box.pack(expand=True, fill="both", padx=10, pady=10)
        text_box.insert("1.0", result_text)
        text_box.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = LCSApp(root)
    root.mainloop()
