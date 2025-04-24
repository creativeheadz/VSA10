# main.py
import os
import importlib.util
import sys
import platform
import logging

# Setup logging
logging.basicConfig(
    filename='vsa_api_tool.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)
logger = logging.getLogger(__name__)

# ANSI color codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# Enable ANSI colors in Windows terminal
if platform.system() == 'Windows':
    import ctypes
    kernel32 = ctypes.WinDLL('kernel32')
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_subdirectories(root_path=None):
    """Get all subdirectories in the given path."""
    if root_path is None:
        # Use the directory of the script as the root path
        root_path = os.path.dirname(os.path.abspath(__file__))
    
    try:
        # Get all directories in the root path, excluding __pycache__ and hidden directories
        subdirs = [d for d in os.listdir(root_path) 
                  if os.path.isdir(os.path.join(root_path, d)) 
                  and not d.startswith('.') 
                  and d != '__pycache__']
        return root_path, subdirs
    except Exception as e:
        print(f"Error getting subdirectories: {str(e)}")
        return root_path, []

def get_python_files(directory):
    """Get all Python files in the given directory."""
    try:
        # Get all Python files in the directory
        py_files = [f for f in os.listdir(directory) if f.endswith('.py') and not f.startswith('__') and f != 'main.py']
        return py_files
    except Exception as e:
        print(f"Error getting Python files: {str(e)}")
        return []

def get_script_friendly_name(file_path):
    """Extract friendly name from a Python script if available."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip().startswith('__friendly_name__'):
                    # Extract the string value after the assignment
                    parts = line.split('=', 1)
                    if len(parts) == 2:
                        # Remove quotes and strip whitespace
                        friendly_name = parts[1].strip()
                        # Remove single or double quotes if present
                        if (friendly_name.startswith('"') and friendly_name.endswith('"')) or \
                           (friendly_name.startswith("'") and friendly_name.endswith("'")):
                            friendly_name = friendly_name[1:-1]
                        return friendly_name
    except Exception as e:
        logger.warning(f"Failed to extract friendly name from {file_path}: {e}")
    
    # Return None if no friendly name found
    return None

def load_and_run_module(file_path):
    """Load and run a Python module from the given path, handling null bytes."""
    module_name = os.path.splitext(os.path.basename(file_path))[0]
    source_code = None
    cleaned = False

    logger.info(f"Attempting to load module: {file_path}")

    try:
        try:
            with open(file_path, 'rb') as f:
                content = f.read()
        except Exception as read_err:
            logger.error(f"Error reading file binary {file_path}: {read_err}")
            print(f"{Colors.RED}Error reading file binary {file_path}: {read_err}{Colors.END}")
            input("Press Enter to continue...")
            return

        if b'\0' in content:
            logger.warning(f"Null bytes found in {file_path}")
            print(f"\n{Colors.YELLOW}Warning: {file_path} contains null bytes.{Colors.END}")
            print(f"{Colors.GREEN}Cleaning null bytes and reading as UTF-8...{Colors.END}")
            cleaned_content = content.replace(b'\0', b'')
            try:
                source_code = cleaned_content.decode('utf-8')
                cleaned = True
                try:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(source_code)
                    logger.info(f"Cleaned and overwrote file: {file_path}")
                    print(f"{Colors.GREEN}Original file overwritten with cleaned UTF-8 content.{Colors.END}")
                except Exception as write_err:
                    logger.warning(f"Could not overwrite cleaned file: {write_err}")
                    print(f"{Colors.YELLOW}Warning: Could not overwrite original file with cleaned content: {write_err}{Colors.END}")
                # After cleaning, re-read the file to ensure it's clean
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        source_code = f.read()
                except Exception as reread_err:
                    logger.error(f"Error re-reading cleaned file {file_path}: {reread_err}")
                    print(f"{Colors.RED}Error re-reading cleaned file {file_path}: {reread_err}{Colors.END}")
                    input("Press Enter to continue...")
                    return
            except UnicodeDecodeError as decode_err:
                logger.error(f"Error decoding cleaned file {file_path}: {decode_err}")
                print(f"{Colors.RED}Error decoding file {file_path} as UTF-8 after cleaning: {decode_err}{Colors.END}")
                print(f"{Colors.YELLOW}Execution may fail if null bytes were part of multi-byte characters.{Colors.END}")
                try:
                    source_code = cleaned_content.decode(errors='ignore')
                except Exception as fallback_decode_err:
                    logger.error(f"Could not decode cleaned content: {fallback_decode_err}")
                    print(f"{Colors.RED}Could not decode cleaned content with default encoding: {fallback_decode_err}{Colors.END}")
                    input("Press Enter to continue...")
                    return
        else:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    source_code = f.read()
            except UnicodeDecodeError:
                logger.warning(f"Could not read {file_path} as UTF-8. Trying default encoding.")
                print(f"{Colors.YELLOW}Warning: Could not read {file_path} as UTF-8. Trying default encoding.{Colors.END}")
                try:
                    with open(file_path, 'r') as f:
                        source_code = f.read()
                except Exception as read_err:
                    logger.error(f"Error reading file {file_path} with default encoding: {read_err}")
                    print(f"{Colors.RED}Error reading file {file_path} with default encoding: {read_err}{Colors.END}")
                    input("Press Enter to continue...")
                    return
            except Exception as read_err:
                logger.error(f"Error reading file {file_path}: {read_err}")
                print(f"{Colors.RED}Error reading file {file_path}: {read_err}{Colors.END}")
                input("Press Enter to continue...")
                return

        if source_code is None:
            logger.error(f"Could not read source code from {file_path}")
            print(f"{Colors.RED}Could not read source code from {file_path}.{Colors.END}")
            input("Press Enter to continue...")
            return

        # Double-check for null bytes in the final source_code
        if '\x00' in source_code:
            logger.error(f"Null bytes still present in {file_path} after cleaning!")
            print(f"{Colors.RED}Null bytes still present in {file_path} after cleaning!{Colors.END}")
            input("Press Enter to continue...")
            return

        logger.info(f"Executing module: {module_name}")

        spec = importlib.util.spec_from_loader(module_name, loader=None, origin=file_path)
        if spec is None:
            logger.error(f"Could not create module spec for {module_name}")
            print(f"{Colors.RED}Could not create module spec for {module_name}.{Colors.END}")
            input("Press Enter to continue...")
            return

        module = importlib.util.module_from_spec(spec)
        if module is None:
            logger.error(f"Could not create module object for {module_name}")
            print(f"{Colors.RED}Could not create module object for {module_name}.{Colors.END}")
            input("Press Enter to continue...")
            return

        setattr(module, '__file__', file_path)
        setattr(module, '__name__', module_name)
        sys.modules[module_name] = module

        try:
            compiled_code = compile(source_code, file_path, 'exec')
            exec(compiled_code, module.__dict__)
        except Exception as exec_err:
            logger.error(f"Error executing code in {file_path}: {exec_err}")
            raise

        if hasattr(module, 'main'):
            logger.info(f"Found main() in {module_name}, running it.")
            module.main()
        elif hasattr(module, module_name):
            logger.info(f"Found {module_name}() in {module_name}, running it.")
            func = getattr(module, module_name)
            import inspect
            sig = inspect.signature(func)
            required_args = [param for param, param_obj in sig.parameters.items()
                           if param_obj.default == inspect.Parameter.empty and
                              param_obj.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD]
            if required_args:
                args = []
                print(f"\nFunction {module_name} requires {len(required_args)} argument(s):")
                for arg_name in required_args:
                    arg_value = input(f"Enter value for '{arg_name}': ")
                    args.append(arg_value)
                func(*args)
            else:
                func()
        else:
            logger.info(f"No main or {module_name} function found in {module_name}.")
            print(f"Module {module_name} executed (no 'main' or '{module_name}' function found).")

        input("\nPress Enter to continue...")

    except Exception as e:
        import traceback
        logger.error(f"Exception running {file_path}: {e}", exc_info=True)
        print(f"{Colors.RED}\n{'='*20} Error Running Script {'='*20}{Colors.END}")
        print(f"{Colors.RED}Script: {file_path}{Colors.END}")
        print(f"{Colors.RED}Error Type: {type(e).__name__}{Colors.END}")
        print(f"{Colors.RED}Error Message: {e}{Colors.END}")
        print(f"{Colors.YELLOW}\nTraceback:{Colors.END}")
        traceback.print_exc()
        print(f"{Colors.RED}{'='*58}{Colors.END}")
        input("\nPress Enter to continue...")

def print_menu_header(title):
    """Print a formatted menu header."""
    width = 60
    print(f"\n{Colors.BOLD}{Colors.HEADER}{'═' * width}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}{title.center(width)}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.HEADER}{'═' * width}{Colors.END}\n")

def print_menu_item(index, text, color=Colors.BLUE):
    """Print a formatted menu item with aligned numbers."""
    # Format index with leading zeros if it's a number
    if isinstance(index, int):
        # Determine padding based on the maximum potential number of items
        # This ensures all numbers have the same width
        formatted_index = f"{index:02d}"
    else:
        formatted_index = str(index)
    
    print(f"{Colors.BOLD}[{color}{formatted_index}{Colors.END}{Colors.BOLD}]{Colors.END} {text}")

def print_menu_footer(width=60):
    """Print a formatted menu footer."""
    print(f"\n{Colors.HEADER}{'─' * width}{Colors.END}")

# Global variable to store environment information
api_environment_info = None

def check_connectivity():
    """Check connectivity by running get_environment_information.py and return results."""
    global api_environment_info
    
    # Look for the get_environment_information.py script in API subdirectories
    root_path, subdirs = get_subdirectories()
    
    # First try to find the script in a common location - 'common' or 'system' directories
    target_script = 'get_environment_information.py'
    script_path = None
    
    # Check common locations first
    common_dirs = ['common', 'system', 'info', 'utils', 'tools', 'environment']
    for common_dir in common_dirs:
        if common_dir in subdirs:
            potential_path = os.path.join(root_path, common_dir, target_script)
            if os.path.exists(potential_path):
                script_path = potential_path
                break
    
    # If not found in common locations, search all subdirectories
    if not script_path:
        for subdir in subdirs:
            potential_path = os.path.join(root_path, subdir, target_script)
            if os.path.exists(potential_path):
                script_path = potential_path
                break
    
    if not script_path:
        logger.warning(f"Could not find {target_script} in any subdirectory")
        return {
            "connected": False,
            "error": f"Could not find {target_script} in any subdirectory"
        }
    
    logger.info(f"Found {target_script} at {script_path}")
    
    try:
        # Method 1: Run the script directly as a subprocess to capture output
        # This helps if the script prints results rather than returning them
        try:
            import subprocess
            import json
            
            # Save current directory
            current_dir = os.getcwd()
            # Change to script directory to ensure relative imports work
            script_dir = os.path.dirname(script_path)
            os.chdir(script_dir)
            
            # Run the script and capture output
            result = subprocess.run(
                [sys.executable, os.path.basename(script_path)],
                capture_output=True,
                text=True,
                check=False
            )
            
            # Restore original directory
            os.chdir(current_dir)
            
            # Check if output contains JSON
            if result.returncode == 0 and result.stdout:
                # Try to find JSON in the output
                try:
                    # Look for JSON-like content in the output
                    import re
                    json_match = re.search(r'({[\s\S]*})', result.stdout)
                    if json_match:
                        json_str = json_match.group(1)
                        data = json.loads(json_str)
                        if 'Data' in data:
                            api_environment_info = data
                            return {
                                "connected": True,
                                "customer_id": data.get('Data', {}).get('CustomerId', 'Unknown'),
                                "customer_name": data.get('Data', {}).get('CustomerName', 'Unknown'),
                                "product_version": data.get('Data', {}).get('ProductVersion', 'Unknown'),
                                "full_info": data
                            }
                except json.JSONDecodeError:
                    logger.debug("Could not parse JSON from subprocess output")
                except Exception as e:
                    logger.debug(f"Error processing subprocess output: {str(e)}")
        except Exception as e:
            logger.debug(f"Subprocess method failed: {str(e)}")
        
        # Method 2: Import and run the module (original method with enhancements)
        # Temporarily add the script directory to sys.path for imports
        script_dir = os.path.dirname(script_path)
        if script_dir not in sys.path:
            sys.path.insert(0, script_dir)
        
        # Import the module
        module_name = os.path.splitext(os.path.basename(script_path))[0]
        spec = importlib.util.spec_from_file_location(module_name, script_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Try more function names that might be present
        result = None
        function_names = ['get_environment_info', 'get_environment', 
                          'get_environment_information', 
                          'environment_info', 'main']
        
        for func_name in function_names:
            if hasattr(module, func_name):
                logger.info(f"Found {func_name} function in {module_name}")
                try:
                    func = getattr(module, func_name)
                    result = func()
                    if result:
                        break
                except Exception as e:
                    logger.debug(f"Error calling {func_name}: {str(e)}")
        
        # Clean up sys.path
        if script_dir in sys.path:
            sys.path.remove(script_dir)
        
        if result and isinstance(result, dict):
            # Check if the result has the expected structure directly
            # or under a 'Data' key as some APIs return a wrapper object
            if 'Data' in result:
                api_environment_info = result
                data_section = result['Data']
            elif isinstance(result, dict) and any(k in result for k in ['CustomerId', 'CustomerName', 'ProductVersion']):
                api_environment_info = {'Data': result}
                data_section = result
            else:
                # Search for nested data that might contain environment info
                data_section = None
                for key, value in result.items():
                    if isinstance(value, dict) and any(k in value for k in ['CustomerId', 'CustomerName', 'ProductVersion']):
                        data_section = value
                        api_environment_info = {'Data': value}
                        break
                
                if not data_section:
                    logger.warning(f"Could not find environment data in the result structure")
                    return {
                        "connected": False,
                        "error": "Unexpected data structure in result"
                    }
            
            return {
                "connected": True,
                "customer_id": data_section.get('CustomerId', 'Unknown'),
                "customer_name": data_section.get('CustomerName', 'Unknown'),
                "product_version": data_section.get('ProductVersion', 'Unknown'),
                "full_info": api_environment_info
            }
        
        # Last resort: Look at the module's globals
        if hasattr(module, 'environment_data') or hasattr(module, 'data') or hasattr(module, 'result'):
            potential_data = getattr(module, 'environment_data', None) or getattr(module, 'data', None) or getattr(module, 'result', None)
            if potential_data and isinstance(potential_data, dict):
                # Process the data like above
                if 'Data' in potential_data:
                    api_environment_info = potential_data
                    data_section = potential_data['Data']
                else:
                    api_environment_info = {'Data': potential_data}
                    data_section = potential_data
                
                return {
                    "connected": True,
                    "customer_id": data_section.get('CustomerId', 'Unknown'),
                    "customer_name": data_section.get('CustomerName', 'Unknown'),
                    "product_version": data_section.get('ProductVersion', 'Unknown'),
                    "full_info": api_environment_info
                }
        
        logger.warning(f"Could not extract environment information from {target_script}")
        return {
            "connected": False,
            "error": f"Could not extract environment information"
        }
    
    except Exception as e:
        logger.error(f"Error checking connectivity: {str(e)}", exc_info=True)
        return {
            "connected": False,
            "error": str(e)
        }

def display_connection_info(connection_status):
    """Display connection information in the directory menu."""
    if connection_status and connection_status.get("connected", False):
        customer_id = connection_status.get("customer_id", "Unknown")
        customer_name = connection_status.get("customer_name", "Unknown")
        product_version = connection_status.get("product_version", "Unknown")
        
        print(f"\n{Colors.GREEN}✓ Connected to API: {customer_id}{Colors.END}")
        print(f"{Colors.CYAN}Customer: {customer_name}{Colors.END}")
        print(f"{Colors.CYAN}Version: {product_version}{Colors.END}")
    else:
        error = connection_status.get("error", "Unknown error") if connection_status else "Not connected"
        print(f"\n{Colors.RED}✗ Not connected to API: {error}{Colors.END}")
        print(f"{Colors.YELLOW}Some features may not work properly.{Colors.END}")

def display_directory_menu():
    """Display a menu of subdirectories."""
    root_path, subdirs = get_subdirectories()
    
    # Get connection status
    connection_status = check_connectivity()

    while True:
        clear_screen()
        print_menu_header("VSAx API Tool - Directory Menu")

        # Sort subdirectories alphabetically for consistency
        subdirs.sort()

        for i, subdir in enumerate(subdirs, 1):
            print_menu_item(i, subdir)

        # For the exit option, keep consistent formatting
        print_menu_item(len(subdirs) + 1, f"{Colors.YELLOW}Exit{Colors.END}", Colors.RED)
        
        # Display connection information before the footer
        display_connection_info(connection_status)
        
        print_menu_footer()

        try:
            choice_str = input(f"{Colors.GREEN}Enter your choice: {Colors.END}")
            if not choice_str.isdigit():
                print(f"\n{Colors.RED}Please enter a number.{Colors.END}")
                input(f"{Colors.CYAN}Press Enter to continue...{Colors.END}")
                continue

            choice = int(choice_str)

            if 1 <= choice <= len(subdirs):
                selected_dir = os.path.join(root_path, subdirs[choice - 1])
                display_files_menu(selected_dir)
            elif choice == len(subdirs) + 1:
                print(f"\n{Colors.YELLOW}Exiting program...{Colors.END}")
                break
            else:
                print(f"\n{Colors.RED}Invalid choice. Please try again.{Colors.END}")
                input(f"{Colors.CYAN}Press Enter to continue...{Colors.END}")
        except ValueError: # Should be caught by isdigit check, but keep for safety
            print(f"\n{Colors.RED}Please enter a number.{Colors.END}")
            input(f"{Colors.CYAN}Press Enter to continue...{Colors.END}")
        except KeyboardInterrupt:
             print(f"\n{Colors.YELLOW}Exiting program...{Colors.END}")
             break


def display_files_menu(directory):
    """Display a menu of Python files in the directory."""
    py_files = get_python_files(directory)
    friendly_names = {}
    
    # Pre-fetch friendly names for each file
    for file in py_files:
        file_path = os.path.join(directory, file)
        friendly_name = get_script_friendly_name(file_path)
        friendly_names[file] = friendly_name

    while True:
        clear_screen()
        dir_name = os.path.basename(directory)
        print_menu_header(f"Scripts in '{dir_name}'")

        # Sort files alphabetically for consistency
        py_files.sort()

        for i, file in enumerate(py_files, 1):
            # Use only the friendly name if available, otherwise use the filename
            if friendly_names[file]:
                display_text = friendly_names[file]
            else:
                display_text = file
            print_menu_item(i, display_text)

        # For the back option, keep consistent formatting
        print_menu_item(len(py_files) + 1, f"{Colors.YELLOW}Back to Directory Menu{Colors.END}", Colors.CYAN)
        print_menu_footer()

        try:
            choice_str = input(f"{Colors.GREEN}Enter your choice: {Colors.END}")
            if not choice_str.isdigit():
                print(f"\n{Colors.RED}Please enter a number.{Colors.END}")
                input(f"{Colors.CYAN}Press Enter to continue...{Colors.END}")
                continue

            choice = int(choice_str)

            if 1 <= choice <= len(py_files):
                selected_file = os.path.join(directory, py_files[choice - 1])
                print(f"\n{Colors.YELLOW}Running {py_files[choice - 1]}...{Colors.END}")
                # Ensure the directory of the script is in sys.path for imports
                script_dir = os.path.dirname(selected_file)
                if script_dir not in sys.path:
                    sys.path.insert(0, script_dir)
                # Also add the root API directory to sys.path for potential shared modules like config
                root_api_dir = os.path.dirname(os.path.abspath(__file__))
                if root_api_dir not in sys.path:
                     sys.path.insert(1, root_api_dir) # Insert after script dir

                load_and_run_module(selected_file)

                # Clean up sys.path if added
                if script_dir in sys.path and script_dir != root_api_dir:
                    try:
                        sys.path.remove(script_dir)
                    except ValueError:
                        pass # Should not happen, but safer
                if root_api_dir in sys.path and len(sys.path) > 1 and sys.path[1] == root_api_dir:
                     try:
                         # Be careful removing if it was already there or is the primary path
                         # This logic might need refinement depending on structure
                         pass # Avoid removing the main API dir for now
                     except ValueError:
                         pass


            elif choice == len(py_files) + 1:
                return # Go back to the directory menu
            else:
                print(f"\n{Colors.RED}Invalid choice. Please try again.{Colors.END}")
                input(f"{Colors.CYAN}Press Enter to continue...{Colors.END}")
        except ValueError: # Should be caught by isdigit check, but keep for safety
            print(f"\n{Colors.RED}Please enter a number.{Colors.END}")
            input(f"{Colors.CYAN}Press Enter to continue...{Colors.END}")
        except KeyboardInterrupt:
             print(f"\n{Colors.YELLOW}Returning to Directory Menu...{Colors.END}")
             return # Go back to the directory menu


def check_env_file():
    """Check if .env file exists and contains required variables. If not, prompt the user."""
    try:
        from dotenv import load_dotenv, set_key
    except ImportError:
        print(f"{Colors.YELLOW}python-dotenv module not found. Installing...{Colors.END}")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "python-dotenv"])
        from dotenv import load_dotenv, set_key
    
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
    
    # Load existing environment variables
    load_dotenv(env_path)
    
    required_vars = {
        'ENDPOINT': "API endpoint URL (e.g., https://example.vsax.net/api/v3/)",
        'TOKEN_ID': "API token ID",
        'TOKEN_SECRET': "API token secret"
    }
    
    need_to_update = False
    new_values = {}
    
    for var, description in required_vars.items():
        if not os.getenv(var):
            print(f"\n{Colors.YELLOW}{var} not found in environment variables.{Colors.END}")
            value = input(f"{Colors.CYAN}Please enter {description}: {Colors.END}")
            new_values[var] = value
            need_to_update = True
    
    if need_to_update:
        # Check if .env file exists
        if not os.path.exists(env_path):
            with open(env_path, 'w') as f:
                for var, value in new_values.items():
                    f.write(f"{var}={value}\n")
            print(f"\n{Colors.GREEN}.env file created with your values.{Colors.END}")
        else:
            # Update existing .env file
            for var, value in new_values.items():
                set_key(env_path, var, value)
            print(f"\n{Colors.GREEN}.env file updated with your values.{Colors.END}")
        
        input(f"{Colors.CYAN}Press Enter to continue...{Colors.END}")

def main():
    """Main function to run the program."""
    try:
        check_env_file()  # Check .env before displaying menu
        display_directory_menu()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Program interrupted by user. Exiting...{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}An unexpected error occurred in main:{Colors.END}")
        import traceback
        traceback.print_exc()
        input(f"{Colors.CYAN}Press Enter to exit...{Colors.END}")


if __name__ == "__main__":
    main()
