# Gemini CLI App (Sentiment Analysis & Translation)

This is a Python-based **command-line application** that uses the **Google Gemini API** and **MongoDB Atlas** to provide:

* User registration and login
* Sentiment analysis
* Language detection and translation
* Persistent user activity logs (per user)

The application is intentionally built as a  **CLI-first backend project** , focusing on:

* Data persistence
* State management
* Backend design thinking
* Clean separation of responsibilities

---

## Project Status (Current)

✅ Completed

* MongoDB integration (Atlas)
* User registration & login using database
* Duplicate email prevention
* Sentiment analysis with Gemini API
* Translation with Gemini API
* Storing sentiment & translation logs
* Logs linked to the logged-in user

---

## Project Structure

```
project-root/
│
├── app.py                 # Main application logic (menus, flow)
├── database.py            # MongoDB connection and CRUD operations
├── .env                   # Environment variables (not committed)
├── .env.example           # Sample env file
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
```

---

## Prerequisites

* Anaconda / Miniconda
* Python 3.9+
* MongoDB Atlas cluster
* Google Gemini API key

---

## Step 1: Create Conda Environment

```bash
conda create -n gemini-app python=3.10
```

List environments:

```bash
conda env list
```

---

## Step 2: Activate Environment

```bash
conda activate gemini-app
```

---

## Step 3: Environment Variables

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_gemini_api_key
DB_NAME=geminiBotDB
DB_USER=your_mongodb_username
DB_PASSWORD=your_mongodb_password
```

> ⚠️ Do not commit `.env` to version control

---

## Step 4: Install Dependencies

`requirements.txt`

```
google-generativeai
python-dotenv
pymongo
```

Install:

```bash
pip install -r requirements.txt
```

---

## Step 5: Run the Application

```bash
python app.py
```

---

## Application Flow

1. User registers or logs in
2. Logged-in user becomes the **current session user**
3. User performs:
   * Sentiment analysis
   * Translation
4. Each action:
   * Produces Gemini output
   * Is stored in MongoDB
   * Is linked to the logged-in user
5. User can view personal activity history

---

## Database Design (Conceptual)

### Users Collection

```json
{
  "_id": ObjectId,
  "name": "string",
  "email": "string",
  "password": "hashed_string"
}
```

### Sentiment Logs Collection

```json
{
  "_id": ObjectId,
  "user_id": ObjectId,
  "ask": "string",
  "reply": "string",
  "created_at": "datetime"
}
```

### Translation Logs Collection

```json
{
  "_id": ObjectId,
  "user_id": ObjectId,
  "ask": "string",
  "reply": "string",
  "created_at": "datetime"
}
```

---

## Design Principles Used

* CLI-first development
* No frontend or API until backend logic is clear
* MongoDB as persistent source of truth
* App-level state for current user
* Database-level storage for history

---

## Security Notes

* Password hashing is implemented using bcrypt

## Future Enhancements (Optional)

* Add timestamps and indexing
* Add API layer (FastAPI)
* Add frontend UI
* Role-based access

---

## License

Educational / learning purpose only
