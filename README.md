# Spritesheet Cruncher

We crank spritesheets! This is a tool for automatically splitting up spritesheets into individual images, if you don't want to do it by hand. (And who does?)

## Installation

```bash
$ git clone https://LyubomirT/spritesheet-cruncher.git
```

```bash
$ cd spritesheet-cruncher
```

```bash
$ pip install -r requirements.txt
```

The installation process is classic for GitHub repositories. You clone the repository, navigate to it, and install the requirements. You can also install the requirements in a virtual environment, if you want to keep your system clean.

## Usage

At the moment, we have two files you can use: `splitter.py` and `preview.py`. The first one is the main file, that you will use to split your spritesheet. The second one is a previewer, that you can use to preview the spritesheet before splitting it to make sure everything is in order and your hard drive won't be filled with garbage.

### Splitter

The splitter is the main file. It is used to split spritesheets into individual images. However, it pretty much works best with spritesheets that have a grid-like structure or are perfect squares. If you have a spritesheet that is not a perfect square, you can still use the splitter, but you'd better resize the spritesheet to a perfect square first, so that the splitter can work properly.

The splitter file supports the following CLI arguments:

1. `image_path` - The path to the spritesheet you want to split. This is a required argument and does not need to be specified with a flag.
2. `--output_path` - The path to the folder where you want to save the split images. If not specified, the images will be saved in the `output` folder in the same directory as the spritesheet.
3. `--cell_size` - The size of the individual images. If not specified, the splitter will default to 100x100 pixels.

Here is an example of how you can use the splitter:

```bash
$ python splitter.py spritesheet.png --output_path "/home/user/thisisme/Desktop/sprites" --cell_size 50
```

### Previewer

The previewer here lets you take a look at how your image will be split before you actually split it. It is useful if you want to make sure that the spritesheet will be split properly and you won't end up with a bunch of garbage images you'll have to delete anyway.

The previewer file supports the following CLI arguments:

1. `image_path` - The path to the spritesheet you want to preview. This is a required argument and does not need to be specified with a flag.
2. `--cell_size` - The size of the individual images. If not specified, the previewer will default to 100x100 pixels.
3. `--linecolor` - The color of the lines that will be drawn on the image (either `black` or `white`). If not specified, the previewer will default to black.

The previewer, when run, will open a window with the preview of the spritesheet. It's basically a simple Tkinter window (ttk so it'll be native on all platforms) with the spritesheet drawn on it and lines drawn on top of it to show where the images will be split.

Here is an example of how you can use the previewer:

```bash
$ python preview.py spritesheet.png --cell_size 50 --linecolor white
```

## License

This project is licensed under the BSD 3-Clause License. See the [LICENSE](LICENSE) file for more information. If you want to use this project in your own project, you can do so, but you must include the license file in your project and you must include the license text in your project's documentation.

## Contributing

Thank you for your interest in supporting this project! If you want to contribute, you can do so by opening an issue or a pull request. If you want to open a pull request, please make sure that your code is well-documented and that it follows a similar coding style. If you want to open an issue, please make sure that you describe the issue in detail and that you include steps to reproduce it.

## Contact

You can contact me by creating a Discussion on the repository or by DMing me on Discord (@lyubomirt). I will try to respond as soon as possible, but I can't guarantee that I will respond immediately. If you want to contact me about a bug, please open an issue instead. Additionally, you can join my [Discord server](https://discord.gg/dwCE2RdUZ3) since I'm usually online there.

### We crank spritesheets!