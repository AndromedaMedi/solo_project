from db.run_sql import run_sql
from models.city import City
import repositories.country_repository as country_repository
import repositories.user_repository as  user_reposiotry


def save(city):
    sql = "INSERT INTO cities (name, country_id, user_id, visited) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [city.name, city.country.id, city.user.id, city.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city

def select_all():
    cities = []
    sql = "SELECT * FROM cities"
    results = run_sql(sql)
    for row in results:
        country = country_repository.select(row['country_id'])
        user = user_reposiotry.select(row['user_id'])
        city = City(row['name'], country, user, row['visited'], row['id'])
        cities.append(city)
    return cities 

def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result:
        country = country_repository.select(result['country_id'])
        user = user_reposiotry.select(result['user_id'])
        city = City(result['name'], country, user, result['visited'], result['id'])
    return city

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(city):
    sql = "UPDATE cities SET (name, country_id, user_id, visited) = (%s, %s, %s, %s) WHERE id = %s"
    values = [city.name, city.country.id, city.user.id, city.visited, city.id]
    run_sql(sql, values)

