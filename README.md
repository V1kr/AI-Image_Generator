# AI Image Generator

## Overview

This project is an AI-powered image generator application built using the **FastHTML** framework for rapid web development and the **FAL API** for generating images. The application allows users to input prompts and generate images using AI models hosted on FAL's cloud service.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Why Use FAL API and FastHTML](#why-use-fal-api-and-fasthtml)
3. [Features](#features)
4. [Setup and Installation](#setup-and-installation)
5. [How to Run](#how-to-run)
6. [Getting Your FAL API Key](#getting-your-fal-api-key)
7. [Usage](#usage)
8. [Contributing](#contributing)
9. [License](#license)

## Project Structure

The project is divided into multiple files for better readability and maintainability:

- **`app.py`**: The main entry point for the application. It initializes the FastHTML app, sets up the routes, and starts the server.
- **`routes.py`**: Contains the route handlers for the application. It defines the logic for the homepage and the image generation endpoint.
- **`templates.py`**: Manages the HTML structure, CSS, and JavaScript needed for the front-end interface. It contains functions to render different components of the webpage.
- **`client.py`**: Handles interactions with the FAL API. It includes functions to submit requests and fetch results from the API.

## Why Use FAL API and FastHTML

### FAL API

- **Purpose**: The FAL API is utilized to leverage its AI capabilities to generate images based on user input prompts.
- **Why FAL?**: FAL provides a powerful cloud-based AI model hosting service. It allows for rapid deployment and scaling of AI models without needing extensive backend infrastructure.
- **Ease of Use**: With simple API requests, you can interact with powerful AI models and receive high-quality generated content.

### FastHTML

- **Purpose**: FastHTML is a lightweight and fast web framework ideal for creating dynamic web applications.
- **Why FastHTML?**: It provides a declarative approach to defining HTML, CSS, and JavaScript, making the codebase cleaner and more manageable. The framework is designed for speed and simplicity, ensuring that applications run efficiently.

## Features

- **AI Image Generation**: Generate images based on text prompts using advanced AI models.
- **Responsive Design**: A modern, user-friendly interface that works well on both desktop and mobile devices.
- **Customization Options**: Users can specify various parameters such as image size, number of inference steps, seed value, and guidance scale.
- **Multiple Image Support**: Generate up to 4 images at once.
- **Safety Checker**: An optional safety checker feature to ensure generated content adheres to safety standards.

## Setup 

Clone the Repository:

```bash
git clone https://github.com/Vikrs05/AI-Image-Generator
cd AI-Image-Generator
```

## Install Dependencies

Make sure you have Python installed. Then, install the necessary Python packages:

```bash
pip install fasthtml fal_client
```

### Run the Application

Execute the following command in your terminal:

```bash
python app.py
```

### Access the Application

Open your web browser and go to [http://localhost:8000](http://localhost:8000).

## Getting Your FAL API Key

To use the image generation features, you need a valid FAL API key:

1. Go to the [FAL Dashboard]([(https://fal.ai/dashboard/keys)]).
2. Log in or sign up for an account.
3. Navigate to the API keys section and create a new key.
4. Copy the generated key and use it in the application when prompted.

## Usage

1. **Enter Your FAL API Key**: Input your API key obtained from the FAL Dashboard.
2. **Provide a Prompt**: Enter a descriptive prompt for the image you want to generate (e.g., "photo of a rhino dressed in a suit and tie").
3. **Customize Parameters**:
   - Select image size.
   - Set the number of inference steps.
   - Choose a seed value or randomize it.
   - Adjust the guidance scale.
   - Specify the number of images to generate (up to 4).
   - Enable or disable the safety checker.
4. **Generate Images**: Click "Submit" to generate images based on your input.
5. **View Results**: Generated images will be displayed on the right side of the interface.

