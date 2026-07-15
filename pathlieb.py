from pathlib import Path

def main():
    main_path = Path(".")
    
    # iterdir() iterates everyone, is_dir() check folder
    top_dirs = [d for d in main_path.iterdir() if d.is_dir()]

    for top_dir in top_dirs:
        with open(f"{top_dir.name}.txt", "w") as file:
            
            # rglob("*") - checks all i think
            for item in top_dir.rglob("*"):
                
                if item.is_file() and item.suffix.lower() == ".dwg":
                    
                    # item.parent , item.name gives the folder path and filename
                    file.write(f"{item.parent};{item.name}\n")
                    print(f"DWG FILE DETECTED: {item.name}")

if __name__ == "__main__":
    main()