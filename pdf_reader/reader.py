import sys, pathlib, pymupdf


doc = pymupdf.open("../data/raw/ssrn-3800977.pdf") #open
out = open("../data/outputs/out.txt", "wb") #create text output

def extract_text(doc, out):
    for page in doc: #iterate the doc pages
        text = page.get_text().encode("utf-8") #get plain text
        out.write(text)
        out.write(bytes((12,))) 
    out.close()

def extract_images(doc, out):
    for page_index in range(len(doc)):
        page = doc[page_index]
        image_list = page.get_images()

        if image_list:
            print(f"Found {len(image_list)} images on page {page_index}")
        else:
            print("No images found on page", page_index)

        for image_index, img in enumerate(image_list, start=1): # enumerate the image list
            xref = img[0] # get the XREF of the image
            pix = pymupdf.Pixmap(doc, xref) # create a Pixmap

            if pix.n - pix.alpha > 3: # CMYK: convert to RGB first
                pix = pymupdf.Pixmap(pymupdf.csRGB, pix)

            pix.save("page_%s-image_%s.png" % (page_index, image_index)) # save the image as png
            pix = None

def main():
    extract_text(doc, out)

if __name__ == "__main__":
    main()
