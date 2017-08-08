from models import *
from flask.views import MethodView
from schemas import SpinerSchema
from flask import jsonify
from flask import request
from spiner import spiner
from ext import db


class SpienrView(MethodView):
    order_fields = ['color', 'name', 'id']
    filter_fields = ['color', 'name']

    def __init__(self, *args, **kwargs):
        super(SpienrView, self).__init__(*args, **kwargs)
        self.queryset = Spiner.query

    def get(self, spiner_id=None):
        ser = SpinerSchema(many=True)
        spiners = self.queryset
        if spiner_id is None:

            filter_field = request.args.get('filter_by_color', None)
            if filter_field:
                spiners = spiners.filter_by(color=filter_field)
            order_field = request.args.get('order_by', None)
            if order_field and order_field in self.order_fields:
                spiners = spiners.order_by(order_field)
            spiners = spiners.all()
        else:
            spiners = [self.queryset.get(spiner_id)]
        data = ser.dump(spiners).data
        return jsonify(data)

    def post(self):
        ser = SpinerSchema()
        data = request.json
        spiner = ser.load(data, db.session).data
        spiner.save()
        return jsonify(ser.dump(spiner).data), 201


spiner_view = SpienrView.as_view('spiner_api')

spiner.add_url_rule('spiner/', view_func=spiner_view, methods=['GET', 'POST'])
spiner.add_url_rule('spiner/<int:spiner_id>/', view_func=spiner_view, methods=['GET', 'PUT', 'DELETE', 'POST'])
