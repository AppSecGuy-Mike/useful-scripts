#! /usr/bin/env python
# Just place this script in the folder you want 
# to remove white space from file names.
import os

def main():
  
    for count, filename in enumerate(os.listdir("./")):
        src ='./'+ filename
        dst = filename.replace(" ", "-")
        dst ='./'+ dst
        os.rename(src, dst)
    
# Driver Code
if __name__ == '__main__':
      
    main()

