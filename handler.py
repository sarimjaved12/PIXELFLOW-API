import json
import base64
from PIL import Image
import io
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO) # Set to INFO for general messages

def process_image(event, context):
    logger.info("Lambda function invoked.")
    try:
        # Check if event body exists and is not None
        if event and 'body' in event and event['body'] is not None:
            # HTTP API sends body as a string, parse it
            body = json.loads(event['body'])
            logger.info(f"Received payload keys: {body.keys()}")

            image_base64 = body.get('image_base64')
            width = body.get('width', None)
            height = body.get('height', None)
            quality = body.get('quality', 75)

            if not image_base64:
                logger.error("No image_base64 found in payload.")
                return {
                    "statusCode": 400,
                    "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
                    "body": json.dumps({"message": "image_base64 is required"})
                }

            # Decode the base64 image
            image_bytes = base64.b64decode(image_base64)
            img = Image.open(io.BytesIO(image_bytes))
            logger.info(f"Original image dimensions: {img.width}x{img.height}")

            # Resize image if dimensions are provided
            if width is not None and height is not None:
                img.thumbnail((width, height), Image.Resampling.LANCZOS)
                logger.info(f"New image dimensions after thumbnail: {img.width}x{img.height}")

            # Save processed image to a bytes buffer
            output_buffer = io.BytesIO()
            
            if img.mode in ('RGBA', 'P'): # Handle images with alpha channel or palette
                img = img.convert('RGB')
            img.save(output_buffer, format="JPEG", quality=quality)
            processed_image_base64 = base64.b64encode(output_buffer.getvalue()).decode('utf-8')
            logger.info("Image processed and re-encoded to base64.")

            response_body = {
                "message": "Image processed successfully!",
                "original_dimensions": f"{img.width}x{img.height}",
                "processed_image_base64": processed_image_base64
            }

            return {
                "statusCode": 200,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps(response_body)
            }
        else:
            logger.error("Event body is missing or empty.")
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
                "body": json.dumps({"message": "Request body is missing or empty."})
            }

    except json.JSONDecodeError:
        logger.error(f"JSON Decode Error: Invalid JSON in request body. Body: {event.get('body', 'N/A')}")
        return {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"message": "Invalid JSON format in request body."})
        }
    except Exception as e:
        
        logger.error(f"An unhandled error occurred: {e}", exc_info=True) 
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"message": f"Internal server error: {e}"})
        }