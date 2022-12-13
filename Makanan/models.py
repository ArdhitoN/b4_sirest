from django.db import connection
from authentication.models import *


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

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
        # print(row)
        return restaurant

    def getByRnameAndRbranch(self, rname, rbranch):
        cursor = connection.cursor()
        query = f"""
                    SELECT * FROM restaurant WHERE rname = '{rname}' and rbranch = '{rbranch}';
                """
        cursor.execute(query)
        row = cursor.fetchone()
        restaurant = Restaurant(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
        # print(row)
        return restaurant

    
    def getAll(self):
        cursor = connection.cursor()
        query = f"""
                    SELECT * FROM restaurant;
                """
        cursor.execute(query)
        
        restaurant_objects = dictfetchall(cursor)

        list_restaurant= []


        for i in range(len(restaurant_objects)):
            restaurant = Restaurant(restaurant_objects[i]['rname'], 
                                    restaurant_objects[i]['rbranch'], 
                                    restaurant_objects[i]['email'],
                                    restaurant_objects[i]['rphonenum'],
                                    restaurant_objects[i]['street'],
                                    restaurant_objects[i]['district'],
                                    restaurant_objects[i]['city'],
                                    restaurant_objects[i]['province'],
                                    restaurant_objects[i]['rating'],
                                    restaurant_objects[i]['rcategory']) 

                                        
            list_restaurant.append(restaurant)

        # print(list_restaurant)

        return list_restaurant




class Restaurant_Category:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Restaurant_Category_Repository:
    def getAllRestaurantCategory(self):
        cursor = connection.cursor()
        query = f"""
                    SELECT * FROM RESTAURANT_CATEGORY;    
                """ 

        cursor.execute(query)

        restaurant_category_objects = dictfetchall(cursor)

        list_restaurant_category= []
        for i in range(len(restaurant_category_objects)):
            restaurant_category = Restaurant_Category(restaurant_category_objects[i]['id'], 
                                            restaurant_category_objects[i]['name']) 
                                        
            list_restaurant_category.append(restaurant_category)

        # print(list_food_category)

        return list_restaurant_category
    
    def getById(self, id):
        cursor = connection.cursor()
        query = f"""
                    SELECT * FROM restaurant_category WHERE id = \'{id}\';
                """

        cursor.execute(query)

        row = cursor.fetchone()

        restaurant_category = Restaurant_Category(row[0], row[1])

        return restaurant_category




class Restaurant_Op_Hours:

    def __init__(self, name, branch, day, starthours, endhours):
        self.name = name
        self.branch = branch
        self.day = day
        self.starthours = starthours
        self.endhours = endhours


class Restaurant_Op_Hours_Repository:
    def getAllRestaurantOpHours(self, rname, rbranch):
        cursor = connection.cursor()
        query = f"""
                    SELECT * FROM RESTAURANT_OPERATING_HOURS
                    where name = '{rname}' and branch = '{rbranch}'
                    ;    
                """ 

        cursor.execute(query)

        restaurant_opHours_objects = dictfetchall(cursor)

        list_restaurant_opHours= []
        for i in range(len(restaurant_opHours_objects)):
            restaurant_opHours = Restaurant_Op_Hours(restaurant_opHours_objects[i]['name'], 
                                            restaurant_opHours_objects[i]['branch'],
                                            restaurant_opHours_objects[i]['day'],
                                            restaurant_opHours_objects[i]['starthours'],
                                            restaurant_opHours_objects[i]['endhours']) 
                                        
            list_restaurant_opHours.append(restaurant_opHours)

        # print(list_food_opHours)

        return list_restaurant_opHours

class Restaurant_Promo:
    def __init__(self, rname, rbranch, pid, start, promoend):
        self.rname = rname
        self.rbranch = rbranch
        self.pid = pid
        self.start = start
        self.promoend = promoend

class Restaurant_Promo_Repository:

    def getAllRestaurantPromo(self, rname, rbranch):
        cursor = connection.cursor()
        query = f"""
                    SELECT * FROM RESTAURANT_PROMO
                    where rname = '{rname}' and rbranch = '{rbranch}'
                    ;    
                """ 

        cursor.execute(query)

        restaurant_promo_objects = dictfetchall(cursor)

        list_restaurant_promo = []
        for i in range(len(restaurant_promo_objects)):
            restaurant_promo = Restaurant_Promo(restaurant_promo_objects[i]['rname'], 
                                            restaurant_promo_objects[i]['rbranch'],
                                            restaurant_promo_objects[i]['pid'],
                                            restaurant_promo_objects[i]['start'],
                                            restaurant_promo_objects[i]['promoend']) 
                                        
            list_restaurant_promo.append(restaurant_promo)

        # print(list_food_promo)

        return list_restaurant_promo


class Food:

    def __init__(self, RName, RBranch, FoodName, Description, Stock, Price, FCategory):
        self.RName = RName
        self.RBranch = RBranch
        self.FoodName = FoodName
        self.Description = Description
        self.Stock = Stock
        self.Price = Price
        self.FCategory = FCategory

        self.FCategoryName = ""
        self.IngredientName = []

    

class FoodRepository:
    
    def getAllRestaurantFood(self, rname, rbranch):
        cursor = connection.cursor()
        query = f"""
                    SELECT * FROM food WHERE rname = '{rname}' and rbranch = '{rbranch}';
                """
        cursor.execute(query)
        
        food_objects = dictfetchall(cursor)

        list_food = []
        for i in range(len(food_objects)):
            food = Food(food_objects[i]['rname'], 
                        food_objects[i]['rbranch'],
                        food_objects[i]['foodname'],
                        food_objects[i]['description'],
                        food_objects[i]['stock'], 
                        food_objects[i]['price'], 
                        food_objects[i]['fcategory']
            )

                                        
            list_food.append(food)

        # print(list_food_promo)

        return list_food

    def getFoodByName(self, rname, rbranch, foodname):
        cursor = connection.cursor()
        query = f"""
                    SELECT * FROM food WHERE rname = '{rname}' and rbranch = '{rbranch}' and foodname= '{foodname}'
                    ;
                """
        cursor.execute(query)
        
        food_objects = dictfetchall(cursor)

        list_food = []
        for i in range(len(food_objects)):
            food = Food(food_objects[i]['rname'], 
                        food_objects[i]['rbranch'],
                        food_objects[i]['foodname'],
                        food_objects[i]['description'],
                        food_objects[i]['stock'], 
                        food_objects[i]['price'], 
                        food_objects[i]['fcategory']
            )

                                        
            list_food.append(food)

        # print(list_food_promo)

        return list_food[0]

    
    def createFood(self, rname, rbranch, foodname, description, stock, price, fcategory):
        
        cursor = connection.cursor()

        query = f"""
                    INSERT INTO FOOD
                    VALUES ('{rname}','{rbranch}', '{foodname}' , '{description}', {stock}, {price}, '{fcategory}');
                    ;    
                """ 
        
        
        try:
            cursor.execute(query)
            
            return True
            
        except Exception as error:
            return error
    


    def updateFood(self, rname, rbranch, foodname, new_description, new_stock, new_price, new_fcategory):
        
        # Ingredient diupdate terpisah

        cursor = connection.cursor()
        query = f"""
                    UPDATE FOOD
                    SET description= '{new_description}', stock= {new_stock}, price= {new_price}, fcategory = '{new_fcategory}'
                    WHERE rname= '{rname}' and rbranch = '{rbranch}' and foodname = '{foodname}'
                    ;    
                """ 
        
        
        try:
            cursor.execute(query)
            return True
            
        except Exception as error:
            return error


    def deleteFood(self, rname, rbranch, foodname):

        cursor = connection.cursor()

      
        query = f"""
                    DELETE FROM FOOD
                    WHERE rname= '{rname}' and rbranch = '{rbranch}' and foodname = '{foodname}'
                    ;    
                """ 
        try:
            cursor.execute(query)
            return True

        except Exception as error:
            return error

            


class Food_Category:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Food_Category_Repository:
    def getAllFoodCategory(self):
        cursor = connection.cursor()
        query = f"""
                    SELECT * FROM FOOD_CATEGORY;    
                """ 

        cursor.execute(query)

        food_category_objects = dictfetchall(cursor)

        list_food_category= []
        for i in range(len(food_category_objects)):
            food_category = Food_Category(food_category_objects[i]['id'], 
                                            food_category_objects[i]['name']) 
                                        
            list_food_category.append(food_category)

        # print(list_food_category)

        return list_food_category

    def getCategoryById(self, id):
        cursor = connection.cursor()
        query = f"""
                    SELECT * FROM FOOD_CATEGORY
                    where id= '{id}';    
                """ 

        cursor.execute(query)

        food_category_objects = dictfetchall(cursor)

        food_category = Food_Category(food_category_objects[0]['id'], 
                                            food_category_objects[0]['name']) 
                                        
        # print(list_food_category)

        return food_category



class Ingredient:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Ingredient_Repository:
    def getAllIngredient(self):
        cursor = connection.cursor()
        query = f"""
                    SELECT * FROM INGREDIENT;    
                """ 

        cursor.execute(query)

        ingredient_objects = dictfetchall(cursor)

        list_ingredient= []
        for i in range(len(ingredient_objects)):
            ingredient = Ingredient(ingredient_objects[i]['id'], 
                                            ingredient_objects[i]['name']) 
                                        
            list_ingredient.append(ingredient)

        # print(list_ingredient)

        return list_ingredient

    def getIngredientById(self, id):
        cursor = connection.cursor()
        query = f"""
                    SELECT * FROM INGREDIENT
                    where id= '{id}';    
                """ 

        cursor.execute(query)

        ingredient_object = dictfetchall(cursor)

        ingredient = Ingredient(ingredient_object[0]['id'], 
                                            ingredient_object[0]['name']) 
                                        
        # print(list_food_category)

        return ingredient



class Food_Ingredient:
    def __init__(self, RName, RBranch, FoodName, Ingredient):
        self.RName = RName
        self.RBranch = RBranch
        self.FoodName = FoodName
        self.Ingredient = Ingredient


class Food_Ingredient_Repository:
    
    def getIngredientId(self, rname, rbranch, foodname):
        cursor = connection.cursor()
        query = f"""
                    SELECT ingredient FROM FOOD_INGREDIENT
                    where rname= '{rname}' and rbranch = '{rbranch}'
                    and foodname = '{foodname}'
                    ;    
                """ 

        cursor.execute(query)

        ingredient_id_objects = dictfetchall(cursor)

        list_ingredient_id = []

        for i in range(len(ingredient_id_objects)):
            list_ingredient_id.append(ingredient_id_objects[i]['ingredient'])
                                        
        # print(list_food_category)

        return list_ingredient_id


    def createFoodIngredient(self, rname, rbranch, foodname, ingredient):
        
        cursor = connection.cursor()

        query = f"""
                    INSERT INTO FOOD_INGREDIENT
                    VALUES ('{rname}','{rbranch}', '{foodname}' , '{ingredient}')
                    ;    
                """ 
        
        
        try:
            cursor.execute(query)
            return True
            
        except Exception as error:
            return error
    
    
    def deleteFoodIngredient(self, rname, rbranch, foodname, ingredient):

        cursor = connection.cursor()
        query = f"""
                    DELETE FROM FOOD_INGREDIENT
                    WHERE rname= '{rname}' and rbranch = '{rbranch}' and foodname = '{foodname}' and ingredient= '{ingredient}'
                    ;    
                """ 
        
        cursor.execute(query)
        return True
            