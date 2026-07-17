from flask import Flask, render_template, request, jsonify
from matrix import *

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():

    try:

        data = request.get_json()

        operation = data["operation"]

        A = data.get("A", [])
        B = data.get("B", [])

        result = None
        error = None

        if operation == "add":

            result, error = add(A, B)

        elif operation == "subtract":

            result, error = subtract(A, B)

        elif operation == "multiply":

            result, error = multiply(A, B)

        elif operation == "determinant":

            if len(A) != len(A[0]):
                error = "Matrix A must be square."
            else:
                result = determinant(A)

        elif operation == "inverse":

            result, error = inverse(A)

        else:

            error = "Unknown operation."

        if error:

            return jsonify({
                "error": error
            })

        return jsonify({
            "result": result
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        })


if __name__ == "__main__":
    app.run(debug=True)