from fasthtml.common import *
import fal_client
import os

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

# Route to render the main page with form inputs
@rt('/')
def index():
    return Div(
        Div(
            Div(
                H1('AI Image Generator'),
                Form(
                    Div(
                        Label('Enter Your FAL API Key:'),
                        Input(type='password', name='fal_key', placeholder='Paste your FAL key here'),
                        _class='form-group'
                    ),
                    Div(
                        Label('Enter Your Prompt:'),
                        Input(type='text', name='prompt', placeholder='e.g., photo of a rhino dressed in a suit and tie...'),
                        _class='form-group'
                    ),
                    Div(
                        Label('Image Size:'),
                        Select(
                            Option('landscape_4_3', value='landscape_4_3'),
                            Option('square_hd', value='square_hd'),
                            Option('square', value='square'),
                            Option('portrait_4_3', value='portrait_4_3'),
                            Option('portrait_16_9', value='portrait_16_9'),
                            Option('landscape_16_9', value='landscape_16_9'),
                            name='image_size'
                        ),
                        _class='form-group'
                    ),
                    Div(
                        Label('Number of Inference Steps:'),
                        Input(type='range', name='num_inference_steps', min='0', max='36', value='0', 
                              oninput='updateInferenceSteps(this.value)'),
                        Span('0', id='numInferenceStepsDisplay', style='margin-left: 10px;'),  # Display initial value
                        _class='form-group'
                    ),
                    Div(
                        Label('Seed:'),
                        Div(
                            Input(type='number', name='seed', id='seedInput', placeholder='random', value=''),
                            Button('↻', type='button', _class='randomize-btn', onclick='randomizeSeed()'),
                            _class='form-group-seed'
                        ),
                        _class='form-group'
                    ),
                    Div(
                        Label('Guidance Scale (CFG):'),
                        Input(type='range', name='guidance_scale', min='0', max='2', step='0.1', value='1', 
                              oninput='updateGuidanceScale(this.value)'),
                        Span('1', id='guidanceScaleDisplay', style='margin-left: 10px;'),  # Display initial value
                        _class='form-group'
                    ),
                    Div(
                        Label('Number of Images:'),
                        Input(type='number', name='num_images', min='1', max='4', value='1'),  # Allow up to 4 images
                        _class='form-group'
                    ),
                    Div(
                        Label('Enable Safety Checker:'),
                        Input(type='checkbox', name='enable_safety_checker', checked=True),  # Checked by default
                        _class='form-group'
                    ),
                    Button('Submit', type='submit', hx_post='/generate', hx_target='#result'),
                    _hx_boost=True,
                ),
                _class='form-container'  # Use the form-container class for layout
            ),
            Div(
                Div(id='result', _class='image-container'),  # Separate container for displaying the image
                _class='image-container'
            ),
            _class='main-container'  # Main container for layout
        )
    )

# Route to handle the form submission
@rt('/generate', methods=['POST'])
def generate(fal_key: str, prompt: str, image_size: str, num_inference_steps: int, seed: int, guidance_scale: float, num_images: int = 1, enable_safety_checker: bool = True):
    # Check for missing inputs
    if not fal_key:
        return Div(P("FAL API Key is required."), id='result', _class='image-container')
    if not prompt:
        return Div(P("Prompt is required."), id='result', _class='image-container')
        
    # Set the environment variable in Python
    os.environ['FAL_KEY'] = fal_key

    # Confirm the environment variable is set
    print(f"API Key set to: {os.environ['FAL_KEY']}")

    # Log the provided values
    print(f"FAL Key: {fal_key}")
    print(f"User Prompt: {prompt}")
    print(f"Number of Images: {num_images}")
    print(f"Enable Safety Checker: {enable_safety_checker}")

    # flux api handler
    handler = fal_client.submit(
        "fal-ai/flux/dev",
        arguments={
            "model_name": "stabilityai/stable-diffusion-xl-base-1.0",
            "prompt": prompt,
            "image_size": image_size,
            "num_inference_steps": num_inference_steps,
            "seed": seed if seed else None,
            "guidance_scale": guidance_scale,
            "num_images": num_images,
            "enable_safety_checker": enable_safety_checker
        },
    )
 
    try:
        result = handler.get()
        print(result)

        # Extract all image URLs from the result
        images = result.get('images', [])[:4]  # Limit to 4 images for display
        
        # Generate a list of Img elements for each URL
        image_elements = [Img(src=image['url'], alt=f"Generated Image {i+1}", style="margin-bottom: 20px;") for i, image in enumerate(images)]

        # Prepare the response to replace the content of #result div
        return Div(
            *image_elements,  # Unpack the list to pass as individual arguments
            id='result',  # Ensures the div with id 'result' is replaced
            _class='image-container'
        )
    except Exception as e:
        print(f"Error during API call: {e}")
        return Div(P(f"Error: {str(e)}"), id='result', _class='image-container')

# Start the FastHTML app
serve()