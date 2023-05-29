import requests
from bs4 import BeautifulSoup as bs
from tkinter import *
from tkinter import ttk
from urllib.parse import urljoin, urlparse
from functools import partial
def is_valid(url):
    """
    Проверяем, является ли url действительным URL
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)
def get_all_images(url):
    """
    Возвращает все URL‑адреса изображений по одному `url`
    """
    soup = bs(requests.get(url).content, "html.parser")
    urls = []
    for img in soup.find_all("img"):
        img_url = img.attrs.get("src")
        if not img_url:
            continue

        img_url = urljoin(url, img_url)

        if is_valid(img_url):
            urls.append(img_url)
    with open('test.txt', 'w') as r:
       for i in urls:
           r.write("%s\n" % i)
           
    return urls

def new():
    '''
    проверяем, что находится в entry.get()
    '''
    if 'https://' or 'http://' in entry.get():
        brt = ttk.Button(text='Нажми ещё', command=partial(get_all_images, entry.get()))
        brt.pack(anchor=CENTER, padx=5, pady=5)
    
    
root = Tk()
root.title('Чоо, я рили сделал это сам!?')
root.geometry('600x300')
entry = ttk.Entry()
entry.pack(anchor=CENTER, padx=6, pady=3)

btn = Button(text='Нажми', command=new)
btn.pack(anchor=CENTER, padx=6, pady=3)

x = input('sos')
y = get_all_images(x)
print(y)
root.mainloop()