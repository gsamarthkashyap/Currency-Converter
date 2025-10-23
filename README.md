# Currency Converter (Full Stack)

## 📌 Project Overview
The Currency Converter is a web application designed to provide real-time currency conversion rates. It helps users quickly convert amounts between different currencies with a simple and intuitive interface. This project demonstrates full-stack development by integrating a React frontend with a Django backend, along with external API support for exchange rate data.

This is a full-stack Currency Converter application built using:
- **Frontend**: React (for UI)
- **Backend**: Django (API for exchange rates)
- **Database**: SQLite (for storing user preferences, if needed)
- **API Integration**: Fetching real-time currency exchange rates

The app allows users to select two currencies and get the converted amount instantly.

---

## 🛠️ Installation & Setup

### 🔹 Prerequisites
Ensure you have the following installed on your system:
- Node.js (for frontend) ➜ [Download Node.js](https://nodejs.org/)
- Python (for backend) ➜ [Download Python](https://www.python.org/downloads/)
- Git (for version control) ➜ [Download Git](https://git-scm.com/)

### 🔹 Clone the Repository
```sh
git clone https://github.com/your-username/currency-converter.git
cd currency-converter
```

---

## 🖥️ Frontend Setup (React)
```sh
cd frontend
npm install   # Install dependencies
npm start     # Run the frontend (localhost:3000)
```

---

## 🖥️ Backend Setup (Django)
```sh
cd backend
python -m venv venv        # Create a virtual environment
source venv/bin/activate   # Activate virtual environment (Mac/Linux)
venv\Scripts\activate      # Activate virtual environment (Windows)

pip install -r requirements.txt  # Install dependencies
python manage.py migrate         # Apply database migrations
python manage.py runserver       # Start Django server (localhost:8000)
```

---

## 🌎 API Integration
The backend fetches real-time exchange rates from an external API.
To set up your API key:
1. Get a free API key from [ExchangeRate-API](https://www.exchangerate-api.com/)
2. Create a `.env` file in the `backend` directory and add:
   ```sh
   EXCHANGE_RATE_API_KEY=your_api_key_here
   ```
3. Restart the backend server.

---

## 🚀 Features
✅ Convert between multiple currencies

✅ Real-time exchange rates

✅ Modern & responsive UI (React)

✅ Backend API for currency conversion (Django)

✅ Error handling for API failures

✅ Simple database setup (optional)

---

## 🛠️ Contribution
1. **Fork** the repository.
2. **Clone** your forked repository:
   ```sh
   git clone https://github.com/your-username/currency-converter.git
   ```
3. **Create a new branch**:
   ```sh
   git checkout -b feature-branch
   ```
4. **Make your changes** and commit:
   ```sh
   git add .
   git commit -m "Your commit message"
   ```
5. **Push to your fork**:
   ```sh
   git push origin feature-branch
   ```
6. **Submit a pull request**!

---

## 📝 License
This project is open-source and available under the MIT License.

---

### 🎯 Happy Coding! 🚀

