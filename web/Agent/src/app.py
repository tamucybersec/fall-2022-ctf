import flask

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    user_agent = flask.request.headers.get('User-Agent')

    if user_agent == "https://tx.ag/pwnsimps":
        return "gigem{y0u_jus7_g0t_c0c0nu7_m4ll3d}"
    else:
        return "Incorrect User-Agent: \"https://tx.ag/pwnsimps\" required"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

