import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk


# -------------------- Functions --------------------

def generate_qr():
    """Generate QR code from user input."""

    data = text_entry.get("1.0", tk.END).strip()

    if data == "":
        messagebox.showwarning(
            "Empty Input",
            "Please enter some text or a URL."
        )
        return

    try:
        # Create QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4
        )

        qr.add_data(data)
        qr.make(fit=True)

        # Create image
        qr_image = qr.make_image(
            fill_color="black",
            back_color="white"
        )

        # Store image
        global generated_image
        generated_image = qr_image

        # Resize image for preview
        preview_image = qr_image.resize(
            (250, 250)
        )

        # Convert for Tkinter
        global qr_photo
        qr_photo = ImageTk.PhotoImage(
            preview_image
        )

        # Display image
        qr_label.config(
            image=qr_photo,
            text=""
        )

        status_label.config(
            text="✅ QR Code generated successfully!"
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            f"Could not generate QR code:\n{e}"
        )


def save_qr():
    """Save generated QR code."""

    if generated_image is None:
        messagebox.showwarning(
            "No QR Code",
            "Please generate a QR code first."
        )
        return

    file_path = filedialog.asksaveasfilename(
        title="Save QR Code",
        defaultextension=".png",
        filetypes=[
            ("PNG Image", "*.png"),
            ("JPEG Image", "*.jpg"),
            ("All Files", "*.*")
        ]
    )

    if file_path:
        try:
            generated_image.save(
                file_path
            )

            messagebox.showinfo(
                "Saved",
                f"QR Code saved successfully!\n\n"
                f"{file_path}"
            )

            status_label.config(
                text="💾 QR Code saved successfully!"
            )

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Could not save QR code:\n{e}"
            )


def clear_all():
    """Clear input and QR code."""

    text_entry.delete(
        "1.0",
        tk.END
    )

    qr_label.config(
        image="",
        text="QR Code will appear here"
    )

    status_label.config(
        text=""
    )

    global generated_image
    generated_image = None


# -------------------- Main Window --------------------

root = tk.Tk()

root.title("QR Code Generator")

root.geometry("650x700")

root.resizable(
    False,
    False
)


# -------------------- Global Variable --------------------

generated_image = None
qr_photo = None


# -------------------- Title --------------------

title_label = tk.Label(
    root,
    text="📱 QR Code Generator",
    font=("Arial", 26, "bold")
)

title_label.pack(
    pady=20
)


subtitle_label = tk.Label(
    root,
    text="Enter text or a URL and generate your QR code",
    font=("Arial", 11)
)

subtitle_label.pack(
    pady=5
)


# -------------------- Input Label --------------------

input_label = tk.Label(
    root,
    text="Enter Text / URL:",
    font=("Arial", 12, "bold")
)

input_label.pack(
    pady=(20, 5)
)


# -------------------- Text Input --------------------

text_entry = tk.Text(
    root,
    width=55,
    height=5,
    font=("Arial", 11)
)

text_entry.pack(
    pady=5
)


# -------------------- Buttons --------------------

button_frame = tk.Frame(root)

button_frame.pack(
    pady=15
)


generate_button = tk.Button(
    button_frame,
    text="🔲 Generate QR",
    font=("Arial", 11, "bold"),
    width=18,
    command=generate_qr
)

generate_button.grid(
    row=0,
    column=0,
    padx=5
)


save_button = tk.Button(
    button_frame,
    text="💾 Save QR",
    font=("Arial", 11, "bold"),
    width=18,
    command=save_qr
)

save_button.grid(
    row=0,
    column=1,
    padx=5
)


clear_button = tk.Button(
    button_frame,
    text="🧹 Clear",
    font=("Arial", 11, "bold"),
    width=18,
    command=clear_all
)

clear_button.grid(
    row=0,
    column=2,
    padx=5
)


# -------------------- QR Preview --------------------

preview_title = tk.Label(
    root,
    text="QR Code Preview",
    font=("Arial", 13, "bold")
)

preview_title.pack(
    pady=(15, 5)
)


qr_label = tk.Label(
    root,
    text="QR Code will appear here",
    width=35,
    height=15,
    relief="solid",
    font=("Arial", 11)
)

qr_label.pack(
    pady=10
)


# -------------------- Status --------------------

status_label = tk.Label(
    root,
    text="",
    font=("Arial", 11)
)

status_label.pack(
    pady=10
)


# -------------------- Start Application --------------------

root.mainloop()