CREATE TABLE Genre(
    genreID varchar(255) NOT NULL,
    genreName varchar(255) NOT NULL,
    description varchar(255) NOT NULL,
    PRIMARY KEY (genreID)
);

-- The following may be added to the CREATE statement
-- Primary Key Syntax (added after field name and NOT NULL)
--     PRIMARY KEY (fieldName)
--          or for compound PK
--     CONSTRAINT PK_compoundFieldName PRIMARY KEY (field1,field2)
-- Foreign Key Syntax (added after field list)
--     FOREIGN KEY (field name) REFERENCES tableName(fieldName)
-- Boolean Field Type
--     For some SQL environments 'bool' may have to be changed to 'int'
-- Text Field Max Size
--     Edit (255) to required length
-- Validation of length of text (added after create statement as new statement
--     CHECK (CHAR_LENGTH(fieldName) > value)
-- Range Check (added after field list)
--     CHECK (fieldName >= value)
--     CHECK (fieldName >= value AND fieldName <= value2)
-- Restricted choice
--     CHECK(fieldName in ('value1','value2','value3')) 

-- Note
-- At N5 Check constraints (that are ignored by a MySQL server) 
-- are being used instead of triggers.

INSERT INTO Genre VALUES("G-01","Action","High-energy movies that feature intense physical stunts, battles, car chases, and explosions");
INSERT INTO Genre VALUES("G-02","Adventure","Movies that take viewers on epic journeys, often involving exploration, treasure hunting, or dangerous quests in exotic or fantastical locations");
INSERT INTO Genre VALUES("G-03","Animation","Uses drawn, computer-generated, or stop-motion imagery to tell stories, often appealing to both children and adults");
INSERT INTO Genre VALUES("G-04","Comedy","Designed to entertain through humor, these movies use wit, satire, slapstick, or absurd situations to make audiences laugh");
INSERT INTO Genre VALUES("G-05","Crime","Focuses on criminal activities, heists, investigations, and the morality of justice");
INSERT INTO Genre VALUES("G-06","Documentary","Non-fiction movies that educate or inform about real events, people, or topics");
INSERT INTO Genre VALUES("G-07","Drama","Serious movies that focus on character development, emotional narratives, and realistic storytelling, often dealing with social issues or personal struggles");
INSERT INTO Genre VALUES("G-08","Fantasy","Features magical, supernatural, or mythical elements, often set in imaginative worlds with unique rules");
INSERT INTO Genre VALUES("G-09","Fantasy Crime","A genre combining magical, mythical worlds with the investigative and procedural elements of crime stories");
INSERT INTO Genre VALUES("G-10","Historical","Recreates events or eras from history, often mixing fact and fiction for dramatic effect");
INSERT INTO Genre VALUES("G-11","Horror","Aimed at evoking fear or suspense, these movies include supernatural entities, psychological tension, or gore");
INSERT INTO Genre VALUES("G-12","Musical","Characters express themselves through song and dance, integrating music into the storyline");
INSERT INTO Genre VALUES("G-13","Mystery","Revolves around solving a puzzle or crime, keeping audiences guessing until the end with twists and turns");
INSERT INTO Genre VALUES("G-14","Romance","Focused on love stories, emotional connections, and romantic relationships, often with obstacles the characters must overcome");
INSERT INTO Genre VALUES("G-15","Romance Thriller","A mix of intense suspense and action with a central romantic storyline");
INSERT INTO Genre VALUES("G-16","Science Fiction","Explores futuristic concepts, advanced technology, space exploration, or alternate realities");
INSERT INTO Genre VALUES("G-17","Science Fiction Horror","Combines horror with futuristic or scientific concepts � from alien threats to rogue technology or mutated life forms");
INSERT INTO Genre VALUES("G-18","Thriller","Fast-paced and filled with suspense, thrillers keep viewers on edge through tension, twists, and high stakes");
INSERT INTO Genre VALUES("G-19","Western","Set in the American frontier, these films often involve cowboys, outlaws, and justice in untamed lands");
INSERT INTO Genre VALUES("G-20","Western Musical","A combinination of the rugged, adventurous spirit of the Wild West with song and dance numbers that drive the narrative or reflect characters emotions");
