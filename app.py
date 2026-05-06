from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///products.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# MODELO PRODUCT

class Product(db.Model):
    __tablename__ = "products"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Product(name='{self.name}', price={self.price}, stock={self.stock})>"

# CREAR TABLAS

def init_db():
    with app.app_context():
        db.create_all()
        print("✅ Tablas creadas correctamente")

# CREATE (INSERTAR)

def insert_products():
    with app.app_context():
        product1 = Product(name="Laptop", price=1200.50, stock=10)
        product2 = Product(name="Mouse", price=25.99, stock=50)
        product3 = Product(name="Teclado", price=45.00, stock=30)

        db.session.add(product1)
        db.session.add(product2)
        db.session.add(product3)

        db.session.commit()
        print("✅ Productos insertados")

# READ (CONSULTAR)

def query_products():
    with app.app_context():
        print("\n📋 Lista de productos:")
        products = Product.query.all()
        for p in products:
            print(p)

        print("\n🔍 Buscar producto por ID")
        product = Product.query.filter_by(id=1).first()
        if product:
            print("Encontrado:", product)
        else:
            print("Producto no encontrado")

# UPDATE (ACTUALIZAR)

def update_product():
    with app.app_context():
        print("\n✏️ Actualizando producto")

        product = Product.query.filter_by(id=1).first()

        if product:
            product.name = "Laptop Gamer"
            product.price = 1500.00
            product.stock = 5

            db.session.commit()
            print("✅ Producto actualizado:", product)
        else:
            print("❌ Producto no encontrado")

# DELETE (ELIMINAR)

def delete_product():
    with app.app_context():
        print("\n🗑 Eliminando producto")

        product = Product.query.filter_by(id=2).first()

        if product:
            db.session.delete(product)
            db.session.commit()
            print("✅ Producto eliminado")
        else:
            print("❌ Producto no encontrado")

# MAIN

if __name__ == "__main__":
    init_db()
    insert_products()
    query_products()
    update_product()
    delete_product()
    query_products()