import fal_client

def submit_to_fal(prompt, image_size, num_inference_steps, seed, guidance_scale, num_images, enable_safety_checker):
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

    return handler.get()
