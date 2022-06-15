INSERT INTO app_api_techtag 
VALUES(2,"Python");
INSERT INTO app_api_techtag 
VALUES(3,"Django");
INSERT INTO app_api_techtag 
VALUES(4,"JavaScript");
INSERT INTO app_api_techtag 
VALUES(5,"React");
INSERT INTO app_api_techtag 
VALUES(6,"Linux");
INSERT INTO app_api_techtag 
VALUES(7,"Windows");
INSERT INTO app_api_techtag 
VALUES(8,"AWS");
INSERT INTO app_api_techtag 
VALUES(9,"C");
INSERT INTO app_api_techtag 
VALUES(10,"C#");
INSERT INTO app_api_techtag 
VALUES(11,"C++");
INSERT INTO app_api_techtag 
VALUES(12,"Java");
INSERT INTO app_api_techtag 
VALUES(13,"Flutter");
INSERT INTO app_api_techtag 
VALUES(14,"Dart");
INSERT INTO app_api_techtag 
VALUES(15,"Go");
INSERT INTO app_api_techtag 
VALUES(16,".NET");
INSERT INTO app_api_techtag 
VALUES(17,"VSCode");
INSERT INTO app_api_techtag 
VALUES(18,"PowerShell");
INSERT INTO app_api_techtag 
VALUES(19,"Bash");
INSERT INTO app_api_techtag 
VALUES(20,"Kubernetes");
INSERT INTO app_api_techtag 
VALUES(21,"Containers");
INSERT INTO app_api_techtag 
VALUES(22,"SQL");
INSERT INTO app_api_techtag 
VALUES(23,"FOIL");
INSERT INTO app_api_techtag 
VALUES(24,"Swift");
INSERT INTO app_api_techtag 
VALUES(25,"HTML");
INSERT INTO app_api_techtag 
VALUES(26,"CSS");
INSERT INTO app_api_techtag 
VALUES(27,"Flexbox");
INSERT INTO app_api_techtag 
VALUES(28,"RegEx");
INSERT INTO app_api_techtag 
VALUES(29,"R");
INSERT INTO app_api_techtag 
VALUES(30,"JSON");
INSERT INTO app_api_techtag 
VALUES(31,"Php");


DROP TABLE app_api_entry

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



DELETE FROM app_api_entry WHERE id=17;




INSERT INTO app_api_developer
VALUES(6,"Wharf","Sheldon",
"KlingMeister", "ws1445@starfleet.net", 6)