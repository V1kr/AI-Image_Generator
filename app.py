from fasthtml.common import *
from routes import index, generate  # Import the route functions

# Create the FastHTML app with custom CSS for styling
app, rt = fast_app(hdrs=(
    Style("""
        body {
              font-family: 'Helvetica Neue', Arial, sans-serif;
              background-color: #1c1c1c;  /* Dark background color */
              color: #ffffff;  /* Contrasting text color */
              display: flex;
              justify-content: center;
              align-items: center;
              min-height: 100vh;  /* Ensure it covers the full height */
              margin: 0;
              padding: 0 20px;
          }

          .main-container {
              display: flex;
              flex-direction: row; /* Keeps form and image side by side */
              width: 90%;  /* Keep the width unchanged */
              max-width: 1600px;  /* Keep the max-width unchanged */
              margin: auto;
              gap: 40px; /* Adequate space between form and image sections */
          }

          .form-container, .image-container {
              flex: 1;
              background-color: #2b2b2b;  /* Consistent background color */
              padding: 40px;  /* Ample padding for more spacious feel */
              border-radius: 10px; /* Softer, more rounded corners */
              box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3); /* Subtle shadow */
              overflow: hidden; /* Prevents content overflow */
              border: none; /* Ensures no extra borders are added */
          }

          .form-container {
              min-width: 500px; /* Larger minimum width for the form */
              flex-grow: 2;  /* Form container grows more */
          }

          .image-container {
              flex-grow: 3;  /* Image container grows more */
              display: flex;
              flex-direction: column; /* Align images vertically */
              justify-content: flex-start;
              align-items: center;
              max-height: 100%; /* Allow the container to grow with content */
              overflow: auto; /* Enable scrolling if content overflows */
              padding: 0; /* Removed padding to avoid multiple borders */
              gap: 20px; /* Space between images */
          }

          .form-group {
              margin-bottom: 25px;
          }

          .form-group-seed {
              display: flex; /* Align seed input and button horizontally */
              align-items: center;
              gap: 10px; /* Space between seed input and button */
          }

          label {
              display: block;
              margin-bottom: 10px;
              font-weight: 500; /* Medium font weight for labels */
              color: #f0f0f0;  /* Slightly lighter label text color */
          }

          input[type="text"], input[type="password"], input[type="number"], input[type="range"], select, textarea {
              width: 100%;
              padding: 14px;  /* Slightly more padding for input fields */
              border: 1px solid #555; /* Subtle border color for inputs */
              border-radius: 4px;
              background-color: #2c2c2c;  /* Slightly different input background */
              color: #ffffff;
              font-size: 16px;  /* Standard font size */
              box-sizing: border-box; /* Ensure padding is included in width calculation */
          }

          button {
              width: 100%;
              padding: 15px;  /* Slightly increased button padding */
              background-color: #0069d9; /* Slightly darker button color */
              color: white;
              border: none;
              border-radius: 4px;
              cursor: pointer;
              font-size: 18px;  /* Larger font size for better readability */
              transition: background-color 0.3s ease; /* Smooth transition */
          }

          button:hover {
              background-color: #0051a3; /* More subtle hover effect */
          }

          #result img {
              width: 100%;  /* Make images full width */
              border-radius: 8px; /* More rounded image corners */
              box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Subtle image shadow */
              border: none; /* Ensures no extra borders are added to the image */
              margin: 0; /* Prevents extra margins that could appear as borders */
          }
        
    """),
    Script("""
    function updateInferenceSteps(value) {
        document.getElementById('numInferenceStepsDisplay').innerText = value;
    }
    function updateGuidanceScale(value) {
        document.getElementById('guidanceScaleDisplay').innerText = value;
    }
    function randomizeSeed() {
        const randomSeed = Math.floor(Math.random() * 10000000);
        document.getElementById('seedInput').value = randomSeed;
    }
    """)
))

# Register routes using decorators directly on route functions
@rt('/')
def main_route():
    return index()

@rt('/generate', methods=['POST'])
def generate_route(fal_key: str, prompt: str, image_size: str, num_inference_steps: int, seed: int, guidance_scale: float, num_images: int = 1, enable_safety_checker: bool = True):
    return generate(fal_key, prompt, image_size, num_inference_steps, seed, guidance_scale, num_images, enable_safety_checker)

if __name__ == "__main__":
    serve(port=8000)
