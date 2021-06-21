linklist = []

class Node:
    def __init__(self, link):
        self.link = link
        self.ref = None

class LinkList:
    def __init__(self):
        self.mulai_node = None

    def print_LL(self):
        if self.mulai_node is None:
            print("kosong bang linked list lu")
        else:
            nilai = self.mulai_node
            while nilai is not None:
                print(nilai.link,"-->",end=" ")
                nilai = nilai.ref

    def tambah_diawal(self, link):
        node_baru = Node(link)
        node_baru.ref = self.mulai_node
        self.mulai_node = node_baru

    def tambah_diakhir(self, link):
        node_baru = Node(link)

        if self.mulai_node is None:
            self.mulai_node = node_baru
        else:
            nilai = self.mulai_node
            while nilai.ref is not None:
                nilai = nilai.ref
            nilai.ref = node_baru

    def tambah_setelah(self, link, x):
        nilai = self.mulai_node
        while nilai is not None:
            if x == nilai.link:
                break
            else:
               nilai = nilai.ref
        if nilai is None:
            print("Lahhhh, Masih kosong bosque")
        else:
            node_baru = Node(link)
            node_baru.ref = nilai.ref
            nilai.ref = node_baru

    def tambah_sebelum(self, link, x):
        if self.mulai_node is None:
            print("Lahhhh, Masih kosong bosque")
            return
        if self.mulai_node.link == x:
            node_baru = Node(link)
            node_baru.ref = self.mulai_node
            self.mulai_node = node_baru
            return
        nilai = self.mulai_node
        while nilai.ref is not None:
            if nilai.ref.link == x:
                break
            nilai= nilai.ref
        if nilai.ref is None:
            print("Nilai Ngga ada bang, mau tambah dimana sih?")
        else:
            node_baru = Node(link)
            node_baru.ref = nilai.ref
            nilai.ref = node_baru
            return

    def tambah_LL(self):
        i = 0
        print('\n')
        jumlah = int(input("Masukkan Jumlah Data Linked List : "))
        if jumlah == 0:
            return
        while i < jumlah:
            link = input("Masukkan Data Linked List ke %i :" % (i+1))
            i = i+1
            self.tambah_diakhir(link)

    def hapus_diawal(self):
        if self.mulai_node is None:
            print("Data lu masih kosong Bosqueee")
        else:
            self.mulai_node = self.mulai_node.ref

    def hapus_diakhir(self):
        if self.mulai_node is None:
            print("Data lu masih kosong Bosqueee")
        else:
            nilai = self.mulai_node
            while nilai.ref.ref is not None:
                nilai = nilai.ref
            nilai.ref = None

    def hapus_nilai(self,x):
        if self.mulai_node is None:
            print("Data lu masih kosong Bosqueee")
            return
        if self.mulai_node.link == x:
            self.mulai_node = self.mulai_node.ref
            return
        nilai = self.mulai_node
        while nilai.ref is not None:
            if nilai.ref.link == x:
                break
            nilai = nilai.ref
        if nilai.ref is None:
            print("Nilai Ngga ada bang, mau hapus apa sih?")
        else:
            nilai.ref = nilai.ref.ref


    def tambah_sebelum2(self,link,x):
        nilai = self.mulai_node
        if self.mulai_node is None:
            print("Lahhhh, Masih kosong bosque")
            return
        while nilai is not None:
            if x == nilai.link:
                node_baru = Node(link)
                node_baru.ref = self.mulai_node
                self.mulai_node = node_baru
                return
            if nilai.ref.link == x:
                break
            nilai= nilai.ref
        if nilai.ref is None:
            print("Nilai Ngga ada bang, mau tambah dimana sih?")
        else:
            node_baru = Node(link)
            node_baru.ref = nilai.ref
            nilai.ref = node_baru
            return


"""LL1 = LinkList()
LL1.tambah_diawal(100)
#LL1.tambah_diakhir(200)
LL1.tambah_diawal(300)
#LL1.tambah_diakhir(400)

print('\n', "nilai Linked List ")
LL1.print_LL()
LL1.hapus_diawal()

print('\n', "nilai Linked List ")
LL1.tambah_setelah(100, 100)
#LL1.hapus_diakhir()
LL1.print_LL()

print('\n', "nilai Linked List ")
LL1.tambah_sebelum(10, 100)
LL1.print_LL()
"""

LL1 = LinkList()
LL1.tambah_diawal(50)
LL1.tambah_diawal(25)
LL1.tambah_diawal(15)
LL1.tambah_diawal(10)
LL1.tambah_sebelum(5,10)
#LL1.print_LL()
#LL1.tambah_LL()


#hhasil AKhir
LL1.print_LL()













"""class LinkList:
    def __init__(self):
        self.mulai_node = None

    def print_LL(self):
        if self.mulai_node is None:
            print("kosong bang linked list lu")
        else:
            nilai = self.mulai_node
            while nilai is not None:
                print(nilai.link)
                nilai = nilai.ref

    def tambah_diawal(self, link):
        node_baru = Node(link)
        node_baru.ref = self.mulai_node
        self.mulai_node = node_baru

    def tambah_diakhir(self, link):
        node_baru = Node(link)

        if self.mulai_node is None:
            self.mulai_node = node_baru
            return
        nilai = self.mulai_node
        while nilai.ref is not None:
            nilai = nilai.ref
            nilai.ref = node_baru

    def hapus_diawal(self):
        if self.mulai_node is None:
            print("Data lu masih kosong Bosqueee")
            return
        self.mulai_node = self.mulai_node.ref

    def hapus_diakhir(self):
        if self.mulai_node is None:
            print("Data lu masih kosong Bosqueee")
            return
        nilai = self.mulai_node
        while nilai.ref is not None:
            nilai = nilai.ref
            nilai.ref = None"""



