# menginpor modul  sys untuk exit()
import sys
def main():
  # membuat judul program
  print ("PROGRAM PEMBAGIAN BILANGAN")
  
  # meminta user measukkan bilangan
  a = float(input("masukkan a: "))
  b = float(input("masukkan b: "))
  
  #mendefinisikan blok try...except
  try:
    hasil = a/b
  except ZeroDivisionError:
    print("\nError:Nilai b tidak boleh nol")
    sys.exit(1) #menghentikan program
   #menampilakn hasil
   print("\na : ", a)
   print("b : ", b)
   print("a / b = ",hasil)
if __name__=="__main__":
  main()
