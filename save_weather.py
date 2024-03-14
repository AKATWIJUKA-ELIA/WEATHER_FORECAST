from PIL import ImageGrab
import os

class Save:
    def save_weather_as_image():
        # Capture the screenshot
        img = ImageGrab.grab()

        # Construct the correct file path (assuming Windows)
        filename = 'screenshot.pdf'
        user_profile_dir = os.environ.get('USERPROFILE')  # Get the user profile directory
        screenshot_dir = os.path.join(user_profile_dir, 'Downloads', 'Weather')  # Create path within Documents
        file_path = os.path.join(screenshot_dir, filename)

        # Ensure the directory exists before saving
        os.makedirs(screenshot_dir, exist_ok=True)  # Create the directory if it doesn't exist

        # Save the screenshot
        img.save(file_path)
        print(f"Screenshot saved successfully: {file_path}")
        
    def save_weather():
        os.system("^p")
Save.save_weather()
#Save.save_weather_as_image()        
