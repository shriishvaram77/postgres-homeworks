-- 1. Создать таблицу student с полями student_id serial, first_name varchar, last_name varchar, birthday date, phone varchar
CREATE TABLE student
(
	student_id serial,
	first_name varchar,
	last_name varchar,
	birthday date,
	phone varchar
)

-- 2. Добавить в таблицу student колонку middle_name varchar
ALTER TABLE student
ADD COLUMN middle_name

-- 3. Удалить колонку middle_name
ALTER TABLE student
DROP COLUMN middle_name

-- 4. Переименовать колонку birthday в birth_date
ALTER TABLE student
RENAME birthday TO birth_date

-- 5. Изменить тип данных колонки phone на varchar(32)
ALTER TABLE student
ALTER COLUMN phone
SET DATA TYPE varchar (32)

-- 6. Вставить три любых записи с автогенерацией идентификатора
INSERT INTO student (first_name, last_name, phone)
VALUES
('John', 'Kennedy', '4445556545')
('Keisha', 'Peterson', '3245670987')
('Karl', 'Ditrich', '4908909876')

-- 7. Удалить все данные из таблицы со сбросом идентификатор в исходное состояние
TRUNCATE TABLE student