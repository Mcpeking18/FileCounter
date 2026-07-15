import pandas as pd
from pathlib import Path

def clean(parth,top_dirc):
    abc = str(parth).removeprefix(f"{str(top_dirc)}\\")
    x = abc.find("\\")
    return abc[x+1:]


def main():
    main_path = Path('.')

    top_dirs = [
        d for d in main_path.iterdir()
        if d.is_dir() and str(d).endswith(".git") == False
    ]
    #this is the list of directories in main directory
    #yes its in windows path class not a string

    for top_dir in top_dirs:
        
        sheet_dirs = [
            d for d in top_dir.iterdir()
            if d.is_dir()
        ]
        #now this is list of directories in the one of the directory of main

        with pd.ExcelWriter(f"{top_dir}.xlsx") as Excel: #to write on excel named {top_dir} ( creates a file if not exist)

            for sheet_dir in sheet_dirs:

                peth , name = [],[] #path , name of file

                for item in sheet_dir.rglob("*.dwg"): #find dwg files and append simple
                    peth.append(clean(item.parent,top_dir))
                    name.append(item.name)

                dic = {
                    "Path" : peth,
                    "Name" : name
                }
                #added dictionary to save it all and put in workbook dataframe

                workbook = pd.DataFrame(dic) #dataframe is created

                #this database will now be inserted into {sheet_dir} named sheet in {top_dir} named excel file
                workbook.to_excel(
                    Excel, 
                    sheet_name=str(sheet_dir.name),
                    index=False
                )
        
if __name__ == "__main__":
    main()