HMTime = int(input("How many people we have: "))

name = {}  
genres = {"Horror": 0, "Romance": 0, "Comedy": 0, "History": 0, "Adventure": 0, "Action": 0}

for i in range(HMTime):
    x = input("Enter name and 3 genres (separated by spaces): ").split()
    if len(x) >= 4:  
        person_name = x[0]
        person_genres = x[1:4]  
        name[person_name] = person_genres 
        
        for genre in person_genres:
            if genre in genres:
                genres[genre] += 1



sorted_genres = sorted(
    genres.items(),
    key=lambda x: (-x[1], x[0])
)

for genre, count in sorted_genres:
    print(f"{genre}: {count}")
