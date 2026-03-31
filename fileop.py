import os

# ---------------------------
# 1. WRITE to a file
# ---------------------------
print("---- Writing to file ----")
with open("example.txt", "w") as f:
    f.write("Hello Rohith!\n")
    f.write("This is a file operations demo.\n")
    f.write("Python is simple and powerful.\n")

# ---------------------------
# 2. READ the entire file
# ---------------------------
print("\n---- Reading full file ----")
with open("example.txt", "r") as f:
    print(f.read())

# ---------------------------
# 3. READ line-by-line
# ---------------------------
print("\n---- Reading line by line ----")
with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())

# ---------------------------
# 4. APPEND new data
# ---------------------------
print("\n---- Appending data ----")
with open("example.txt", "a") as f:
    f.write("This line is appended.\n")

# ---------------------------
# 5. READLINES() example
# ---------------------------
print("\n---- Using readlines() ----")
with open("example.txt", "r") as f:
    lines = f.readlines()
    print(lines)

# ---------------------------
# 6. Using tell() and seek()
# ---------------------------
print("\n---- Using tell() and seek() ----")
with open("example.txt", "r") as f:
    print("Pointer at start:", f.tell())    # 0
    
    data = f.read(10)                       # read first 10 characters
    print("Read first 10 chars:", data)
    print("Pointer after read(10):", f.tell())
    
    f.seek(0)                                # Move pointer to beginning
    print("Pointer after seek(0):", f.tell())

    data2 = f.read(5)
    print("Read first 5 chars again:", data2)

# ---------------------------
# 7. Check if file exists
# ---------------------------
print("\n---- Checking file exists ----")
if os.path.exists("example.txt"):
    print("File exists!")
else:
    print("File does not exist.")

# ---------------------------
# 8. DELETE file (optional)
# ---------------------------
choice = input("\nDo you want to delete the file? (yes/no): ")
if choice.lower() == "yes":
    os.remove("example.txt")
    print("File deleted!")
else:
    print("File not deleted.")
