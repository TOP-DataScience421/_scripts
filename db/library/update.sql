update ignore publishers
set name = 'издательство-с-длинным-названием';


update publishers
set name = 'АСТ'
where name = 'издательство-с-длинным-названием';


update publishers
set name = 'издательство-с-длинным-названием'
where id = 4;

