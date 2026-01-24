import os
from PyPDF2 import PdfReader, PdfWriter

BASE_DIR = "pdf-data"
OUTPUT_DIR = "output"

os.makedirs(OUTPUT_DIR, exist_ok=True)

print("🚀 Starting folder-wise PDF extraction (all levels)...\n")

for root, dirs, files in os.walk(BASE_DIR):
    pdf_files = [f for f in files if f.lower().endswith(".pdf")]

    if not pdf_files:
        continue

    relative_path = os.path.relpath(root, BASE_DIR)
    output_name = relative_path.replace(os.sep, "_") + ".pdf"
    output_path = os.path.join(OUTPUT_DIR, output_name)

    print(f"📂 Folder: {relative_path}")
    writer = PdfWriter()
    page_count = 0

    for file in pdf_files:
        pdf_path = os.path.join(root, file)
        print(f"  ➜ Processing: {file}")

        try:
            reader = PdfReader(pdf_path)
            if reader.pages:
                writer.add_page(reader.pages[0])
                page_count += 1
                print("    ✅ Page extracted")
            else:
                print("    ⚠️ No pages found")

        except Exception as e:
            print(f"    ❌ Error: {e}")

    with open(output_path, "wb") as f:
        writer.write(f)

    print(f"📝 Created: {output_name} ({page_count} pages)\n")

print("✅ Folder-wise extraction completed.\n")
