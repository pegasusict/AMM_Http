CREATE TABLE `Stats` (
  `id` Int PRIMARY KEY,
  `name` varchar(255) UNIQUE,
  `range` int,
  `value` int
);

CREATE TABLE `File` (
  `id` integer PRIMARY KEY,
  `track_id` int,
  `audio_ip` string(80),
  `import_path` string,
  `quarantine_path` string,
  `definitive_path` string,
  `imported` timestamp,
  `processed` timestamp
);

CREATE TABLE `Track` (
  `id` integer PRIMARY KEY,
  `mbid` varchar(255) UNIQUE,
  `key_id` varchar(255),
  `title` varchar(255),
  `subtitle` varchar(255)
);

CREATE TABLE `Album` (
  `id` int PRIMARY KEY,
  `mbid` varchar(255) UNIQUE,
  `title` varchar(255),
  `subtitle` varchar(255),
  `tracks` int,
  `discs` int,
  `label_id` int
);

CREATE TABLE `Person` (
  `id` int PRIMARY KEY,
  `mbid` varchar(255),
  `first_name` varchar(255),
  `middle_name` varchar(255),
  `last_name` varchar(255),
  `born` datetime,
  `deceased` datetime
);

CREATE TABLE `Disc` (
  `albumid` int,
  `discno` int,
  `title` varchar(255),
  `subtitle` varchar(255),
  PRIMARY KEY (`albumid`, `discno`)
);

CREATE TABLE `Key` (
  `id` int PRIMARY KEY,
  `name` varchar(255)
);

CREATE TABLE `Label` (
  `id` int PRIMARY KEY,
  `name` varchar(255),
  `parent_id` int,
  `owner_id` int
);

CREATE TABLE `Genre` (
  `id` int PRIMARY KEY,
  `name` varchar(255),
  `parent_id` int
);

CREATE TABLE `TrackPerson` (
  `track_id` Int,
  `person_id` Int,
  `role` ENUM ('artist', 'conductor', 'composer', 'lyricist', 'producer'),
  PRIMARY KEY (`track_id`, `person_id`)
);

CREATE TABLE `AlbumPerson` (
  `album_id` Int,
  `person_id` Int,
  `role` ENUM ('artist', 'conductor', 'composer', 'lyricist', 'producer'),
  PRIMARY KEY (`album_id`, `person_id`)
);

CREATE TABLE `TrackGenre` (
  `track_id` Int,
  `genre_id` Int,
  PRIMARY KEY (`track_id`, `genre_id`)
);

CREATE TABLE `AlbumGenre` (
  `album_id` Int,
  `genre_id` Int,
  PRIMARY KEY (`album_id`, `genre_id`)
);

ALTER TABLE `File` ADD FOREIGN KEY (`track_id`) REFERENCES `Track` (`id`);

ALTER TABLE `Track` ADD FOREIGN KEY (`key_id`) REFERENCES `Key` (`id`);

ALTER TABLE `Album` ADD FOREIGN KEY (`label_id`) REFERENCES `Label` (`id`);

CREATE TABLE `Album_Disc` (
  `Album_id` int,
  `Disc_albumid` int,
  PRIMARY KEY (`Album_id`, `Disc_albumid`)
);

ALTER TABLE `Album_Disc` ADD FOREIGN KEY (`Album_id`) REFERENCES `Album` (`id`);

ALTER TABLE `Album_Disc` ADD FOREIGN KEY (`Disc_albumid`) REFERENCES `Disc` (`albumid`);


ALTER TABLE `Label` ADD FOREIGN KEY (`parent_id`) REFERENCES `Label` (`id`);

ALTER TABLE `Label` ADD FOREIGN KEY (`owner_id`) REFERENCES `Person` (`id`);

ALTER TABLE `Genre` ADD FOREIGN KEY (`parent_id`) REFERENCES `Genre` (`id`);

CREATE TABLE `Track_TrackPerson` (
  `Track_id` integer,
  `TrackPerson_track_id` Int,
  PRIMARY KEY (`Track_id`, `TrackPerson_track_id`)
);

ALTER TABLE `Track_TrackPerson` ADD FOREIGN KEY (`Track_id`) REFERENCES `Track` (`id`);

ALTER TABLE `Track_TrackPerson` ADD FOREIGN KEY (`TrackPerson_track_id`) REFERENCES `TrackPerson` (`track_id`);


CREATE TABLE `Person_TrackPerson` (
  `Person_id` int,
  `TrackPerson_person_id` Int,
  PRIMARY KEY (`Person_id`, `TrackPerson_person_id`)
);

ALTER TABLE `Person_TrackPerson` ADD FOREIGN KEY (`Person_id`) REFERENCES `Person` (`id`);

ALTER TABLE `Person_TrackPerson` ADD FOREIGN KEY (`TrackPerson_person_id`) REFERENCES `TrackPerson` (`person_id`);


CREATE TABLE `Album_AlbumPerson` (
  `Album_id` int,
  `AlbumPerson_album_id` Int,
  PRIMARY KEY (`Album_id`, `AlbumPerson_album_id`)
);

ALTER TABLE `Album_AlbumPerson` ADD FOREIGN KEY (`Album_id`) REFERENCES `Album` (`id`);

ALTER TABLE `Album_AlbumPerson` ADD FOREIGN KEY (`AlbumPerson_album_id`) REFERENCES `AlbumPerson` (`album_id`);


CREATE TABLE `Person_AlbumPerson` (
  `Person_id` int,
  `AlbumPerson_person_id` Int,
  PRIMARY KEY (`Person_id`, `AlbumPerson_person_id`)
);

ALTER TABLE `Person_AlbumPerson` ADD FOREIGN KEY (`Person_id`) REFERENCES `Person` (`id`);

ALTER TABLE `Person_AlbumPerson` ADD FOREIGN KEY (`AlbumPerson_person_id`) REFERENCES `AlbumPerson` (`person_id`);


CREATE TABLE `Track_TrackGenre` (
  `Track_id` integer,
  `TrackGenre_track_id` Int,
  PRIMARY KEY (`Track_id`, `TrackGenre_track_id`)
);

ALTER TABLE `Track_TrackGenre` ADD FOREIGN KEY (`Track_id`) REFERENCES `Track` (`id`);

ALTER TABLE `Track_TrackGenre` ADD FOREIGN KEY (`TrackGenre_track_id`) REFERENCES `TrackGenre` (`track_id`);


CREATE TABLE `Genre_TrackGenre` (
  `Genre_id` int,
  `TrackGenre_genre_id` Int,
  PRIMARY KEY (`Genre_id`, `TrackGenre_genre_id`)
);

ALTER TABLE `Genre_TrackGenre` ADD FOREIGN KEY (`Genre_id`) REFERENCES `Genre` (`id`);

ALTER TABLE `Genre_TrackGenre` ADD FOREIGN KEY (`TrackGenre_genre_id`) REFERENCES `TrackGenre` (`genre_id`);


CREATE TABLE `Album_AlbumGenre` (
  `Album_id` int,
  `AlbumGenre_album_id` Int,
  PRIMARY KEY (`Album_id`, `AlbumGenre_album_id`)
);

ALTER TABLE `Album_AlbumGenre` ADD FOREIGN KEY (`Album_id`) REFERENCES `Album` (`id`);

ALTER TABLE `Album_AlbumGenre` ADD FOREIGN KEY (`AlbumGenre_album_id`) REFERENCES `AlbumGenre` (`album_id`);


CREATE TABLE `Genre_AlbumGenre` (
  `Genre_id` int,
  `AlbumGenre_genre_id` Int,
  PRIMARY KEY (`Genre_id`, `AlbumGenre_genre_id`)
);

ALTER TABLE `Genre_AlbumGenre` ADD FOREIGN KEY (`Genre_id`) REFERENCES `Genre` (`id`);

ALTER TABLE `Genre_AlbumGenre` ADD FOREIGN KEY (`AlbumGenre_genre_id`) REFERENCES `AlbumGenre` (`genre_id`);

