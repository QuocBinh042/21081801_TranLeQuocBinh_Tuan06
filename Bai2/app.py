from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Docker Flask!"

if __name__ == '__main__':
    # Để container có thể nhận kết nối từ bên ngoài, cần lắng nghe trên 0.0.0.0
    app.run(host='0.0.0.0', port=5000, debug=True)