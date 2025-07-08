{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4d4679ca-77c2-4a12-8567-f3b9730dbffa",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import joblib\n",
    "\n",
    "model = joblib.load('iris_model.pkl')\n",
    "\n",
    "st.title(\"🌸 Iris Flower Classifier\")\n",
    "\n",
    "sepal_length = st.slider(\"Sepal Length\", 4.0, 8.0)\n",
    "sepal_width = st.slider(\"Sepal Width\", 2.0, 4.5)\n",
    "petal_length = st.slider(\"Petal Length\", 1.0, 7.0)\n",
    "petal_width = st.slider(\"Petal Width\", 0.1, 2.5)\n",
    "\n",
    "if st.button(\"Predict\"):\n",
    "    pred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])\n",
    "    st.write(f\"Prediction: {pred[0]}\")\n"
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
