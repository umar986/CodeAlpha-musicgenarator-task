# 🎶 AI Music Generator 🤖

<p align="center">
  <img src="https://img.shields.io/badge/Project%20Status-Completed-brightgreen?style=for-the-badge&logo=appveyor" alt="Project Status Badge">
  <img src="https://img.shields.io/badge/Tech%20Stack-Python%20%7C%20HTML%2FJS-blue?style=for-the-badge&logo=python&logoColor=white" alt="Technology Badge">
  <img src="https://img.shields.io/badge/Flask%20API-Backend-red?style=for-the-badge&logo=flask" alt="Flask API Badge">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge&logo=opensourceinitiative&logoColor=white" alt="License Badge">
</p>

<p align="center">
  <img src="https://lh3.googleusercontent.com/d/1PuN2sdYkGURRFXlGd_zAjXQrYzmPaOhi=w200?authuser=0" alt="CodeAlpha Logo" width="100"/>
  <br>
  <h3 align="center">A Capstone Project for the CodeAlpha Artificial Intelligence Internship</h3>
  <h4 align="center">Music Generation with AI</h4>
</p>

---

## ✨ Project Overview

This project demonstrates the use of **Artificial Intelligence** techniques to generate unique, **mood-based music** tracks. Users can interact with a minimalist web interface to select a desired emotion (e.g., Energetic, Melancholic, Synthwave), and the Python-Flask backend instantly processes the request to create a corresponding **MIDI file**.

The core logic uses the `music21` library to programmatically construct musical sequences, varying parameters like **pitch range** and **note duration** based on the selected mood, thus providing a personalized auditory experience.

### 🎯 Key Project Highlights:

* **AI Implementation:** Algorithmic music generation based on predefined mood parameters.
* **Minimalist Web UI:** A clean and modern user interface built with HTML/Tailwind CSS for seamless interaction.
* **RESTful API:** A Flask backend serving as a robust bridge between the user interface and the music generation core.

---

## 🛠️ Technology Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Backend Framework** | **Python (Flask)** | Handles API routing, server logic, and file delivery. |
| **Music Generation** | **`music21` & `numpy`** | Used for creating musical notes, streams, and generating the MIDI output file. |
| **Frontend Styling** | **HTML5 & Tailwind CSS** | Provides the modern, responsive, and visually appealing "Glassmorphism" design. |
| **Interactivity** | **Vanilla JavaScript** | Manages user input (mood selection) and asynchronous communication with the backend API. |

---

## 🚀 Getting Started

Follow these steps to set up and run the AI Music Generator on your local machine.

### Prerequisites

To run this project, you need to have:

* **Python 3.x** installed.
* **pip** (Python package installer).

### Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/MuzammilBaloch-22/](https://github.com/MuzammilBaloch-22/)[Your-Repo-Name].git
    cd [Your-Repo-Name]
    ```

2.  **Install Python Dependencies:**
    Install the necessary libraries for the Flask backend logic.
    ```bash
    pip install music21 numpy flask
    ```

### How to Run

1.  **Start the Backend Server:**
    Run the `backend.py` file. The server will start on `http://0.0.0.0:5000`.
    ```bash
    python backend.py
    ```

2.  **Launch the Frontend:**
    Open the `index.html` file in any modern web browser. (Using a browser extension like "Live Server" is recommended to handle fetch requests properly.)

---

## 💻 Usage Instructions

1.  **Select a Mood:** On the web interface, click any of the available mood buttons (e.g., *Energetic, Ambient, Synthwave*).
2.  **Generate Music:** Click the large **"🎶 Generate Music"** button.
3.  **Download:** The backend will generate a unique MIDI track based on the selected mood, and it will be automatically downloaded to your system as a `.mid` file (e.g., `generated_energetic.mid`).
4.  **Playback:** You can listen to the generated MIDI file using any standard music software or online MIDI player.

---
<br>

## 🧑‍💻 The Developer

<p align="center">
  <img src="https://img.shields.io/badge/Developer%20Name-Muzammil%20Ahmed-9370DB?style=for-the-badge&logo=probot&logoColor=white" alt="Developer Name Badge">
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/muzammil-ahmed-0902612a5/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-Profile-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
  </a>
  &nbsp;
  <a href="https://github.com/MuzammilBaloch-22" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-MuzammilBaloch--22-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Badge"/>
  </a>
  &nbsp;
  <a href="https://www.instagram.com/muzammil_baloch_22/" target="_blank">
    <img src="https://img.shields.io/badge/Instagram-Follow-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram Badge"/>
  </a>
</p>
<br>

---
