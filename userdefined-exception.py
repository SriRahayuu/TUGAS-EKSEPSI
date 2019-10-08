import math

# membuat eksepsi AbsractError
class AbsractError(RuntimeError):
  def __init__ (self, s):
    self.s = s
# mendefinisikan kelas abstract
  def _init__(self):
    raise AbsractError("ERROR:'"+"DuaDimensi"+"'adalah kelas abstract")
  def luas(self)
    raise NotimplementedError
  def kelililng (self):
    raise NotimplementedError
    
# membuat kelas lingkaran,
# turuna dari dua kelas duamensi
class lingkaran (DuaDimensi)
    def __ init__(self, r):
      self.r = r
    def luas(self):
      return math.pi * self.r *self.r
    def keliling keliling(luas):
      return 2 *math.pi *self.r
def main():
    # instansiasi kelas lingkaran : BENAR
    onbl = lingkaran(3)
    
    print("LINGKARAN")
    print('Luas\t\t:", objl.luas())
    print("keliling\t:", objl.keliling())
    
    # instansiasi kelas DuaDimensi : SALAH
    try:
         print("nmembuat objek" + +dari kelas DuaDimensi...")
         objl2 = DuaDImensi
    except AbstractError as error:
         print(error.s)
    else:
         print("DUADIMENSI")
         print("luas\t\t:",objl2.luas())
         print(keliling\t:",objl2.keliling())
         
if __name__ == "__main__":
    main()

    
 
    
    

