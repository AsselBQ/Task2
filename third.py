import os
import argparse
import sys

def display_help():
    print("How to use:", sys.argv[0], "[OPTIONS]")
    print("create directories and txt files with a personalized message")
    print("Options:")
    print("  -f <<firstname>>  Your first name (mandatory)")
    print("  -l <<lastname>>   Your last name (optional)")
    print("  -c                Capitalize the names (optional)")
    print("  -p                Display this help message")
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="create directories and txt files with a personalized message")
    parser.add_argument("-f", "--firstname", required=True, help="Your first name (mandatory)")
    parser.add_argument("-l", "--lastname", help="Your last name (optional)")
    parser.add_argument("-c", "--capitalize", action="store_true", help="Capitalize the names (optional)")
    parser.add_argument("-p", "--print-help", action="store_true", help="Display this help message")
    args = parser.parse_args()

    if args.print_help:
        display_help()

    home_dir = os.path.expanduser("~")
    tmp_dir = os.path.join(home_dir, "tmp")
    os.makedirs(tmp_dir, exist_ok=True)

    num_sub_dirs = 5
    for i in range(num_sub_dirs):
        sub_dir = os.path.join(tmp_dir, f"training_project_{i+1}")
        os.makedirs(sub_dir, exist_ok=True)
        
        with open(os.path.join(sub_dir, f"module_{i+1}_a.txt"), "w") as f_a:
            with open(os.path.join(sub_dir, f"module_{i+1}_b.txt"), "w") as f_b:
                
                first_name = args.firstname.capitalize()
                last_name = args.lastname.capitalize() if args.lastname else ""

                if args.capitalize:
                    first_name = first_name.upper()
                    last_name = last_name.upper()
                
                f_a.write(f"Hello {first_name} {last_name} Welcome to file {i+1}.A\n")
                f_b.write(f"Hello {first_name} {last_name} Welcome to file {i+1}.B\n")
                
    print(f"The Directory, sub_dirs and txt files are successfully created")

if __name__ == "__main__":
    main()
