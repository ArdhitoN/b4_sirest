from django.db import connection

class Transaction:
    def __init__(self, email, datetime, street, district, city, province,
    total_food, total_discount, delivery_fee, total_price, rating, pmid, psid, dfid):
        self.email = email
        self.datetime = datetime
        self.street = street
        self.district = district
        self.total_food = total_food
        self.total_discount = total_discount
        self.delivery_fee = delivery_fee
        self.total_price = total_price
        self.rating = rating
        self.pmid = pmid
        self.psid = psid
        self.dfid = dfid
        self.city = city
        self.province = province
    
    def get_all(self):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM TRANSACTION;")
        rows = cursor.fetchall()
        transactions = []
        for row in rows:
            transactions.append(Transaction(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13]))
        return transactions

    # Method restoran


    # Method pelanggan
    
