def main():
  try:
     # membuka file
     r = open("data ke file.txt", "r")
     
     try:
        # menilis data ke file
        f.write("pemrograman phython")
        
      finally:
          f.close()  # menutup file
   except ioError:
      print("\nERROR:file tidak dapat" + "dibuka/ditulis")
      
if __name__==__main__:
    main()
          
