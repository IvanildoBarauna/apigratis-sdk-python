from api_brasil import APIBrasilClient
from api_brasil.features.interfaces import APIBrasilFeature



class SMSApi(APIBrasilFeature):
    """ Class to interact with the Vehicles API. """
    def __init__(self, api_brasil_client: APIBrasilClient, device_token: str):
        self.api_brasil_client = api_brasil_client
        self.device_token = device_token

    def set_phone_number(self, number: str):
        """ Set the plate to be used in the API requests """
        self.number = number
    
    def send(self, message: str) -> tuple:
        """ Method to consult the API with the plate set in the class. """
        endpoint = "/sms/send"

        if not self.number:
            raise ValueError("The phone_number number is not set. Use the 'set_phone_number' method to set the phone_number.")
        
        response, status_code = self.api_brasil_client.post_request(
            endpoint=endpoint,
            device_token=self.device_token,
            body={
                "number": self.number,
                "message": message
            }
        )

        return response, status_code