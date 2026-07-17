import datetime
from datetime import datetime, timezone, timedelta
from flask_login import UserMixin
from pgvector.sqlalchemy import Vector
from sqlalchemy.sql import func
from app.extensions import db
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    admin = db.Column(db.Boolean, default=False)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    addresses = db.relationship('Address', backref='user', lazy=True)  # one-to-many
    comments = db.relationship('Comment', backref='user', lazy=True)
    carts = db.relationship('Cart', backref='user', lazy=True)
    price_alerts = db.relationship('PriceAlert', back_populates='user')

    @property
    def current_address(self):
        return next((a for a in self.addresses if a.current_address), None)
