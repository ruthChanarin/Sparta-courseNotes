
import pandas


nme = ['Tommy', 'Ruth', 'Ruth', 'Taslima', 'Isak', 'Killian', 'Yuvraj']
deg = ["Biochemistry", "English", "English", "English", "ComputerScience", "Biomedicine", "Biology"]
age = [24, 28, 28, 25, 30, 25, 23]

# dictionary of lists
dict = {'name': nme, 'degree': deg, 'score': age}
df = pd.DataFrame(dict)
print(df)

