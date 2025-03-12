# Movie Platform App

<details>
  <summary>Table of Contents</summary>
  
- [About the Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
    - [Backend](#backend)
    - [Frontend](#frontend)
- [Recommendations for Improvement](#recommendations-for-improvement)
</details>

## About the Project 🎬🎥🍿

The **Movie Platform App** is a web application designed to manage a collection of movies. It allows users to **add, view, update, and delete** movie records, with a planned expansion for more advanced features in the future. The project is structured as a **monorepo**, meaning both the backend and frontend exist within the same repository but are managed separately.

### **Tech Stack**

- **Backend:** Django, Django REST Framework, PostgreSQL
- **Frontend:** Angular
- **Containerization:** Docker (backend only)

## Getting Started 🚀🛠️📖

To run the project, follow the setup instructions below. Whether you choose to use Docker or set it up manually, ensure you have the required dependencies installed.

### **Prerequisites** ✅📌🔧

Ensure you have the following installed before proceeding:

- **Docker** (for backend setup) → [Download Docker](https://www.docker.com/)
- **Node.js & npm** (for frontend setup) → [Download Node.js](https://nodejs.org/)
- **Python 3.11** (if running backend without Docker)
- **PostgreSQL** (only if not using Docker for database)

## Setup 🏗️📂🔨

### **Backend**

#### **Using Docker (Recommended)** 🐳🚀⚙️

1. Navigate to the project root directory.
2. Run the following command to build and start the backend:
   ```sh
   docker-compose up --build
   ```
3. The backend API will be available at `http://localhost:8000`. 🌐🖥️⚡
4. To stop the Docker containers, run:
   ```sh
   docker-compose down
   ```

#### **Without Docker** ⚡🐍📦

1. Navigate to the backend folder:
   ```sh
   cd backend
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # MacOS/Linux
   venv\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables in `backend/.env`:
   ```ini
   POSTGRES_DB=postgres
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   DB_HOST=localhost  # Change to 'db' if using Docker
   DB_PORT=5432
   ```
5. Apply database migrations:
   ```sh
   python manage.py migrate
   ```
6. Create a superuser (optional, for Django Admin):
   ```sh
   python manage.py createsuperuser
   ```
7. Start the backend server:
   ```sh
   python manage.py runserver 0.0.0.0:8000
   ```

### **Frontend** 🎨🖥️🌍

Once the frontend is set up, the following steps will be used:

1. Navigate to the frontend directory:
   ```sh
   cd frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the development server:
   ```sh
   npm run start
   ```
4. The frontend will be accessible at `http://localhost:4200` (if using Angular's default port).

---

## Recommendations for Improvement 🚀📌💡

- **Enhance API Features:** Add authentication, search, and filtering for movies. 🔍🔑🎬
- **Add Unit Tests:** Implement backend tests using Django’s built-in testing framework. ✅🛠️🧪
- **Improve Error Handling:** Implement better exception handling and custom error messages. ⚠️🔄
- **Deploy the Application:** Set up CI/CD pipelines for automated deployment. 🌍🚀⚙️
- **Improve Documentation:** Extend API documentation using Swagger or Postman collections. 📖📝📌
- **Optimize Performance:** Consider caching mechanisms and database indexing for faster queries. ⚡💾
- **Enhance UI/UX:** Implement a user-friendly, responsive frontend design with intuitive navigation. 🖥️🎨💡
