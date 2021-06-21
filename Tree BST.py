class Node(object):
    def __init__(self, ujung):
        self.ujung = ujung
        self.kiri = None
        self.kanan = None

    def tambahnilai(self, nilai):
        if self.ujung is None:
            self.ujung = nilai
            return
        if self.ujung == nilai:
            return
        if self.ujung > nilai:
            if self.kiri:
                self.kiri.tambahnilai(nilai)
            else:
                self.kiri = Node(nilai)
        else:
            if self.kanan:
                self.kanan.tambahnilai(nilai)
            else:
                self.kanan = Node(nilai)

    def carinilai(self, nilai):
        if self.ujung == nilai:
            print("nih dia", nilai)
        if nilai < self.ujung:
            if self.kiri:
                self.kiri.carinilai(nilai)
            else:
                print("yah ",nilai," ga ketemu di pohon")
        else:
            if self.kanan:
                self.kanan.carinilai(nilai)
            else:
                print("yah ",nilai," ga ketemu pohon")

    def preorder(self):
        print(self.ujung)
        if self.kiri:
            self.kiri.preorder()
        if self.kanan:
            self.kanan.preorder()

    def inorder(self):
        if self.kiri:
            self.kiri.inorder()
        print(self.ujung,end="")
        if self.kanan:
            self.kanan.inorder()

    def postorder(self):
        if self.kiri:
            self.kiri.postorder()
        if self.kanan:
            self.kanan.postorder()
        print(self.ujung, end="")

akar = Node(None)
banyak = [12,8,10,4,2,6,9,22,19,20]
for i in banyak:
    akar.tambahnilai(i)

akar.carinilai(60)




print("                ",akar.ujung,"      ")

print("    ",akar.kiri.ujung,"                  "
      ,akar.kanan.ujung,"    ")


print("  ",akar.kiri.kiri.ujung,"   "
      ,akar.kiri.kanan.ujung,"          "
      ,akar.kanan.kiri.ujung," "
      ,akar.kanan.kanan," ",)


print(akar.kiri.kiri.kiri.ujung," "
      ,akar.kiri.kiri.kanan.ujung," "
      ,akar.kiri.kanan.kiri.ujung," "
      ,akar.kiri.kanan.kanan," "
      ,akar.kanan.kiri.kiri," "
      ,akar.kanan.kiri.kanan.ujung," "
)

print(akar.postorder())

"""    def tambahnilai(self, nilai):

        if self.ujung is None:
            self.ujung = nilai
            return
        if self.ujung == nilai:
            return
        if self.ujung > nilai:
            if self.kiri:
                self.kiri.tambahnilai(nilai)
            else:
                self.kiri = Node(nilai)
        else:
            if self.kanan:
                self.kanan.tambahnilai(nilai)
            else:
                self.kanan = Node(nilai)

    def carinilai(self, nilai):
        if self.ujung == nilai:
            print("nih dia", nilai)
        if nilai < self.ujung:
            if self.kiri:
                self.kiri.carinilai(nilai)
            else:
                print("yah ",nilai," ga ketemu di pohon")
        else:
            if self.kanan:
                self.kanan.carinilai(nilai)
            else:
                print("yah ",nilai," ga ketemu pohon")

akar = Node(None)
banyak = [12,8,10,4,6,2,9,22,19,20]
for i in banyak:
    akar.tambahnilai(i)

akar.carinilai(60)

"""
