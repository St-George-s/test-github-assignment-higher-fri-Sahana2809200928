CREATE TABLE Customer(
    customerID varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    forename varchar(255) NOT NULL,
    surname varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    premiumAccount BOOLEAN NOT NULL,
    PRIMARY KEY (customerID)
);

-- Note
-- At N5 Check constraints (that are ignored by a MySQL server) 
-- are being used instead of triggers.

INSERT INTO Customer VALUES("Cust-01","Jp8%Zq2&XmF","Stephanie","Ferguson","zimmy674@snapmail.org",0);
INSERT INTO Customer VALUES("Cust-02","Xp3!Wp2#VmZ","Charlotte","Phillips","charlott_phillips@cloudmail.co.uk",1);
INSERT INTO Customer VALUES("Cust-03","Z5$Lm3@WpY","William","Edwards","will_i_am@flashmail.net",1);
INSERT INTO Customer VALUES("Cust-04","Y2$Wp7#VtZn","Lily","Underwood","underwood88@flashmail.net",1);
INSERT INTO Customer VALUES("Cust-05","Xp@2Lk8#Mv","Abigail","York","ayork@cloudmail.co.uk",1);
INSERT INTO Customer VALUES("Cust-06","Y&3Lx5$WpT","Isaac","Turner","turnerisaac@flashmail.net",1);
INSERT INTO Customer VALUES("Cust-07","Fq3%Y7@WpX","Benjamin","Roberts","therealbenroberts@flashmail.net",1);
INSERT INTO Customer VALUES("Cust-08","Lk9&Vq4$ZqT","Nathan","White","whiteboy@snapmail.org",1);
INSERT INTO Customer VALUES("Cust-09","Mx@4V1pRtK","Caleb","Evans","calev@inbox.com",1);
INSERT INTO Customer VALUES("Cust-10","Wm7!Lp8$VtZ","Theodore","Lewis","theolewis@cloudmail.co.uk",1);
INSERT INTO Customer VALUES("Cust-11","R5%Xm9$VtWpK","Derek","Tsang","itsyaboy@snapmail.org",0);
INSERT INTO Customer VALUES("Cust-12","Y9$Wp2&XmTq","Andrew","Anderson","double_a@flashmail.net",0);
INSERT INTO Customer VALUES("Cust-13","Zc3&Lp4#Xt","Emily","Daniels","emily_daniels@flashmail.net",1);
INSERT INTO Customer VALUES("Cust-14","Xq2$Yt9!Lp","Ryan","Johnson","arrjay@snapmail.org",0);
INSERT INTO Customer VALUES("Cust-15","K7@Wp3!LqZt","Daniel","Fisher","daniel6354@inbox.com",1);
INSERT INTO Customer VALUES("Cust-16","T7$Vq9@FqM","Alexander","Campbell","alexander900@inbox.com",0);
INSERT INTO Customer VALUES("Cust-17","Zc!8Xp2#Wm","Tessa","Adams","tessa88@cloudmail.co.uk",1);
INSERT INTO Customer VALUES("Cust-18","X7!Vn4$ZqT","Theo","Harrison","matthew.harrison2@cloudmail.co.uk",1);
INSERT INTO Customer VALUES("Cust-19","Vp4#Lm3&Zn","Martha","Smith","oliver.morgan@cloudmail.co.uk",1);
INSERT INTO Customer VALUES("Cust-20","Z5!Wp8@VqLn","Willow","Carter","willowc213@flashmail.net",1);
INSERT INTO Customer VALUES("Cust-21","T7$Yq@9&Fk","Xavier","Garcia","xavierxox@inbox.com",1);
INSERT INTO Customer VALUES("Cust-22","R7@Xm3!VqF","Eleanor","Bennett","eb654@flashmail.net",1);
INSERT INTO Customer VALUES("Cust-23","Xp5$Zq2#VnWt","Larry","Parker","indyana@inbox.com",0);
INSERT INTO Customer VALUES("Cust-24","Zt3&Wp5%LqYn","Dominic","Smith","iamdoms@snapmail.org",1);
INSERT INTO Customer VALUES("Cust-25","J$4Zt&8WpL","Zachary","Reed","zach.reed@inbox.com",0);
INSERT INTO Customer VALUES("Cust-26","Wm8!Zp3$Vk","Jasmine","Owens","jayoh@inbox.com",1);
INSERT INTO Customer VALUES("Cust-27","Y5@Wp2#LxF","Liam","Norton","marvelousnorton@cloudmail.co.uk",0);
INSERT INTO Customer VALUES("Cust-28","H#7kL2!vTp","Jack","Collins","jc80@snapmail.org",0);
INSERT INTO Customer VALUES("Cust-29","Lq9@Xm4%WpF","Finn","James","mrjames22@inbox.com",1);
INSERT INTO Customer VALUES("Cust-30","Kp5%Y9$WnZ","Gabriel","Mitchell","gabe_mitchell@cloudmail.co.uk",0);
INSERT INTO Customer VALUES("Cust-31","Fq7@Wp2#LqZt","Penelope","Davis","penelope.davis@flashmail.net",1);
INSERT INTO Customer VALUES("Cust-32","R4%Xm7$WpK","Sophia","Hall","sophiah18@snapmail.org",0);
INSERT INTO Customer VALUES("Cust-33","Zc7%Y!2wFq","Ruby","Grant","rubyrubyruby@cloudmail.co.uk",0);
INSERT INTO Customer VALUES("Cust-34","Wm9$Wp8!VqXT","Elijah","West","westelijah@flashmail.net",1);
INSERT INTO Customer VALUES("Cust-35","Vt&9Jp3#Lm","Marcus","McGowan","mercutio@cloudmail.co.uk",1);
INSERT INTO Customer VALUES("Cust-36","Y5!Vt7$XpWm","Hannah","Hughes","doubleh@snapmail.org",1);
INSERT INTO Customer VALUES("Cust-37","T7$Wp9&LqKX","Quinn","Taylor","quinntaylor@flashmail.net",1);
INSERT INTO Customer VALUES("Cust-38","Jq8!Zp3@VtF","Samuel","King","theking@cloudmail.co.uk",0);
INSERT INTO Customer VALUES("Cust-39","R7$Zq&5XnF","Amelia","Lee","amelia9055@snapmail.org",1);
INSERT INTO Customer VALUES("Cust-40","Wk7@Vm8#Zc","Bella","Vaughn","screen_sage@inbox.com",0);
INSERT INTO Customer VALUES("Cust-41","T9#Xn2@VkZ","Amelie","Quinn","h_quinn90@inbox.com",1);
INSERT INTO Customer VALUES("Cust-42","Jt!9Lp4@Vm","Olivia","Brooks","silverscreenlover@inbox.com",1);
INSERT INTO Customer VALUES("Cust-43","Yq2!Wp4$VnT","Omar","Siddiqui","valentineg@inbox.com",1);
INSERT INTO Customer VALUES("Cust-44","Zt8@Wp3!XmTq","Aleksander","Novak","viktorvondoom@inbox.com",1);
INSERT INTO Customer VALUES("Cust-45","Lx&5Zp@4Kt","Daisy","Robertson","daisyy@snapmail.org",1);
INSERT INTO Customer VALUES("Cust-46","Wd$8xFq&9Z","Isla","Harper","harpy@flashmail.net",1);
INSERT INTO Customer VALUES("Cust-47","Jp3%Wp8&FqM","Fatima","Hussein","fhus_80@freemail.com",1);
INSERT INTO Customer VALUES("Cust-48","F7$Lp3!TqWk","Zoe","Foster","zoeeefoster@inbox.com",0);
INSERT INTO Customer VALUES("Cust-49","F9!Xp2#VqM","Rebecca","Shearer","becks@inbox.com",0);
INSERT INTO Customer VALUES("Cust-50","R9%Xm8@ZqL","Violet","Rose","slayallday@snapmail.org",0);
