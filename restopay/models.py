from django.db import connection
class TransactionActor:

    def __init__(self, email, nik, bankname, accountno, restopay, adminid):

        self.email = email
        self.nik = nik
        self.bankname = bankname
        self.accountno = accountno
        self.restopay = restopay
        self.adminid = adminid

class TransactionActorRepository:

    def getAll(self):

        cursor = connection.cursor()

        cursor.execute("SELECT * from transaction_actor")
        rows = cursor.fetchall()

        # [
        #     (row[0], row[1], row[2], row[3], row[4], row[5]),
        #     (row[0], row[1], row[2], row[3], row[4], row[5])
        # ]

        #taList = [TransactionActor(**row) for row in rows]

        taList = []
        for row in rows:
            taList.append(TransactionActor(row[0], row[1], row[2], row[3], row[4], row[5]))

        return taList