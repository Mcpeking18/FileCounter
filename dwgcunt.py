import os

def clean_path(path_name,file_name):
    return path_name.removeprefix(".\\") + ";" + file_name + "\n"

def check(current_path,file):
    direc = os.listdir(current_path)
    for file_folder in direc:
        child_path = os.path.join(current_path,file_folder)
        if os.path.isfile(child_path):
            if file_folder.lower().endswith(".dwg"):
                file.write(clean_path(current_path,file_folder))
                print("DWG FILE DETECTED")
        else:
            check(child_path,file)

def main():
    main_path = "."
    main_path_dir = [d for d in os.listdir(main_path) if os.path.isdir(d)]

    for top_dir in main_path_dir:
        new_path = os.path.join(main_path,top_dir)
        with open(f"{top_dir}.txt", "w") as file: 
            check(new_path,file)     

if __name__ == "__main__":
    main()