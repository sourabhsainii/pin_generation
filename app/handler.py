from model.pin_generate_request import PinGenerateRequest
from model.pin import Pin
from generatePinService import generatePinService

def generate_pin(
    request: PinGenerateRequest,
    context
) -> Pin:
    """Generates a pin"""

    print("request:::::::: ",request.body)

    pinService = generatePinService()

    data = pinService.generatePin(request.body)

    print('data to save ::: ', data)

    generatedPin = pinService.saveToDB(data)
    return generatedPin