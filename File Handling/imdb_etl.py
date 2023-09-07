import csv

def twenty_ten_onwards(film, year):
    if int((film[4])) >= year:
        return True
               
        
def only_movies(film, title_type):
    if film[0] == title_type:
        return True

        
def transform_imbd_details(filename):
    new_imdb_data = []
    with open(filename, newline='') as csvfile:
        imdb_csv = csv.reader(csvfile, delimiter=",")
        
        iterable_csv = iter(imdb_csv)
        next(iterable_csv)  
        
        for film in imdb_csv:
            if twenty_ten_onwards(film, 2010) and only_movies(film, 'movie'):

                transformation = []

                transformation.append(film[0])
                transformation.append(film[1])
                transformation.append(film[4])
                transformation.append(film[6])
                transformation.append(film[7])

                new_imdb_data.append(transformation)

    return new_imdb_data


def create_new_imbd_details(old_file_name="imdbtitles.csv", new_file_name = "new_imdb_details.csv"):
    new_user_data = transform_imbd_details(old_file_name)
    with open(new_file_name, "w", newline='') as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(new_user_data)

create_new_imbd_details()

