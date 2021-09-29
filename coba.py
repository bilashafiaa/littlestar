def tukar(L1,i,j):
    L1[i],L1[j]=L1[j],L1[i]
    
def bubble1(L):
    ubah = True
    pj = len(L)
    for i in range (1,pj):
        ubah = False
        for j in range (1,pj):
            if L[j] < L[j-1]:
                ubah = True
                tukar(L,j,j-1)
            j+=1
        print(L)
        
        if not ubah:
            print("hasil akhir = %s" %str(L))
        pj-=1

print("===============================================================")
print("Sebelum Bubble Sort")
list1=[67,13,71,39,45]
print(list1)
print("Setelah Bubble Sort")
bubble1(list1)
