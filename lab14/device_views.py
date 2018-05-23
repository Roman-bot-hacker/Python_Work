from app import app
from app import db
from flask import jsonify
from house_device import HouseDevice
from flask import request
from house_device_structure import DeviceStructure


device_structure = DeviceStructure()


#add device
@app.route("/devices", "POST")
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

    return jsonify(new_device)


#see all
@app.route('/devices', methods=["GET"])
def get_all():
    all_devices = HouseDevice.query.all()
    result = device_structure.dump(all_devices)

    return jsonify(result)


#get device
@app.route('/devices/<id>', methods=["GET"])
def get_device(id):
    device = HouseDevice.query.get(id)

    return jsonify(device)


#update device
@app.route('/devices/<id>', methods=["PUT"])
def device_update(id):
    model = request.json['model']
    producer = request.json['producer']
    power = request.json['power']

    new_device = HouseDevice()
    new_device.device_model = model
    new_device.device_producer = producer
    new_device.device_power = power

    db.session.commit()

    return jsonify(new_device)


#delete device
@app.route('/devices/<id>', methods=["DELETE"])
def device_delete(id):
    device = HouseDevice.query.get(id)
    db.session.delete(device)
    db.session.commit()

    return jsonify(device)