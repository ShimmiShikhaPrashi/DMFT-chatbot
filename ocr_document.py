import os
import fitz
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

PDF_PATH = r"data\PMKKKY_Revised_Guidelines_2024.pdf"
OUTPUT_FILE = r"data\pmkkky_text.txt"


def extract_text_from_pdf():

    print("Starting OCR...")

    if not os.path.exists(PDF_PATH):
        print("ERROR: PDF not found!")
        return

    all_text = []

    try:
        pdf = fitz.open(PDF_PATH)

        print(f"Total pages found: {len(pdf)}")

        for page_number in range(len(pdf)):

            print(f"Processing page {page_number + 1}...")

            page = pdf.load_page(page_number)

            # Higher resolution for better OCR
            matrix = fitz.Matrix(3, 3)

            pix = page.get_pixmap(
                matrix=matrix,
                alpha=False
            )

            image = Image.frombytes(
                "RGB",
                [pix.width, pix.height],
                pix.samples
            )

            text = pytesseract.image_to_string(
                image,
                lang="eng"
            )

            print(
                f"Page {page_number + 1}: "
                f"{len(text)} characters extracted"
            )

            if text.strip():

                all_text.append(
                    f"\n\n===== PAGE {page_number + 1} =====\n\n{text}"
                )

        pdf.close()

        final_text = "\n".join(all_text)

        print(f"\nTotal characters extracted: {len(final_text)}")

        with open(
            OUTPUT_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(final_text)

        print("\nOCR COMPLETED!")
        print(f"Saved to: {OUTPUT_FILE}")

    except Exception as error:

        print("\nOCR ERROR:")
        print(error)


if __name__ == "__main__":
    extract_text_from_pdf()