# Face Recognition Attendance System

## Introduction

The **Face Recognition Attendance System** is a robust solution designed to automate the attendance process using real-time facial recognition technology. Built with Python, Tkinter, and OpenCV, this system provides an efficient and reliable method for managing attendance, ensuring accuracy and ease of use.

## Features

### Real-Time Face Detection

### Home Page
1. **Student Management System**:
   - Save student information.
   - Take photo samples for face recognition.
   - Update existing student information.
   - Delete student records.
   - Clear all fields.

2. **Train Photo Samples**:
   - Train the system with collected photo samples for accurate face recognition.

3. **Take Attendance with Face Detection**:
   - Automatically mark attendance using real-time face detection.

4. **Attendance Report**:
   - Generate attendance reports in Excel format.
   - Store attendance data in a MySQL database.

5. **Developer Page**:
   - Information about the developer and project.

6. **Help Desk**:
   - Provide assistance and support for users.

7. **Exit System**:
   - Safely exit the application.

## Technology Stack

- **Programming Language**: Python
- **Libraries and Tools**: Tkinter, OpenCV, Haarcascade (Object Detection), LBPH (Face Recognition), Pillow
- **Database**: MySQL

## Installation

### Prerequisites

Make sure you have Python and MySQL installed on your system.

- **Download MySQL**: [MySQL Community Downloads](https://dev.mysql.com/downloads/mysql/)

### Installing Required Libraries

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/face-recognition-attendance-system.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd face-recognition-attendance-system
   ```

3. **Install the necessary Python libraries**:
   ```bash
   pip install opencv-python
   pip install opencv-contrib-python
   pip install mysql-connector-python
   pip install pillow
   ```

### Setting Up the Database

1. **Log in to MySQL**:
   ```bash
   mysql -u root -p
   ```

2. **Enter your MySQL password (`00000`)**.

3. **Create the database**:
   ```sql
   CREATE DATABASE face_recognizer;
   ```

4. **Use the database**:
   ```sql
   USE face_recognizer;
   ```

### Running the Application

1. **Run the main application script**:
   ```bash
   python app.py
   ```

## Usage

1. **Home Page**: Navigate through various features like student management, training samples, taking attendance, generating reports, and more.
2. **Student Management**: Save, update, delete, and manage student records.
3. **Training Samples**: Train the system with photo samples for accurate face recognition.
4. **Attendance**: Mark attendance using real-time face detection and generate reports.

