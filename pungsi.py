#def Luas_Persegi_Panjang(panjang,lebar,tinggi):
   # return(p*l*t)
   # return(panjang*lebar*tinggi)

#p= int(input("panjang :"))
#l= int(input("lebar :"))
#t= int(input("tinggi :"))

#print("Luas persegi panjang: ", Luas_Persegi_Panjang(p,l,t))


def hitung_pangkat(basis, eksponen):
    """
    Menghitung basis^eksponen menggunakan rekursi.
    
    Args:
        basis (int/float): Angka dasar.
        eksponen (int): Pangkat (asumsi bilangan bulat non-negatif).
        
    Returns:
        float: Hasil dari basis^eksponen.
    """
    if eksponen == 0:
        return 1  # Kasus dasar: x^0 = 1
    elif eksponen < 0:
        # Menangani eksponen negatif (misal: x^-n = 1/x^n)
        return 1 / hitung_pangkat(basis, -eksponen)
    else:
        # Langkah rekursif: x^n = x * x^(n-1)
        return basis * hitung_pangkat(basis, eksponen - 1)