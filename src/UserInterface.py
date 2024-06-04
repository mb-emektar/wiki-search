import tkinter as tk
from tkinter import messagebox
from PyTerrierSearch import PyTerrierSearch  # PyTerrierSearch sınıfını içe aktar

# PyTerrierSearch örneğini başlat
index_path = './indices/dpr-w100-small'
dataset_name = "irds:dpr-w100"
pt_search = PyTerrierSearch(index_path, dataset_name)

def search(query_str):
    '''
    PyTerrierSearch sınıfının search fonksiyonunu çağır ve sonuçları döndür
    '''
    return pt_search.search(query_str)

def on_search():
    query = search_entry.get()
    if not query:
        messagebox.showwarning("Input Error", "Please enter a search query.")
        return
    
    results = search(query)
    result_text.delete(1.0, tk.END)
    if results:
        for result in results:
            result_text.insert(tk.END, f"Doc ID: {result['doc_id']}\n")
            result_text.insert(tk.END, f"Title: {result['title']}\n")
            result_text.insert(tk.END, f"Text: {result['text']}\n\n")
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
