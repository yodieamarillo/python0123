/*apuntes de sql*/
create database 'NOMBRE DEL LA BASE DATOS';
use 'NOMBRE DE LA BASE DATOS'; /* voy a usar esa base de datos*/

create table user(
    id_user int primary autoincrement not null ,
    userDescription varchar(255),
    contenido text,
    fecha timestamp default now update on timestamp,
    score int,
    product_fk int,
    foregin_key(product_fk) alter product
);

create table product(
    id_product int primary not null,
    description_proct varchar(234)
    price varchar(200),
);
/*insertt */
insert product(id_product ,description_proct,price) values('value1','value2','21313213')
/* consultas */
select * from user
select * from product where id_product!='value1' /* el where va con cualquier opeardor arimetico*/

/*update*/
update product
   set  description_proct='celuar'
where id=1
/*eliminar*/
delete from product where id=1
/*eliminar una tabla */
drop table prodcut

update user 
    set score+=1
where product_fk=(select price from product where id=1)