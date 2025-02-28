import os

def ensure_directory_exists(directory):
    """Create a directory if it doesn't exist
    
    Args:
        directory (str): Directory path
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

def get_file_extension(filename):
    """Get the file extension
    
    Args:
        filename (str): The filename
        
    Returns:
        str: The file extension
    """
    return os.path.splitext(filename)[1]

def validate_csv_file(filepath):
    """Validate that a file is a CSV file
    
    Args:
        filepath (str): Path to the file
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not os.path.exists(filepath):
        return False
        
    ext = get_file_extension(filepath).lower()
    return ext == '.csv' 