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

    
    return f"""
Min (La valeur Min du signal): {np.min(y)} <br>
Max (La valeur Max du signal): {np.max(y)} <br>
Moyenne (Average) : {np.mean(y)} <br>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
