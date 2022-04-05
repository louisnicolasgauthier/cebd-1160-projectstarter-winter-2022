from flask import Flask, jsonify
import BAL.customer

def sales_service():

    app = Flask(__name__)
    app.config["DEBUG"] = True

    @app.route('/v1/customers', methods=['GET'])
    def get_all_sales():
        return jsonify(BAL.customer.get_all_customers())

    @app.route('/v1/customers/<id>', methods=['GET'])
    def get_sale_by_id(id):
        return jsonify(BAL.customer.get_customer(id)[0])

    @app.route('/v1/customers/Search/Last/<lastname>', methods=['GET'])
    def get_sale_by_lastname(lastname):
        return jsonify(BAL.customer.get_customer_by_last_name(lastname))

    @app.route('/', methods=['GET'])
    def home():
        return """<h1>Sales Statistics</h1><p>This site is a prototype API for reporting sales
         statistics for use with Python and Pandas clients.</p>"""

    app.run(host='0.0.0.0')