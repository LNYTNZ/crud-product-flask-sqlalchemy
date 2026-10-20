from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#---------------------------------------------------------------
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///tutorial.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#---------------------------------------------------------------
class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Product(name='{self.name}', price={self.price}, stock={self.stock})>"
#---------------------------------------------------------------
def init_db():
    with app.app_context():
        db.create_all()
        print("Base de datos creada satisfactoriamente")
#---------------------------------------------------------------
def insert_products():
    with app.app_context():
        # Crear los productos
        product1 = Product(name="Martillo", price=45.5, stock=10)
        product2 = Product(name="Destornillador", price=20.0, stock=25)
        product3 = Product(name="Taladro", price=350.0)  # el stock queda en 0

        # Agregarlos a la sesión
        db.session.add(product1)
        db.session.add(product2)
        db.session.add(product3)

        # Guardar los cambios
        db.session.commit()
        print("Productos insertados.....")
#---------------------------------------------------------------
def query_products():
    with app.app_context():
        # Traer todos los productos
        products = Product.query.all()
        for product in products:
            print(product)
#---------------------------------------------------------------
def update_product():
    with app.app_context():
        # Buscar el producto con id 1
        product = Product.query.filter_by(id=1).first()
        if product:
            product.price = 50.0
            product.stock = 15
            db.session.commit()
            print("Producto actualizado.....")
        else:
            print("No se encontró el producto")
#---------------------------------------------------------------
def delete_product():
    with app.app_context():
        # Buscar el producto con id 2
        product = Product.query.filter_by(id=2).first()
        if product:
            db.session.delete(product)
            db.session.commit()
            print("Producto eliminado.....")
        else:
            print("No se encontró el producto")
#---------------------------------------------------------------
if __name__ == "__main__":
    init_db()           # Crea la base de datos y las tablas
    insert_products()   # Inserta registros de ejemplo
    query_products()    # Consulta registros
    update_product()    # Actualiza un registro
    query_products()    # Para ver el cambio
    delete_product()    # Elimina un registro
    query_products()    # Para ver que se borró