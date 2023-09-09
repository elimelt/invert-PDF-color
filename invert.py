import fitz
print(fitz)

import argparse

def invert_colors(input_path, output_path):
    # open PDF file
    with fitz.open(input_path) as doc:
        for page in doc:
            # render page as pixmap
            pix = page.getPixmap()
            # invert colors of pixmap
            data = pix.getImageData(output=fitz.PIX_FMT_RGBA)
            data = bytearray(data)
            for i in range(0, len(data), 4):
                data[i] = 255 - data[i]  # red
                data[i+1] = 255 - data[i+1]  # green
                data[i+2] = 255 - data[i+2]  # blue
            pix.setImageData(data)
            # replace page contents with inverted pixmap
            page.setPixmap(pix)
        # save the modified document
        doc.save(output_path)

if __name__ == '__main__':
    # create argument parser
    parser = argparse.ArgumentParser(description='Invert colors of a PDF file')
    parser.add_argument('input_path', help='path to the input PDF file')
    parser.add_argument('output_path', help='path to the output PDF file')

    # parse arguments
    args = parser.parse_args()

    # call invert_colors function with input and output paths
    invert_colors(args.input_path, args.output_path)
