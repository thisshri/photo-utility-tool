# photo-utility-tool [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)


This script takes an image and adds white padding to the image to make it 1:1 image.

### How to run
1. Clone the repository:

    `git clone git@github.com:thisshri/photo-utility-tool.git`

2. Go to src directory and run:

    `./main.py --i foo.jpg`

### Arguments

| Flag | Description | Default |
| :--- | :--- | :--- |
| `--i IMAGE_FILE(S)_OR_DIR(S)` | Path(s) of image file(s) or directory(ies) containing images. Accepts multiple values. **Required.** | — |
| `-r`, `--recursive` | Recursively search directories for images. | `False` |
| `-s`, `--size` | Output image size in pixels (width and height). | `800` |
| `-o`, `--overwrite` | Overwrite the original file instead of saving a new copy (`<name>_sqaure_.<ext>`). | `False` |

### Usage examples

Pad a single image (saves `foo_sqaure_.jpg` next to the original):

```
./main.py --i foo.jpg
```

Pad several images at once:

```
./main.py --i foo.jpg bar.png baz.jpeg
```

Pad every image in a directory:

```
./main.py --i ./photos
```

Recursively pad every image under a directory tree:

```
./main.py --i ./photos -r
```

Resize output to 1200×1200 instead of the default 800×800:

```
./main.py --i foo.jpg -s 1200
```

Overwrite originals in place (recursive, custom size):

```
./main.py --i ./photos -r -s 1024 -o
```


### Examples
Image in the `1st row` was padded on top and bottom to make it 1:1 where as image in `2nd row` was padded on left and right.

| Image Padding | Before                                                 | After                                                  |
| :-----------: |:------------------------------------------------------:|:------------------------------------------------------:|
| Vertical      | <kbd><img src="https://i.imgur.com/mLq8v8g.jpg"></kbd> | <kbd><img src="https://i.imgur.com/OQQASzb.jpg"></kbd> |
| horizontal    | <kbd><img src="https://i.imgur.com/TgBKaQj.jpg"></kbd> | <kbd><img src="https://i.imgur.com/uTL3Yv0.jpg"></kbd> |

