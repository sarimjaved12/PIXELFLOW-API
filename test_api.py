import base64
import requests
import json
import os


API_ENDPOINT = "YOUR API ENDPOINT HERE" 


INPUT_IMAGE_PATH = "input_image.jpg"
OUTPUT_IMAGE_PATH = "api_processed_output.jpg"

def test_image_api():
    if not os.path.exists(INPUT_IMAGE_PATH):
        print(f"Error: Input image '{INPUT_IMAGE_PATH}' not found.")
        print("Please ensure 'input_image.jpg' is in the same directory as 'test_api.py'.")
        return

    try:

        with open(INPUT_IMAGE_PATH, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

        
        payload = {
            "image_base64": encoded_string,
            "width": 150,  # Request a resize to max 150px wide/high
            "height": 150,
            "quality": 75  # Set JPEG compression quality (0-100)
        }

        #  Sending the POST request to the API
        print(f"Sending request to API: {API_ENDPOINT}")
        response = requests.post(API_ENDPOINT, json=payload)
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)

        #  Parse the response
        response_data = response.json()
        print("API Response:")
        print(json.dumps(response_data, indent=2))

        if response_data.get('processed_image_base64'):
            processed_image_base64 = response_data['processed_image_base64']
            decoded_image_bytes = base64.b64decode(processed_image_base64)

            #  Saving the processed image
            with open(OUTPUT_IMAGE_PATH, "wb") as f:
                f.write(decoded_image_bytes)
            print(f"\nProcessed image saved to: {OUTPUT_IMAGE_PATH}")
            print("Check its dimensions and quality to confirm the resize worked!")
        else:
            print("No 'processed_image_base64' found in the API response. Something might be wrong with the Lambda function's return.")

    except requests.exceptions.RequestException as e:
        print(f"Network or API request error: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response Status Code: {e.response.status_code}")
            print(f"Response Body: {e.response.text}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON response. Response was: {response.text}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    
    try:
        import requests
    except ImportError:
        print("\n--- IMPORTANT ---")
        print("The 'requests' library is not installed.")
        print("Please activate your virtual environment (e.g., 'venv\\Scripts\\activate.bat' on Windows)")
        print("and then run: pip install requests")
        print("-----------------\n")
        exit(1)

    test_image_api()