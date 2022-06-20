from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet

main = Tk()
# Add image file
bg = PhotoImage(file="./src/assets/bkg.png")
btn = PhotoImage(file="./src/assets/btn2.png")


class Application(Frame):
    def __init__(self, file, key, master=None):
        Frame.__init__(self, master)
        self.file = file
        self.key = key
        main.geometry("700x500")
        main.config(bg="gray17")
        main.resizable(False, False)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # Show image using label
        label1 = Label(main, image=bg)
        label1.place(x=0, y=0)
        canvas = Canvas(
            main,
            width=600,
            height=400,
            bg="#120142",
            border="0",
            highlightthickness="0",
        )
        canvas.place(x=50, y=50)

        title = Label(
            main,
            text="File Encrypter",
            font=("Helvetica", 30),
            bg="#120142",
            fg="white",
            border=None,
        )
        title.place(x=230, y=80)
        self.setInputs()

    def setInputs(self):
        self.fileLb = Label(
            main,
            text="File path:",
            font=("Helvetica", 20),
            bg="#120142",
            fg="white",
            border=None,
        )
        self.fileLb.place(x=130, y=180)
        self.file = Text(main, borderwidth=0, highlightthickness=0, width=35, height=2)
        self.file.place(x=260, y=185)
        self.keyLb = Label(
            main,
            text="Key path:",
            font=("Helvetica", 20),
            bg="#120142",
            fg="white",
            border=None,
        )
        self.keyLb.place(x=130, y=270)
        self.key = Text(main, borderwidth=0, highlightthickness=0, width=35, height=2)
        self.key.place(x=260, y=275)
        self.submit = Button(
            main,
            image=btn,
            text="Submit",
            command=self.submit,
            borderwidth=0,
            highlightthickness=0,
        )
        self.submit.place(x=370, y=350)

    def submit(self):
        if self.file.get("1.0", "end-1c") != "" and self.key.get("1.0", "end-1c") == "":
            key = Fernet.generate_key()
            with open("key.key", "wb") as key_file:
                key_file.write(key)
                print("FILE: ", self.file.get("1.0", "end-1c"))
            with open(self.file.get("1.0", "end-1c"), "rb") as file_to_encrypt:
                file_data = file_to_encrypt.read()
                encrypted_file = Fernet(key).encrypt(file_data)
            with open(self.file.get("1.0", "end-1c"), "wb") as encrypted_file_to_write:
                encrypted_file_to_write.write(encrypted_file)
            messagebox.showinfo("Success", "Your file has been encrypted")
        elif (
            self.key.get("1.0", "end-1c") != "" and self.file.get("1.0", "end-1c") != ""
        ):
            with open(self.key.get("1.0", "end-1c"), "rb") as key_file:
                key = key_file.read()
            with open(self.file.get("1.0", "end-1c"), "rb") as file_to_decrypt:
                file_data = file_to_decrypt.read()
                decrypted_file = Fernet(key).decrypt(file_data)
            with open(self.file.get("1.0", "end-1c"), "wb") as decrypted_file_to_write:
                decrypted_file_to_write.write(decrypted_file)
            messagebox.showinfo("Success", "Your file has been decrypted")
        else:
            messagebox.showerror("Error", "Please fill in one of the fields")


if __name__ == "__main__":
    file = ""
    key = ""
    app = Application(file, key)
    app.master.title("The Vault - Encrypt/Decrypt your files!")
    app.mainloop()
