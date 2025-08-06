import pymupdf

doc = pymupdf.open("../data/raw/Environmental Cost of AI _ FT.pdf") #open
out = open("../data/outputs/out.txt", "wb") #create text output
for page in doc: #iterate the doc pages
    text = page.get_text().encode("utf-8") #get plain text
    out.write(text)
    out.write(bytes((12,))) 
out.close()

