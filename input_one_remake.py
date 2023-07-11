import pandas as pd
import numpy as np

def remake_out(file):
    # path_to_data = "../.."
    # data = pd.read_csv(f"{path_to_data}{filename}")     f"{path_to_data}{file}"
    df=pd.read_excel(file, sheet_name=None)
    key_lists=list(df.keys())
    file_name=file.split("\\")[-1]
    print(file_name)
    for key in key_lists:
        label_row_index = 100 #np.nan
        for row_index, row in df[key].iterrows():
            for cell in row:
                if isinstance(cell, str) and not df[key].isna().loc[row_index].any():
                    label_row_index = row_index
                    break
            if label_row_index != 100: 
                break

        # Set the column labels using the identified row
        if label_row_index!=100:
            df[key].columns = df[key].iloc[label_row_index]
        # Drop the rows before the label row and reset the index
            df[key] = df[key].iloc[label_row_index + 1:].reset_index(drop=True)
            df[key].to_excel(f'{file_name} {key}.xlsx', index=False)
        else: pass
    pass
if __name__ == "__main__":
    # User inputs filename
    filename = input("Enter filename: ")
 
    # Ensure it's a string
    if not filename.isalpha():
        filename = str(filename)
 
    # Automated validation
    remake_out(filename)