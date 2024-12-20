import os

# Set the directory where the images are stored
directory = directory = 'C:\\Users\\Parth Gautam\\Desktop\\Face_recognition_based_attendance_system\\Face_recognition_based_attendance_system - Copy\\TrainingImage'
  # Replace with your folder path

# The old number to replace and the new number
old_number = 'Naman.0.138.'  # Replace with the number you want to change
new_number = 'Naman.1.138.'  # Replace with the new number

# Loop through all files in the directory
for filename in os.listdir(directory):
    if old_number in filename:  # Check if the old number is in the filename
        # Create the new filename by replacing the old number with the new number
        new_filename = filename.replace(old_number, new_number)
        
        # Get the full paths for the old and new filenames
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_filename)
        
        # Rename the file
        os.rename(old_file, new_file)

print("Renaming completed.")
