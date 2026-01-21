from flask import Flask, request, render_template_string
import numpy as np

app = Flask(__name__)
CSV_PATH = "/data/values.csv"

@app.route("/", methods=["GET", "POST"])
def home():
    msg = ""
    if request.method == "POST":
        eq = request.form["equation"]
        x = np.linspace(-10, 10, 400)
        try:
            
            y = eval(eq, {"__builtins__": {}}, {"x": x, "np": np})
            
            np.savetxt(CSV_PATH, np.c_[x, y], delimiter=",", header="x,y", comments='')
            msg = f"Successfully saved equation: {eq}"
        except Exception:
            msg = "Error in equation! Use 'x' and 'np.sin(x)' etc."
            
    return render_template_string('''
        <h2>Step 1: Equation Generator</h2>
        <form method="post">
            y = <input type="text" name="equation" placeholder="x**2 + 3*x" size="40">
            <button type="submit">Compute & Save</button>
        </form>
        <p style="color: blue;">{{ msg }}</p>
        <p><a href="http://localhost:8082" target="_blank">Go to Page 2 to see the Plot →</a></p>
    ''', msg=msg)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
