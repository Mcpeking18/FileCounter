import pandas as pd
from pathlib import Path

def clean(parth,top_dirc):
    abc = str(parth)
    abc = abc.removeprefix(f"{str(top_dirc)}\\")
    x = abc.find("\\")
    return abc[x+1:]


def main():
    main_path = Path('.')

    top_dirs = [
        d for d in main_path.iterdir()
        if d.is_dir() and str(d).endswith(".git") == False
    ]

    for top_dir in top_dirs:
        
        sheet_dirs = [
            d for d in top_dir.iterdir()
            if d.is_dir()
        ]

        with pd.ExcelWriter(f"{top_dir}.xlsx") as Excel:

            for sheet_dir in sheet_dirs:

                peth , name = [],[]

                for item in sheet_dir.rglob("*.dwg"):
                    peth.append(clean(item.parent,top_dir))
                    name.append(item.name)

                dic = {
                    "Path" : peth,
                    "Name" : name
                }

                workbook = pd.DataFrame(dic)
                workbook.to_excel(
                    Excel, 
                    sheet_name=str(sheet_dir.name),
                    index=False
                )
        
main()    