
import requests
# Creating favourite_lyrics file.
with open('favourite_lyrics.txt', 'w+') as lyrics_file:
    # Song counter, begins at 0.
    song_counter = 0

    # Ask user for artist and song title until song counter is 5.
    while song_counter < 5:
        artist = input('What is your favourite artist?')
        title = input('What is your favourite song from them?')
        url = 'https://api.lyrics.ovh/v1/{}/{}'.format(artist, title)
        response = requests.get(url)
        song = response.json()
        # Try catch, will catch error if no lyrics are found and print error from the API.
        # If lyrics found, will print artist, title and song to the file.
        # If lyrics found, will add 1 to the song_counter.
        try:
            if song['lyrics']:
                lyrics_file.write((artist + '\n').title())
                lyrics_file.write((title + '\n\n').title())
                lyrics_file.write(str(song['lyrics']))
                lyrics_file.write('\n\n\n\n')
                song_counter = song_counter + 1
        except Exception:
            print(song['error'])