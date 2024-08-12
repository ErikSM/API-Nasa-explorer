from tkinter import *

import webview
import webbrowser
import urllib.request


#  ----------------------------------------------------------------------------


#  --   [[[ Using webview ]]]


def page_url_in_tkinter(url_test):

    webview.create_window('Image Open in tkinter (webview)', url_test)
    webview.start()


url_image = "https://apod.nasa.gov/apod/image/2405/AuroraStartrails_chiragupreti1024.jpg"
url_2 = "https://api.nasa.gov/neo/rest/v1/neo/2001221?api_key=NgtvBLp13upL4FK2z6qyWSRJNcJ3U1w4fJcokZmi"
url_3 = "https://api.nasa.gov/"  # slow
page_url_in_tkinter(url_2)


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
# url_open(page_test)


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
