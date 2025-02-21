CREATE TABLE IF NOT EXISTS kh(
    id int auto_increment primary key,
    hoten varchar(255) not null,
    email varchar(255) not null
);
insert INTO kh(id, hoten, email)
values (1, 'tuyet', 'tuyetmat@gmail.com'),
    (2, 'anh', 'anhtuyet@gmail.com');
SELECT *
FROM kh;