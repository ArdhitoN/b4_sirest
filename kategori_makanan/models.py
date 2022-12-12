from django.db import connection

class FoodCategory:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.used = False

class FoodCategoryRepository:
    def get_all(self):
        cursor = connection.cursor()
        query = """SELECT * FROM FOOD_CATEGORY;"""
        cursor.execute(query)
        rows = cursor.fetchall()
        categories = []
        for row in rows:
            categories.append(FoodCategory(row[0], row[1]))

        used_query = f"""
        SELECT id FROM FOOD_CATEGORY
        WHERE EXISTS (
            SELECT FCategory FROM FOOD
            WHERE FCategory = id);"""
        cursor.execute(used_query)
        rows = cursor.fetchall()
        used_id = []
        for row in rows:
            used_id.append(row[0])
            
        for category in categories:
            if category.id in used_id:
                category.used = True
                
        return categories
        
    def delete_category(self, id):
        cursor = connection.cursor()
        query =f"DELETE FROM FOOD_CATEGORY WHERE id = '{id}';"
        cursor.execute(query)

    def add_category(self, name):
        cursor = connection.cursor()
        get_query = f"""
        SELECT id FROM FOOD_CATEGORY
        ORDER BY id DESC
        LIMIT 1;
        """
        cursor.execute(get_query)
        max_id = int(cursor.fetchall()[0][0][2:])
        id = f"FC{max_id+1}"
        insert_query = f"""
        INSERT INTO FOOD_CATEGORY
        VALUES ('{id}', '{name}');
        """
        cursor.execute(insert_query)