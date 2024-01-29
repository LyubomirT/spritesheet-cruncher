# This is the preview.py script that can be executed as a different command
import argparse
from PIL import Image, ImageDraw
import os
import wx

def preview_image(image_path, cell_size):
   """Creates a wx window with the image and lines drawn to simulate the cells, but the image itself doesn't change."""

   image = Image.open(image_path)
   width, height = image.size

   # Create a new image with the same size as the original image
   preview = image.copy()

   # Draw the grid lines on the preview image
   draw = ImageDraw.Draw(preview)
   for i in range(0, height, cell_size):
       draw.line((0, i, width, i), fill="black")
   for j in range(0, width, cell_size):
       draw.line((j, 0, j, height), fill="black")

   # Create a wx app and a frame
   app = wx.App()
   frame = wx.Frame(None, title="Preview", size=(800, 600))

   # Scale the preview image to fit the frame, preserving the aspect ratio
   frame_width, frame_height = frame.GetSize()
   ratio = min(frame_width / width, frame_height / height)
   scaled_width = int(width * ratio)
   scaled_height = int(height * ratio)
   scaled_preview = preview.resize((scaled_width, scaled_height))

   # Convert the PIL image to a wx image and display it on the frame
   wx_image = wx.Image(scaled_width, scaled_height)
   wx_image.SetData(scaled_preview.tobytes())
   wx_bitmap = wx_image.ConvertToBitmap()
   wx.StaticBitmap(frame, -1, wx_bitmap)

   # Show the frame and start the app
   frame.Show()
   app.MainLoop()

if __name__ == "__main__":
   parser = argparse.ArgumentParser(description="Preview an image with cells")
   parser.add_argument("image_path", type=str, help="Path to the image file")
   parser.add_argument("--cell_size", type=int, default=100, help="Size of each cell (default: 100 pixels)")

   args = parser.parse_args()

   preview_image(args.image_path, args.cell_size)
