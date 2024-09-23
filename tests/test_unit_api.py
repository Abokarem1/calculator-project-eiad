
from calculator_client.client import Client
from calculator_client.api.actions import calculate
from calculator_client.models.calculation import Calculation
from calculator_client.models.opertions import Opertions
import pytest


class testApi():
    client = Client("http://localhost:5000/#/actions/calculate")
    def test_api_add(self):
        res = calculate.sync(client=self.client, body=Calculation(operation= Opertions.ADD , operand1=1, operand2=1))
        assert res.result==2
    def test_api_subb(self):
        res = calculate.sync(client=self.client, body=Calculation(operation= Opertions.SUBTRACT , operand1=1, operand2=1))
        assert res.result==0
    def test_api_divide(self):
        res = calculate.sync(client=self.client, body=Calculation(operation= Opertions.DIVIDE , operand1=6, operand2=2))
        assert res.result==3
    def test_api_multply(self):
        res = calculate.sync(client=self.client, body=Calculation(operation= Opertions.MULTIPLY , operand1=1, operand2=4))
        assert res.result==4
        
        