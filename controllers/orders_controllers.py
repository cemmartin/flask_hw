from flask import Blueprint
from flask import render_template
from models.order_list import orders

orders_blueprint = Blueprint("orders", __name__)

@orders_blueprint.route("/orders")
def index():
    return render_template('index.jinja', title="Ice Cream Shop Orders", orders=orders) #should orders be tasks here?