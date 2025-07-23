import os
import platform

def shutdown():
    """Safe shutdown with user confirmation"""
    confirm = input("Are you sure you want to shutdown? (y/n): ").lower()
    
    if confirm == 'y':
        system = platform.system().lower()
        
        if system == "windows":
            os.system("shutdown /s /t 1")
        elif system == "linux" or system == "darwin":
            os.system("shutdown -h now")
        else:
            print(f"Unsupported operating system: {system}")
    else:
        print("Shutdown cancelled.")

# Example usage
shutdown()