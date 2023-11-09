CREATE table if not exists users (
	id SERIAL PRIMARY KEY,
	username VARCHAR(30) UNIQUE NOT NULL,
	password VARCHAR(102) NOT NULL
);

CREATE TABLE if not exists articles (
	id SERIAL PRIMARY KEY,
	user_id INT NOT NULL,
	title VARCHAR(50),
	article_text TEXT,
	is_favorite bool,
	is_public bool,
	likes INT,
	FOREIGN KEY (user_id) REFERENCES users (id)
);

