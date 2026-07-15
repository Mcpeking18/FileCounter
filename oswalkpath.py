from pathlib import Path

def main():
    # Define our starting point as a Path object
    main_path = Path(".")
    
    # iterdir() looks at the contents, is_dir() ensures it's a folder
    top_dirs = [d for d in main_path.iterdir() if d.is_dir()]

    for top_dir in top_dirs:
        with open(f"{top_dir.name}.txt", "w") as file:
            
            # rglob("*") recursively finds EVERYTHING inside the folder
            for item in top_dir.rglob("*"):
                
                # Check if it's a file and has the right extension (suffix)
                if item.is_file() and item.suffix.lower() == ".dwg":
                    
                    # item.parent gives the folder path (automatically clean!)
                    # item.name gives the filename
                    file.write(f"{item.parent};{item.name}\n")
                    print(f"DWG FILE DETECTED: {item.name}")

if __name__ == "__main__":
    main()