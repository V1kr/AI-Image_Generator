from fasthtml.common import *
import os
from client import submit_to_fal
from templates import render_main_page, render_error_page, render_images

def index():
    return render_main_page()

def generate(fal_key: str, prompt: str, image_size: str, num_inference_steps: int, seed: int, guidance_scale: float, num_images: int = 1, enable_safety_checker: bool = True):
    if not fal_key or not prompt:
        return render_error_page("FAL API Key and Prompt are required.")
    
    os.environ['FAL_KEY'] = fal_key

    print(f"API Key set to: {os.environ['FAL_KEY']}")
    print(f"User Prompt: {prompt}")
    print(f"Number of Images: {num_images}")
    print(f"Enable Safety Checker: {enable_safety_checker}")

    try:
        result = submit_to_fal(prompt, image_size, num_inference_steps, seed, guidance_scale, num_images, enable_safety_checker)
        return render_images(result.get('images', []))
    except Exception as e:
        print(f"Error during API call: {e}")
        return render_error_page(str(e))
