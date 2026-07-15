import os

def main():
    main_path = "."
    
    # Get just the top-level directories to name our text files
    top_dirs = [d for d in os.listdir(main_path) if os.path.isdir(d)]

    for top_dir in top_dirs:
        with open(f"{top_dir}.txt", "w") as file:
            
            # os.walk handles all the deep-diving automatically
            for current_path, sub_folders, files in os.walk(top_dir):
                for file_name in files:
                    if file_name.lower().endswith(".dwg"):
                        
                        # Clean the path and write
                        clean_dir = current_path.removeprefix(".\\").removeprefix("./")
                        file.write(f"{clean_dir};{file_name}\n")
                        print(f"DWG FILE DETECTED: {file_name}")

if __name__ == "__main__":
    main()