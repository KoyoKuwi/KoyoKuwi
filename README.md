KoyoKuwi
==========

Proyek ini hanya untuk _guyonan_ (candaan) yang dibuat setelah frasa _koyo kuwi_ muncul pada komentar Facebook.

_Koyo kuwi_ merupakan frasa dalam bahasa Jawa yang bermakna _seperti itu_ jika diterjemahkan ke dalam bahasa Indonesia.

This project is just a _guyonan_ (joke) commited after phrase _koyo kuwi_ appeared on Facebook comment.

_Koyo kuwi_ is a phrase in Javanese language, the meaning is _like that_ in English



Kebutuhan
---------
* Python 3

Penggunaan
----------
Contoh penggunaan pada file demo.py

    import koyokuwi
	import sys

	def main():
		if len(sys.argv) != 3:
			print("Invalid input")
			print("Penggunaan: demo.py koyo.txt kuwi.txt")
		else:
			koyo = sys.argv[1]
			kuwi = sys.argv[2]
			score = koyokuwi.score(koyo, kuwi)
	        
			print("Kemiripan kedua dokumen adalah : {:0.2f} %".format(score))

	if __name__  == "__main__":
		main()


Eksekusi demo.py

    $ python demo.py "samples/komodo.txt" "samples/komodo.txt"
    Kemiripan kedua dokumen adalah : 100.00 %

    $ python demo.py "samples/komodo.txt" "samples/badak sumatera.txt"
    Kemiripan kedua dokumen adalah : 30.30 %

    $ python demo.py "samples/komodo.txt" "samples/badak jawa.txt"
    Kemiripan kedua dokumen adalah : 30.67 %

    $ python demo.py "samples/badak jawa.txt" "samples/badak sumatera.txt"
    Kemiripan kedua dokumen adalah : 44.34 %


Pustaka
-------
Program ini diadaptasi dari MIT OpenCourseWare,
[Introduction to Algorithms](http://courses.csail.mit.edu/6.006/fall11/notes.shtml).