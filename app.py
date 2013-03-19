import os
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')
app.DEBUG = True

ZENCODER_API_KEY = os.environ.get("ZENCODER_API_KEY", "no-key-found")
FILEPICKER_API_KEY = os.environ.get("FILEPICKER_API_KEY",
        "AdRiKkbGGRzi7FNSAPS2Iz")  # A sample key to get you started,
                                   #create one at http://www.filepicker.io


@app.route('/')
def hello():
    return render_template('index.html',
            zencoder_api_key=ZENCODER_API_KEY,
            filepicker_api_key=FILEPICKER_API_KEY)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
