from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo


class Ninja:
    db = "dojos_and_ninjas"

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.dojo_id = data["dojo_id"]

    @classmethod
    def save_ninja(cls, data):
        query = """
            INSERT INTO ninjas
            (first_name, last_name, age, dojo_id)
            VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)
        """
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def delete_one(cls,id):
        query = """
            DELETE FROM ninjas WHERE id = %(id)s;
        """
        data = {'id':id}
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def get_one_ninja(cls,data):
        query = """
            SELECT * FROM ninjas WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def update_ninja(cls,data):
        query = """
            UPDATE ninjas
            SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s
            WHERE id = %(id)s;
        """
        return connectToMySQL(cls.db).query_db(query,data)




