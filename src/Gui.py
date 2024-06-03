import tkinter as tk
from tkinter import messagebox
import os

def search(query_str):
    '''
    ix = open_dir("indexdir")
    with ix.searcher(weighting=scoring.BM25F()) as searcher:
        query = QueryParser("content", ix.schema).parse(query_str)
        results = searcher.search(query, limit=10)
        return [result['content'] for result in results]
	'''
    return ["Result 1", "Result 2", "Result 3", "Result 2", "Result 3", "Result 2", "Result 3", "Result 2", "Result 3", "Result 2", "Result 3", "Result 2", "Result 3"]

def on_search():
    query = search_entry.get()
    if not query:
        messagebox.showwarning("Input Error", "Please enter a search query.")
        return
    
    results = search(query)
    result_text.delete(1.0, tk.END)
    if results:
        for result in results:
            result_text.insert(tk.END, result + "\n\n")
    else:
        result_text.insert(tk.END, "No results found.")


root = tk.Tk()
root.title("BM25 Search Engine")

tk.Label(root, text="Enter your search query:").pack(pady=10)
search_entry = tk.Entry(root, width=50)
search_entry.pack(pady=10)
search_button = tk.Button(root, text="Search", command=on_search)
search_button.pack(pady=10)

result_text = tk.Text(root, wrap=tk.WORD, width=80, height=20)
result_text.pack(pady=10)

root.mainloop()