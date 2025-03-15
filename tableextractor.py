from PyPDF2 import PdfReader
import pdfplumber
import pandas as pd



def table(pdf_path):
        with pdfplumber.open(pdf_path) as pdf:
            all_tables = []
            for page in pdf.pages:
                tables = page.extract_table()  # Extract tables from the page
                if tables:                      # If tables exist on the page Convert to Pandas DataFrame
                        
                        df = pd.DataFrame(tables)  
                        all_tables.append(df)
                        for i, table in enumerate(all_tables):
                            table.columns = table.iloc[0]           # Set the first row as column headers
                            table = table[1:]                       # Remove the first row from data
                            table = table.dropna(how="all")                           # Remove fully empty rows
                            all_tables[i] = table.reset_index(drop=True)              # Reset index
                            for i, table in enumerate(all_tables):
                                table.columns = table.iloc[0]                            # Set the first row as column headers
                                table = table[1:]                                        # Remove the first row from data
                                table = table.dropna(how="all")                          # Remove fully empty rows
                                all_tables[i] = table.reset_index(drop=True)             # Reset index

                                for i, table in enumerate(all_tables):  
                                    print(f"Cleaned Table {i+1}:")
                                    print(table)
                                    table.to_csv(f'table_{i+1}.csv', index = False)

        return True