def main()
    print ("PROGRAM PEMBAGIAN BILANGAN")
    
    # meminta user memasukkan bilangan
    a = float(input("masukkan a: "))
    b = float(input("masukkan b: "))
    
    #mendefinisikkan blok try...except
    try:
      hasil = a/b 
    except zeroDivisionError:
      print("\nERROR: Nilai b tidak boleh nol")
      
     #menampilkan hasil
     print("\na : ", a)
     Print('b : ", b)
     
     # kode dinbawah ini akan menambulkan kesalahan 
     #dengan  tipe NameError
     print("a/b = ", hasil)
     
i __name__=="__main__":
  main()
