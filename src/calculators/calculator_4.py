from statistics import mean
from typing import Dict, List
from flask import request as FlaskRequest
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class Calculator4:
    def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        mean = self.__calculate_mean(input_data)
        formatted_response = self.__format_response(mean)
        return formatted_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("body mal formatado!")

        input_data = body["numbers"]
        return input_data

    def __calculate_mean(self, numbers: List[float]) -> float:
        return mean(numbers)

    def __format_response(self, mean: float) -> Dict:
        return {"data": {"Calculator": 4, "result": mean}}
