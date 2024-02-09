import tkinter as tk
import requests
from bs4 import BeautifulSoup

def scrape():
    url = entry.get()
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for link in soup.find_all('a'):
        listbox.insert(tk.END, link.get('href'))

root = tk.Tk()
root.title("Web Scraper")

label = tk.Label(root, text="Enter URL:")
entry = tk.Entry(root)
button = tk.Button(root, text="Scrape", command=scrape)
listbox = tk.Listbox(root)

label.pack(pady=10)
entry.pack(pady=10)
button.pack(pady=10)
listbox.pack(fill=tk.BOTH, expand=True)

root.mainloop()
