from app.models.baseModel import BaseModel
'''
Ammenity class inherite of base model and is linked to one place
'''
class Amenity(BaseModel):
    def __init__(self, name):
        """
        Initialize a review by name given
        args:
            name(str max=50): to define name of the review
        raises:
            TypeError: if attributes have correct type
            ValueError: if attribute respect exigence
        """
        super().__init__()

        if not isinstance(name, str):
            raise TypeError("name must be a string")
        elif len(name) > 50 or len(name) < 1:
            raise ValueError("name must be 50 characters max")
        else:
            self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        elif len(name) > 50:
            raise ValueError("name must be 50 characters max")
        else:
            self._name = name

    def to_dict(self):
        return {'name': self._name,
                'id': self.id}

    def __str__(self):
        return "{}".format(self.name)
