from decimal import Decimal
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]
from django.db import connection

class promo:
    def __init__(self, id, name, quantity,jenis, tanggal = None,mintrans = None):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.tanggal = tanggal
        self.mintrans = mintrans
        self.jenis = jenis
        self.used = False

class PromoRepository:
    def get_all(self):
        cursor = connection.cursor()
        queryHS = f"""SELECT * FROM promo natural join special_day_promo;"""
        cursor.execute(queryHS)
        rows = cursor.fetchall()
        categories = []
        i = 0
        for row in rows:
            categories.append(promo(row[0], row[1],row[2],"Special Day Promo" ))
            categories[i].tanggal = row[3]
            i += 1

        queryMT = f"""SELECT * FROM promo natural join min_transaction_promo;"""
        cursor.execute(queryMT)
        rows = cursor.fetchall()
    
        for row in rows:
            categories.append(promo(row[0], row[1],row[2],"Promo Minimum Transaksi"))
            categories[i].mintrans = row[3]
            i+=1
        
        used_id = []
        queryused = f"""SELECT pid FROM restaurant_promo;"""

        
        
        cursor.execute( queryused)
        rows = cursor.fetchall()
        
        for row in rows:
            used_id.append(row[0])
            
        for category in categories:
            if category.id in used_id:
                category.used = True
                
        return categories
    
    def insertHS(self, name, quantity, tanggal):
        print("MAsuk")
        cursor = connection.cursor()
        cursor.execute(f"SELECT count(id) from promo")
        countangka = cursor.fetchall()
        cursor.execute(f"SELECT id from promo")
        idangka = cursor.fetchall()
        print(countangka)
        # idbaru = countangka[0][0] + 2
        id = countangka[0][0] 
        while (id in idangka) :
            id += 1
        idbaru = id

        query = f"""INSERT INTO promo (id,promoname, discount) VALUES ( '{idbaru}','{name}', '{quantity}');"""
        cursor.execute(query)
        query = f"""INSERT INTO special_day_promo (id,date) VALUES ('{idbaru}','{tanggal}');"""
        cursor.execute(query)
    
    def insertMT(self, name, quantity, mintrans):
        cursor = connection.cursor()
        cursor.execute(f"SELECT count(id) from promo")
        countangka = cursor.fetchall()
        print(countangka)
        # idbaru = countangka[0][0] + 2
        cursor.execute(f"SELECT id from promo")
        idangka = cursor.fetchall()
        print(countangka)
        # idbaru = countangka[0][0] + 2
        id = countangka[0][0] 
        while (id in idangka) :
            id += 1
        idbaru = id
        print(idbaru)
        query = f"""INSERT INTO promo (id,promoname, discount) VALUES ( '{idbaru}','{name}', '{quantity}');"""
        cursor.execute(query)
        query = f"""INSERT INTO min_transaction_promo (id,minimumtransactionnum) VALUES ('{idbaru}','{mintrans}');"""
        cursor.execute(query)
        # query = f"""INSERT INTO min_transaction_promo (minimumtransactionnum) VALUES ('{mintrans}');"""

    def ubah(self,id,tanggal_awal,mintrans_awal,kuantitas,tanggal,mintrans):
        cursor = connection.cursor()
        if (tanggal_awal  == None):
           
         query1 = f"""update  promo set discount = '{kuantitas}' where id = '{id}';"""
         cursor.execute(query1)

         query2 = f"""update min_transaction_promo set minimumtransactionnum = '{mintrans}' where id = '{id}';"""
         cursor.execute(query2)
        else :
            query1 = f"""update promo set discount = '{kuantitas}' where id = '{id}';"""
            cursor.execute(query1)
    
            query2 = f"""update special_day_promo set date = '{tanggal}' where id = '{id}';"""
            cursor.execute(query2)
        

    def detail_promo(self, id):
        cursor = connection.cursor()
        get_query = f"""SELECT * FROM promo where promo.id = '{id}';"""
        cursor.execute(get_query)
        rows = cursor.fetchall()

        print( rows)

        queryHS = f"""SELECT id FROM special_day_promo;"""
        queryMT = f"""SELECT id FROM min_transaction_promo;"""
        
        cursor.execute( queryHS)
        
        rowsHS = cursor.fetchall()
        # cursor.execute(queryMT)
        
        # rowsMT = cursor.fetchall()

        idHS = []
        # idMT = []
        promotjan = []
        for row in rowsHS:
            idHS.append(row[0])
        # for row in rowsMT:  
        #     idMT.append(row[0])     
        for row in rows :
            if row[0] in idHS :
                queryHS = f"""SELECT * FROM promo natural join special_day_promo where 
                promo.id = '{id}';"""
                cursor.execute( queryHS)
                rowHS = cursor.fetchall()[0]

    
                promotjan.append(promo( rowHS[0],  rowHS[1], rowHS[2],"Special Day Promo" ))
                promotjan[0].tanggal =  rowHS[3]
            else :

                queryMT = f"""SELECT * FROM promo natural join min_transaction_promo where 
                promo.id = '{id}';"""
                cursor.execute( queryMT)
                rowMT = cursor.fetchall()[0]
                # print(rowsMT)

                promotjan.append(promo(rowMT[0], rowMT[1],rowMT[2], "Promo Minimum Transaksi"))
                promotjan[0].mintrans = rowMT[3]

        return promotjan

#  for rowHS in rowsHS:
#                     promotjan.append(promo( rowHS[0],  rowHS[1], rowHS[2],"Special Day Promo" ))
#                     promotjan.tanggal =  rowHS[3]
#             else :

#                 queryMT = f"""SELECT * FROM promo natural join min_transaction_promo where 
#                 promo.id = '{id}';"""
#                 cursor.execute( queryMT)
#                 rowsMT = cursor.fetchall()
#                 print(rowsMT)

#                 for rowMT in rowsMT:
#                     promotjan.append(promo(rowMT[0], rowMT[1],rowMT[2], "Promo Minimum Transaksi"))
#                     promotjan.mintrans = rowMT[3]

        return promotjan
            
    def delete_promo(self, id):
        cursor = connection.cursor()

        used_id = []
        queryHS = f"""SELECT id FROM special_day_promo;"""

        cursor.execute( queryHS)
        rowsHS = cursor.fetchall()
        for row in rowsHS:
            used_id.append(row[0])

        if id in used_id:
            query = f"""DELETE FROM special_day_promo WHERE id = '{id}';"""
            cursor.execute(query)
        else:
            query = f"""DELETE FROM min_transaction_promo WHERE id = '{id}';"""
            cursor.execute(query)

        query =f"DELETE FROM promo WHERE id = '{id}';"
        cursor.execute(query)

   