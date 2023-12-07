
#Design a class called Album. The class should contain:
# The data fields albumName (String), numberOfSongs (int) and albumArtist (String).
# A __str__ method that returns a string that represents an Album object in the following format:
#(albumName, albumArtist, numberOfSongs)

class Album:

    def __init__(self, albumName, numberOfsongs, albumArtist):
        self.albumName = albumName
        self.numberOfsongs = numberOfsongs
        self.albumArtist = albumArtist

    def __str__(self):
        return self.albumName, self.albumArtist, self.numberOfsongs
    

#Create a new list called albums1, add 5 albums to it and print it out.
print("Number 1:")
artist_1 = Album("Astroworld", 17, "Travis Scott")
artist_2 = Album("Utopia", 19, "Travis Scoot")
artist_3 = Album("Her loss", 16, "Drake")
artist_4 = Album("Certified Lover Boy", 21, "Drake")
artist_5 = Album("Donda", 32, "Kanye West")

albums1 = [artist_1, artist_2, artist_3, artist_4, artist_5]

for i in albums1:
    print(i.albumName, i.numberOfsongs, i.albumArtist)

#Sort the list according to the numberOfSongs and print it out.
print("\n Number 2:")
albums1.sort(key = lambda x: x.numberOfsongs)
for i in albums1:
    print(i.albumName, i.numberOfsongs, i.albumArtist)

#Swap the element at position 1 of albums1 with the element at position 2 and print it out.
#def posSwap(list, position_1, position_2, position_3):
print("\n Number 3:")
def posSwap(list, position_1, position_2):
    list[position_1], list[position_2] = list[position_2], list[position_1]
    #return list

elements_1 = 1
elements_2 = 2

print(posSwap(albums1, elements_1, elements_2))
for i in albums1:
    print(i.albumName, i.numberOfsongs, i.albumArtist)

# Create a new list called albums2.
albums2 = []

# Add 5 albums to the albums2 List and print it out.
print("\n Number 4:")
singer_1 = Album("Heartbreak on a fullmoon", 14, "Chris Brown")
singer_2 = Album("ATLiens", 24, "OutKast")
singer_3 = Album("Al-Naafiysh(The Soul)", 10, "Hashm")
singer_4 = Album("Drukqs", 5, "Apex Twin")
singer_5 = Album("TRON: Legacy", 20, "Daft Punk")

albums2 = [singer_1, singer_2, singer_3, singer_4, singer_5]
for i in albums2:
    print(i.albumName, i.numberOfsongs, i.albumArtist)

# Copy all of the albums from albums1 into albums2.
print("\n Number 5:")
def copy(list_1):
    list_copy = list_1[::]
    return list_copy

albums2 = copy(albums1)
for i in albums2:
    print(i.albumName, i.numberOfsongs, i.albumArtist)

albums2.extend(albums1)
for i in albums2:
    print(i.albumName, i.numberOfsongs, i.albumArtist)

print("\n Number 6:")
#Add the following two elements to albums2:
#(Dark Side of the Moon, Pink Floyd, 9)
#(Oops!... I Did It Again, Britney Spears, 16)
singer_6 = Album("Dark Side of the Moon", 9, "Pink Floyd")
singer_7 = Album("Oops!...I Did It Again", 16, "Britney Spears")

albums2.append(singer_6)
albums2.append(singer_7)
for i in albums2:
    print(i.albumName, i.numberOfsongs, i.albumArtist)

print("\n Number 7:") 
#Sort the courses in albums2 alphabetically according to the album name and print it out.
albums2.sort(key= lambda x: x.albumName)
for i in albums2:
    print(i.albumName)

print("\n Number 8:")
# Search for the album “Dark Side of the Moon” in albums2 and print out the index of the album in the List
for i in albums2:
    #print(i.albumName)
    if i.albumName == "Dark Side of the Moon":
        print("The index of 'Dark Side of Moon' is", albums2.index(i))