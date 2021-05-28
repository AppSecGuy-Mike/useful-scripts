#! /usr/bin/env python
# Just place this script in the folder you want 
# to convert .xlsx or .xls to .csv and sit back and enjoy. ;)
import os
import pandas as pd

def main():
  
    for count, filename in enumerate(os.listdir("./")):
        file_name, file_extension = os.path.splitext(filename)
        if file_extension == ".xlsx" or file_extension == ".xls":
            src ='./'+ filename
            dst = filename.replace(" ", "-")
            dst ='./'+ dst
            os.rename(src, dst)
    
            # Read and store content
            # of an excel file 
            read_file = pd.read_excel(dst, index_col=None, na_values=['NA'], usecols = "A:G")
  
            # Write the dataframe object
            # into csv file
            read_file.to_csv(file_name.replace(" ", "-") + ".csv", 
                 index = None,
                 header=True)
  
# Driver Code
if __name__ == '__main__':
      
    main()

