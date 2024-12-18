//v0.1.1

CREATE TABLE `Stats` (
  `id` Int PRIMARY KEY,
  `name` varchar(32) UNIQUE,
  `value` int DEFAULT 0
);
CREATE TABLE `StatRange` (
  `stat_id` int PRIMARY KEY,
  `range_start` float DEFAULT 0,
  `range_end` float
);

CREATE TABLE `File` (
  `id` integer PRIMARY KEY,
  `track_id` int,
  `audio_ip` varchar(80),
  `import_path` varchar(255),
  `imported` timestamp DEFAULT now(),
  `processed` timestamp,
  `bitrate` int,
  `codec` ENUM ('mp3', 'mp2', 'flac', 'wav', 'mp4', 'm4a'),
  `length` float,
  `stage` int DEFAULT 0
);
CREATE TABLE `FilePath` (
  `file_id` int PRIMARY KEY,
  `path` varchar(255),
  `definitive` bool
);

CREATE TABLE `Track` ( `id` integer PRIMARY KEY );
CREATE TABLE `TrackTitle` (
  `track_id` int PRIMARY KEY,
  `title` varchar(40),
  `main` bool DEFAULT 1
);
CREATE TABLE `TrackMBid` (
  `track_id` int PRIMARY KEY,
  `mbid` varchar(80) UNIQUE
);
CREATE TABLE `Key` (
  `id` int PRIMARY KEY,
  `name` varchar(8)
);
CREATE TABLE `TrackKey` (
  `track_id` int,
  `key_id` int
  PRIMARY KEY (`track_id`, `key_id`)

);
CREATE TABLE `TrackGenre` (
  `track_id` Int,
  `genre_id` Int,
  PRIMARY KEY (`track_id`, `genre_id`)
);
CREATE TABLE `TrackPerson` (
  `track_id` Int,
  `person_id` Int,
  `role` ENUM ('artist', 'conductor', 'composer', 'lyricist', 'producer'),
  PRIMARY KEY (`track_id`, `person_id`)
);
CREATE TABLE `Track_TrackPerson` (
  `Track_id` integer,
  `TrackPerson_track_id` Int,
  PRIMARY KEY (`Track_id`, `TrackPerson_track_id`)
);
CREATE TABLE `Track_TrackGenre` (
  `Track_id` integer,
  `TrackGenre_track_id` Int,
  PRIMARY KEY (`Track_id`, `TrackGenre_track_id`)
);

CREATE TABLE `Album` (
  `id` int PRIMARY KEY,
  `tracks` smallint,
  `discs` smallint
);
CREATE TABLE `AlbumLabel` (
  `album_id` int,
  `label_id` int
);
CREATE TABLE `AlbumTitle` (
  `id` int PRIMARY KEY,
  `album_id` int,
  `title` varchar(64),
  `main` bool DEFAULT 1
);
CREATE TABLE `AlbumMBid` (
  `album_id` int PRIMARY KEY,
  `mbid` varchar(80) UNIQUE
);
CREATE TABLE `AlbumPicture` (
  `id` int PRIMARY KEY,
  `album_id` int,
  `picture_path` varchar(255)
);
CREATE TABLE `AlbumPerson` (
  `album_id` Int,
  `person_id` Int,
  `role` ENUM ('artist', 'conductor', 'composer', 'lyricist', 'producer'),
  PRIMARY KEY (`album_id`, `person_id`)
);
CREATE TABLE `AlbumGenre` (
  `album_id` Int,
  `genre_id` Int,
  PRIMARY KEY (`album_id`, `genre_id`)
);
CREATE TABLE `Album_AlbumPerson` (
  `Album_id` int,
  `AlbumPerson_album_id` Int,
  PRIMARY KEY (`Album_id`, `AlbumPerson_album_id`)
);
CREATE TABLE `Album_AlbumGenre` (
  `Album_id` int,
  `AlbumGenre_album_id` Int,
  PRIMARY KEY (`Album_id`, `AlbumGenre_album_id`)
);

CREATE TABLE `Person` ( `id` int PRIMARY KEY );
CREATE TABLE `PersonName` (
  `id` int PRIMARY KEY,
  `person_id` int,
  `name` varchar(80),
  `type` ENUM ('first', 'middle', 'last')
);
CREATE TABLE `PersonMBid` (
  `person_id` int PRIMARY KEY,
  `mbid` varchar(80) UNIQUE
);
CREATE TABLE `PersonDate` (
  `id` int PRIMARY KEY,
  `person_id` int,
  `date` date,
  `born_deceased` bool DEFAULT 1
);
CREATE TABLE `PersonPicture` (
  `id` int PRIMARY KEY,
  `person_id` int,
  `picture_path` varchar(255)
);
CREATE TABLE `Person_TrackPerson` (
  `Person_id` int,
  `TrackPerson_person_id` Int,
  PRIMARY KEY (`Person_id`, `TrackPerson_person_id`)
);
CREATE TABLE `Person_AlbumPerson` (
  `Person_id` int,
  `AlbumPerson_person_id` Int,
  PRIMARY KEY (`Person_id`, `AlbumPerson_person_id`)
);

CREATE TABLE `Disc` (
  `id` int PRIMARY KEY,
  `album_id` int,
  `disc_no` smallint DEFAULT 1
);
CREATE TABLE `DiscTitle` (
  `id` int PRIMARY KEY,
  `disc_id` int,
  `title` varchar(255),
  `main` bool
);

CREATE TABLE `Label` (
  `id` int PRIMARY KEY,
  `name` varchar(64)
);
CREATE TABLE `LabelParent` (
  `label_id` int,
  `parent_id` int,
  PRIMARY KEY (`label_id`, `parent_id`)
);
CREATE TABLE `LabelOwner` (
  `label_id` int,
  `owner_id` in,
  PRIMARY KEY (`label_id`, `owner_id`)
);

CREATE TABLE `Genre` (
  `id` int PRIMARY KEY,
  `name` varchar(80)
);
CREATE TABLE `GenreParent` (
  `genre_id` int,
  `parent_id` int,
  PRIMARY KEY (`genre_id`, `parent_id`)
);
CREATE TABLE `Genre_GenreParent` (
  `Genre_id` int,
  `GenreParent_genre_id` int,
  PRIMARY KEY (`Genre_id`, `GenreParent_genre_id`)
);
CREATE TABLE `Genre_GenreParent(1)` (
  `Genre_id` int,
  `GenreParent_parent_id` int,
  PRIMARY KEY (`Genre_id`, `GenreParent_parent_id`)
);
CREATE TABLE `Genre_TrackGenre` (
  `Genre_id` int,
  `TrackGenre_genre_id` Int,
  PRIMARY KEY (`Genre_id`, `TrackGenre_genre_id`)
);
CREATE TABLE `Genre_AlbumGenre` (
  `Genre_id` int,
  `AlbumGenre_genre_id` Int,
  PRIMARY KEY (`Genre_id`, `AlbumGenre_genre_id`)
);

ALTER TABLE `StatRange` ADD FOREIGN KEY (`stat_id`) REFERENCES `Stats` (`id`);

ALTER TABLE `File` ADD FOREIGN KEY (`track_id`) REFERENCES `Track` (`id`);
ALTER TABLE `FilePath` ADD FOREIGN KEY (`file_id`) REFERENCES `File` (`id`);

ALTER TABLE `TrackTitle` ADD FOREIGN KEY (`track_id`) REFERENCES `Track` (`id`);
ALTER TABLE `TrackMBid` ADD FOREIGN KEY (`track_id`) REFERENCES `Track` (`id`);
ALTER TABLE `Track_TrackPerson` ADD FOREIGN KEY (`Track_id`) REFERENCES `Track` (`id`);
ALTER TABLE `Track_TrackPerson` ADD FOREIGN KEY (`TrackPerson_track_id`) REFERENCES `TrackPerson` (`track_id`);
ALTER TABLE `TrackKey` ADD FOREIGN KEY (`track_id`) REFERENCES `Track` (`id`);
ALTER TABLE `TrackKey` ADD FOREIGN KEY (`key_id`) REFERENCES `Key` (`id`);
ALTER TABLE `Track_TrackGenre` ADD FOREIGN KEY (`Track_id`) REFERENCES `Track` (`id`);
ALTER TABLE `Track_TrackGenre` ADD FOREIGN KEY (`TrackGenre_track_id`) REFERENCES `TrackGenre` (`track_id`);

ALTER TABLE `AlbumLabel` ADD FOREIGN KEY (`album_id`) REFERENCES `Album` (`id`);
ALTER TABLE `AlbumLabel` ADD FOREIGN KEY (`label_id`) REFERENCES `Label` (`id`);
ALTER TABLE `AlbumTitle` ADD FOREIGN KEY (`album_id`) REFERENCES `Album` (`id`);
ALTER TABLE `AlbumMBid` ADD FOREIGN KEY (`album_id`) REFERENCES `Album` (`id`);
ALTER TABLE `Album` ADD FOREIGN KEY (`id`) REFERENCES `AlbumPicture` (`album_id`);
ALTER TABLE `Album_AlbumPerson` ADD FOREIGN KEY (`Album_id`) REFERENCES `Album` (`id`);
ALTER TABLE `Album_AlbumPerson` ADD FOREIGN KEY (`AlbumPerson_album_id`) REFERENCES `AlbumPerson` (`album_id`);
ALTER TABLE `Album_AlbumGenre` ADD FOREIGN KEY (`Album_id`) REFERENCES `Album` (`id`);
ALTER TABLE `Album_AlbumGenre` ADD FOREIGN KEY (`AlbumGenre_album_id`) REFERENCES `AlbumGenre` (`album_id`);

ALTER TABLE `PersonName` ADD FOREIGN KEY (`person_id`) REFERENCES `Person` (`id`);
ALTER TABLE `PersonMBid` ADD FOREIGN KEY (`person_id`) REFERENCES `Person` (`id`);
ALTER TABLE `PersonDate` ADD FOREIGN KEY (`person_id`) REFERENCES `Person` (`id`);
ALTER TABLE `Person` ADD FOREIGN KEY (`id`) REFERENCES `PersonPicture` (`person_id`);
ALTER TABLE `Person_TrackPerson` ADD FOREIGN KEY (`Person_id`) REFERENCES `Person` (`id`);
ALTER TABLE `Person_TrackPerson` ADD FOREIGN KEY (`TrackPerson_person_id`) REFERENCES `TrackPerson` (`person_id`);
ALTER TABLE `Person_AlbumPerson` ADD FOREIGN KEY (`Person_id`) REFERENCES `Person` (`id`);
ALTER TABLE `Person_AlbumPerson` ADD FOREIGN KEY (`AlbumPerson_person_id`) REFERENCES `AlbumPerson` (`person_id`);

ALTER TABLE `Disc` ADD FOREIGN KEY (`album_id`) REFERENCES `Album` (`id`);
ALTER TABLE `DiscTitle` ADD FOREIGN KEY (`disc_id`) REFERENCES `Disc` (`id`);

ALTER TABLE `LabelParent` ADD FOREIGN KEY (`label_id`) REFERENCES `Label` (`id`);
ALTER TABLE `LabelParent` ADD FOREIGN KEY (`parent_id`) REFERENCES `Label` (`id`);
ALTER TABLE `LabelOwner` ADD FOREIGN KEY (`label_id`) REFERENCES `Label` (`id`);
ALTER TABLE `LabelOwner` ADD FOREIGN KEY (`owner_id`) REFERENCES `Person` (`id`);

ALTER TABLE `Genre_GenreParent` ADD FOREIGN KEY (`Genre_id`) REFERENCES `Genre` (`id`);
ALTER TABLE `Genre_GenreParent` ADD FOREIGN KEY (`GenreParent_genre_id`) REFERENCES `GenreParent` (`genre_id`);
ALTER TABLE `Genre_GenreParent(1)` ADD FOREIGN KEY (`Genre_id`) REFERENCES `Genre` (`id`);
ALTER TABLE `Genre_GenreParent(1)` ADD FOREIGN KEY (`GenreParent_parent_id`) REFERENCES `GenreParent` (`parent_id`);
ALTER TABLE `Genre_TrackGenre` ADD FOREIGN KEY (`Genre_id`) REFERENCES `Genre` (`id`);
ALTER TABLE `Genre_TrackGenre` ADD FOREIGN KEY (`TrackGenre_genre_id`) REFERENCES `TrackGenre` (`genre_id`);
ALTER TABLE `Genre_AlbumGenre` ADD FOREIGN KEY (`Genre_id`) REFERENCES `Genre` (`id`);
ALTER TABLE `Genre_AlbumGenre` ADD FOREIGN KEY (`AlbumGenre_genre_id`) REFERENCES `AlbumGenre` (`genre_id`);
