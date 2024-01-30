import argparse
from PIL import Image, ImageDraw, ImageTk
import tkinter as tk
from tkinter import ttk

def preview_image(image_path, cell_size, line_color):
    """Previews an image with lines dividing it into cells of the specified size."""

    image = Image.open(image_path)
    width, height = image.size

    num_cells_width = max(0, (width - 1) // cell_size)
    num_cells_height = max(0, (height - 1) // cell_size)
    remainder_width = width % cell_size
    remainder_height = height % cell_size

    draw = ImageDraw.Draw(image)
    for i in range(1, num_cells_height):
        draw.line([(0, i * cell_size), (width, i * cell_size)], fill=line_color, width=1)
    for j in range(1, num_cells_width):
        draw.line([(j * cell_size, 0), (j * cell_size, height)], fill=line_color, width=1)

    draw.line([(width - remainder_width, 0), (width, 0)], fill=line_color, width=1)
    draw.line([(0, height - remainder_height), (width, height - remainder_height)], fill=line_color, width=1)
    if remainder_width and remainder_height:
        draw.line([(width - remainder_width, height - remainder_height), (width, height)], fill=line_color, width=1)

    if remainder_width:
        draw.line([(width, 0), (width, height - remainder_height)], fill=line_color, width=1)

    root = tk.Tk()
    root.title("Image Preview")

    root.geometry("%dx%d" % (width, height))

    image_tk = ImageTk.PhotoImage(image)
    label = ttk.Label(root, image=image_tk)
    label.pack()

    root.mainloop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Preview an image with cell divisions")
    parser.add_argument("image_path", type=str, help="Path to the image file")
    parser.add_argument("--cell_size", type=int, default=100, help="Size of each cell (default: 100 pixels)")
    parser.add_argument("--linecolor", type=str, choices=["white", "black"], default="black", help="Color of the split lines (default: black)")

    args = parser.parse_args()

    preview_image(args.image_path, args.cell_size, args.linecolor)
