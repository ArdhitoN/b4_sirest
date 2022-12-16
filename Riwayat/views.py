from django.shortcuts import render
from django.shortcuts import redirect



from authentication.models import *
from authentication.views import *
from django.db import connection
# Create your views here.
# def Baca_Pelanggan(request):
#     # current_user = auth.get_user(request)
#     cursor = connection.cursor()
from authentication.models import *

class table_R :
    def __init__(self, email, pfname, plname,kfname, klname, datetime, name, rating):
        self.email = email
        self.pfname = pfname
        self.plname = plname
        self.kfname = kfname
        self.klname = klname
        self.datetime = datetime
        self.name = name
        self.rating = rating
class table_P :
    def __init__(self, email, rname, rbranch,kfname, klname, datetime, name, rating):
        self.email = email
        self.rname = rname
        self.rbranch = rbranch
        self.kfname = kfname
        self.klname = klname
        self.datetime = datetime
        self.name = name
        self.rating = rating
class table_K :
    def __init__(self, email, rname, rbranch,pfname, plname, datetime, name, rating):
        self.email = email
        self.rname = rname
        self.rbranch = rbranch
        self.pfname = pfname
        self.plname = plname
        self.datetime = datetime
        self.name = name
        self.rating = rating
def tabel(request):
    cursor = connection.cursor()
    if 'user_email' not in request.session:
        return redirect('/authentication/login')
        
    uar = UserAccRepository()
    if(uar.isRestaurant(request.session.get('user_email'))):
        # return redirect('/authentication/login')
        email = request.session.get('user_email')
        restaurandb = RestaurantRepository()
        restaurant = restaurandb.getByEmail(email)
        daftar_R = []
        querytable1 = f'''
            select t.email, cus.fname , cus.lname, cur.fname,cur.lname, t.datetime, ts.name, t.rating
            from transaction t,
            (Select us.email, us.fname,us.lname from user_acc us natural join customer ) as cus,
            (Select use.email, use.fname,use.lname from user_acc use natural join courier ) as cur,
            transaction_food tf,
            transaction_history th, transaction_status ts
            where t.email = cus.email and t.courierid = cur.email and (t.email, t.datetime) = (tf.email, tf.datetime)
            and (t.email, t.datetime) = (th.email, th.datetime) and th.tsid = ts.id and ts.id in ('TS_STAT003') and tf.rname = '{restaurant.rname}' and tf.rbranch = '{restaurant.rbranch}';'''

        cursor.execute(querytable1)
        hasil1 = cursor.fetchall()

        i = 0
        for row in hasil1 :
            daftar_R.append(table_R(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
            i+=1
        
        context = { 'daftar':  daftar_R}

        return render(request, "tabel_R.html", context)
    
    elif(uar.isCustomer(request.session.get('user_email'))):
        email = request.session.get('user_email')
        customerdb = CustomerRepository()
        customer = customerdb.getByEmail(email)
        daftar_P = []

        querytable2 = f''' select t.email, tf.rname, tf.rbranch, cur.fname,cur.lname, t.datetime, ts.name, t.rating
        from transaction t,
        (Select us.email, us.fname,us.lname from user_acc us natural join customer ) as cus,
        (Select use.email, use.fname,use.lname from user_acc use natural join courier ) as cur,
        transaction_food tf,
        transaction_history th, transaction_status ts
        where t.email = cus.email and t.courierid = cur.email and (t.email, t.datetime) = (tf.email, tf.datetime)
        and (t.email, t.datetime) = (th.email, th.datetime) and th.tsid = ts.id and ts.id in ('TS_STAT004','TS_STAT006') and cus.email = '{customer.email}';'''

        cursor.execute(querytable2)
        hasil2 = cursor.fetchall()
    
        i = 0
        for row in hasil2 :
            daftar_P.append(table_P(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
            i+=1
        
        context = { 'daftar':  daftar_P}

        return render(request, "tabel_P.html", context)
    
    elif(uar.isCourier(request.session.get('user_email'))):
        email = request.session.get('user_email')
        courierdb = CourierRepository()
        courier = courierdb.getByEmail(email)
        daftar_K = []
        print("masuk courie")
        querytable3 = f''' select t.email, tf.rname, tf.rbranch, cus.fname , cus.lname, t.datetime, ts.name, t.rating
        from transaction t,
        (Select us.email, us.fname,us.lname from user_acc us natural join customer ) as cus,
        (Select use.email, use.fname,use.lname from user_acc use natural join courier ) as cur,
        transaction_food tf,
        transaction_history th, transaction_status ts
        where t.email = cus.email and t.courierid = cur.email and (t.email, t.datetime) = (tf.email, tf.datetime)
        and (t.email, t.datetime) = (th.email, th.datetime) and th.tsid = ts.id and ts.id in ('TS_STAT004','TS_STAT006') and cur.email = '{courier.email}';'''

        cursor.execute(querytable3)
        hasil3 = cursor.fetchall()

        # print(hasil3[0])
        for row in hasil3 :
            # print(row[0])
            daftar_K.append(table_K(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
        context = { 'daftar':  daftar_K}

        return render(request, "tabel_K.html", context)
    
    else :
        return redirect('/authentication/login')

class Detail_riwayat:
    def __init__(self, email,datetime,pfname, plname,street,district, city	,province,rname,rbranch,foodname,note,street2,district2,city2,province2, totalfood,totaldiscount	,deliveryfee ,totalprice, pmname,psname,tsname,kfname,klname,platenum,vehicletype,vehiclebrand) :
        self.email = email
        self.datetime = datetime
        self.pfname = pfname
        self.plname = plname

        self.street = street
        self.district = district
        self.city = city
        self.province = province

        self.rname  = rname
        self.rbranch = rbranch
        self.foodname = foodname
        self.note = note

        self.street2 = street2
        self.district2 = district2
        self.city2 = city2
        self.province2 = province2

        self.totalfood = totalfood
        self.totaldiscount = totaldiscount
        self.deliveryfee = deliveryfee
        self.totalprice = totalprice
        self.pmname = pmname
        self.psname = psname
        self.tsname = tsname

        self.kfname = kfname
        self.klname = klname
        self.platenum = platenum
        self.vehicletype = vehicletype
        self.vehiclebrand = vehiclebrand

class detail2 :
    def __init__(self,tsname,datetime) :
        self.tsname = tsname
        self.datetime = datetime

def detail_riwayat(request, email,datetime) :
    cursor = connection.cursor()
   
    querytable4 = f'''select t.email,t.datetime, cus.fname,cus.lname, t.street, t.district, t.city, t.province, tf.rname, tf.rbranch,tf.foodname ,tf.note,r.street,r.district,r.city,r.province, t.totalfood, t.totaldiscount, t.deliveryfee, t.totalprice, pm.name, ps.name,ts.name,
     cur.fname, cur.lname, cur.platenum, cur.vehicletype, cur.vehiclebrand
    from transaction t,
    (Select us.email, us.fname,us.lname from user_acc us natural join customer ) as cus,
    (Select * from courier natural join user_acc ) as cur,
    transaction_food tf, restaurant r,
    transaction_history th, transaction_status ts, payment_method pm, payment_status ps
    where t.email = cus.email and t.courierid = cur.email and (t.email, t.datetime) = (tf.email, tf.datetime) and t.pmid = pm.id and t.psid = ps.id
    and (t.email, t.datetime) = (th.email, th.datetime) and th.tsid = ts.id and ts.id in ('TS_STAT004','TS_STAT006') and (r.rname, r.rbranch) = (tf.rname,tf.rbranch) and t.email = '{email}' and t.datetime = '{datetime}';'''

    cursor.execute(querytable4)
    hasil4 = cursor.fetchall()
    daftar_detail = []
    i = 0
    for row in hasil4 :
        daftar_detail.append(Detail_riwayat(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23],row[24],row[25], row[26], row[27]))
        i+=1
    querytable5 = f'''select ts.name, t.datetime
    from transaction t,
    (Select us.email, us.fname,us.lname from user_acc us natural join customer ) as cus,
    (Select * from courier natural join user_acc ) as cur,
    transaction_food tf, restaurant r,
    transaction_history th, transaction_status ts, payment_method pm, payment_status ps
    where t.email = cus.email and t.courierid = cur.email and (t.email, t.datetime) = (tf.email, tf.datetime) and t.pmid = pm.id and t.psid = ps.id
    and (t.email, t.datetime) = (th.email, th.datetime) and th.tsid = ts.id  and (r.rname, r.rbranch) = (tf.rname,tf.rbranch) and t.email = '{email}' and t.datetime = '{datetime}';'''

    cursor.execute(querytable5)
    hasil5 = cursor.fetchall()
    daftar_detail2 = []
    i = 0
    for row in hasil5 :
        daftar_detail2.append(detail2(row[0],row[1]))
        i+=1
    
    context = { 'daftar':  daftar_detail, 'daftar2': daftar_detail2}

    return render(request, "Detail.html", context)


# select t.email,t.datetime, cus.fname,cus.lname, t.street, t.district, t.city, t.province, tf.rname, tf.rbranch,tf.foodname ,t.totalfood, t.totaldiscount, t.deliveryfee, t.totalprice, pm.name, ps.name,
#      cur.fname, cur.lname, cur.platenum, cur.vehicletype, cur.vehiclebrand
#     from transaction t,
#     (Select us.email, us.fname,us.lname from user_acc us natural join customer ) as cus,
#     (Select * from courier use natural join user_acc ) as cur,
#     transaction_food tf,
#     transaction_history th, transaction_status ts
#     where t.email = cus.email and t.courierid = cur.email and (t.email, t.datetime) = (tf.email, tf.datetime)
#     and (t.email, t.datetime) = (th.email, th.datetime) and th.tsid = ts.id and ts.id in ('TS_STAT004','TS_STAT006');



class Courier:

    def __init__(self, email, platenum, drivinglicensenum, vehicletype, vehiclebrand):
        self.email = email
        self.platenum = platenum
        self.drivinglicensenum = drivinglicensenum
        self.vehicletype = vehicletype
        self.vehiclebrand = vehiclebrand

class CourierRepository:

    def getByEmail(self, email):
        cursor = connection.cursor()
        query = f"""
                    SELECT * FROM courier WHERE email = \'{email}\';
                """
        cursor.execute(query)
        row = cursor.fetchone()
        courier = Courier(row[0], row[1], row[2], row[3], row[4])
        print(row)
        print(courier)
        return courier


    def createCourier(self, email, platenum, drivinglicensenum, vehicletype, vehiclebrand):
        cursor = connection.cursor()

        query = f"""
                    INSERT INTO COURIER
                    VALUES ('{email}','{platenum}', '{drivinglicensenum}' , '{vehicletype}', '{vehiclebrand}');
                    ;    
                """ 
        
        try:
            cursor.execute(query)
            return True
            
        except Exception as error:
            return error