import React, { useState } from "react";
import "./CurrencyConverter.css";

const CurrencyConverter = () => {
  const [amount, setAmount] = useState("");
  const [fromCurrency, setFromCurrency] = useState("USD");
  const [toCurrency, setToCurrency] = useState("INR");
  const [convertedAmount, setConvertedAmount] = useState(null);

  const swapCurrencies = () => {
    setFromCurrency(toCurrency);
    setToCurrency(fromCurrency);
    setConvertedAmount(null); // Clear result when swapping
  };

  const handleConvert = async () => {
    if (!amount) return;
    
    try {
      const response = await fetch(
        `http://127.0.0.1:8000/convert/?amount=${amount}&from=${fromCurrency}&to=${toCurrency}`
      );
      const data = await response.json();
      setConvertedAmount(data.converted_amount);
    } catch (error) {
      console.error("Error fetching exchange rate:", error);
    }
  };

  return (
    <div className="container">
      <h2>Currency Converter</h2>
      <input
        type="number"
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
        placeholder="Enter Amount"
      />
      <div className="currency-select">
        <select 
          value={fromCurrency} 
          onChange={(e) => {
            setFromCurrency(e.target.value);
            setConvertedAmount(null); // Clear previous result
          }}
        >
          <option value="USD">USD</option>
          <option value="INR">INR</option>
          <option value="EUR">EUR</option>
          <option value="AUD">AUD</option>
          <option value="GBP">GBP</option>
        </select>

        {/* Swap Button */}
        <button className="swap-button" onClick={swapCurrencies}>🔄</button>

        <select 
          value={toCurrency} 
          onChange={(e) => {
            setToCurrency(e.target.value);
            setConvertedAmount(null); // Clear previous result
          }}
        >
          <option value="USD">USD</option>
          <option value="INR">INR</option>
          <option value="EUR">EUR</option>
          <option value="AUD">AUD</option>
          <option value="GBP">GBP</option>
        </select>
      </div>
      <button onClick={handleConvert}>Get Exchange Rate</button>

      {convertedAmount !== null && (
        <p>
          {amount} {fromCurrency} = {convertedAmount} {toCurrency}
        </p>
      )}
    </div>
  );
};

export default CurrencyConverter;
