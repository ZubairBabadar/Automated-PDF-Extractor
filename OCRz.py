import fitz  # PyMuPDF

pdf_path = "Internal Document Final.pdf"
doc = fitz.open(pdf_path)

def eximg(doc):
    for i, page in enumerate(doc):
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]  # Image reference ID
            base_image = doc.extract_image(xref)  # Extract image
            image_bytes = base_image["image"]

            with open(f"image{i}_{img_index}.png", "wb") as f:
                f.write(image_bytes)

    return True
