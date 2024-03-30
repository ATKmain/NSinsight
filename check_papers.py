import os
import fitz  # PyMuPDF

def test_pdf_files(folder_path):
    # Ensure the folder exists
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    # Loop through all files in the specified folder
    for file_name in os.listdir(folder_path):
        # Construct the full file path
        file_path = os.path.join(folder_path, file_name)
        # Check if the file is a PDF
        if file_path.endswith('.pdf'):
            try:
                # Open the PDF file
                with fitz.open(file_path) as doc:
                    text = ""
                    # Extract text from each page
                    for page in doc:
                        text += page.get_text()
                    # Check if there is any text extracted
                    if text.strip():  # If there is text
                        word_count = len(text.split())
                        #print(f"OK: '{file_name}', Words: {word_count}")
                        if word_count < 1000:  # If there is text
                            print(f"Too Short: '{file_name}', Words: {word_count}")

                    else:  # If no text was extracted
                        print(f"Failed: '{file_name}' content may not be text or is an image")
            except Exception as e:
                print(f"Erorr: '{file_name}', Error: {e}")

# Example usage
folder_path = 'data/'  # Update this path to the folder containing your PDF files
test_pdf_files(folder_path)
