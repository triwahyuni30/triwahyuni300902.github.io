class VolumeBalok:
    Panjang = None
    Lebar = None
    Tinggi = None

VB = VolumeBalok()
VolumeBalok.Panjang=9
VolumeBalok.Lebar=15
VolumeBalok.Tinggi=7

hasil=VolumeBalok.Panjang*VolumeBalok.Lebar*VolumeBalok.Tinggi

print ("Panjang Balok = ", VolumeBalok.Panjang)
print ("Lebar Balok = ", VolumeBalok.Lebar)
print ("Tinggi Balok = ", VolumeBalok.Tinggi)
print ("Hasil dari Volume Balok = ", hasil)