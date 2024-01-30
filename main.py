class workshop:
    def checkNumber():
        num = int(input("bir yazı giriniz"))
        if num > 0:
            print("pozitifdir")
        elif num < 0:
            print("negatifdir")
        elif num == 0:
            print("nötrdür")
        else:
            print("bir sayı giriniz")

    def checkNumberBigger():
        num1 = int(input("bir yazı giriniz"))
        num2 = int(input("bir yazı giriniz"))
        num3 = int(input("bir yazı giriniz"))
        if (num1 >= num2) and (num1 >= num3):
            biggestNum = num1
        elif (num2 >= num) and (num2 >= num3):
            biggestNum = num2
        else:
            biggestNum = num3
        print("The biggset number"+str(biggestNum))

    def forStars():
        count = 3
        message = "*"
        for x in range(1, count+1, 1):  # (startNumber,endNumber,increase amount)
            print(x*message)

        # forStars() output
            # *
            # **
            # ***

    def primeNumber():
        num = int(input("bir sayı giriniz :"))
        isPrimeNum = True
        for x in range(2, num):
            if x == 0:
                continue
            if x == 1:
                continue
            if num % x == 0:
                isPrimeNum = False
                break
        if isPrimeNum:
            print("sayı asal ")
        else:
            print("sayı asal değil")
        # ? primeNumber()

    def calculateFactorial(num):
        if (num == 0):
            print("sonuç :1")
        if (num < 0):
            print("Negatif sayıların faktöriyeli yoktur")
        total = 1
        for x in range(1, num+1):
            total *= x
        return total
        # num=input("Faktöriyel hesaplanıcak numara : ")
        # print(calculateFactorial(int(num)))
        # output
        # Faktöriyel hesaplanıcak numara : 5
        # 120

    def matrixTotal():
        matris1 = [[1, 3, 5], [2, 4, 1], [1, 5, 7]]
        matris2 = [[3, 3, 4], [2, 4, 1], [3, 5, 4]]
        totalMatris = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for x in range(len(matris1)):
            for y in range(len(matris2)):
                totalMatris[x][y] = matris1[x][y]+matris2[x][y]
        return (totalMatris)

        # print(matrixTotal())
        #     # [[4, 6, 9], [4, 8, 2], [4, 10, 11]]
    def orderString():
        sentence = "Bugün hava çok güzel"
        sentenceArray = sentence.split()
        sentenceArray.sort()
        print(sentenceArray)
        # orderString()
        # ['Bugün', 'güzel', 'hava', 'çok']

    # from calculaterModule import math as operate

    # op=input("işlem : ")
    # operate.calculate(op)

    def chanceNumbersValue():
        # x ile y değerlerini ters çevir
        x = 10
        y = 20
        # yol 1
        # temp = x
        # x = y
        # y = temp

        print("x ="+str(x))
        print("y = "+str(y))
        # yol 2
        x, y = y, x

        # chanceNumbersValue() output
        # x =10
        # y = 20

    def calculateMil():
        km = input("kilometre verisini giriniz : ")
        mil = 0.6213711922
        print(km+" Kilometre " + str(float(km)*mil)+" mil eder")
        # calculateMil() output
        # kilometre verisini giriniz : 1
        # 1 Kilometre 0.6213711922 mil eder


class basicLogic:

    def forArray():
        #! Variables
        # ? for döngüsü eleman türü değiştirme ve diziler vardır
        a = 10  # integer(int)
        b = 10.0  # float(float)
        tc = "12356789101"  # String(str)
        isim = "isim"
        soyisim = "soyisim"
        diziler = [a, b, tc, isim, soyisim]
        for eleman in diziler:
            print(str(eleman)+" eleman türü " + str(type(eleman)))
            print("***********************")
        # forArray() output
            # 10 eleman türü <class 'int'>
            # ***********************
            # 10.0 eleman türü <class 'float'>
            # ***********************
            # 12356789101 eleman türü <class 'str'>
            # ***********************
            # isim eleman türü <class 'str'>
            # ***********************
            # soyisim eleman türü <class 'str'>
            # ***********************
    #! ************ String foksiyornları ************

        def upperCaseLowerCaseIf():
            # ? uperCase ve loweCase ve if kullanımı
            firstString = "deneme TAHTASI"
            secoundString = "DENEME tahtasi"
            print(firstString.upper())
            print(secoundString.upper())
            print(firstString.lower())
            print(secoundString.lower())
            if (firstString.upper() == secoundString.upper()):
                print("upper fonksiyonu çalıştı")
            else:
                print("upper fonksiyonu çalışmadı")

            if (firstString.lower() == secoundString.lower()):
                print("lower fonksiyonu çalıştı")
            else:
                print("lower fonksiyonu çalışmadı")

            # upperCaseLowerCaseIf() output
                # DENEME TAHTASI
                # DENEME TAHTASI
                # deneme tahtasi
                # deneme tahtasi
                # upper fonksiyonu çalıştı
                # lower fonksiyonu çalıştı

            # ? substring

        def substring():
            message = "Hello world"
            print(message[2])
            print(message[2:5])
            print(message[2:])
            print(message[:2])
            # substring() output
            # l
            # llo
            # llo world
            # He

        def length():
            # ? length(len) fonksiyonu
            message = "Hello world"
            print(len(message))
            print(message[len(message)-1:len(message)])
            # length() output
            # 11
            # d

        def replace():
            # ? replace kullanımı

            message = "Hello world"
            print(message)
            print(message.replace("Hello", "HELLO"))
            print(message.replace("world", "WORLD"))
            # replace() output
            # Hello world
            # HELLO world
            # Hello WORLD

        def SplitStrip():
            # ? Split: böler  ve Strip: boşluk siler  kullanımı

            message = "Fahri AYDIN 25 KONYA "
            message2 = "Fahri;AYDIN;25;KONYA "

            print(message.split())
            print(message.split(" "))
            print(message.strip().split(" "))
            print(message2.strip().split(";"))
            # SplitStrip() output
            # ['Fahri', 'AYDIN', '25', 'KONYA']
            # ['Fahri', 'AYDIN', '25', 'KONYA', '']
            # ['Fahri', 'AYDIN', '25', 'KONYA']
            # ['Fahri', 'AYDIN', '25', 'KONYA']

        def inputs():
            # ?  input kullanımı
            # ? default string veri alır
            name = input("Adınız :")
            surName = input("Soyadınız :")
            print(name+" "+surName)
            sayi1 = input("sayı 1 :")
            sayi2 = input("sayı 2 :")
            print(int(sayi1)+int(sayi2))
            # inputs() output
            # Adınız :isim
            # Soyadınız :soyad
            # isim soyad
            # sayı 1 :5
            # sayı 2 :6
            # 11

    #! return fonkiyornları

        def calculateTriangeArea(a, b):
            return a*b/2

            # output
            # alan = calculateTriangeArea(2,3)
            # print(alan)
            # 3.0
    #!lambda fonkişyonu
        # def calculateTriangeArea2(a, b): return a*b/2
        # x = calculateTriangeArea2
        # print(type(calculateTriangeArea2))
        # print(type(x))
        # print(x(2, 3))

        # output
        # <class 'function'>
        # <class 'function'>
        # 3.0
   #! CLASSLAR
        # normal Class
        class Maths:
            def sum(self, num1, num2):
                return num1+num2

            def subtraction(self, num1, num2):
                return num1-num2

            def divide(self, num1, num2):
                return num1/num2

            def multiply(self, num1, num2):
                return num1*num2
                # output
                # math = Maths()
                # print(math.sum(2, 3))
                # 5
        # costructer clasları (__init__)

            class Maths2:
                def __init__(self, num1, num2):
                    self.num1 = num1
                    self.num2 = num2
                    print(self)
                    print(
                        "bu bir costructer yapısıdır bu class her çalıştığında bu yapı çalışır")

                def sum(self):
                    return self.num1 + self.num2

                def subtraction(self):
                    return self.num1 - self.num2

                def divide(self):
                    return self.num1 / self.num2

                def multiply(self):
                    return self.num1 * self.num2
                # output
                #  # math2 = Maths2(2, 3)
                # print(math2.sum())
                    # <__main__.Maths2 object at 0x0000016E56DF9410>
                    # bu bir costructer yapısıdır bu class her çalıştığında bu yapı çalışır
                    # 5
        # Property  ve inherit class

            class Person:
                def __init__(self, firstName, surName, age):
                    self.firstName = firstName
                    self.surName = surName
                    self.age = age

            person1 = Person("Fahri", "Aydın", 23)
            print(person1.firstName)
            # output : Fahri
            # ? inherit class kullanımı
            # *class className(inhertitClasName):

            class Worker(Person):
                def __init__(self, salary):
                    self.salary = salary

            class Customer(Person):
                def __init__(self, creditCardNumber):
                    self.creditCardNumber = creditCardNumber
    #! module kullanımı
        # import mathModule as math  # ! module ekleme as: isimlendirme yapar

        # math.sum(5, 6)  # ? output 11
        # print(math.customer["firstName"])  # ? output fahri
    #! from module kullanımı  modulden istenilen yeri ekler (import eder)
        # from mathModule import sum as topla
        # topla(5,5)
   #! json dosyaları verileri ile ilgili işlemler
        def json():
            import json
            data = '{"firstName":"fahri","lastName":"aydın"}'
            y = json.loads(data)
            print(y["firstName"])
            print(y["lastName"])
            customer = {
                "firstName": "fahri",
                "lastName": "aydin"
            }
            customerJson = json.dumps(customer)
            print(customerJson)


class arrays:
    def defaultList():
        # ? append remove clear

        # Köşeli parentezli  array yazmı ve clear komutu
        firstStudents = ["AHMET", "VELİ", "MAHMUT", "FAHRİ"]
        # * diziyi temizler none döndürür
        print(("CLEAR array  : ")+str(firstStudents))
        # list yazımlı  array
        print(("CLEAR array  : ")+str(firstStudents.clear()))

        students = list(("AHMET", "VELİ", "MAHMUT",
                        "FAHRİ", "AHMET", "AHMET"))

        print(("ÖĞRENCİLER : ")+str(students))
        students.append("FERHAT")  # * elamanı dizi'nin sonuna ekler
        print("ÖĞRENCİLER : "+str(students))
        students.remove("AHMET")  # * elemanı diziden kaldırır
        print("ÖĞRENCİLER : "+str(students))
        # * dizideki elemanın sayısını söyler
        print("AHMET sayısı : "+str(students.count("AHMET")))
        # * 0 indexinden başlar ilk buluğu elemanın indexsini gösterir
        print("AHMET indexi : "+str(students.index("AHMET")))
        students.pop(1)  # * index'teki elamanı array'den çıkartır
        print("AHMET pop : "+str(students))
        students.insert(1, "MAYUMUN")  # * index'teki yere arraye ekler
        print("AHMET insert : "+str(students))
        students.reverse()  # * dizideki elemanları ters çevirir
        print("Ters çevir (reverse) : "+str(students))
        print("ÖĞRENCİ SAYISI : "+str(len(students)))

        #! dizi mantığı aşağıda yer alır incele  ve copy kullanımı
        students3 = students.copy()
        students2 = students  # kısa yol almak gibi
        students2[0] = "Kayseri"  # 2 dizide de değişti fakat
        print("students3 : " + str(students3))  # bu dizide değişiklik yok
        print("students2 : " + str(students2))
        print("students : " + str(students))

        print("students extend öncesi: " + str(students) +
              " dizi genişliği : "+str(len(students)))
        students.extend(students3)  # diziler birleştir
        print("students extend sonrası : " + str(students) +
              " dizi genişliği : "+str(len(students)))
        students.sort()  # diziler sırala a-z
        print("students : " + str(students))

        # defaultList() output
        # CLEAR array  : ['AHMET', 'VELİ', 'MAHMUT', 'FAHRİ']
        # CLEAR array  : None
        # ÖĞRENCİLER : ['AHMET', 'VELİ', 'MAHMUT', 'FAHRİ', 'AHMET', 'AHMET']
        # ÖĞRENCİLER : ['AHMET', 'VELİ', 'MAHMUT', 'FAHRİ', 'AHMET', 'AHMET', 'FERHAT']
        # ÖĞRENCİLER : ['VELİ', 'MAHMUT', 'FAHRİ', 'AHMET', 'AHMET', 'FERHAT']
        # AHMET sayısı : 2
        # AHMET indexi : 3
        # AHMET pop : ['VELİ', 'FAHRİ', 'AHMET', 'AHMET', 'FERHAT']
        # AHMET insert : ['VELİ', 'MAYUMUN', 'FAHRİ', 'AHMET', 'AHMET', 'FERHAT']
        # Ters çevir (reverse) : ['FERHAT', 'AHMET', 'AHMET', 'FAHRİ', 'MAYUMUN', 'VELİ']
        # ÖĞRENCİ SAYISI : 6
        # students3 : ['FERHAT', 'AHMET', 'AHMET', 'FAHRİ', 'MAYUMUN', 'VELİ']
        # students2 : ['Kayseri', 'AHMET', 'AHMET', 'FAHRİ', 'MAYUMUN', 'VELİ']
        # students : ['Kayseri', 'AHMET', 'AHMET', 'FAHRİ', 'MAYUMUN', 'VELİ']
        # students extend öncesi: ['Kayseri', 'AHMET', 'AHMET', 'FAHRİ', 'MAYUMUN', 'VELİ'] dizi genişliği : 6
        # students extend sonrası : ['Kayseri', 'AHMET', 'AHMET', 'FAHRİ', 'MAYUMUN', 'VELİ', 'FERHAT', 'AHMET', 'AHMET', 'FAHRİ', 'MAYUMUN', 'VELİ'] dizi genişliği : 12
        # students : ['AHMET', 'AHMET', 'AHMET', 'AHMET', 'FAHRİ', 'FAHRİ', 'FERHAT', 'Kayseri', 'MAYUMUN', 'MAYUMUN', 'VELİ', 'VELİ']

    def tupleLists():  # (read only)elemanı değiştirilemeyen listeler
        # tek elemanlı ise tuple sonuna  virgül (,) ekleyerek tuple olduğunu belirtiriz
        tupleValue = ("Fahri",)
        print(type(tupleValue))

        tupleList = (0, 1, 2, 3, "Ankara", (0, 1, 2, 3), [1, 2])
        lists = [0, 1, 2, 3, "Ankara", (0, 1, 2, 3), [1, 2]]
        lists[0] = 6
        print(tupleList[-2])
        print(lists[-2])
        # tupleList[0] = 6 err=>'tuple' object does not support item assignment
        print(type(tupleList))
        print(type(lists))
        print(len(tupleList))
        print(len(lists))
        print(tupleList)
        print(lists)
        # tupleLists() output
        # <class 'tuple'>
        # (0, 1, 2, 3)
        # (0, 1, 2, 3)
        # <class 'tuple'>
        # <class 'list'>
        # 7
        # 7
        # (0, 1, 2, 3, 'Ankara', (0, 1, 2, 3), [1, 2])
        # [6, 1, 2, 3, 'Ankara', (0, 1, 2, 3), [1, 2]]

    def setList():
        studentSet = {"ahmet", "ali", "salih", "derin"}
        studentSet2 = set("ahmet")
        print(type(studentSet))
        print(type(studentSet2))

        print(studentSet)
        if "ahmet" in studentSet:
            print("ahmet listede var")

        studentSet.add("mahmut")
        print(studentSet)

        studentSet.update({"nida", "nisa", "selin", "gizem"})
        print(len(studentSet))

        studentSet.update(("ceren",))
        print(len(studentSet))

        studentSet.remove("mahmut")  # bulamaz ise silmez hata çıkartır
        print(studentSet)
        studentSet.discard("mahmut")  # bulamaz ise silmez hata çıkarmaz
        print(studentSet)
        studentSet.clear()
        print(len(studentSet))
        print(studentSet)
        del studentSet
        # setList() output
        # <class 'set'>
        # <class 'set'>
        # {'ali', 'derin', 'salih', 'ahmet'}
        # ahmet listede var
        # {'mahmut', 'salih', 'ahmet', 'derin', 'ali'}
        # 9
        # 10
        # {'nida', 'gizem', 'nisa', 'ceren', 'salih', 'ahmet', 'selin', 'derin', 'ali'}
        # {'nida', 'gizem', 'nisa', 'ceren', 'salih', 'ahmet', 'selin', 'derin', 'ali'}
        # 0
        # set()

    def setUnion():
        setA = {1, 2, 3, 4, 5, 6}
        setB = {4, 5, 6, 7, 8, 9}
        print(setA | setB)
        print(setA.union(setB))
        print(setB.union(setA))

        # setUnion() output
        # {1, 2, 3, 4, 5, 6, 7, 8, 9}
        # {1, 2, 3, 4, 5, 6, 7, 8, 9}
        # {1, 2, 3, 4, 5, 6, 7, 8, 9}

    def setIntersection():
        setA = {1, 2, 3, 4, 5, 6}
        setB = {4, 5, 6, 7, 8, 9}
        print(setA & setB)
        print(setA.intersection(setB))
        print(setB.intersection(setA))
        # setIntersection() output
        # {4, 5, 6}
        # {4, 5, 6}
        # {4, 5, 6}

    def setDifference():
        setA = {1, 2, 3, 4, 5, 6}
        setB = {4, 5, 6, 7, 8, 9}
        print(setA - setB)
        print(setB-setA)

        print(setA.difference(setB))
        print(setB.difference(setA))

        # setDifference() output
        # {1, 2, 3}
        # {8, 9, 7}
        # {1, 2, 3}
        # {8, 9, 7}

    def setSymmetricDifference():
        setA = {1, 2, 3, 4, 5, 6}
        setB = {4, 5, 6, 7, 8, 9}
        print(setA ^ setB)
        print(setA.symmetric_difference(setB))
        print(setB.symmetric_difference(setA))

        # setSymmetricDifference() output
        # {1, 2, 3, 7, 8, 9}
        # {1, 2, 3, 7, 8, 9}
        # {1, 2, 3, 7, 8, 9}

    def setDictionaries():
        enToTr = {
            "book": "kitap",
            "table": "masa",
            "mouese": "fare"
        }
        trToEn = dict(
            kitap="book",
            masa="table",
            fare="mouese"
        )
        del (enToTr["table"])

        print(type(enToTr))
        print(type(trToEn))
        enToTr["book"] = "book 1"
        enToTr["pencil"] = "kalem"
        print(enToTr)
        print(trToEn)
        # setDictionaries() output
        # <class 'dict'>
        # <class 'dict'>
        # {'book': 'book 1', 'mouese': 'fare', 'pencil': 'kalem'}
        # {'kitap': 'book', 'masa': 'table', 'fare': 'mouese'}

    def mapFunc():
        numbers = [2, 3, 5, 6]
        sqrNumbers = []
        for num in numbers:
            square = num*num
            sqrNumbers.append(square)
        sqrNumbers2 = list(map(lambda x: x**2, numbers))
        print(sqrNumbers)
        print(sqrNumbers2)

    def filterFunc():
        numbers = [2, 3, 5, 6]
        numbersFilter = list(filter(lambda x: x > 2, numbers))
        print(numbersFilter)

    def reducerFunc():
        from functools import reduce
        numbers = [1,2,3,4,5]
        numbersReduce = reduce(lambda x, y: x * y, numbers)
        print(numbersReduce)# output :180



class fileOperate:
    import os
    # dosya açma izinler
    # default => r : okuma formatı                  (read only)
    # w : dosya yoksa oluştur(dosya üzerine yazar)  (append)
    # a : okuma ve düzenleme(ekleme) izni verir     (write )
    # x : oluştur demek (varsa hata verir)          (create)
    # %%

    def fileRead():

        f = open("customer.txt")
        # print(f.read())

        for l in f:
            print(l)  # okunmuyan satırları satır satır okur

        f.close()

    def fileAppend():
        fileToAppend = open("stutdents.txt", "w")
        fileToAppend.write("\n")
        fileToAppend.write("Derin")
        fileToAppend.close()

    def fileDelete():
        if os.path.exists("stutdents.txt"):
            os.remove("stutdents.txt")
            print("belge silindi")
        else:
            print("belge yok")

        if os.path.exists("stutdents"):
            os.rmdir("stutdents")
            print("dosya silindi")
        else:
            print("dosya yok")

    def fileWrite():
        students = ["Fahri", "selin", "mahmut", "fatma"]
        file = open("student.txt", "a")
        for word in students:
            file.write("\n")
            file.write(word)
        file.close()


class dbOparate:
    import sqlite3 as db
    # where      = Arar
    # or         = veya anlamına gelir  ve karşıladığı durumları veri listesine alır
    # and        = ve anlamına gelir  2 durumuda karşılaması gerekir
    # count(sayilicakVeri)= elemanları sayar
    # order by   =asc(a > z veya K > B) || asc(z > a veya B > K) => en sonda yazar
    # like " "= içerinde veri içersinde değerler aranır(%  %=> % işareti başında ve sonunda ne olduğu önemsiz olur)
    # insert =  insert into tabloAdı  (kolonAdı,kolonAdı,kolonAdı) (veri,veri,veri)
    # update = update tabloAdı set KolonAdı = "DeğiştirilcekVeri" where koşulKolon="koşulVeri"
    # delete =delete from TabloAdı where koşulKolon="koşulVeri"
    #!Select operation

    def listDb():
        import sqlite3 as db

        connection = db.connect("chinook.db")
        curser = connection.execute(
            """
            select FirstName,LastName,City from customers 
            where City="Prague" or city="Berlin"
            order by  FirstName,LastName desc
            """)
        for row in curser:
            print("First name = "+row[0])
            print("Lastname = "+row[1])
            print("***********************")
        connection.close()

    def groupByOrder():
        import sqlite3 as db

        connection = db.connect("chinook.db")
        curser = connection.execute(
            """
                select City,count(*) from customers 
                group by city
                order by  City asc
                """)
        for row in curser:
            print("City = "+row[0])
            print("count = "+str(row[1]))
            print("***********************")
        connection.close()

    def likeCommand():
        import sqlite3 as db
        connection = db.connect("chinook.db")
        curser = connection.execute(
            """
            select City ,count(*) from customers 
            where city like '%a%'
            order by  FirstName,LastName desc
            """)
        for row in curser:
            print("City = "+row[0])
            print("Lastname = "+str(row[1]))
            print("***********************")
        connection.close()

    #! insert
    def insertCustomer():
        import sqlite3 as db
        connection = db.connect("chinook.db")
        connection.execute("""
                        insert into customers 
                        (firstName , lastName,city,Email)
                        values("fahri","aydın","konya","fahriaydn@gmail.com")
                        """)
        connection.commit()
        connection.close()

    def updateCustomer():
        import sqlite3 as db
        connection = db.connect("chinook.db")
        connection.execute("""
                        update  customers set city="istanbul" 
                        where firstName="fahri"
                        """)
        connection.commit()
        connection.close()

    def deleteCustomer():
        import sqlite3 as db
        connection = db.connect("chinook.db")
        connection.execute("""
                        delete from customers 
                        where firstName="Mahmut"
                        """)
        connection.commit()
        connection.close()

    def joinOperasyonlari():
        import sqlite3 as db
        connection = db.connect("chinook.db")
        cursor = connection.execute("""select 
                                    albums.Title, 
                                    artists.Name from artists 
                                    inner join albums
                                    on artists.ArtistId = albums.ArtistId
                                    order by albums.Title
                                    """)
        for row in cursor:
            print("Title = "+row[0]+" Name = "+row[1])

        connection.close()


class tryCatch:
    def demos():
        import sys

        liste = [7, 'engin', 0, 3, "6"]

        for x in liste:
            try:
                print("Sayı: " + str(x))
                sonuc = 1/int(x)
                print("Sonuç : " + str(sonuc))
            except ValueError:
                print(str(x) + " bir sayı değil")
            except ZeroDivisionError:
                print(str(x) + " için sıfıra bölme hatası")
            except:
                print(str(x) + " hesaplanamadı")
                print("Sistem diyor ki : " + str(sys.exc_info()[0]))
            finally:
                print("İşlemler bitti")

        try:
            file = open("abc.txt")
        except:
            print("dosya hatası")
        finally:
            file.close()
            print("dosya kapandı")
