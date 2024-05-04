with open ("hr_system.txt") as resources:
    for line in resources:
        data = line.split(" ")
        paycheck = float(data[3])/24
        if(data[2].lower() == "enginner"):
            paycheck += 1000
        print(f"{data[0]} (ID{data[1]}), {data[2]} - ${paycheck:.2f}")