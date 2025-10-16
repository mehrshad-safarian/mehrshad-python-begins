from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/info')  # مسیر API
def info():
    data = {
        "name": "M0023S",
        "job": "Developer",
        "favorite": "Metal Gear"
    }
    return jsonify(data)  # داده رو به JSON تبدیل می‌کنه

if __name__ == '__main__':
    app.run(debug=True)
