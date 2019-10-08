def main():
   # membuat judul program
   print("PROGRAM PEMBAGIAN BILANGAN")
  
   # mendefinisikan blol try...except
   try:
      # meminta user memasukkan bilangan
      a = float(input("masukkan a: "))
      b = float(input("masukkan b: "))
      
      # melakukan pembagian
      hasil = a/b
      
   except(ZeriDvisionError, ValueError,Keyboardinterrupt):
      print("nERROR:Anda telah melakukan "+"kesalahan")
   else:
      print("\na : ", a)
      print("b : ", b)
      print("a / b = ", hasil)
      
if __name__ == "__main__":
    main()
  
