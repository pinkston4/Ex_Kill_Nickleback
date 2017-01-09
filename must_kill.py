songs = {
	('Nickleback', 'photograph'),
	('Nickleback', 'Animals'),
	('Tool', 'schism'),
	('Tom Petty and The Heartbreakers', 'Mary-Janes last Dance'),
	('Nickleback', 'How you remind me'),
	('A day to remember', 'All signs point to lauderdale'),
	('Skip James', 'Devil got my woman')
}

actual_music = {song for song in songs if song[0] != 'Nickleback'}

print(actual_music)