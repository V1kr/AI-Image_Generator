AI Image Generator with FastHTML and FAL API

This application allows users to generate AI images based on text prompts using a web interface built with FastHTML and the FAL API. (Built for FLUX.1 [dev])

## Requirements

- Python 3.7+
- pip

## Installation

  1.Clone the Repository
  
  2.Install Dependencies:
    -pip install fal-client
    
  3.Setup:
    -Obtain a FAL API key from the FAL platform.
    -Set your FAL API key in the environment.
  
  4.Running the Application:
    -"python app.py" in terminal
    -Visit http://localhost:XXXX as listed in your terminal to access the web interface.

## Using the Application
  -Enter Your FAL API Key: Required for authentication with the FAL API.
  -Input a Prompt: Describe the image you want to generate.
  -Configure Settings: Choose image size, number of inference steps, seed, guidance scale, and number of images.
  -Submit: Click "Submit" to generate and view images.
  
## Troubleshooting
  -Ensure your FAL API key is valid.
  -Check console output for any error messages.
