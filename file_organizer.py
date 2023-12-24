import os
import shutil

# Path to the directory you want to organize
source_folder = r'C:\Users\User\Desktop\PDO\assesment1\evidence'

# File type categorization
file_categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    # Add more categories as needed
}

# Function to move files
def move_file(file, category_folder):
    try:
        os.makedirs(category_folder, exist_ok=True)  # Create target folder if it doesn't exist
        shutil.move(file, category_folder)
    except Exception as e:
        print(f"Error moving file {file}: {e}")

# Main script
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)
    if os.path.isfile(file_path):
        file_ext = os.path.splitext(filename)[1].lower()
        for category, extensions in file_categories.items():
            if file_ext in extensions:
                category_folder = os.path.join(source_folder, category)
                move_file(file_path, category_folder)
                break
