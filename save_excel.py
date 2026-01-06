import os
import pandas as pd

def save_excel(df_new, output_excel, erase=True):
    if erase or not os.path.exists(output_excel):
        df_final = df_new
    else:
        df_existing = pd.read_excel(output_excel)
        df_final = pd.concat([df_existing, df_new], ignore_index=True)

    df_final.to_excel(output_excel, index=False)
