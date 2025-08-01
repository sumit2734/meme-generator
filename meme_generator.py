from PIL import Image, ImageDraw, ImageFont
import os

def generate_meme(image_path, top_text, bottom_text, output_path):
    img = Image.open(image_path)

    # Convert to RGB if image has transparency (RGBA)
    if img.mode == 'RGBA':
        img = img.convert('RGB')

    draw = ImageDraw.Draw(img)

    # Load font with dynamic size based on image height
    try:
        font_size = int(img.height / 10)
        font = ImageFont.truetype("arial.ttf", size=font_size)
    except IOError:
        print("⚠️ Arial not found. Using default font.")
        font = ImageFont.load_default()

    def draw_text_with_outline(text, y):
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        x = (img.width - text_width) / 2

        # Outline
        for dx in [-2, 0, 2]:
            for dy in [-2, 0, 2]:
                draw.text((x + dx, y + dy), text, font=font, fill='black')

        draw.text((x, y), text, font=font, fill='white')

    draw_text_with_outline(top_text.upper(), 10)
    draw_text_with_outline(bottom_text.upper(), img.height - font_size - 10)

    img.save(output_path)
    print(f"✅ Meme saved as: {output_path}")

# 🖼 Auto-detect first image in folder
image_file = next((f for f in os.listdir('.') if f.lower().endswith(('.png', '.jpg', '.jpeg'))), None)

if not image_file:
    raise FileNotFoundError("❌ No image file found in this folder. Please add a .jpg or .png file.")

# 🧠 Set your meme text here
TOP_TEXT = "When code finally runs"
BOTTOM_TEXT = "Without any errors 😎"

# 🔥 Run meme generator
generate_meme(image_file, TOP_TEXT, BOTTOM_TEXT, "output_meme.jpg")



