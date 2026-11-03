Kucing = ["Anggora", "Persia", "Siam", "Maine Coon", "Bengal", "munchkin"]

#mencetak element
print(Kucing[0])

#mengganti element
Kucing[2] = "kampung"
print(Kucing)

#menambah element
Kucing.insert(3, "Scottish Fold")
Kucing.append("british shorthair")
print(Kucing)

#menghapus element
del Kucing [0]
popped = Kucing.pop()
print (f'pop : {popped}')
print(Kucing)
Kucing.remove ("Bengal")
print(Kucing)

#mengurutkan element
print(sorted(Kucing))
Kucing.sort()
print(Kucing)
Kucing.reverse ()
print(Kucing)

print(f'Terdapat {len(Kucing)} kucing di dalam list')