{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4d4679ca-77c2-4a12-8567-f3b9730dbffa",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, request, jsonify\n",
    "import joblib\n",
    "\n",
    "app = Flask(__name__)\n",
    "model = joblib.load(\"iris_model.pkl\")\n",
    "\n",
    "@app.route('/predict', methods=['POST'])\n",
    "def predict():\n",
    "    data = request.get_json()\n",
    "    features = [data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']]\n",
    "    prediction = model.predict([features])\n",
    "    return jsonify({'prediction': int(prediction[0])})\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
