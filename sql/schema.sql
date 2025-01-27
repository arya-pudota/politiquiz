PRAGMA foreign_keys = ON;

CREATE TABLE questions (
	qid INTEGER NOT NULL,
	text VARCHAR(1024) NOT NULL,
	topic VARCHAR(20) NOT NULL,
	lean INTEGER NOT NULL,
	text_detail VARCHAR(1024),
  	PRIMARY KEY(qid)
);

CREATE TABLE answers (
    aid INTEGER NOT NULL,
    qid INTEGER NOT NULL,
	text INTEGER NOT NULL,
	lean INTEGER NOT NULL,
	PRIMARY KEY (qid, aid),
	FOREIGN KEY (qid) REFERENCES questions(qid) ON UPDATE CASCADE ON DELETE CASCADE
);