# Recipify Project Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [Key Features](#key-features)
3. [Architecture and Technology Stack](#architecture-and-technology-stack)
4. [Installation and Setup](#installation-and-setup)
5. [Usage Guide](#usage-guide)
6. [AI Functionality and Comparison](#ai-functionality-and-comparison)
7. [Frontend Design](#frontend-design)
8. [Deployment Process](#deployment-process)
9. [Contributors](#contributors)
10. [Future Enhancements](#future-enhancements)

---

### 1. Project Overview

**Recipify** is an AI-powered web application designed to streamline meal preparation by curating recipes based on available ingredients and providing nutritional breakdowns. Unlike many existing solutions, Recipify offers multiple recipe suggestions, maximizing user options and fostering a creative cooking experience. The app helps users reduce food waste, manage dietary needs, and explore new meal ideas with ease.

---

### 2. Key Features

- **Ingredient-Based Recipe Suggestions**: Users input ingredients and receive a list of recipe suggestions.
- **Nutritional Information**: Provides details on calories, protein, carbohydrates, and fats for each recipe.
- **User Authentication**: Integration with Google for secure, easy login.
- **Responsive UI**: Designed for a seamless experience across devices.
- **Multi-Option Recipe Suggestions**: Provides more than one recipe to suit various dietary and taste preferences.
- **On-Demand AI Integration**: Supports personalized and context-specific recipe generation, making each session unique.

---

### 3. Architecture and Technology Stack

#### Frontend:
- **HTML/CSS**: For page structure and styling.
- **JavaScript**: Handles interactive features.
- **Django Templates**: Renders dynamic content.

#### Backend:
- **Django Framework**: Manages views, routing, and data processing.
- **On-Demand AI Platform**: Provides real-time recipe generation based on user input.

#### Authentication: SOON
- **Firebase Authentication**: Allows users to log in securely via Google OAuth.

#### Deployment:
- **Vercel**: Hosts the app and manages deployment for both frontend and backend.

---

### 4. Installation and Setup

#### Prerequisites
- Python 3.x
- PostgreSQL


#### Steps to Set Up Locally

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd recipify
2. **Set up virtual environment**:
   ```bash
   python3 -m venv env
   source env/bin/activate
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
4. **Set up the database:**:
   Configure PostgreSQL/sqlite3, create a new database, and update settings.py with your database credentials.
5. **Run migrations**:
   ```bash
   python manage.py migrate
6. **Run the development server**:
   ```bash
   python manage.py runserver
### 5. Usage Guide

#### Accessing the Application

1. Navigate to the main page (enter the Vercel URL if deployed).
2. Use the search bar to input ingredients you have.
3. Browse multiple recipe suggestions, each tailored to ingredients and dietary preferences.

#### Authentication

* **Sign In**: Use Google Authentication to securely log in.
* **Profile Management**: Save favorite recipes and view personalized recommendations.

#### Saving and Viewing Recipes

* Click on the recipe card for details.
* Save recipes to favorites for quick access.

### 6. AI Functionality and Comparison

Recipify’s **AI-based recipe generation** is powered by an on-demand AI platform. Unlike platforms like **ChefGPT** or **DishGen**, which may provide only a single recipe, Recipify offers multiple suggestions, giving users the flexibility to choose what best suits their needs.

### 7. Frontend Design

The frontend is **responsive** and user-friendly:

* **Header**: Contains the logo and navigation links for quick access.
* **Recipe Cards**: Display recipe names, macros, ingredients, and preparation steps.
* **Profile Section**: Allows users to save, view, and manage recipes.

### 8. Deployment Process

To deploy the application:

1. **Collect Static Files**:
    ```bash
    python manage.py collectstatic
    ```
2. **Vercel Setup**:
    * Push the repository to Vercel.
    * Ensure `settings.py` is configured with environment variables.
3. **Railway Setup for PostgreSQL**:
    * Link the PostgreSQL database on Railway to your Vercel app.

### 9. Contributors

* **Akash** - Backend/API/Deployment
* **Kartikey Roshan** - Frontend/Ideation
* **Himanshu Jorwal** - Frontend/PPT Design
* **Ankit Kumar** - Backend

