CREATE DATABASE IF NOT EXISTS master_python;
use master_python;

CREATE TABLE usuarios(
    id int(20) auto_increment,
    nombre      varchar(100),
    apellidos   varchar(255),
    email       varchar(255) not null,
    password    varchar(255) not null,
    fecha       date not null,
    CONSTRAINT  pk_usuarios PRIMARY KEY(id),    -- Clave primaria enlace con otras tablas
    CONSTRAINT  uq_email    UNIQUE(email)       --Quiere decir que el campo es unico y no repetible
    )ENGINE=InnoDb;                             --Integral diferencial entre tablas

CREATE TABLE notas(
    id          int(25)  auto_increment not null,
    usuario_id  int(20) not null,
    titulo      varchar(255) not null,
    descripcion MEDIUMTEXT,
    fecha       date not null,
    CONSTRAINT  pk_notas PRIMARY KEY (id),
    CONSTRAINT  fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
    -- Relacion de tablas mediante el id de usuario
)ENGINE= InnoDb