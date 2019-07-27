from bson.objectid import ObjectId
from flask import current_app


def get_all_cars():
    try:
        data = current_app.cars_collection.find({})
    except Exception as e:
        print(e)
        data = None
    return list(data)


def get_car_by_id(_id: str):
    try:
        data = current_app.cars_collection.find_one({'_id': ObjectId(_id)})
    except Exception as e:
        print(e)
        data = None
    return data


def save_car(car):
    try:
        car.pop('_id')
        car['sold'] = False
        current_app.cars_collection.insert(car)
    except Exception as e:
        print(e)


def update_car(car):
    try:
        query = {'_id': ObjectId(car.pop('_id'))}
        current_app.cars_collection.update(query, {'$set': car}, upsert=False)
    except Exception as e:
        print(e)


def delete_car(_id):
    try:
        current_app.cars_collection.remove({'_id': ObjectId(_id)})
    except Exception as e:
        print(e)