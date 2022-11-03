from fastapi import FastAPI
import uvicorn

from source.roman_number_converter import RomanNumeralsConverter

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/roman_converter/{integer_number}")
def read_item(integer_number: int, Converted_Roman_Numberal: str):
    roman_converter_obj = RomanNumeralsConverter()
    roman_letter = roman_converter_obj.roman_converter(integer_number)
    return {"integer_number": integer_number, "converted_roman_numberal": roman_letter}


if __name__ == "__main__":
    uvicorn.run(app)