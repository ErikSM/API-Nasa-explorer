from tkinter import *

import webview
import webbrowser
import urllib.request


#  ----------------------------------------------------------------------------


#  --   [[[ Using webview ]]]


def page_url_in_tkinter(url_test):
    window_test = Tk()
    window_test.geometry("800x450")

    webview.create_window('Image Open in tkinter (webview)', url_test)
    webview.start()


url_image = "https://apod.nasa.gov/apod/image/2405/AuroraStartrails_chiragupreti1024.jpg"
#  page_url_in_tkinter(url_image)


#  ----------------------------------------------------------------------------


#  --   [[[ Using web browser(sample) ]]]


def url_open(url_test):
    root = Tk()
    root.title("URL open on browser (WebBrowsers)")
    root.geometry("400x50")
    root.config(bd=5)

    but = Button(root, text='open browser', command=lambda: webbrowser.open(url_test))
    but.pack()

    root.mainloop()


page_test = "https://api.nasa.gov/"
#  url_open(page_test)


#  ----------------------------------------------------------------------------


#  --   [[[ Using urllib ]]]


def save_image_from_url(url_test):

    response = urllib.request.urlopen(url_test)

    with open("AuroraStartrails_chiragupreti1024.jpg", "wb") as file:
        chunk_size = 4096
        while True:
            chunk = response.read(chunk_size)
            if not chunk:
                break
            file.write(chunk)


url_to_save = "https://apod.nasa.gov/apod/image/2405/AuroraStartrails_chiragupreti1024.jpg"
#  save_image_from_url(url_to_save)

