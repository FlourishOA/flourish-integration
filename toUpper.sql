DROP FUNCTION IF EXISTS lowerword;
SET GLOBAL  log_bin_trust_function_creators=TRUE;
DELIMITER |
CREATE FUNCTION lowerword( str VARCHAR(128), word VARCHAR(5) )
RETURNS VARCHAR(128)
DETERMINISTIC
BEGIN
  DECLARE i INT DEFAULT 1;
  DECLARE loc INT;

  SET loc = LOCATE(CONCAT(word,' '), str, 2);
  IF loc > 1 THEN
    WHILE i <= LENGTH (str) AND loc <> 0 DO
      SET str = INSERT(str,loc,LENGTH(word),LCASE(word));
      SET i = loc+LENGTH(word);
      SET loc = LOCATE(CONCAT(word,' '), str, i);
    END WHILE;
  END IF;
  RETURN str;
END;
|
DELIMITER ;
DROP FUNCTION IF EXISTS tcase;
SET GLOBAL  log_bin_trust_function_creators=TRUE;
DELIMITER |
CREATE FUNCTION tcase( str VARCHAR(128) )
RETURNS VARCHAR(128)
DETERMINISTIC
BEGIN
  DECLARE c CHAR(1);
  DECLARE s VARCHAR(128);
  DECLARE i INT DEFAULT 1;
  DECLARE bool INT DEFAULT 1;
  DECLARE punct CHAR(17) DEFAULT ' ()[]{},.-_!@;:?/';
  SET s = LCASE( str );
  WHILE i <= LENGTH( str ) DO
    BEGIN
      SET c = SUBSTRING( s, i, 1 );
      IF LOCATE( c, punct ) > 0 THEN
        SET bool = 1;
      ELSEIF bool=1 THEN
        BEGIN
          IF c >= 'a' AND c <= 'z' THEN
            BEGIN
              SET s = CONCAT(LEFT(s,i-1),UCASE(c),SUBSTRING(s,i+1));
              SET bool = 0;
            END;
          ELSEIF c >= '0' AND c <= '9' THEN
            SET bool = 0;
          END IF;
        END;
      END IF;
      SET i = i+1;
    END;
  END WHILE;

  SET s = lowerword(s, 'A');
  SET s = lowerword(s, 'An');
  SET s = lowerword(s, 'And');
  SET s = lowerword(s, 'As');
  SET s = lowerword(s, 'At');
  SET s = lowerword(s, 'But');
  SET s = lowerword(s, 'By');
  SET s = lowerword(s, 'For');
  SET s = lowerword(s, 'If');
  SET s = lowerword(s, 'In');
  SET s = lowerword(s, 'Of');
  SET s = lowerword(s, 'On');
  SET s = lowerword(s, 'Or');
  SET s = lowerword(s, 'The');
  SET s = lowerword(s, 'To');
  SET s = lowerword(s, 'Via');

  RETURN s;
END;
|
DELIMITER ;

SELECT journal_name, pub_name, category FROM api_journal LIMIT 10;
/*
UPDATE api_journals SET
  category = tcase(category),
  journal_name = tcase(journal_name),
  pub_name = tcase(pub_name);
*/
SELECT "";
SELECT tcase(journal_name), tcase(pub_name), tcase(category) FROM api_journal LIMIT 150;
-- SELECT tcase(jname), tcase(pname), tcase(category) FROM Journals LIMIT 150;

