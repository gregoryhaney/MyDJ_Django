
INSERT INTO app_api_techtag 
VALUES(43,"Blockchain");
INSERT INTO app_api_techtag 
VALUES(44,"Predictive Analytics");
INSERT INTO app_api_techtag 
VALUES(45,"AI");
INSERT INTO app_api_techtag 
VALUES(46,"ML");
INSERT INTO app_api_techtag 
VALUES(47,"Edge Computing");
INSERT INTO app_api_techtag 
VALUES(48,"VR");
INSERT INTO app_api_techtag 
VALUES(49,"AR");
INSERT INTO app_api_techtag 
VALUES(50,"5G");
INSERT INTO app_api_techtag 
VALUES(51,"Cybersecurity");
INSERT INTO app_api_techtag 
VALUES(52,"3d Printing");


DROP TABLE app_api_entry_moodtag

CREATE TABLE app_api_entry (
    id INT PRIMARY KEY,
    datetime DATETIME,
    subject VARCHAR(150),
    body VARCHAR(8000),
    is_public BOOLEAN,
    techtag INT,
    moodtag INT,
    developer INT
    );

DROP TABLE app_api_entry_techtag;
DROP TABLE app_api_entry_moodtag;

CREATE TABLE app_api_entry_techtag (
    id integer PRIMARY KEY NOT NULL,
    entry_id integer,
    techtag_id integer);

CREATE TABLE app_api_entry_moodtag (
    id integer PRIMARY KEY NOT NULL,
    entry_id integer,
    moodtag_id integer);

CREATE TABLE app_api_user_developer (
    id integer PRIMARY KEY NOT NULL,
    user_id integer NOT NULL,
    developer_id integer NOT NULL);



INSERT INTO app_api_entry
VALUES(11,"2021-07-21T12:25:27.144Z","Five ways I found to write cleaner code",
"A velit sapiente quasi omnis officia amet. Quidem sed ea illo ea qui qui. Nesciunt ipsam omnis laboriosam sit et nobis dignissimos. Architecto quaerat magni soluta earum. Iure architecto eum enim repudiandae expedita distinctio. Ut omnis maxime quaerat eius nemo vero. Quia nihil velit et beatae omnis eos itaque pariatur.",
true,18,3,2);
INSERT INTO app_api_entry
VALUES(12,"2022-03-29T13:24:27.144Z","How to use the arrow function like a boss",
"Quidem sed ea illo ea qui qui. Nesciunt ipsam omnis laboriosam sit et nobis dignissimos. Architecto quaerat magni soluta earum. Saepe numquam in non dolore. Qui est non neque adipisci. Tempora voluptatem aut sit molestiae modi.",
true,7,12,1);
INSERT INTO app_api_entry
VALUES(13,"2021-04-04T13:24:27.144Z","Deep dive on React components",
"Dolores sit tempore qui itaque quisquam est sit non. Dolor reprehenderit sit sed accusantium et. Non nisi et ipsa quasi hic et dolor. Odit sint omnis quibusdam assumenda. Quidem sed ea illo ea qui qui. Nesciunt ipsam omnis laboriosam sit et nobis dignissimos. Architecto quaerat magni soluta earum.",
false,2,16,3);



UPDATE auth_user
SET last_name = "Wharf",
    first_name = "Sheldon",
    email = "sw1445@starfleet.net"
WHERE id = 6

UPDATE app_api_entry
SET subject = "My first month as a new developer",
    body = "Aut sed a officia est repellat. Voluptatibus quia aut sequi dignissimos rerum. Eum ipsum nihil praesentium. Consequatur et sit architecto dicta et."
WHERE id = 2




Aut sed a officia est repellat. Voluptatibus quia aut sequi dignissimos rerum. Eum ipsum nihil praesentium. Consequatur et sit architecto dicta et.

DELETE FROM app_api_entry WHERE id=16;




INSERT INTO app_api_entry_techtag VALUES(31,8,12);
INSERT INTO app_api_entry_techtag VALUES(32,10,13);
INSERT INTO app_api_entry_techtag VALUES(33,11,38);
INSERT INTO app_api_entry_techtag VALUES(34,8,19);
INSERT INTO app_api_entry_techtag VALUES(35,10,21);
INSERT INTO app_api_entry_techtag VALUES(36,11,29);
INSERT INTO app_api_entry_techtag VALUES(37,12,1);
INSERT INTO app_api_entry_techtag VALUES(38,12,16);
INSERT INTO app_api_entry_techtag VALUES(39,31,6);
INSERT INTO app_api_entry_techtag VALUES(64,6,14);

INSERT INTO app_api_entry_moodtag VALUES(28,8,16);
INSERT INTO app_api_entry_moodtag VALUES(29,10,3);
INSERT INTO app_api_entry_moodtag VALUES(30,11,19);
INSERT INTO app_api_entry_moodtag VALUES(31,8,3);
INSERT INTO app_api_entry_moodtag VALUES(32,10,16);
INSERT INTO app_api_entry_moodtag VALUES(33,11,21);
INSERT INTO app_api_entry_moodtag VALUES(34,12,2);
INSERT INTO app_api_entry_moodtag VALUES(36,12,9);
INSERT INTO app_api_entry_moodtag VALUES(60,6,46);


INSERT INTO app_api_user_developer VALUES(7,7,7);
INSERT INTO app_api_user_developer VALUES(8,8,8);
INSERT INTO app_api_user_developer VALUES(9,9,9);
INSERT INTO app_api_user_developer VALUES(10,10,10);
INSERT INTO app_api_user_developer VALUES(11,1,1);

INSERT INTO app_api_developer VALUES(7,"Smith","Jane","Janie","js@me.co",7);
INSERT INTO app_api_developer VALUES(8,"Bonds","Barry","Bae","bb@k.net",8);
INSERT INTO app_api_developer VALUES(9,"Mahal","Taj","TeeK","taj@u.us",9);
INSERT INTO app_api_developer VALUES(10,"Yard","Cort","Hoops","cy2@cy.me",10);
INSERT INTO app_api_developer VALUES(11,"Reg","Pots","PottyMouth","pr9@pr.biz",11);

DELETE FROM app_api_developer WHERE id > 6;
DELETE FROM app_api_entry_techtag WHERE id < 7









