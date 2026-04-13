#!/bin/python3

import os
from PIL import Image
from argparse import ArgumentParser

IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp')
DEFAULT_OUTPUT_SIZE = 800


def create_square_image(image):
    """
    Create new image with 1:1 aspect ration by adding white padding to the
    required sides of images.
    """
    padding = round(
        abs(image.width - image.height) / 2
    )

    top = right = bottom = left = 0
    if image.height > image.width:
        left = right = padding
    else:
        top = bottom = padding

    width = left + image.size[0] + right
    height = top + image.size[1] + bottom
    square_image = Image.new(
        image.mode,
        (width, height),
        color=(255, 255, 255)
        )
    square_image.paste(image, (left, top))
    return square_image


def is_image(filename):
    return filename.lower().endswith(IMAGE_EXTENSIONS)


def collect_images(path, recursive):
    if not os.path.isdir(path):
        return [path]

    if recursive:
        return [
            os.path.join(root, entry)
            for root, _, files in os.walk(path)
            for entry in sorted(files)
            if is_image(entry)
        ]

    return [
        os.path.join(path, entry)
        for entry in sorted(os.listdir(path))
        if is_image(entry) and os.path.isfile(os.path.join(path, entry))
    ]


def main():
    parser = ArgumentParser(
        description='Create new image with aspect ration 1:1 by padding it' +
        ' with white background'
    )

    parser.add_argument(
        '--i',
        metavar='IMAGE_FILE(S)_OR_DIR(S)',
        nargs='*',
        type=str,
        required=True,
        dest='inputs',
        help='Path of image file(s) or directory(ies) containing images.'
    )

    parser.add_argument(
        '-r',
        '--recursive',
        action='store_true',
        dest='recursive',
        help='Recursively search directories for images.'
    )

    parser.add_argument(
        '-s',
        '--size',
        type=int,
        default=DEFAULT_OUTPUT_SIZE,
        dest='size',
        help='Output image size in pixels (width and height). '
             'Default: %(default)s.'
    )

    parser.add_argument(
        '-o',
        '--overwrite',
        action='store_true',
        dest='overwrite',
        help='Overwrite the original file instead of saving a new copy.'
    )

    args = parser.parse_args()

    for path in args.inputs:
        for image_file in collect_images(path, args.recursive):
            process_image(image_file, args.size, args.overwrite)


def process_image(image_file, size, overwrite):
    image = create_square_image(Image.open(image_file))
    image = image.resize((size, size))

    if overwrite:
        output_path = image_file
    else:
        file_name, file_ext = image_file.rsplit('.', 1)
        output_path = file_name + '_sqaure_.' + file_ext

    image.save(output_path)


if __name__ == "__main__":
    main()
