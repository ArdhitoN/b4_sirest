# from django.db import models

# from django.contrib.auth.models import AbstractUser


# # Create your models here.
# class User(AbstractUser):
#     is_admin = models.BooleanField(default=False)
#     is_restoran = models.BooleanField(default=False)
#     is_kurir = models.BooleanField(default=False)
#     is_pelanggan = models.BooleanField(default=False)
# commented to use psql only

from django.db import connection

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
    def getByEmailPassword(self, email, password):
            cursor = connection.cursor()
            query = f"""SELECT * FROM user_acc WHERE email = \'{email}\' AND password = \'{password}\';"""
            cursor.execute(query)
            row = cursor.fetchone()
            try:
                useracc = UserAcc(row[0], row[1], row[2], row[3], row[4])
                print(useracc)
                print(row)
                return useracc
            except Exception as e:
                print("Error at getbyemailpassword")
    
    def getByEmail(self, email):
        cursor = connection.cursor()
        query = f"""SELECT * FROM user_acc WHERE email = \'{email}\';"""
        cursor.execute(query)
        row = cursor.fetchone()
        try:
            useracc = UserAcc(row[0], row[1], row[2], row[3], row[4])
            print(useracc)
            print(row)
            return useracc
        except Exception as e:
            print("Error at getbyemailpassword")
    
    def isUserExist(self, email, password):
            cursor = connection.cursor()
            query = f"""SELECT * FROM user_acc WHERE email = \'{email}\' AND password = \'{password}\';"""
            cursor.execute(query)
            row = cursor.fetchone()

            if row is not None:
                return True
            else:
                print("none: isuserexist")
                return False
    
    def isAdmin(self, email):
        # setelah check isUserExist
        cursor = connection.cursor()
        query = f"""SELECT * FROM user_acc U
                    WHERE EXISTS (
                    SELECT 1
                    FROM admin A
                    WHERE A.email = \'{email}\' AND U.email = A.email
                    );;
                """
        cursor.execute(query)
        row = cursor.fetchone()

        if row is not None:
            return True
        else:
            print("none: admin")
            return False
    
    def isCustomer(self, email):
        # setelah check is user exist
        cursor = connection.cursor()
        query = f"""SELECT * FROM user_acc U
                    WHERE EXISTS (
                        SELECT 1
                        FROM TRANSACTION_ACTOR TA
                        JOIN CUSTOMER C ON TA.email = C.email
                        AND U.email = TA.email
                        AND U.email = \'{email}\'
                    );
                """
        cursor.execute(query)
        row = cursor.fetchone()

        if row is not None:
            return True
        else:
            print("none: customer")
            return False
    
    def isRestaurant(self, email):
        # setelah check is user exist
        cursor = connection.cursor()
        query = f"""
                    SELECT * FROM user_acc U
                    WHERE EXISTS (
                        SELECT 1
                        FROM transaction_actor TA
                        JOIN restaurant R ON TA.email = R.email
                        AND U.email = TA.email
                        AND U.email = \'{email}\'
                    );
                """
        cursor.execute(query)
        row = cursor.fetchone()

        if row is not None:
            return True
        else:
            print("none: restaurant")
            return False
    
        
class TransactionActor:

    def __init__(self, email, nik, bankname, accountno, restopay, adminid):
        self.email = email
        self.nik = nik
        self.bankname = bankname
        self.accountno = accountno
        self.restopay = restopay
        self.adminid = adminid
    
    def __str__(self):
        return f"Ta Email: {self.email} Password: {self.email}"

class TransactionActorRepository:

    def getByEmail(self, email):
        cursor = connection.cursor()
        query = f"""
                    SELECT * from transaction_actor WHERE email = \'{email}\';
                """
        cursor.execute(query)
        row = cursor.fetchone()
        ta = TransactionActor(row[0], row[1], row[2], row[3], row[4], row[5])
        print(row)
        print(ta)
        return ta

class Customer:

    def __init__(self, email, birthdate, sex):
        self.email = email
        self.birthdate = birthdate
        self.sex = sex

class CustomerRepository:

    def getByEmail(self, email):
        cursor = connection.cursor()
        query = f"""
                    SELECT * FROM customer WHERE email = \'{email}\';
                """
        cursor.execute(query)
        row = cursor.fetchone()
        customer = Customer(row[0], row[1], row[2])
        print(row)
        print(customer)
        return customer

class Restaurant:

    def __init__(self, rname, rbranch, email, rphonenum, street, district, city, province, rating, rcategory):
        self.rname = rname
        self.rbranch = rbranch
        self.email = email
        self.rphonenum = rphonenum
        self.street = street
        self.district = district
        self.city = city
        self.province = province
        self.rating = rating
        self.rcategory = rcategory

class RestaurantRepository:

    def getByEmail(self, email):
        cursor = connection.cursor()
        query = f"""
                    SELECT * FROM restaurant WHERE email = \'{email}\';
                """
        cursor.execute(query)
        row = cursor.fetchone()
        restaurant = Restaurant(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
        print(row)
        return restaurant

    