from app.models.baseModel import BaseModel

"""Represents a place in HBnB, with title, location, price, owner, amenities, and reviews."""



class Place(BaseModel):
    def __init__(self, title, price, latitude, longitude, owner, description="", amenities=[], reviews={}):

        super().__init__()

        if not isinstance (title, str):
            raise TypeError ("Title must be a string")
        elif len(title) > 100:
            raise ValueError ("Title must be max 100 characters")
        else:
            self.title = title


        if description is not None and not isinstance (description, str):
            raise TypeError("Description must be a string")
        else:
            self.description = description


        if not isinstance (price, float):
            raise TypeError ("Price must be a float")
        elif price <= 0:
            raise ValueError ("Price must be superior to 0")
        else:
            self.price = price


        if not isinstance (latitude, float):
            raise TypeError ("Latitude must be a float")
        elif latitude < -90 or latitude > 90:
            raise ValueError ("Latitude must be between -90 and 90")
        else:
            self.latitude = latitude


        if not isinstance (longitude, float):
            raise TypeError ("Longitude must be a float")
        elif longitude < -180 or longitude > 180:
            raise ValueError ("Longitude must be between -180 and 180")
        else:
            self.longitude = longitude


        if not hasattr(owner, 'id'):
            raise ValueError("Invalid owner")
        else:
            self.owner = owner


        self.reviews = []
        self.amenities = []



    def add_review(self, review):
        """Add a review to the place"""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place"""
        self.amenities.append(amenity)


    def __str__(self):
        return "{}- {} ({}€)".format(self.title, self.description, self.price)

    def to_dict(self):
        return {
        'id': self.id,
        'title': self.title,
        'description': self.description,
        'latitude': self.latitude,
        'longitude': self.longitude,
        'owner': {
            'id': self.owner.id,
            'first_name': self.owner.first_name,
            'last_name': self.owner.last_name,
            'email': self.owner.email
        } if self.owner else None,
        'amenities': [
            {
                'id': amenity.id,
                'name': amenity.name
            } for amenity in self.amenities
        ]
    }

    def to_bibl(self):
        return {
        'id': self.id,
        'title': self.title,
        'price': self.price,
        'description': self.description,
        'latitude': self.latitude,
        'longitude': self.longitude,
        'owner_id': self.owner.id
    }
