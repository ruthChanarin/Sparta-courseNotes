import csv

def transform_user_details(csv_file_name):
    new_user_data = []
    with open(csv_file_name, newline='') as csvfile:
        user_details_csv = csv.reader(csvfile, delimiter=",")

        for user in user_details_csv:
            transformation = []
            transformation.append(user[1]) # first name
            transformation.append(user[2]) # last name
            transformation.append(user[-1]) # email

            new_user_data.append(transformation)

    return new_user_data

def create_new_user_details(old_file_name="user_details.csv", new_file_name = "new_user_details.csv"):
    new_user_data = transform_user_details(old_file_name)
    with open(new_file_name, "w", newline='') as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(new_user_data)

create_new_user_details()