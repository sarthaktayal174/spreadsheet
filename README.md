# Google Sheets Clone

A web-based spreadsheet application built using Django and Vanilla JavaScript with DataTables.js. This project aims to replicate core functionalities of Google Sheets, allowing users to create, edit, and manage tabular data efficiently.

## Features

- **50x26 Default Table Layout**
- **Dynamic Data Handling**
- **Inline Editing**
- **Sorting & Filtering**
- **Backend API for Data Persistence**
- **Vanilla JavaScript & DataTables.js Integration**
- **Django Backend with PostgreSQL**

## Installation & Setup

### Prerequisites

- Python (Django Framework)
- PostgreSQL
- Node.js (Optional for Frontend Enhancements)

### Steps to Run the Project

1. Clone the repository.
 ```
git clone <repository_url>
cd spreadsheet_project
```  
2. Set up a virtual environment.
```
python -m venv venv
venv\Scripts\activate  # (For Windows)
```
3. Install required dependencies.
```
pip install -r requirements.txt
```
4. Configure the database.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'spreadsheet_db',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
5. Apply migrations.
```
python manage.py makemigrations
python manage.py migrate
```
6. Run the development server.
```
python manage.py runserver
```
7. Open the browser and access the application.


## API Endpoints

- **Retrieve Data**
- **Update Data**
- **Delete Data**
- **Add New Rows/Columns**

## Usage

- Users can input and modify data in a table.
- Data is auto-saved in the backend.
- Supports real-time updates and persistence.
- Sorting and searching for data within the table.

## Technologies Used

- **Backend:** Django, PostgreSQL
- **Frontend:** HTML, CSS, JavaScript, DataTables.js

## Future Enhancements

- User Authentication
- Multi-user Collaboration
- Export/Import CSV & Excel Files
- Formula Support
- Real-time Collaboration with WebSockets

## License

This project is licensed under the MIT License.
