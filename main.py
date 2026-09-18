print("\n ===== LOGIN SECURITY ANALYZER =====")
print("\nAnalyzing login records...\n")

try:
    with open("logins.txt", "r") as file:
        data = file.readlines()

except FileNotFoundError:
    print("Error: logins.txt was not found.")
    exit()

failed_attempts = {}

for line in data:
    parts = line.strip().split(",")
    if len(parts) == 3:
    username, ip, status = parts

    if status == "failed":
        if ip in failed_attempts:
            failed_attempts[ip] += 1
        else:
            failed_attempts[ip] = 1

for ip, count in failed_attempts.items():
    if count >= 3:
        print("\n⚠ Suspicious Activity Detected")
        print(f"Suspicious activity detected from IP: {ip}")
        print(f"Number of failed login attempts: {count}")
        print("Reason: Multiple failed login attempts")