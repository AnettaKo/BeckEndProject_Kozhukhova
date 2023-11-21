from my_functions.data_storage import read_data
from my_functions.interface import main_menu


if __name__ == '__main__':

    my_wardrobe = read_data()
    main_menu(my_wardrobe)

# from typing import Annotated
# from fastapi import FastAPI, Form
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
#
# app = FastAPI()
#
# origins = ["*"]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
# @app.get("/my_wardrobe")
# async def read_articles():
#     return read_data()
# #
# # @app.get("/items/{item_id}")
# # async def read_item(item_id: int):
# #     return {"item_id": item_id}
# #
# # @app.post("/login/")
# # async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
# #     print (username)
# #     return {"username": username}
# #
# if __name__ == "__main__":
#     uvicorn.run("main:app",
#                 host='127.0.0.1',
#                 port=8000,
#                 reload=True,
#                 log_level="info")