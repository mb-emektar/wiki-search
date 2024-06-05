import tkinter as tk
from tkinter import messagebox
from PyTerrierSearch import PyTerrierSearch

# Load the PyTerrierSearch class
index_path = './indices/dpr-w100-small'
dataset_name = "irds:dpr-w100"
pt_search = PyTerrierSearch(index_path, dataset_name)

current_page = 1
total_results = 0
page_size = 10

def search(query_str):
    global total_results
    total_results = pt_search.search(query_str)
    return pt_search.get_page(current_page, page_size)

def update_results():
    result_text.delete(1.0, tk.END)

    if total_results:
        results = pt_search.get_page(current_page, page_size)
        for idx, result in enumerate(results):
            start_index = result_text.index(tk.END)

            result_text.insert(tk.END, f"Doc ID: {result['doc_id']}\n")
            result_text.insert(tk.END, f"Title: {result['title']}\n")
            result_text.insert(tk.END, f"Text: {result['text']}\n\n")

            end_index = result_text.index(tk.END)

            # Set background color for each line
            for line_idx in range(int(float(start_index)), int(float(end_index))):
                if line_idx % 2 == 0:
                    result_text.tag_configure("even", background="#ffffff")
                    result_text.tag_add("even", f"{line_idx}.0", f"{line_idx + 1}.0")
                else:
                    result_text.tag_configure("odd", background="#f0f0f0")
                    result_text.tag_add("odd", f"{line_idx}.0", f"{line_idx + 1}.0")

    else:
        result_text.insert(tk.END, "No results found.")

# Rest of the code remains the same


def on_search():
    global current_page
    query = search_entry.get()
    if not query:
        messagebox.showwarning("Input Error", "Please enter a search query.")
        return
    
    current_page = 1
    search(query)
    update_results()
    update_page_buttons()

def next_page():
    global current_page
    if current_page * page_size < total_results:
        current_page += 1
        update_results()
        update_page_buttons()

def previous_page():
    global current_page
    if current_page > 1:
        current_page -= 1
        update_results()
        update_page_buttons()

def update_page_buttons():
    next_button.config(state=tk.NORMAL if current_page * page_size < total_results else tk.DISABLED)
    prev_button.config(state=tk.NORMAL if current_page > 1 else tk.DISABLED)

root = tk.Tk()
root.title("BM25 Search Engine")

tk.Label(root, text="Enter your search query:").pack(pady=10)
search_entry = tk.Entry(root, width=50)
search_entry.pack(pady=10)
search_button = tk.Button(root, text="Search", command=on_search)
search_button.pack(pady=10)

result_text = tk.Text(root, wrap=tk.WORD, width=80, height=20)
result_text.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

prev_button = tk.Button(button_frame, text="Previous", command=previous_page)
prev_button.grid(row=0, column=0, padx=5)
next_button = tk.Button(button_frame, text="Next", command=next_page)
next_button.grid(row=0, column=1, padx=5)

update_page_buttons()

root.mainloop()
