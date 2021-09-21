class BangunDatar :
    SegitigaSamakaki = None
    Jajargenjang = None

BD = BangunDatar()
SegitigaSamakaki = None
Jajargenjang = None

rows = 5
for i in range(rows + 1, 0, -1): 
    #nested reverse loop
   for j in range(0, i - 1):
         # display star
         print ("*", end=' ')
print (" ")
    
print ("Jajar Genjang")
n = int (input("Masukkan N : "))
i = 1
a = n
while (i<=n):
    print(" "*(n-1), "*" * a) 
    n = n-1