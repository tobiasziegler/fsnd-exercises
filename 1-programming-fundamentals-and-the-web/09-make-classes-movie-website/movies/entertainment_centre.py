import media

toy_story = media.Movie("Toy Story",
"A story of a boy and his toys that come to life",
"http://upload.wikimedia.org/wikipedia/1/13/Toy_Story.jpg",
"https://www.youtube.com/watch?v=vwyZH85NQC4")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
"A marine on an alien planet",
"http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
"https://www.youtube.com/watch?v=-9ceBgWV8io")

#print(avatar.storyline)
#avatar.show_trailer()

deadpool = media.Movie("Deadpool",
"A fast-talking mercenary with a morbid sense of humor is subjected to a rogue experiment that leaves him with accelerated healing powers and a quest for revenge",
"https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
"https://www.youtube.com/watch?v=FyKWUTwSYAs")

deadpool.show_trailer()
