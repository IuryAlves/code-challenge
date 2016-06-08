# coding: utf-8


from src.app import app


if __name__ == '__main__':
    PORT = app.config.get("PORT", 5000)
    HOST = app.config.get("HOST", 'localhost')
    app.run(host=HOST, port=PORT)
