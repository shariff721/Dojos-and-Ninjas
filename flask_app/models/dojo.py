from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja


class Dojo:
    db = "dojos_and_ninjas"

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.ninja = []

    @classmethod
    def save_dojo(cls, data):
        qurey = """
            INSERT INTO dojos
            (name) VALUES (%(name)s);
        """
        return connectToMySQL(cls.db).query_db(qurey, data)

    @classmethod
    def get_all_dojos(cls):
        query = """
            SELECT * FROM dojos;
        """
        results = connectToMySQL(cls.db).query_db(query)
        all_dojos = []
        for one_dojo in results:
            all_dojos.append(cls(one_dojo))
        return all_dojos

    @classmethod
    def get_one_dojo(cls, data):
        query = """
            SELECT * FROM dojos
            WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = """
            SELECT * FROM dojos
            JOIN ninjas on ninjas.dojo_id = dojos.id
            WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        print (results)
        one_dojo = cls(results[0])

        for ninja_dict in results:
            ninja_data = {
                'id': ninja_dict['ninjas.id'],
                'dojo_id': ninja_dict['dojo_id'],
                'first_name': ninja_dict['first_name'],
                'last_name': ninja_dict['last_name'],
                'age': ninja_dict['age'],
                'created_at': ninja_dict['ninjas.created_at'],
                'updated_at': ninja_dict['ninjas.updated_at'],
            }
            one_ninja = ninja.Ninja(ninja_data)
            one_dojo.ninja.append(one_ninja)
        return one_dojo

