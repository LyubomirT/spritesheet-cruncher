import argparse
from PIL import Image
import os
from colorizer import ANSI_Colorizer

colorizer = ANSI_Colorizer()


def split_image(image_path, cell_size, output_dir):
    """Splits an image into cells of the specified size and saves them to the output directory."""

    print("Initializing...")

    image = Image.open(image_path)
    width, height = image.size

    print(colorizer.colorize("\n\nImage successfully loaded!\n\n", "green"))

    print(colorizer.colorize("Image size: {}x{}".format(width, height), "yellow"))

    print(colorizer.colorize("Cell size: {}x{}".format(cell_size, cell_size), "yellow"))

    print(colorizer.colorize("Output directory: {}".format(output_dir), "yellow"))

    num_cells_width = width // cell_size
    num_cells_height = height // cell_size

    print("=========================================")

    print(colorizer.colorize("\n\nSplitting image...\n\n", "green"))

    total_cells = num_cells_width * num_cells_height
    current_cell = 0

    for i in range(num_cells_height):
        for j in range(num_cells_width):
            cell = image.crop((j * cell_size, i * cell_size, (j + 1) * cell_size, (i + 1) * cell_size))
            cell_filename = f"cell_{i}_{j}.png"
            cell.save(os.path.join(output_dir, cell_filename))
            current_cell += 1
            print(colorizer.colorize(f"Saved {output_dir}/{cell_filename} (Progress: {current_cell}/{total_cells})", "cyan"))

    print(colorizer.colorize("\n\nDone!\n\n", "green"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split an image into cells")
    parser.add_argument("image_path", type=str, help="Path to the image file")
    parser.add_argument("--cell_size", type=int, default=100, help="Size of each cell (default: 100 pixels)")
    parser.add_argument("--output_dir", type=str, default="output", help="Directory to save the output cells (default: 'output')")

    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)  # Create output directory if it doesn't exist

    split_image(args.image_path, args.cell_size, args.output_dir)
