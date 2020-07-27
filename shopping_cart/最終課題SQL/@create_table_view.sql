drop table if exists `J[g`;

create table `J[g`(
    `id` int(11) not null auto_increment,
    `¤iID` int(11) unsigned not null,
    `ÚqID` int(11) unsigned not null,
    `Ê` int default null,
    `Å¿i` int not null,
    `Å²¿i` int not null, 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

drop table if exists `¤iJeS[`;

create table `¤iJeS[`(
    `id` int(11) not null auto_increment,
    `JeS[` varchar(30) not null default '',
    `Å¦ID` int(11) unsigned not null,
    `JeS[ø¦` varchar(20) default null,
    `ítO` varchar(10) not null default '0',
    `õl` varchar(200) default null, 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


drop table if exists `ó¾×`;

create table `ó¾×`(
    `id` int(11) not null auto_increment,
    `óID` int(11) unsigned not null,
    `¤iID` int(11) unsigned not null,
    `Åàz` int not null,
    `Å²àz` int not null, 
    `ÅÌP¿` int not null,
    `ÌP¿` int not null,
    `Ê` int default null,
    `ítO` varchar(10) default '0',
    `õl` varchar(100) default null,
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

drop table if exists `ó`;

create table `ó`(
    `id` int(11) not null auto_increment,
    `óú` date not null,
    `ÚqID` int(11) unsigned not null,
    `¶v` int not null,
    `Åvàz` int not null,
    `Å²vàz` int not null, 
    `Å¿vz` int not null,
    `Åz¿` int default '0',
    `Å²z¿` int default '0',
    `­ÏÝ`varchar(10) default '0',
    `üàmFÏÝ` varchar(10) default '0',
    `õl` varchar(100) default null,
    `ítO` varchar(10) default '0',
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

drop table if exists `z¿`;

create table `z¿`(
    `id` int(11) not null auto_increment,
    `z¿` int not null,
    `næ` varchar(40) not null,
    `ítO` varchar(10) default '0', 
    `Å¦ID` int(11) unsigned not null,
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

drop table if exists `Å¦`;

create table `Å¦`(
    `id` int(11) not null auto_increment,
    `Å¦` varchar(30) not null default '',
    `ítO` varchar(10) not null default '0',
    `õl` varchar(200) default null, 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

drop table if exists `ÝÉ`;

create table `ÝÉ`(
    `id` int(11) not null auto_increment,
    `út` date not null,
    `ÝÉÏ®` int not null,
    `¤iID` int(11) not null,
    `ÝÉmFtO` varchar(10) not null default '0',
    `õl` varchar(200) default null, 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


drop table if exists `Úq`;

create table `Úq`(
    `id` int(11) not null auto_increment,
    `¼O` varchar(40) NOT NULL DEFAULT '',
    `Ji` varchar(40) NOT NULL DEFAULT '',
    `XÖÔ` varchar(7) NOT NULL,
    `Z` varchar(100) NOT NULL,
    `dbÔ` varchar(15) NOT NULL,
    `z¿ID` varchar(11) not null,
    `[AhX` varchar(80) not null,
    `OCpX[h` varchar(30) not null,
    `ÚqN` varchar(10) not null default '0',
    `ítO` varchar(10) default '0',
    `õl` varchar(200) character set utf8 collate utf8_unicode_ci default '', 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

drop table if exists `¤i`;

create table `¤i`(
    `id` int(11) not null auto_increment,
    `¤iÔ` varchar(30) not null default '',
    `¤i¼` varchar(60)  NOT NULL DEFAULT '',
    `¤iÚ×` varchar(60) default null,
    `ÌP¿` mediumint(5) unsigned NOT NULL DEFAULT '0',
    `ÏêP¿` mediumint(5) default null,
    `¤iJeS[ID` int(11) unsigned not null,
    `¤iø¦` varchar(20) default null,
    `øtO` varchar(10) not null default '0',
    `ítO` varchar(10) not null default '0',
    `XVú` datetime not null default current_timestamp,
    `õl` varchar(200) default null, 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

drop view if exists ¤iJeS[ê;

create view ¤iJeS[ê as
select ¤iJeS[.id,JeS[,Å¦,JeS[ø¦,¤iJeS[.õl
from ¤iJeS[ inner join Å¦ on Å¦ID = Å¦.id
where ¤iJeS[.ítO = 0;

drop view if exists Úqê;

create view Úqê as
select Úq.id,¼O,Ji,XÖÔ,Z,dbÔ,næ,z¿,[AhX,ÚqN
from Úq inner join z¿ on z¿ID = z¿.id
where Úq.ítO = 0;

drop view if exists ó¾×îñê;

create view ó¾×îñê as
select ó¾×.id,óID,óú,¤iÔ,¤i¼,¤iÚ×,Åàz,Å²àz,Ê
from ó¾× inner join ó on óID = ó.id inner join ¤i on ¤iID = ¤i.id
where ó.ítO = 0;

drop view if exists óîñê;

create view óîñê as
select ó.id,óú,¼O,XÖÔ,Z,Åvàz,Å¿vz
from ó inner join Úq on ÚqID = Úq.id
where ó.ítO = 0;

drop view if exists z¿ê;

create view z¿ê as
select id,næ,z¿
from z¿
where ítO = 0;

drop view if exists üoÉð;

create view üoÉð as
select ¤iID,¤iÔ,¤i¼,¤iÚ×,út,ÝÉÏ®,ÝÉmFtO
from ÝÉ inner join ¤i on ¤iID = ¤i.id;

drop view if exists ¤iê;

create view ¤iê as 
select 
    ÝÉ.¤iID,
    JeS[,
    ¤iÔ,
    ¤i¼,
    ¤iÚ×,
    round(case when øtO = 0 then ÌP¿*(1+(Å¦/100)) else 0 end) as ÅÌP¿,
    case when øtO = 0 then ÌP¿ else 0 end as Å²ÌP¿,
    round(case when øtO = 1 then ÌP¿*(1-(¤iø¦/100))*(1+(Å¦/100)) else 0 end) as Å¤iø¿i,
    round(case when øtO = 1 then ÌP¿*(1-(¤iø¦/100)) else 0 end) as Å²¤iø¿i,
    round(case when øtO = 2 then ÌP¿*(1-(JeS[ø¦/100))*(1+(Å¦/100)) else 0 end) as ÅJeS[ø¿i,
    round(case when øtO = 2 then ÌP¿*(1-(JeS[ø¦/100)) else 0 end) as Å²JeS[ø¿i,
    round(case when øtO = 3 then ÏêP¿*(1+(Å¦/100)) else 0 end) as ÅÏê¿i,
    case when øtO = 3 then ÏêP¿ else 0 end as Å²ÏêP¿,
    Å¦,
    sum(ÝÉÏ®) as ÝÉ,
    øtO,¤i.
    ítO
from 
    ÝÉ inner join ¤i on ¤iID = ¤i.id inner join ¤iJeS[ on ¤iJeS[ID = ¤iJeS[.id inner join Å¦ on Å¦ID = Å¦.id
group by 
    ÝÉ.¤iID
having 
    ¤i.ítO = 0;

drop view if exists Å¦ê;

create view Å¦ê as
select id,Å¦,õl
from Å¦
where ítO = 0;


