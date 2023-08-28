import random
import string
from model.pin_generate_request import PinGenerateRequest
from model.pin import Pin

from dbConfig.dbConfig import intializeDB

class generatePinService():
    
    def generatePin(
            self,
            request:PinGenerateRequest
    ):
        print("request::::::: ", request["group_id"])
        group_id = request['group_id']
        # entity = request['entity']

        alphanumeric_characters = string.ascii_letters + string.digits

        random_characters = ''.join(random.choice(alphanumeric_characters) for _ in range(5))

        special_character = random.choice('!@#$%^&*')

        index_to_insert = random.randint(0, len(random_characters))

        pin = str(group_id) + '_' + random_characters[:index_to_insert] + special_character+ random_characters[index_to_insert:]

        print("Generated PIN:", pin)

        data = {**request,"pin":pin,"group_id":group_id}
        # data["pin"] = pin

        print('data::::::::: ', data)

        pin = self.saveGeneratePin(data)

        db =  intializeDB.createEngine()

        db_pin = Pin(**data)
        db.add(db_pin)
        db.commit()
        db.refresh(db_pin)

        return pin