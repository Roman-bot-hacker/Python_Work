from app import app
from flask import request
from app import db
from house_device import HouseDevice

@app.route('/')
def index():
    firstmember = HouseDevice.query.first()
    return '<h1> Here you can find device list! </h1>'

@app.route('/device')
def view():
    device = HouseDevice.query.first()
    if device is not None:
        return str('First member name \n' + device.to_string())
    else:
        return "Device with this id does not exist"

@app.route('/device/<id>')
def get_device(id):
    device = HouseDevice.query.get(id)
    if device is not None:
        return device.to_string()
    else:
        return "Device with this id does not exist"

@app.route('/device', methods=['POST'])
def add_device():
    device_id = request.json['id']
    model = request.json['model']
    producer = request.json['producer']
    power = request.json['power']

    new_device = HouseDevice()
    new_device.device_id = device_id
    new_device.device_model = model
    new_device.device_producer = producer
    new_device.device_power = power

    db.session.add(new_device)
    db.session.commit()

    return str(new_device.to_string())

@app.route('/device/<id>', methods=['PUT'])
def device_update(id):
    model = request.json['model']
    producer = request.json['producer']
    power = request.json['power']

    new_device = HouseDevice.query.get(id)
    new_device.device_id = id
    new_device.device_model = model
    new_device.device_producer = producer
    new_device.device_power = power

    db.session.commit()

    return new_device.to_string()

@app.route('/device/<id>', methods=['DELETE'])
def device_delete(id):
    device = HouseDevice.query.get(id)
    db.session.delete(device)
    db.session.commit()

    return str("Deleting succssesful")