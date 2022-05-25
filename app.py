from bookface import app

if __name__ == "__main__":
    app.run(debug=True)
    # if we want to make server at our local network add this \/
    #     app.run(debug=True, port = 80, host="0.0.0.0")
