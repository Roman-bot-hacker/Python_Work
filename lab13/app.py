from flask import Flask, abort
from flask_restful import Api, Resource, reqparse, fields, marshal

app = Flask(__name__, static_url_path="")
api = Api(app)

devices = [
    {
        'Id': 0,
        'producer': 'Default',
        'power': 0
    }
]

devices_fields = {
    'id': fields.Integer,
    'producer': fields.String,
    'power': fields.Integer,
}


class DeviceList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', type=int, required=True, help='No Id provided', location='json')
        self.reqparse.add_argument('producer', type=str, location='json')
        self.reqparse.add_argument('power', type=int, location='json')
        super(DeviceList, self).__init__()  # super().__init__() / GoodsList.__init__(self)

    def put(self):
        args = self.reqparse.parse_args()
        device = {
            'Id': devices[-1]['Id'] + 1,
            'id': args['id'],
            'producer': args['producer'],
            'power': args['power']
        }
        devices.append(device)

    def post(self):
        args = self.reqparse.parse_args()
        device = [device for device in devices if device.get('id') == args['id']]
        if len(device) == 0:
            abort(404)
        device = device[0]
        args = self.reqparse.parse_args()
        for key, value in args.items():
            if value is not None:
                device[key] = value

    def get(self, id):
        device = [device for device in devices if device.get('id') == id]
        if len(device) == 0:
            abort(404)
        return {'Good': marshal(device[0], devices_fields)}

    def delete(self, id):
        device = [device for device in devices if device.get('id') == id]
        if len(device) == 0:
            abort(404)
        devices.remove(device[0])
        return {'result': True}


api.add_resource(DeviceList, '/devices', endpoint='devices')
api.add_resource(DeviceList, '/devices/<int:id>', endpoint='device')

if __name__ == '__main__':
    app.run(debug=True)
