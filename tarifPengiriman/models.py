from django.db import connection

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


class TarifPengiriman:

    def __init__(self, id, province, motorfee, carfee):
        self.id = id
        self.province = province
        self.motorfee = motorfee
        self.carfee = carfee
    
    def __str__(self):
        return f"""TarifPengiriman
                    id: {self.id} 
                    province: {self.email}
                    motorfee: {self.motorfee}
                    carfee: {self.carfee}
                    """


class TarifPengirimanRepository:

    def getAllTarifPengiriman(self):
        cursor = connection.cursor()
        query = f"""
                    SELECT * FROM DELIVERY_FEE_PER_KM;    
                """ 

        cursor.execute(query)

        tarif_pengiriman_objects = dictfetchall(cursor)

        list_tarif_pengiriman = []
        for i in range(len(tarif_pengiriman_objects)):
            tarif_pengiriman = TarifPengiriman(tarif_pengiriman_objects[i]['id'], tarif_pengiriman_objects[i]['province'], 
                                            tarif_pengiriman_objects[i]['motorfee'], tarif_pengiriman_objects[i]['carfee'])
            list_tarif_pengiriman.append(tarif_pengiriman)

        # print(list_tarif_pengiriman)

        return list_tarif_pengiriman
        


    "Contoh Ambil satu object"
    # def getByEmail(self, email):
    #     cursor = connection.cursor()
    #     query = f"""
    #                 SELECT * from transaction_actor WHERE email = \'{email}\';
    #             """
    #     cursor.execute(query)
    #     row = cursor.fetchone()
    #     ta = TransactionActor(row[0], row[1], row[2], row[3], row[4], row[5])
    #     print(row)
    #     print(ta)
    #     return ta


    def updateTarifPengiriman(self, id, new_motorfee, new_carfee):

        cursor = connection.cursor()
        query = f"""
                    UPDATE DELIVERY_FEE_PER_KM
                    SET motorfee= {new_motorfee}, carfee= {new_carfee} 
                    WHERE id={id}
                    ;    
                """ 
        
        
        try:
            cursor.execute(query)
            return True
            
        except Exception as error:
            return error

    def hapusTarifPengiriman(self, id):

        cursor = connection.cursor()
        query = f"""
                    DELETE FROM DELIVERY_FEE_PER_KM
                    WHERE id='{id}'
                    ;    
                """ 
        
        cursor.execute(query)
        return True
            

    # if 'user_email' not in request.session:
    #     return redirect('/authentication/login')
    # email = request.session.get('user_email')
    # if request.method == "POST":

    #     jumlahTarik = int(request.POST["nominalPenarikan"])
    #     tar = TransactionActorRepository()
    #     success = tar.reduceByEmail(email, jumlahTarik)

    #     if success:
    #         return redirect('/restopay/')
    #     else:
    #         return index(request, fail_tarik=True)



