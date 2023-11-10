from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
import torch
import sys

if len(sys.argv) != 3:
    print("Usage: python main.py <prompt> <filename.png>")
else:
    prompt = sys.argv[1]
    filename = sys.argv[2]
    print(prompt, filename)
    model_id = "stabilityai/stable-diffusion-2"
    scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
    pipe = StableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, torch_dtype=torch.float16)
    pipe = pipe.to("cuda")
    image = pipe(prompt).images[0]
    image.save(filename)
