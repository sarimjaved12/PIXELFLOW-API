from PIL import Image
import os

def resize_image(input_path, output_path, size=(200, 200), quality=85):
    try:
        with Image.open(input_path) as img:
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            img.thumbnail(size, Image.LANCZOS)
            img.save(output_path, "jpeg", quality=quality)
        print(f"Image resized from {input_path} to {output_path} ({img.width}x{img.height})")
        return True
    except FileNotFoundError:
        print(f"Error: Input file not found at {input_path}")
        return False
    except Exception as e:
        print(f"An error occurred during image processing: {e}")
        return False

if __name__ == "__main__":
    input_file = "input_image.jpg"
    output_file = "resized_output.jpg"
    target_size = (300, 300)
    processing_quality = 85 

    if not os.path.exists(input_file):
        print(f"'{input_file}' not found.")
        print(f"Please place a sample JPG or PNG image in the 'image-processing-api' directory")
        print(f"and name it '{input_file}' before running this script.")
    else:
        print(f"Processing image: {input_file}")
        # Pass processing_quality to the resize_image function
        resize_image(input_file, output_file, target_size, quality=processing_quality)
        if os.path.exists(output_file):
            print(f"Check your '{output_file}' file in the project directory.")
        else:
            print("Failed to create resized image.")

    grayscale_output_file = "grayscale_output.jpg"
    if os.path.exists(input_file):
        try:
            with Image.open(input_file) as img:
                if img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')
                grayscale_img = img.convert("L")
                # Use the defined processing_quality here
                grayscale_img.save(grayscale_output_file, "jpeg", quality=processing_quality)
            print(f"Image converted to grayscale and saved as {grayscale_output_file}")
        except Exception as e:
            print(f"An error occurred during grayscale conversion: {e}")