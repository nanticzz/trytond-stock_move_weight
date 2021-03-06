# This file is part of the stock_move_weight module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .move import *
from .shipment import *

def register():
    Pool.register(
        Move,
        Configuration,
        module='stock_move_weight', type_='model')
