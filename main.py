import argparse
from PIL import Image
import os

def split_image(image_path, cell_size, output_dir):
   """Splits an image into cells of the specified size and saves them to the output directory."""

   image = Image.open(image_path)
   width, height = image.size

   num_cells_width = width // cell_size
   num_cells_height = height // cell_size

   for i in range(num_cells_height):
       for j in range(num_cells_width):
           cell = image.crop((j * cell_size, i * cell_size, (j + 1) * cell_size, (i + 1) * cell_size))
           cell_filename = f"cell_{i}_{j}.jpg"
           cell.save(os.path.join(output_dir, cell_filename))

if __name__ == "__main__":
   parser = argparse.ArgumentParser(description="Split an image into cells")
   parser.add_argument("image_path", type=str, help="Path to the image file")
   parser.add_argument("--cell_size", type=int, default=100, help="Size of each cell (default: 100 pixels)")
   parser.add_argument("--output_dir", type=str, default="output", help="Directory to save the output cells (default: 'output')")

   args = parser.parse_args()

   os.makedirs(args.output_dir, exist_ok=True)  # Create output directory if it doesn't exist

   split_image(args.image_path, args.cell_size, args.output_dir)
