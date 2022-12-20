def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w")
    file.write("Company, Title, Location, Pay, Link\n")

    for job in jobs:
        file.write(f"{job['Company']},{job['Title']},{job['Location']},{job['pay']},{job['link']}\n")

    file.close()