# ...existing code...
from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Create Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///travel.db"

db = SQLAlchemy(app)

class Destination(db.Model): # We create this, so the db will be updated based on the requests from the front-end
    id = db.Column(db.Integer, primary_key = True)
    destination = db.Column(db.String(50), nullable = False) #This make the destination section can't be empty
    country = db.Column(db.String(50), nullable = False)
    rating = db.Column(db.Float, nullable = False)
    
    # Then we should convert the data into dictionary fomat,so we can convert it into json file easily
    def to_dict(self):
        return {
            "id":self.id,
            "destination":self.destination,
            "country":self.country,
            "rating":self.rating
        }
        
    # Then we need to create a quick contact to the manager to set the actual file
with app.app_context():
    db.create_all()
    
#Create Routes
# https://www/thenerdnook.io/
@app.route("/")
def home():
    return jsonify({"message":"Welcome to the travel API"})

# https://www/thenerdnook.io/destinations
@app.route("/destinations", methods = ["GET"]) 
def get_destinations():
    destinations = Destination.query.all() # This will give all rows in the column destination in the database
    return jsonify([destination.to_dict() for destination in destinations])

# https://www/thenerdnook.io/destinations/2
@app.route("/destinations/<int:destination_id>", methods = ["GET"]) 
def get_destination(destination_id):
    destination = Destination.query.get(destination_id)
    if destination:
        return jsonify(destination.to_dict())
    else:
        return jsonify({"Error":"Destination not found!"}), 404
    
# POST
@app.route("/destinations", methods = ["POST"]) 
def add_destination():
    data = request.get_json()
    
    new_destination = Destination(destination = data["destination"],
                                  country = data["country"],
                                  rating = data["rating"])
    db.session.add(new_destination)
    db.session.commit()
    
    return jsonify(new_destination.to_dict()), 201
    
# PUT
@app.route("/destinations/<int:destination_id>", methods = ["PUT"]) 
def update_destination(destination_id):
    data = request.get_json()
    
    destination = Destination.query.get(destination_id)
    if destination: #.destination is the property of the class
        destination.destination = data.get("destination", destination.destination)
        destination.country = data.get("country", destination.country)
        destination.rating = data.get("rating", destination.rating)
        
        db.session.commit()
        
        return jsonify(destination.to_dict())
    else:
        return jsonify({"Error":"Destination not found!"}), 404
    
#DELETE
@app.route("/destinations/<int:destination_id>", methods = ["DELETE"])
def delete_destination(destination_id):
    destination = Destination.query.get(destination_id)
    if destination:
        db.session.delete(destination)
        db.session.commit()
        
        return jsonify({"message":"destination was deleted!"})
    else:
        return jsonify({"Error":"Destination not found!"}), 404
    
if __name__ == "__main__":
    app.run(debug = True)
    
## Conclusion: if we have the front-end, we can use it to send the information to the API, then the API can handle the operation and send it to the database
# then return things to the front-end