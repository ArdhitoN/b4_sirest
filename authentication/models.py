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