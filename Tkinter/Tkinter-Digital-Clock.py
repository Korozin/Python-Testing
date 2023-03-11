import tkinter as tk
from PIL import Image, ImageTk
import base64
import io
import time

# Define the mapping between characters and Base64 data
image_map = {
    '0': 'iVBORw0KGgoAAAANSUhEUgAAACgAAAA5CAAAAABhHzaPAAABRUlEQVR4nO3WPUsDQRAG4OFQ3DNG0mkThTRpr7DwJ/gT9FBr7QIWGkUbhVjYiCBYWWqTVryDQGy1CIqFlVUQwYOggjbqaxHc+8jMrn0y3TIPc7vDsbNElhhKrXL7z2DDL7/sDsdu/J5n6KgaEDganggOx04bwIrexpMEZ+YA4FpXVPMXX5y7o3MAaP+50vYUTa7d9sJK4TMFPfw0Fke53swiAwG8HZmhPnp+wdx4x5wewP6GB0y2FaSWHgBU2ToqyP64m8IXVZCA7hW2xL2pMJHMLYmOyPUNSSmMFVVc0W2KZyFSYZz0xO5kTu0BwIboMhDrjBu57L0pEDGQuylsMYB9CN/PzLA7t9E8rX/Yq5Z2pqlYfbDPQhpbbnz/Z7rmX83z+kZXrEuw+wJY1XDiUYAdVQPCRAsLhxEv/XK0l3il2PtH9AufsbBB2W5l4gAAAABJRU5ErkJggg==',
    '1': 'iVBORw0KGgoAAAANSUhEUgAAAA4AAAA3CAAAAAAZViRoAAAAoElEQVR4nN2SMQoCMRBFn2kshIjd1laWNnsfxVIsF/QqXkDEe7ii7XoLsbf6FrLJTMAD6O9ePj8zkwkAVN16QFYjHQ12kpaJakm6AgSABcC0N4dPSXr07mySYgEwNQJOf4AAo3MaH4DYOiS2DokX7W1+vLNrKBW31vVZf7OvW3Q1l9vR94l+FeWPij/5Oni7lqRb5k7SKmMjncyzV/fNh940XFMUAfJoRQAAAABJRU5ErkJggg==',
    '2': 'iVBORw0KGgoAAAANSUhEUgAAACgAAAA4CAAAAACqQ+UqAAABL0lEQVR4nGNgIABYUHjcHS/+YwVR6q+bWRHq+K5gV/b/PUf7//87meAKZ+JQ938a05P///9nwJ3xDJdCE4//////PwU3kSNi2x9s6i4xrPj/////J8jekSi+iKmwQOA7hkLswOI/XCETIbUwMKpwVCH5CvED9h1EJlwGjp1EKmTg2ImukHEqltz1M4CBY9f/ahR1M7Dm198hDJxRKOrm4MjZvyOhKpgYGBgYuGMZcbkRRYLzwP8qRuzFyu8QZIUG////r8TqmV8BDOgK/1cQEVYG//////+/nFiFb/ArGgrpcVThQCn8vJywYoP///bFchFhqlKdPINs5Q1seWYPqkqeuL1/sefWfwrI6ng/4sjU////b0AxcS1uhQ9QMrb4PdwqXVCMFJj4BpfCZVAlACUE5XxbU4GgAAAAAElFTkSuQmCC',
    '3': 'iVBORw0KGgoAAAANSUhEUgAAACgAAAA5CAAAAABhHzaPAAABGElEQVR4nGNgIABYUHhc7c//YwVR6q+bWRHq+C5jV/b/PUf7//87meAKZ+JQ938a05P///9nwJ3xDJdCE4//////PwU3kSNi2x9s6i4xrPj/////J8jekSi+iKmwQOA7hkLswOI/XCETIbUwMKpwVCH5CvED9h1EJlwGjp1EKmTg2ImukHEqltz1M4CBY9f/ahR1M7Dm198hDJxRKOrm4MjZvyOhKqDBw4jLjYwMHFGoAtiLld8hHLv+VxH2zK8ATF/jDh1iFBIdM6NFyqjCgVEoW3kDS1144weqap64vX+xZS302pX3I45MDa2vT8NNXItLIaQFkAlXKH4Ph8L3HO3//+9C8rDAxDfYVUapv2lBaqXgA7B2DwD8MeeVTDdIdwAAAABJRU5ErkJggg==',
    '4': 'iVBORw0KGgoAAAANSUhEUgAAACgAAAA3CAAAAABbFVf/AAABDklEQVR4nO2VsU4CQRBAZwmVicTFnt4QAqUNv2AobIwfoD+gVHwDSkKiiRRqSeJHYClXGI2Nlja2FiZK8Szgjl2ZPdb+XjV783b25pK5Fcmn9nS0xljQg5so8RU4SBf1u71ywGsDTNJVCz76TVUcAbw7InCveBufmVjKHu4oYmMzC0tKeolZhvmiQyEWYo54rWRfEm/ZAjhT69jp31E4D5xoE0esPDIQM2SV747YhEG2bftEzIXiwWxfql1nIMRcqR7M0ulfdO1u8jBiT72kuQwc7b2jiOjN/HTs1Ok6hy3vO4apPBAn7qL8e9ZQiIX4T5HYMupdqPE1ji3ZDt27K7wBhzFiD26jzq49H8+DX5kQ20GdRTRHAAAAAElFTkSuQmCC',
    '5': 'iVBORw0KGgoAAAANSUhEUgAAACgAAAA4CAAAAACqQ+UqAAABMUlEQVR4nGNgYGBgYODuePEfB1jGgAT4ruBS9v+/C7LCmbjVPWCEqmFiYGBg8WXACRb8R+ZxRGz7g93AfwrI6pRq5Rgkii9iU7gHxXiD///2xnDhth5J4f///z9NJlLh/zf4FTERYeOowhGrsIewYoP/////ryTCVIP///9XEWM958H/1QyMU7FkmZ8BqCq5YxkYZ2DNhb9D0AxlnIOjAPgdCVUB9TUjAw7AyMARhSqAvVj5HcKxC82jWD3zK4Bj5///T4gIEI6d/4lSyL7jP3EKLf7DFQ6KZDaqcKQolK28gZkTCm78QFXNE7f3L7asdYlhBUoK5/2II1P/N/H4/////9NwE9fiUjiN6cn///8z4QrF7+NQ+J6j/f//XUgeFpj0FrvKKPU3LazEBQsLlAYAnXzHEEnlnkAAAAAASUVORK5CYII=',
    '6': 'iVBORw0KGgoAAAANSUhEUgAAACgAAAA4CAAAAACqQ+UqAAABV0lEQVR4nO3Uvy8DYRgH8O97qTiKdGPxI12sNxj8AQaLpEMHGuw2iYGrMEkYLCKERMKEpWujjSY1m4jBJIYOhksECeHo16C5e699396NTfTZLvnk+9z75H1eAADiW0/U1Cmk6rvTMXJChod69yhqxgAQm4K2Tih/mdP5b3VgdUR2ybUhDCzdqOBlIN5itTTbrW8vQZKvuxEhnebIiNCxDf8t3A7HFknaEVItktko7buuuAqxp1iZz1RQxucgDpRb6KbrQsWR5gFwZ2rC+EsU0JSAmfH/scysUD8rbtos+ge1SNrKw3ylzAJZkSFXlJ3NAushlxWu84KNUPUAjNODLXHN2rBF4dtZcxgDALB8nHsPT02uD2PQvm/chMXER+Diome+9KNarVucB2Dvi2apOTZJktdeYk4H940KyQUP9j9o4LO5SRalESZ2HLXMjDobHeHj8OcH/AKVPugrvHPQGgAAAABJRU5ErkJggg==',
    '7': 'iVBORw0KGgoAAAANSUhEUgAAACgAAAA4CAAAAACqQ+UqAAABDklEQVR4nGNgIABYUHjcHS/+YwVR6q+bWRHq+K5gV/b/PUf7//87meAKZ+JQ938a05P///9nwJ3xDJdCE4//////PwU3kSNi2x9s6i4xrPj/////JzB1SrVyDBLFFzEVFgh8R1Fo8P/f3hgubGFj8R9N4f///z9Nxq8Q7nXeSPwBz4RfelThyFbYg0X2/E4UrsH/////V2I1h2MnesKtwmEjx04khZwH/1fjdBvHLiRJ7lic6hgYOKPwSJIFBMsYiVN39v8kotSdQfI1HiBw5j9RCvlO/ydOIbaSghAYVTiqkESF/4k1husTkenx22pijbT9/////8PEqLzz////aGIU1v7/v5gou+WuQFsUAKPHAsVUX3zJAAAAAElFTkSuQmCC',
    '8': 'iVBORw0KGgoAAAANSUhEUgAAACgAAAA5CAAAAABhHzaPAAABb0lEQVR4nO2WvUsDQRDF5w7FjTGSThsV0qS9wsI/wTJFCj3UWjvBQpOgjUIsbEQUBcFSm7TiBQKx1UIUCyurIIIHQQVFT30WZ/Y+Mntnn0y37O/e7gz3ZpYoJnoCq+TmI9gws0/rvR43eMtjaIoyYOkSPFBw2NMbAOblNR5U4PgkAFxIRTF1+sVxN3QCAI0Wl1kdpeGl63ZwMf0eAA381Gb6udpMIAQCeNmJBmXqqenowuvR212ws8EtZvfKCiwNACiwOsIK/7hFxYnC8oGJc5RI22Xc9ZEjUUVJfpacJW2f9auTp4TpP0E7VDjbaTlEdxU1xRVJI+EpJuooanxbcfKi6iVqACiwyXzmAlkbALDyzzoCywzXd9beKWAzINcp4qILdiD4ehwNunMb9aPKW7xqZm2MRgp37U4Iz0IamKt9c9YKT9fUs8LUf/P6UipWVKD7AliQ4NC9AmyKMlD1lTC9bfOkmbU3fK+U+PoR/QKQuCBuN9cV9AAAAABJRU5ErkJggg==',
    '9': 'iVBORw0KGgoAAAANSUhEUgAAACgAAAA5CAAAAABhHzaPAAABTUlEQVR4nGNgIABYUHjcHS/+YwVR6q+bWRHq+K5gV/b/PUf7//87meAKZ+JQ938a05P///9nwJ3xDJdCE4//////PwU3kSNi2x9s6i4xrPj/////JzB1SrVyDBLFFzEVFgh8R1Fo8P/f3hgubGFj8R9N4f///z9Nxq8Q7nXeSPwBz4RfelThyFbYg0X2/E4UrsH/////V2I1h2MnesKtwmEjx04khZwH/1czME7Fkrt+BjBw7PpfDdfGHcvAOANrfv0dwsAZhWwD4xwcOfs3LIdAfc2Iw4kMjAwcUagC2IuV3yEcu9A8itUzvwJQfI0HoIYjbsC+4z9xCrGVFITAqMJRhZQrlK28gZkTCm78QFXNE7f3L7ashV678n7Ekamh9fVpuIlrcSmEtAAy4QrF7+NQ+J6j/f//XUgeFpj0FrvKKPU3LUitFHwA1u4BAJj2/0SbhEtjAAAAAElFTkSuQmCC',
    ':': 'iVBORw0KGgoAAAANSUhEUgAAAA4AAAArCAAAAABtQuaIAAAAJUlEQVR4nGNgYGAw+P//////bxgYGBiYGFAAJdxRQACMBjsMAACOhQxD5ISQsgAAAABJRU5ErkJggg==',
    'A': 'iVBORw0KGgoAAAANSUhEUgAAACgAAAA4CAAAAACqQ+UqAAABYUlEQVR4nO3Wu0vDUBQG8JNgIbUYG3Rw6uDi2sHBxd2xQwetujsKoqClk4MOilVRFAQHl4K7EKGDCA5a8dWxYxGhgqCgaMTPxd7m8SX9A+zdDueX++KeQ0TajC5PlFh9Ah25ocZyrOXMKmd4MVYAW1dwP8RhV68DmFHbeAyDw2MAcKlmNMZPvpm7lxIA1JtusJCSgbm7IJxNfnhgGj/lqW52NyPwQQCv29FQHb1nIvri9eh0B/5vuEayN7YnTAPAIp3HsP0PdylkRcN2wfgZ8qLtkOr6zIhxirz6LDEt2h6tVycr8Zx7Be0gpLKdZoXoIiJ981rIFkUTa0ElzVts6rytOFnrGlvuUxfpYb4yVsVf1xt05WQl0ACwTpx5FewUeCaQdYp2owM7MAKCZMHgBYEPbwQeEvh+7An7HQCNGIEyCgDnKiwBKDInUgMw2ZqyBqQ5LABHrrC3WOZOUtW/P4pfFRiWHF/zRIoAAAAASUVORK5CYII=',
    'P': 'iVBORw0KGgoAAAANSUhEUgAAACgAAAA3CAAAAABbFVf/AAABKklEQVR4nO3UP0vDQBgG8OcCFfrPQtNVBz/BTaUfo4OLoPgpHGzxGyi2aKCFglM33Rx0SNHFNZ3EwdHNTkIHDfRxaexdvGtuVNp3O+539+QNeQMAkpa6y0MrK2RYcIR8KCXIAzCdwlZC5NRl6XA0M0cXL283Fm7nZBtbrZff7r4QkIqUnIX7+mPPq06qUpLkx4UBNkiS10kzAIDynrWjhgazag1XEZ4adp8jbSlJ8th4TzUi+abCliWxGikw/8g2RGAYrs8m/DGDn2PFA4iecQzjXfhtoSSIgeUPECcT4gGAf6Qe0krb2Byz6/Vt0anX0zE289VEGvLcFp6GPHOFk+XoT3xma/jvIV3hkyu8yo6vxSTfc8uRB2ByA2AYZ9+I2ispHRxQ6YRZ5BvaBUS9PNMaoAAAAABJRU5ErkJggg==',
    'M': 'iVBORw0KGgoAAAANSUhEUgAAACgAAAA4CAAAAACqQ+UqAAABaUlEQVR4nO3Wv0sCcRjH8UdJOBPspMAmh5bWGxxaWlzqTwirvSUIoqDCqaGGImsQpCCiRWhqCQwcImgoo1+6OUoICg1BDkXvBvX09Dla2vI73YfndQ/fe/jecSK/rAFHCmxXUFd8vLrpa7tgQWe8GVuQ9dow7eJIecvAgr2NVzcYnQa4tTsaMxdfmnuWDEC55cYSERldfuqFS2bdAS2+c3OD2mwmsGFjTJ5YLHWyKCIioSkRkfq5dp8FQK0RogBUejp6tTu11Yf/Ee4o1YesI1oAa83gOGZiZJ0nHNZFhWJkO6D/ig27vVkESNvZuOwoBuY7NhIuwpGnnf1xl8eTcPHQ41IaXnFE0+FCq3YMPrLv1l5C9xy0ri0g6ebyXeNhT3VmvnuOsKu44B29sKbA/gegD/8YolTR4I0CX94VeKzAjzNHHPkEqj4FyiTAtR0z7q9hCZhttyyBpcMEnHbEoWROdxIpNP8ofgDeuUcHnVvZfAAAAABJRU5ErkJggg==',
    ' ': 'iVBORw0KGgoAAAANSUhEUgAAABUAAABBAQMAAAAExn00AAAAAXNSR0IB2cksfwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAANQTFRFAAAAp3o92gAAAAtJREFUeJxjYBgFAAEEAAGKFER8AAAAAElFTkSuQmCC'
}

class ClockApp:
    def __init__(self, master):
        self.master = master
        master.title("Clock App")
        
        # Load the images and create the labels
        self.image_labels = []
        for i in range(11):
            img = ImageTk.PhotoImage(Image.open(io.BytesIO(base64.b64decode(image_map[' ']))))
            label = tk.Label(master, image=img)
            label.configure(bg='black')
            label.image = img  # keep a reference to prevent garbage collection
            label.grid(row=0, column=i, padx=2)
            self.image_labels.append(label)

        # Update the clock every second
        self.update_clock()
        master.after(1000, self.update_clock)
        
    def update_clock(self):
        # Get the current time and format it
        current_time = time.strftime("%I:%M:%S %p")
        formatted_time = [image_map[char] for char in current_time]

        # Update the image labels
        for i, base64_data in enumerate(formatted_time):
            img = ImageTk.PhotoImage(Image.open(io.BytesIO(base64.b64decode(base64_data))))
            self.image_labels[i].configure(image=img)
            self.image_labels[i].image = img  # keep a reference to prevent garbage collection
    
        # Schedule the next update
        self.master.after(1000, self.update_clock)

root = tk.Tk()
root.configure(bg='black')
root.geometry("440x70")
app = ClockApp(root)
root.mainloop()