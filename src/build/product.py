from faker import Faker
import random

fake = Faker('en_US')

class Productbuild:

    def __init__(self):
        self.result = {}
        self.reset()

    def set_id(self, id_categor=fake.postcode()):
        self.result['category_id'] = id_categor
        return self

    def set_created(self, created=fake.country()):
        self.result['created_at'] = created
        return self

    def set_description(self, description=fake.hostname()):
        self.result["description"] = description
        return self

    def set_image(self, image=fake.url()):
        self.result["image_url"] = image
        return self

    def set_name(self, name=fake.name()):
        self.result["name"] = name
        return self

    def set_photos(self, photo=[]):
        self.result["photos"] = photo
        return self

    def set_price(self, cost=random.random() * 1000):
        self.result["price"] = cost
        return self

    def set_product_id(self, product_id=fake.postcode()):
        self.result["product_id"] = product_id
        return self

    def set_quantity(self, count=random.randint(0, 100)):
        self.result["quantity"] = count
        return self

    def set_rating(self, rep=random.randint(0,100)):
        self.result["rating"] = rep
        return self

    def set_ubgrate(self, coment=fake.postcode()):
        self.result["updated_at"] = coment
        return self

    def reset(self):
        self.set_id()
        self.set_created()
        self.set_product_id()
        self.set_ubgrate()
        self.set_quantity()
        self.set_description()
        self.set_name()
        self.set_image()
        self.set_price()
        self.set_photos()
        self.set_rating()
        return self

    def build(self):
        return self.result