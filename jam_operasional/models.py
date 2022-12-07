from django.db import connection

# Create your models here.
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
        self.operating_hours = []
        self.category = ""
    
class RestaurantRepository:

    # dapet email dari session
    def getByEmail(self, email):
        cursor = connection.cursor()
        query = f"""
                    SELECT * FROM restaurant WHERE email = \'{email}\';
                """
        cursor.execute(query)
        row = cursor.fetchone()
        restaurant = Restaurant(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
        print(row)

        query = f"""
                    SELECT * FROM restaurant_operating_hours WHERE name = \'{restaurant.rname}\' AND branch = \'{restaurant.rbranch}\';
                """
        cursor.execute(query)
        rows = cursor.fetchall()
        
        if row is not None:
            for row in rows:
                restaurant.operating_hours.append(RestaurantOperatingHours(row[0], row[1], row[2], row[3], row[4]))
        print(restaurant.operating_hours)
        # category belom di set
        return restaurant
    
    def addOperatingHours(self, email, day, starthours, endhours):
        cursor = connection.cursor()
        query = f"""
                    SELECT * FROM restaurant WHERE email = \'{email}\';
                """
        cursor.execute(query)
        row = cursor.fetchone()
        restaurant = Restaurant(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])

        try:
            print("try adding new hour")
            query = f"""
                        INSERT INTO restaurant_operating_hours(name, branch, day, starthours, endhours)
                        VALUES (\'{restaurant.rname}\', \'{restaurant.rbranch}\', \'{day}\', \'{starthours}\', \'{endhours}\');
                    """
            cursor.execute(query)
            return True
        except:
            print("cant add hour, prob duplicate key?")
            return False

class RestaurantOperatingHours:

    def __init__(self, name, branch, day, starthours, endhours):
        self.name = name
        self.branch = branch
        self.day = day
        self.starthours = starthours
        self.endhours = endhours
