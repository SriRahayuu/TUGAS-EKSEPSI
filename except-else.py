def main():
    # membuat judul program
    print("PROGRAM PEMBAGIAN BILANGAN")
   
    #meminta user memasukkan bilangan
    a = float(input("masukkan a: "))
    b = float(input("masukkan b: "))
    
    # mendefinisikkan blok try..except
    try:
       hasil = a/b
    except ZeroDivisionError:
       print("\nERROR: Nilai b tidak boleh nol")
    else:
       print("\na : ", a)
       print("b : ", b)
       print("a/b= ", hasil)
       
if __name__=="__main__":
    main()
       
   
