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
        print("request::::::: ", request["applicationId"])
        group_id = request['applicationId']
        # entity = request['entity']

        # extracting last three characters from the ApplicationID
        application_id = str(group_id)[-3:]

        # Create a String of Alpha numeric characters by concatenating ASCII and numbers
        alphanumeric_characters = string.ascii_letters + string.digits

        # generating random characters by choosing a random char from alphanumeric_characters with length 6
        random_characters = ''.join(random.choice(alphanumeric_characters) for _ in range(5))

        # randomly choosing a special char
        special_character = random.choice('!@#$%^&*')

        # generating a random index for special char to place anywhere in the random_characters
        index_to_insert = random.randint(0, len(random_characters))

        # finally concatenating application_id/group_id with above variables to get PIN
        pin = application_id + '_' + random_characters[:index_to_insert] + special_character+ random_characters[index_to_insert:]

        print("generatePin:: pin", pin)

        data = {"pin":pin,"group_id":group_id}

        return data

    def saveToDB(self,data):
        dbSession =  intializeDB.createDBSession()

        db_pin = Pin(**data)
        dbSession.add(db_pin)
        dbSession.commit()
        dbSession.refresh(db_pin)

        # closing the DB session
        dbSession.close()

        return data["pin"]