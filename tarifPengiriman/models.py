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
    


    def updateTarifPengiriman(self, id, new_motorfee, new_carfee):

        cursor = connection.cursor()
        query = f"""
                    UPDATE DELIVERY_FEE_PER_KM
                    SET motorfee= {new_motorfee}, carfee= {new_carfee} 
                    WHERE id= '{id}'
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
                    WHERE id= '{id}'
                    ;    
                """ 
        
        cursor.execute(query)
        return True
            
