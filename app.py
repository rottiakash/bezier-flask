from flask import Flask, render_template, request
import numpy as np
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
    us = request.form["us"]
    res = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <script
      src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
      integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
      integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo"
      crossorigin="anonymous"
    ></script>
    <link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css"
      integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk"
      crossorigin="anonymous"
    />
    <script
      src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"
      integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI"
      crossorigin="anonymous"
    ></script>
    <title>Bezier Curve</title>
  </head>
  <body>
  <div class="d-flex justify-content-center"><h3>Result</h3></div>
  """
    p0 = np.array([float(x) for x in request.form["p0"].split(" ")])
    p1 = np.array([float(x) for x in request.form["p1"].split(" ")])
    p2 = np.array([float(x) for x in request.form["p2"].split(" ")])
    p3 = np.array([float(x) for x in request.form["p3"].split(" ")])

    coords = []

    us = us.split(" ")
    us = list(map(lambda u: float(u), us))
    print(us)
    for u in us:
        b0 = (1 - u) ** 3
        b1 = 3 * u * (1 - u) ** 2
        b2 = 3 * u ** 2 * (1 - u)
        b3 = u ** 3
        line1 = "For u=%f" % (u)
        line2 = "B0,3=%f" % (b0)
        line3 = "B1,3=%f" % (b1)
        line4 = "B2,3=%f" % (b2)
        line5 = "B3,3=%f" % (b3)
        value = (b0 * p0) + (b1 * p1) + (b2 * p2) + (b3 * p3)
        coords.append(value)
        line6 = "P(%f)=" % (u) + str(value)
        line7 = "*******"
        res += """<br><div class="d-flex justify-content-center"><div class="card" style="width: 18rem;">
  
  <div class="card-body">
    %s<br>%s<br>%s<br>%s<br>%s<br>%s<br>%s
  </div>
</div></div><br>""" % (
            line1,
            line2,
            line3,
            line4,
            line5,
            line6,
            line7,
        )

    res += "</body></html>"
    return res


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
