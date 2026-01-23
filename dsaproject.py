
import tkinter as tk

#  LINKED LIST CLASSES


class Node:
   def __init__(self, amino_acid, codons):
       self.amino_acid = amino_acid
       self.codons = codons
       self.next = None


class LinkedList:
   def __init__(self):
       self.head = None


   def add(self, amino_acid, codons):
       new_node = Node(amino_acid, codons)
       if self.head is None:
           self.head = new_node
           return
       temp = self.head
       while temp.next:
           temp = temp.next
       temp.next = new_node


   # Logic: find amino acid
   def find_amino_acid(self, codon):
       temp = self.head
       while temp:
           if codon in temp.codons:
               return temp.amino_acid
           temp = temp.next
       return None


# Codon validation
def is_valid_codon(codon):
   if len(codon) != 3:
       return False
   for ch in codon:
       if ch not in ['A','U','G','C']:
           return False
   return True


# GUI + VISUALIZATION


class CodonApp:
   def __init__(self):
       self.ll = LinkedList()
       # Add amino acids and codons
       self.ll.add("Methionine", ["AUG"])
       self.ll.add("Phenylalanine", ["UUU", "UUC"])
       self.ll.add("Lysine", ["AAA", "AAG"])
       self.ll.add("Alanine", ["GCU", "GCC", "GCA", "GCG"])
       self.ll.add("Serine", ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"])
       self.ll.add("Tyrosine", ["UAU", "UAC"])
       self.ll.add("Stop", ["UAA", "UAG", "UGA"])
       self.ll.add("Glycine", ["GGU", "GGC", "GGA", "GGG"])
       self.ll.add("Valine", ["GUU", "GUC", "GUA", "GUG"])
       self.ll.add("Leucine", ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"])
       self.ll.add("Proline", ["CCU", "CCC", "CCA", "CCG"])
       self.ll.add("Threonine", ["ACU", "ACC", "ACA", "ACG"])
       self.ll.add("Arginine", ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"])
       self.ll.add("Histidine", ["CAU", "CAC"])
       self.ll.add("Glutamine", ["CAA", "CAG"])
       self.ll.add("Asparagine", ["AAU", "AAC"])
       self.ll.add("Glutamic Acid", ["GAA", "GAG"])
       self.ll.add("Aspartic Acid", ["GAU", "GAC"])
       self.ll.add("Cysteine", ["UGU", "UGC"])
       self.ll.add("Tryptophan", ["UGG"]) 
       self.ll.add("Isoleucine", ["AUU", "AUC", "AUA"])
      






       # Tkinter window
       self.root = tk.Tk()
       self.root.title("Codon to Amino Acid Visualizer")
       self.root.geometry("1500x1500")


       # Input label & entry
       tk.Label(self.root, text="Enter an mRNA codon (A, U, G, C):", font=("Arial", 12)).pack(pady=10)
       self.codon_entry = tk.Entry(self.root, font=("Arial", 12))
       self.codon_entry.pack(pady=5)


       # Reusable status label (prevents creating many labels on invalid input)
       self.status_label = tk.Label(self.root, text="", font=("Arial", 12))
       self.status_label.pack(pady=5)


       # Submit button
       tk.Button(self.root, text="Check Codon", command=self.start_visualization, font=("Arial", 12)).pack(pady=10)


       # Canvas for linked list
       self.canvas = tk.Canvas(self.root, width=1000, height=250, bg="white")
       self.canvas.pack(pady=20)


       self.nodes_ui = []
       self.node_list = []
       self.node_positions = []
       self.total_width = 0
       self.current_index = 0
       self.found = False


       self.draw_linked_list()
       self.root.mainloop()


   # Draw linked list nodes
   def draw_linked_list(self):
       x = 50
       y = 50
       w = 180
       h = 80
       temp = self.ll.head
       while temp:
           box = self.canvas.create_rectangle(x, y, x+w, y+h, fill="lightblue")
           text1 = self.canvas.create_text(x+w/2, y+25, text=temp.amino_acid, font=("Arial", 10, "bold"))
           text2 = self.canvas.create_text(x+w/2, y+50, text=", ".join(temp.codons), font=("Arial", 9))
           self.nodes_ui.append(box)
           self.node_list.append(temp)
           # store center x for sliding calculations
           self.node_positions.append(x + w/2)
           if temp.next:
               self.canvas.create_line(x+w, y+h/2, x+w+40, y+h/2, arrow=tk.LAST)
           x += w + 40
           temp = temp.next
       # set total width and scrollregion so canvas can be scrolled/shifted
       self.total_width = x
       self.canvas.config(scrollregion=(0, 0, self.total_width, y + h + 20))


   # Start the traversal visualization
   def start_visualization(self):
       self.codon = self.codon_entry.get().upper()
       if not is_valid_codon(self.codon):
           self.canvas.delete("all")
           self.status_label.config(text="Invalid codon! Must be 3 letters A, U, G, C.", fg="red")
           return
       # Reset variables for new traversal
       self.current_index = 0
       self.found = False
       # Clear canvas and redraw nodes
       self.canvas.delete("all")
       self.nodes_ui = []
       self.node_list = []
       self.node_positions = []
       self.total_width = 0
       self.draw_linked_list()
       # ensure view starts at left
       try:
           self.canvas.xview_moveto(0)
       except Exception:
           pass
       self.root.after(500, self.traverse_step)


   # Traverse nodes one by one
   def traverse_step(self):
       if self.current_index < len(self.node_list):
           box = self.nodes_ui[self.current_index]
           node = self.node_list[self.current_index]


           # Slide to the node, then highlight it
           self.slide_to_node(self.current_index)
           self.canvas.itemconfig(box, fill="yellow")


           if self.codon in node.codons:
               # Found match
               self.canvas.itemconfig(box, fill="lightgreen")
               self.canvas.create_text(500, 200, text=f"Codon {self.codon} codes for {node.amino_acid}",
                                       font=("Arial", 14, "bold"), fill="green")
               self.found = True
               return
           else:
               # Reset node color
               self.canvas.itemconfig(box, fill="lightblue")


           self.current_index += 1
           self.root.after(1000, self.traverse_step)
       else:
           if not self.found:
               self.canvas.create_text(500, 200, text="This codon does not code for any amino acid",
                                       font=("Arial", 14, "bold"), fill="red")


   # Smoothly slide the canvas so the node at `index` is centered (when possible)
   def slide_to_node(self, index, steps=10, delay=20):
       if not self.node_positions or self.total_width <= int(self.canvas['width']):
           return
       target_x = self.node_positions[index]
       visible_w = int(self.canvas['width'])
       max_scroll = max(1, self.total_width - visible_w)
       # compute left coordinate so target_x is centered
       target_left = max(0, min(target_x - visible_w/2, max_scroll))
       target_frac = target_left / max_scroll


       try:
           current_frac = self.canvas.xview()[0]
       except Exception:
           current_frac = 0.0


       delta = (target_frac - current_frac) / max(1, steps)


       def step(i, cur):
           if i >= steps:
               self.canvas.xview_moveto(max(0.0, min(1.0, target_frac)))
               return
           self.canvas.xview_moveto(max(0.0, min(1.0, cur + delta)))
           self.root.after(delay, lambda: step(i+1, cur + delta))


       step(0, current_frac)




if __name__ == "__main__":
   CodonApp()
