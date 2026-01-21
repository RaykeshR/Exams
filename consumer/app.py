from flask import Flask, send_file, render_template_string
import numpy as np
import matplotlib.pyplot as plt
import io, os

app = Flask(__name__)
CSV_PATH = "/data/values.csv"

@app.route("/")
def plot_page():
    if not os.path.exists(CSV_PATH):
        return "<h3>No data found. Please generate an equation in App 1 first.</h3>"
    
    
    data = np.loadtxt(CSV_PATH, delimiter=",", skiprows=1)
    x, y = data[:, 0], data[:, 1]

    
    plt.figure()
    plt.plot(x, y)
    plt.grid(True)
    plt.title("Visualized from Shared Volume")
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close() 
    return send_file(img, mimetype='image/png')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
