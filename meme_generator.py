from PIL import Image, ImageDraw, ImageFont
import os

def generate_meme(image_path, top_text, bottom_text, output_path):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    width, height = img.size

    # Load a font
    font_path = "arial.ttf"  # You must have this font or use a different one
    font_size = int(height / 10)
    font = ImageFont.truetype(font_path, font_size)

    # Outline text
    def draw_text_with_outline(text, y_position):
        text_width, text_height = draw.textsize(text, font=font)
        x = (width - text_width) / 2
        outline_range = 2
        for ox in range(-outline_range, outline_range + 1):
            for oy in range(-outline_range, outline_range + 1):
                draw.text((x + ox, y_position + oy), text, font=font, fill="black")
        draw.text((x, y_position), text, font=font, fill="white")

    draw_text_with_outline(top_text, 10)
    draw_text_with_outline(bottom_text, height - font_size - 20)

    img.save(output_path)
    print(f"Meme saved to {output_path}")

# Example usage
generate_meme("sample.jpg", "TOP TEXT", "BOTTOM TEXT", "output_meme.jpg")
