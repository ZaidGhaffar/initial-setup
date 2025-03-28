import os

def create_file(filepath):
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            pass
        print(f"✅ Created file: {filepath}")
    else:
        print(f"⚠️ File already exists: {filepath}")

def create_folder(folderpath):
    
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)
        print(f"📂 Created folder: {folderpath}")
    else:
        print(f"📁 Folder already exists: {folderpath}")

def setup_project():
    
    base_dir = os.getcwd()  # Get the current working directory
    
    # Define files
    files = [".gitignore", "ReadMe.md", "requirements.txt"]
    
    # Define folders
    folders = ["app", "app/Backend", "app/Frontend"]
    
    # Create files
    for file in files:
        create_file(os.path.join(base_dir, file))
    
    # Create folders
    for folder in folders:
        create_folder(os.path.join(base_dir, folder))
    
    print("🚀 Project boilerplate setup complete!")

if __name__ == "__main__":
    setup_project()
