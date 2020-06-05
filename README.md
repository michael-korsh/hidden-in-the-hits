# Hidden in the Hits

## The Hot 100 Playlists
*Billboard* magazine publishes the Year-End Hot 100: an annual listing of the hundred most popular songs in the United States. Spotify users have also converted each of these Hot 100s into a distinct Spotify playlist:
* [2010 playlist](https://open.spotify.com/playlist/4aUY170nZ3mhkzMpTAXDv2?si=_JHnbbsmShePEDyUCxXr8g)
* [2011 playlist](https://open.spotify.com/playlist/2z3eLip2NlV9quzTEm37cW?si=uufNrP97T5eNNmvmPcfBLg)
* [2012 playlist](https://open.spotify.com/playlist/6ERBbbhAninxZrDNNwFAYD?si=OhsUgsU2TLWGupQgXpTHzg)
* [2013 playlist](https://open.spotify.com/playlist/1KK0RvFmgsUkZ8zELRZgjS)
* [2014 playlist](https://open.spotify.com/playlist/2trgZsxRpWX7sq28yHC40u)
* [2015 playlist](https://open.spotify.com/playlist/6LYxiUgw87zsDPqU0sdalZ)
* [2016 playlist](https://open.spotify.com/playlist/3JbWD8OGutoTKUbR3RvR8u)
* [2017 playlist](https://open.spotify.com/playlist/2XPEN88QyrPQ9zGqS8uS2x)
* [2018 playlist](https://open.spotify.com/playlist/4wSmeoexS546V0zZ0tpMAz)
* [2019 playlist](https://open.spotify.com/playlist/5lO5SKSvwbLetiBt6k7wNX)

## hot_100_script.py
This Python script uses **Spotipy**, a lightweight library to access the Python API, as well as **pandas** and **numpy**. It includes a series of functions that collect the following information from each playlist into a pandas DataFrame:
*Basic Information*
* **Name:** Song name.
* **Artist:** Name(s) of artist(s) of the song.
* **Year:** What year the song appeared on the *Billboard* Hot 100. *Note: Some songs appear multiple times in the dataset. These duplicates were kept to account for biannual popularity and year-to-year position differences*
* **Position:** What position the song was in on the Hot 100.

*Audio Features*
Spotipy includes many other features through their `sp.audio_features` function. You can customize the code to analyze any features you want!
* **Key (int):** The estimated key of the song in pitch class notation (with integer values assigned to each key).
* **Mode (int):** The mode of the song, with major = 1 and minor = 0.
* **Valence (float):** The emotional valence of a song. The Spotify API defines emotional valence as the following:
> "A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry)."

Because key and mode are expressed as an integer, I created two separate dataframes to reference the keys/modes in their respective text format. All three DataFrames are then converted into CSVs.

## hot_100_data.csv
This is a CSV of the above information for all 1,000 data points, with a couple modifications:
* I used SQL to concatenate the keys and modes into a single measurement called Full Key.
* Key and mode are represented in string format rather than int.

---

# About the Project
This repository is a combination of projects for 2 classes (JOUR 377 and CS 217) at Northwestern University. Through it, I conducted data analysis and visualization and created a final data journalism piece on Tableau Public.

For any questions about the data, you can contact me at mkorsh@u.northwestern.edu.
