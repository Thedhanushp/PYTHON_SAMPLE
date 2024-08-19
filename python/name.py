#split name first name and last name
name = input("whats your name ? ").strip().title()
first,last = name.split(" ")
print(f"Hello {first}")#only call first name 