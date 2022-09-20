# coding: utf-8
from sqlalchemy import CheckConstraint, Column, DECIMAL, Date, DateTime, ForeignKey, Index, Integer, SmallInteger, String, Text
from sqlalchemy.dialects.mysql import MEDIUMBLOB, MEDIUMTEXT, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://valhuber.github.io/ApiLogicServer/Project-Rebuild/#rebuilding

from safrs import SAFRSBase
from safrs.util import classproperty

import safrs

BaseClassic = declarative_base()
metadata = BaseClassic.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.mysql import *
########################################################################################################################

"""
class Office(SAFRSBase, Base):
    __tablename__ = 'offices'

    officeCode = Column(String(10), primary_key=True)
    city = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    addressLine1 = Column(String(50), nullable=False)
    addressLine2 = Column(String(50))
    state = Column(String(50))
    country = Column(String(50), nullable=False)
    postalCode = Column(String(15), nullable=False)
    territory = Column(String(10), nullable=False)
    allow_client_generated_ids = True

    EmployeeList = relationship('Employee', cascade_backrefs=True, backref='office')


class Productline(SAFRSBase, Base):
    __tablename__ = 'productlines'

    productLine = Column(String(50), primary_key=True)
    textDescription = Column(String(4000))
    htmlDescription = Column(MEDIUMTEXT)
    image = Column(MEDIUMBLOB)
    allow_client_generated_ids = True

    ProductList = relationship('Product', cascade_backrefs=True, backref='productline')



class Employee(SAFRSBase, Base):
    __tablename__ = 'employees'

    employeeNumber = Column(Integer, primary_key=True)
    lastName = Column(String(50), nullable=False)
    firstName = Column(String(50), nullable=False)
    extension = Column(String(10), nullable=False)
    email = Column(String(100), nullable=False)
    officeCode = Column(ForeignKey('offices.officeCode'), nullable=False, index=True)
    reportsTo = Column(ForeignKey('employees.employeeNumber'), index=True)
    jobTitle = Column(String(50), nullable=False)
    allow_client_generated_ids = True

    # see backref on parent: office = relationship('Office', cascade_backrefs=True, backref='EmployeeList')
    # see backref on parent: parent = relationship('Employee', remote_side=[employeeNumber], cascade_backrefs=True, backref='EmployeeList')

    parent = relationship('Employee', remote_side=[employeeNumber], cascade_backrefs=True, backref='EmployeeList')  # special handling for self-relationships
    CustomerList = relationship('Customer', cascade_backrefs=True, backref='employee')


class Product(SAFRSBase, Base):
    __tablename__ = 'products'

    productCode = Column(String(15), primary_key=True)
    productName = Column(String(70), nullable=False)
    productLine = Column(ForeignKey('productlines.productLine'), nullable=False, index=True)
    productScale = Column(String(10), nullable=False)
    productVendor = Column(String(50), nullable=False)
    productDescription = Column(Text, nullable=False)
    quantityInStock = Column(SmallInteger, nullable=False)
    buyPrice = Column(DECIMAL(10, 2), nullable=False)
    MSRP = Column(DECIMAL(10, 2), nullable=False)
    allow_client_generated_ids = True

    # see backref on parent: productline = relationship('Productline', cascade_backrefs=True, backref='ProductList')

    OrderdetailList = relationship('Orderdetail', cascade_backrefs=True, backref='product')

"""

class CustomerClassic(SAFRSBase, BaseClassic):
    __tablename__ = 'customers'

    customerNumber = Column(Integer, primary_key=True)
    customerName = Column(String(50), nullable=False)
    contactLastName = Column(String(50), nullable=False)
    contactFirstName = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    addressLine1 = Column(String(50), nullable=False)
    addressLine2 = Column(String(50))
    city = Column(String(50), nullable=False)
    state = Column(String(50))
    postalCode = Column(String(15))
    country = Column(String(50), nullable=False)
    salesRepEmployeeNumber = Column(ForeignKey('employees.employeeNumber'), index=True)
    creditLimit = Column(DECIMAL(10, 2))
    allow_client_generated_ids = True

    @classproperty
    def _s_collection_name(cls):
        return "CustomerClassic"
        # return "My:User"
    # see backref on parent: employee = relationship('Employee', cascade_backrefs=True, backref='CustomerList')

    # OrderList = relationship('Order', cascade_backrefs=True, backref='customer')
    # PaymentList = relationship('Payment', cascade_backrefs=True, backref='customer')

"""
class Order(SAFRSBase, Base):
    __tablename__ = 'orders'

    orderNumber = Column(Integer, primary_key=True)
    orderDate = Column(Date, nullable=False)
    requiredDate = Column(Date, nullable=False)
    shippedDate = Column(Date)
    status = Column(String(15), nullable=False)
    comments = Column(Text)
    customerNumber = Column(ForeignKey('customers.customerNumber'), nullable=False, index=True)
    allow_client_generated_ids = True

    # see backref on parent: customer = relationship('Customer', cascade_backrefs=True, backref='OrderList')

    OrderdetailList = relationship('Orderdetail', cascade_backrefs=True, backref='order')


class Payment(SAFRSBase, Base):
    __tablename__ = 'payments'

    customerNumber = Column(ForeignKey('customers.customerNumber'), primary_key=True, nullable=False)
    checkNumber = Column(String(50), primary_key=True, nullable=False)
    paymentDate = Column(Date, nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    allow_client_generated_ids = True

    # see backref on parent: customer = relationship('Customer', cascade_backrefs=True, backref='PaymentList')


class Orderdetail(SAFRSBase, Base):
    __tablename__ = 'orderdetails'

    orderNumber = Column(ForeignKey('orders.orderNumber'), primary_key=True, nullable=False)
    productCode = Column(ForeignKey('products.productCode'), primary_key=True, nullable=False, index=True)
    quantityOrdered = Column(Integer, nullable=False)
    priceEach = Column(DECIMAL(10, 2), nullable=False)
    orderLineNumber = Column(SmallInteger, nullable=False)
    allow_client_generated_ids = True

    # see backref on parent: order = relationship('Order', cascade_backrefs=True, backref='OrderdetailList')
    # see backref on parent: product = relationship('Product', cascade_backrefs=True, backref='OrderdetailList')
"""