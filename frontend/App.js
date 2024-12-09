import React, { useState } from "react";
import CrimeForm from "./components/CrimeForm";
import CrimeMap from "./components/CrimeMap";
import axios from "axios";

const App = () => {
  const [predictions, setPredictions] = useState([]);

  const handlePrediction = (formData) => {
    axios.post("http://localhost:5000/predict", formData)
      .then((response) => {
        setPredictions(response.data.prediction);
      })
      .catch((error) => {
        console.error("Error predicting:", error);
      });
  };

  return (
    <div>
      <h1>Crime Prediction</h1>
      <CrimeForm onSubmit={handlePrediction} />
      {predictions.length > 0 && <CrimeMap predictions={predictions} />}
    </div>
  );
};

export default App;
