import subprocess

def display_commands(commands):
    print("Select an Nmap command:")
    for i in range(1, len(commands) + 1):
        print(f"{i}. {commands[i - 1]}")

def main():
    nmap_commands = [
        "nmap -sP TARGET_IP",
        "nmap -p 22 TARGET_IP",
        "nmap -A TARGET_IP",
        "ipconfig TARGET_IP",
    ]

    display_commands(nmap_commands)

    while True:
        try:
            choice = int(input("Enter the number of the command to run (0 to exit): "))
            if 0 <= choice <= len(nmap_commands):
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if choice == 0:
        print("Exiting.")
        return

    selected_command = nmap_commands[choice - 1]
    ip_address = input("Enter the IP address: ")

    selected_command = selected_command.replace("TARGET_IP", ip_address)

    print(f"Running command: {selected_command}")
    subprocess.run(selected_command, shell=True)

if __name__ == "__main__":
    main()
