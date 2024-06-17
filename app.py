import onnxruntime as rt

from flask import Flask, redirect, request

from model_parameters import numerical_cols, cat_cols, wrap_num_param, wrap_cat_param
from markup import render_index

inference = rt.InferenceSession("static/model.onnx", providers=["CPUExecutionProvider"])
inputs = inference.get_inputs()
label_name = inference.get_outputs()[0].name
last_predicted_price = 0.

app = Flask(__name__)


@app.route("/")
def index():
    return render_index(last_predicted_price)

@app.route("/predict", methods=["POST"])
def make_prediction():
    global last_predicted_price

    selected_amenities = set(request.form.getlist("amenities"))
    host_is_superhost = 0

    if request.form.get("host_is_superhost"):
        host_is_superhost = 1

    default_true = {'availability_30', 'availability_60', 'availability_90', 'availability_365'}
    default_85 = {'number_of_reviews_ltm', 'review_scores_rating'}
    default_custom = {
        'latitude': 41.40889,
        'longitude': 2.18555,
    }

    model_input = {}

    for inp in inputs:
        input_name = inp.name
        if input_name in default_custom:
            model_input[input_name] = wrap_num_param(default_custom[input_name])
            continue
        elif input_name in default_true:
            model_input[input_name] = wrap_num_param(1.)
            continue
        elif input_name in default_85:
            model_input[input_name] = wrap_num_param(85.)
            continue
        elif input_name.startswith("has_"):
            model_input[input_name] = wrap_num_param(1 if input_name in selected_amenities else 0)
            continue
        elif input_name == "host_is_superhost":
            model_input[input_name] = wrap_num_param(host_is_superhost)
            continue
        elif input_name in numerical_cols:
            model_input[input_name] = wrap_num_param(request.form[input_name])
            continue
        elif input_name in cat_cols:
            model_input[input_name] = wrap_cat_param(request.form[input_name])
            continue

    last_predicted_price = inference.run([label_name], model_input)[0][0][0]

    return redirect("/", code=302)


if __name__ == '__main__':
    app.run()
