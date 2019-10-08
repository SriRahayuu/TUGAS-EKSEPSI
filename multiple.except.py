def main():
    # membuat judul program
    print("PROGRAM PEMBAGIAN BILANGAN")
    
    # mendefinisikan blok try...except
    rty:
       # meminta user memasukkan bilangan
       a = float(input("memasukkan a: "))
       b = float(input("memasukkan b: "))
       
       # melakukan pembagian 
       hasil = a/b
      
    # mengantisispasi pembagian dengan 0
    except ZeroDivisionError:
       print("\nERROR: Nilai b tidak boleh nol")
       
    # mengantisipasi variabel a atau b belum diisi
    except ValueError:
       print("\nERROR: a dan b harus berupa angka")
       
    # mengantisipasi variabel a atau b belum diisi
    except Keyboarddinterrupt:
       print("\nERROR: jangan tekan Ctrl+c!")
       
    else:
       print("\na : ", a)
       print("b : ", b)
       print("a/b = ",hasil)
       
if __name__ == "__main__":
    main()
       
    
