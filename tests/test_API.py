import requests
from calculator_client.client import Client
from calculator_client.api.actions import calculate 
from calculator_client.models.calculation import Calculation
from calculator_client.models.opertions import Opertions
from calculator_client.models.result_response import ResultResponse

class TestCalculatorAPI():
    def test_calculator_add(self):
        url = "http://localhost:5000/calculate"

        payload = {
            "operation": "add",
            "operation1": 1,
            "operation2": 2,
        }
        response = requests.post(url, json=payload)
    def test_generated_code_test(self):
        client = Client("http://localhost:5000")
        response = calculate.sync(client = client, body = Calculation(Opertions.ADD, operand1=1, operand2=1))
        assert isinstance(response, ResultResponse)
        assert response.result == 3