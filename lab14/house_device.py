from app import db


class HouseDevice(db.Model):
    __tablename__ = "house_devices"
    device_id = db.Column('id', db.Integer, primary_key = True)
    device_model = db.Column('model', db.String(20))
    device_producer = db.Column('producer', db.String(20))
    device_power = db.Column('power', db.Integer)

    def to_string(self):
        return str("device id: " + str(self.device_id) + "\ndevice model: " + str(self.device_model) + "\ndevice producer: " + str(self.device_producer) + "\ndevice power: " + str(self.device_power))