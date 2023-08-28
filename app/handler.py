from aws_lambda_powertools import logging, tracing

from model.pin_generate_request import PinGenerateRequest
from model.pin import Pin
from generatePinService import generatePinService

logger = logging.Logger()
tracer = tracing.Tracer()

def generate_pin(
    request: PinGenerateRequest,
    context
) -> Pin:
    """Generates a pin"""

    print("request:::::: ", request.body)

    pinService = generatePinService()

    pinService.generatePin(request.body)
