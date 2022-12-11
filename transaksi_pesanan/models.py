import traceback
from django.db import connection
import random

class UserAcc:
    
    def __init__(self, email, password, phonenum, fname, lname):
        self.email = email
        self.password = password
        self.phonenum = phonenum
        self.fname = fname
        self.lname = lname
    
    def __str__(self):
        return f"UA Email: {self.email} Password: {self.email}"

class UserAccRepository:
    
    # get by email only
    def getByEmail(self, email):
        cursor = connection.cursor()
        query = f"""SELECT * FROM user_acc WHERE email = \'{email}\';"""
        cursor.execute(query)
        row = cursor.fetchone()
        try:
            useracc = UserAcc(row[0], row[1], row[2], row[3], row[4])
            return useracc
        except Exception as e:
            print("Error at getbyemailpassword")

class Restoran:
    
    def __init__(self, rname, rbranch, email, rphonenum, street, district, city, province, rating, rcategory):
        
        self.email = email
        self.rname = rname
        self.rbranch = rbranch
        self.rphonenum = rphonenum
        self.street = street
        self.district = district
        self.city = city
        self.province = province
        self.rating = rating
        self.rcategory = rcategory


class Transaksi:

    def __init__(self, email, datetime, street, district, city, province, totalfood, totaldiscount, deliveryfee, totalprice, rating, DFid, PMId, PSid, CourierId ):

        self.email = email
        self.transaction_datetime = datetime
        self.street = street
        self.district = district
        self.city = city
        self.province = province
        self.totalfood = totalfood
        self.totaldiscount = totaldiscount
        self.deliveryfee = deliveryfee
        self.totalprice = totalprice
        self.rating = rating
        self.PMid = PMId
        self.PSid = PSid
        self.DFid = DFid
        self.courierId = CourierId
        self.date_epoch = datetime.timestamp()

    def add_foods(self, foods):
        self.foods = foods

    def add_status(self, tsid):
        if tsid == None:
            tsid = ''
        self.transaction_status = tsid
    
    def add_customer(self, cust):
        self.cust = cust
        self.cust.customer_name = f"{cust.fname} {cust.lname}"
    
    def add_nama_kurir(self, fkname, lkname):
        self.nama_kurir = f"{fkname} {lkname}"
    
    def add_plat(self, plat):
        self.plat = plat
    
    def add_jenis_kendaraan(self, jenis):
        self.jenis_kendaraan = jenis
    
    def add_merk_kendaraan(self, merk):
        self.merk_kendaraan = merk
class TransaksiFood:

    def __init__(self, rname, rbranch, foodname, amount, note):

        self.rname = rname
        self.rbranch = rbranch
        self.foodname = foodname
        self.amount = amount
        self.note = note

class RestaurantRepository:

    def getRestaurantByEmail(self, email):

        cursor = connection.cursor()
        query = f"""SELECT * from RESTAURANT where email = \'{email}\';"""
        #print(query)
        cursor.execute(query)
        row = cursor.fetchone()
        #print(f"MASUK RNAME = \'{row[1]}\'")
        restaurant = Restoran(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])

        return restaurant


class TransaksiRepository:

    def fill_derived_attribute(self, tf):

        cursor = connection.cursor()
        uar = UserAccRepository()

        # query 2, get latest status
        # query2 = f"""SELECT tsid FROM TRANSACTION_HISTORY WHERE email = \'{tf.email}\' AND datetime = \'{tf.transaction_datetime}\' ORDER BY tsid DESC LIMIT 1"""
        query2 = f"""
                  SELECT name FROM transaction_status
                  WHERE id in (
                    SELECT tsid FROM transaction_history
                    WHERE email = \'{tf.email}\' AND datetime = \'{tf.transaction_datetime}\'
                    ORDER BY datetimestatus DESC LIMIT 1
                  );
                """
        cursor.execute(query2)
        row = cursor.fetchone()
        print(f"row query 2 fill_derived: {row}")
        if row is None:
            row = [None]
        tf.add_status(row[0])

        # query3, get customer
        cust = uar.getByEmail(tf.email)
        tf.add_customer(cust)

        # query4, get foods
        #print("MASUK QUERY", query)
        query4 = f"""SELECT rname, rbranch, foodname, amount, note FROM TRANSACTION_FOOD WHERE email = \'{tf.email}\' AND datetime = \'{tf.transaction_datetime}\'"""
        cursor.execute(query4)
        rows = cursor.fetchall()
        foods = [TransaksiFood(row[0], row[1], row[2], row[3], row[4]) for row in rows]
        tf.add_foods(foods)

        # query5, query6 add detail kurir if courierId is not None
        if tf.courierId is not None:
            query5 = f"""
                        SELECT fname, lname FROM user_acc
                        WHERE email = \'{tf.courierId}\';
                      """
            print(query5)
            cursor.execute(query5)
            rowkname = cursor.fetchone()
            print(f"rowkname = {rowkname}")
            tf.add_nama_kurir(rowkname[0], rowkname[1])

            query6 = f"""SELECT * FROM courier WHERE email = \'{tf.courierId}\';"""
            cursor.execute(query6)
            rowcourier = cursor.fetchone()
            tf.add_plat(rowcourier[1])
            tf.add_jenis_kendaraan(rowcourier[3])
            tf.add_merk_kendaraan(rowcourier[4])

        return tf


    def getAllTransaksi(self, rname, rbranch):

        cursor = connection.cursor()
        #query1, get foods with transaction statuses
        print("MASUK TF", rname, rbranch)
        query = f"""SELECT TF.email, TF.datetime, TF.street, TF.district, TF.city, TF.province, TF.totalfood, TF.totaldiscount, TF.deliveryfee, TF.totalprice, TF.rating, TF.DFid, TF.PMID, TF.PSid, TF.courierid
        from TRANSACTION as TF WHERE EXISTS ( SELECT rname from TRANSACTION_FOOD WHERE rname = \'{rname}\' AND rbranch = \'{rbranch}\' AND email = TF.email and datetime = TF.datetime) ;"""
        cursor.execute(query)
        rows = cursor.fetchall()
        

        tfs = [Transaksi(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14]) for row in rows]
        
        uar = UserAccRepository()

        # get latest status
        for i in range(len(tfs)):
            tfs[i] = self.fill_derived_attribute(tfs[i])
        

        return tfs
    
    def detailTransaksiByEmailDatetime(self, email, datetime, rname, rbranch):

        cursor = connection.cursor()
        query = f"""SELECT TF.email, TF.datetime, TF.street, TF.district, TF.city, TF.province, TF.totalfood, TF.totaldiscount, TF.deliveryfee, TF.totalprice, TF.rating, TF.DFid, TF.PMID, TF.PSid, TF.courierid
        from TRANSACTION as TF WHERE email = \'{email}\' AND datetime = \'{datetime}\' AND EXISTS ( SELECT rname from TRANSACTION_FOOD WHERE rname = \'{rname}\' AND rbranch = \'{rbranch}\' AND email = TF.email and datetime = TF.datetime) ;"""

        cursor.execute(query)
        row = cursor.fetchone()
        tf = Transaksi(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14])

        tf = self.fill_derived_attribute(tf)

        return tf
    
    def addTransactionHistory(self, email, datetime, status):
        cursor = connection.cursor()
        # try insert new transaction history
        # insert into transaction_history 
        # values ('fmackeaguej@spiegel.de', '2022-10-20 08:00:00', 'TS_STAT002', now()::timestamp(0));
        try:
            query = f"""
                    INSERT INTO transaction_history
                    VALUES (\'{email}\', \'{datetime}\', \'{status}\', now()::timestamp(0));
                    """
            print(query)
            cursor.execute(query)
            print("adding transaction_history")
            return True
        except:
            traceback.print_exc()
            print("gabisa add transaction_history prob duplicate key")
            return False
    
    def addRandomCourierId(self, email, datetime):
        cursor = connection.cursor()
        query1 = f"""
                    SELECT count(*) FROM courier;
                  """
        cursor.execute(query1)
        row1 = cursor.fetchone()
        print(row1)
        random_number = random.randint(0, (row1[0]-1))
        query2 = f"""
                    SELECT email FROM courier LIMIT 1 OFFSET {random_number};
                  """
        print(query2)
        cursor.execute(query2)
        row2 = cursor.fetchone()
        print(row2)
        courierid = row2[0]
        query3 = f"""
                    UPDATE transaction
                    SET courierid = \'{courierid}\'
                    WHERE email = \'{email}\' AND datetime = \'{datetime}\';
                  """
        print(query3)
        try:
            cursor.execute(query3)
            print("bisa add courier")
        except:
            traceback.print_exc()

        

class Courier:

    def __init__(self, email, platenum, drivinglicensenum, vehicletype, vehiclebrand):

        self.email = email
        self.platenum = platenum
        self.drivinglicensenum = drivinglicensenum
        self.vehicletype = vehicletype
        self.vehiclebrand = vehiclebrand

# class CourierRepository:

#     def getbyEmail(self, email):
#         cursor = connection.cursor()
#         query = f"""SELECT * FROM courier WHERE email = \'{email}\';"""
#         cursor.execute(query)
#         row = cursor.fetchone()
#         try:
#             courier = Courier(row[0], row[1], row[2], row[3], row[4])
#             return courier
#         except Exception as e:
#             print("Error at getbyemail courier")