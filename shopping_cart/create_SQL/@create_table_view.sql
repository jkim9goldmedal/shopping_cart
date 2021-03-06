drop table if exists `J[g`;

create table `J[g`(
    `id` int(11) not null auto_increment,
    `¤iÔ` varchar(30) not null,
    `OCID` varchar(30) not null,
    `Ê` int default null,
    `Å¿i` int not null,
    `Å²¿i` int not null, 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `J[g` AUTO_INCREMENT = 1;

drop table if exists `¤iJeS[`;

create table `¤iJeS[`(
    `id` int(11) not null auto_increment,
    `JeS[Ô` int(11) not null,
    `JeS[` varchar(30) not null default '',
    `Å¦ÇÔ` int(11) not null,
    `JeS[ø¦` int(11) default null,
    `ítO` varchar(10) not null default '0',
    `XVú` datetime not null default current_timestamp,
    `õl` varchar(200) default null, 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `¤iJeS[` AUTO_INCREMENT = 1;


drop table if exists `ó¾×`;

create table `ó¾×`(
    `id` int(11) not null auto_increment,
    `óID` int(11) unsigned not null,
    `¤iÔ` varchar(30) not null,
    `Åàz` int not null,
    `Å²àz` int not null, 
    `ÅÌP¿` int not null,
    `ÌP¿` int not null,
    `Ê` int default null,
    `ítO` varchar(10) default '0',
    `õl` varchar(100) default null,
    `XVú` datetime default current_timestamp,
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `ó¾×` AUTO_INCREMENT = 1;

drop table if exists `ó`;

create table `ó`(
    `id` int(11) not null auto_increment,
    `óú` date not null,
    `OCID` varchar(30) not null,
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
    `XVú` datetime not null default current_timestamp,
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `ó` AUTO_INCREMENT = 1;

drop table if exists `z¿`;

create table `z¿`(
    `id` int(11) not null auto_increment,
    `z¿ÇÔ` int(11) not null,
    `z¿` int not null,
    `næ` varchar(40) not null,
    `ítO` varchar(10) default '0', 
    `Å¦ÇÔ` int(11) not null,
    `XVú` datetime not null default current_timestamp,
    `õl` varchar(100) default null,
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `z¿` AUTO_INCREMENT = 1;


drop table if exists `Å¦`;

create table `Å¦`(
    `id` int(11) not null auto_increment,
    `Å¦ÇÔ` int(11) not null,
    `Å¦` int(11) not null,
    `ítO` varchar(10) not null default '0',
    `XVú` datetime not null default current_timestamp,
    `õl` varchar(200) default null, 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `Å¦` AUTO_INCREMENT = 1;


drop table if exists `ÝÉ`;

create table `ÝÉ`(
    `id` int(11) not null auto_increment,
    `út` date not null,
    `ÝÉÏ®` int not null,
    `¤iÔ` varchar(30) not null,
    `ÝÉmFtO` varchar(10) not null default '1',
    `õl` varchar(200) default null, 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `ÝÉ` AUTO_INCREMENT = 1;


drop table if exists `Úq`;

create table `Úq`(
    `id` int(11) not null auto_increment,
    `¼O` varchar(40) NOT NULL DEFAULT '',
    `Ji` varchar(40) NOT NULL DEFAULT '',
    `XÖÔ` varchar(7) NOT NULL,
    `Z` varchar(100) NOT NULL,
    `dbÔ` varchar(15) NOT NULL,
    `z¿ÇÔ` int(11) not null,
    `[AhX` varchar(80) not null,
    `OCID` varchar(30) not null,
    `OCpX[h` varchar(30) not null,
    `ÚqN` varchar(10) default '2',
    `ítO` varchar(10) default '0',
    `XVú` datetime not null default current_timestamp,
    `õl` varchar(200) character set utf8 collate utf8_unicode_ci default '', 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `Úq` AUTO_INCREMENT = 1;

drop table if exists `¤i`;

create table `¤i`(
    `id` int(11) not null auto_increment,
    `¤iÔ` varchar(30) not null default '',
    `¤i¼` varchar(60)  NOT NULL DEFAULT '',
    `¤iÚ×` varchar(60) default '',
    `ÌP¿` mediumint(5) unsigned NOT NULL DEFAULT '0',
    `ÏêP¿` mediumint(5) default null,
    `¤iJeS[Ô` varchar(10) not null,
    `¤iø¦` int(11) default null,
    `øtO` varchar(10) not null default '0',
    `ítO` varchar(10) not null default '0',
    `XVú` datetime not null default current_timestamp,
    `õl` varchar(200) default null, 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `¤i` AUTO_INCREMENT = 1;

drop view if exists Å¦ê;

create view Å¦ê as
select
    i1.id,
    i1.Å¦ÇÔ,
    i1.Å¦,
    i1.XVú,
    i1.õl
from
    Å¦ as i1
    inner join(
        select
            Å¦.Å¦ÇÔ as f1,
            max(Å¦.id) as f2
        from
            Å¦
        group by
            Å¦.Å¦ÇÔ
    ) i2
        on i2.f1 = i1.Å¦ÇÔ
        and i2.f2 = i1.id;



drop view if exists ¤iJeS[ê;

create view ¤iJeS[ê as
select
    i1.id,
    i1.JeS[Ô,
    i1.JeS[,
    i1.Å¦ÇÔ,
    i1.JeS[ø¦,
    i1.XVú,
    i1.õl
from
    ¤iJeS[ as i1
    inner join(
        select
            ¤iJeS[.JeS[Ô as f1,
            max(¤iJeS[.id) as f2
        from
            ¤iJeS[
        group by
            ¤iJeS[.JeS[Ô
    ) i2
        on i2.f1 = i1.JeS[Ô
        and i2.f2 = i1.id;





drop view if exists Úqê;

create view Úqê as
select
    i1.id,
    i1.¼O,
    i1.Ji,
    i1.XÖÔ,
    i1.Z,
    i1.dbÔ,
    i1.z¿ÇÔ,
    i1.[AhX,
    i1.OCID,
    i1.ÚqN,
    i1.ítO,
    i1.XVú,
    i1.õl
from
    Úq as i1
    inner join(
        select
            Úq.OCID as f1,
            max(Úq.id) as f2
        from
            Úq
        group by
            Úq.OCID
    ) i2
        on i2.f1 = i1.OCID
        and i2.f2 = i1.id;

drop view if exists yOCpzÚqê;

create view yOCpzÚqê as
select
    i1.id,
    i1.¼O,
    i1.Ji,
    i1.XÖÔ,
    i1.Z,
    i1.dbÔ,
    i1.z¿ÇÔ,
    i1.[AhX,
    i1.OCID,
    i1.OCpX[h,
    i1.ÚqN,
    i1.õl
from
    Úq as i1
    inner join(
        select
            Úq.OCID as f1,
            max(Úq.id) as f2
        from
            Úq
        group by
            Úq.OCID
    ) i2
        on i2.f1 = i1.OCID
        and i2.f2 = i1.id
where
    i1.ítO = 0;




drop view if exists z¿ê;

create view z¿ê as
select
    i1.id,
    i1.z¿ÇÔ,
    i1.næ,
    i1.XVú,
    i1.z¿,
    i1.Å¦ÇÔ
from
    z¿ as i1
    inner join(
        select
            z¿.z¿ÇÔ as f1,
            max(z¿.id) as f2
        from
            z¿
        group by
            z¿.z¿ÇÔ
    ) i2
        on i2.f1 = i1.z¿ÇÔ
        and i2.f2 = i1.id;

drop view if exists yüÍ~XmFpzüoÉð;

create view yüÍ~XmFpzüoÉð as
select
    ¤i.id,
    ÝÉ.¤iÔ,
    ¤i¼,
    ¤iÚ×,
    út,
    ÝÉÏ®,
    ÝÉmFtO
from ÝÉ left outer join ¤i on ÝÉ.¤iÔ = ¤i.¤iÔ;

drop view if exists üoÉð;

create view üoÉð as
select
    i1.id,
    i1.¤iÔ,
    i1.¤i¼,
    i1.¤iÚ×,
    i1.út,
    i1.ÝÉÏ®,
    i1.ÝÉmFtO
from
    yüÍ~XmFpzüoÉð as i1
    inner join(
        select
            yüÍ~XmFpzüoÉð.¤iÔ as f1,
            max(yüÍ~XmFpzüoÉð.id) as f2
        from
            yüÍ~XmFpzüoÉð
        group by
            yüÍ~XmFpzüoÉð.¤iÔ
    ) i2
        on i2.f1 = i1.¤iÔ
        and i2.f2 = i1.id;



drop view if exists yüÍ~XmFpz¤iê;

create view yüÍ~XmFpz¤iê as 
select
    ¤i.id,
    ¤i.¤iÔ,
    ¤iJeS[Ô,
    ¤i¼,
    ¤iÚ×,
    round(ÌP¿*(1+(Å¦/100))) as ÅÌP¿,
    ÌP¿ as Å²ÌP¿,
    round(case when øtO = 1 then ÌP¿*(1-(¤iø¦/100))*(1+(Å¦/100)) else 0 end) as Å¤iø¿i,
    round(case when øtO = 1 then ÌP¿*(1-(¤iø¦/100)) else 0 end) as Å²¤iø¿i,
    round(case when øtO = 2 then ÌP¿*(1-(JeS[ø¦/100))*(1+(Å¦/100)) else 0 end) as ÅJeS[ø¿i,
    round(case when øtO = 2 then ÌP¿*(1-(JeS[ø¦/100)) else 0 end) as Å²JeS[ø¿i,
    round(case when øtO = 3 then ÏêP¿*(1+(Å¦/100)) else 0 end) as ÅÏê¿i,
    case when øtO = 3 then ÏêP¿ else 0 end as Å²ÏêP¿,
    Å¦,
    øtO,
    ¤i.ítO,
    ¤i.õl
from 
    ¤i left outer join ¤iJeS[ê on ¤iJeS[Ô = ¤iJeS[ê.JeS[Ô left outer join Å¦ê on ¤iJeS[ê.Å¦ÇÔ = Å¦ê.Å¦ÇÔ
;






drop view if exists ¤iîñêr[;

create view ¤iîñêr[ as
select
    i1.id,
    i1.¤iÔ,
    i1.¤iJeS[Ô,
    i1.¤i¼,
    i1.¤iÚ×,
    i1.ÅÌP¿,
    i1.Å²ÌP¿,
    i1.Å¤iø¿i,
    i1.Å²¤iø¿i,
    i1.ÅJeS[ø¿i,
    i1.Å²JeS[ø¿i,
    i1.ÅÏê¿i,
    i1.Å²ÏêP¿,
    i1.Å¦,
    i1.øtO,
    i1.ítO,
    i1.õl
from
    yüÍ~XmFpz¤iê as i1
    inner join(
        select
            yüÍ~XmFpz¤iê.¤iÔ as f1,
            max(yüÍ~XmFpz¤iê.id) as f2
        from
            yüÍ~XmFpz¤iê
        group by
            yüÍ~XmFpz¤iê.¤iÔ
    ) i2
        on i2.f1 = i1.¤iÔ
        and i2.f2 = i1.id
group by
    i1.¤iÔ;


drop view if exists ¤iÝÉê;

create view ¤iÝÉê as
select
    i1.id,
    i1.¤iÔ,
    i1.¤iJeS[Ô,
    i1.¤i¼,
    i1.¤iÚ×,
    i1.ÅÌP¿,
    i1.Å²ÌP¿,
    i1.Å¤iø¿i,
    i1.Å²¤iø¿i,
    i1.ÅJeS[ø¿i,
    i1.Å²JeS[ø¿i,
    i1.ÅÏê¿i,
    i1.Å²ÏêP¿,
    i1.Å¦,
    sum(ÝÉÏ®) as ÝÉ,
    i1.øtO,
    i1.ítO,
    i1.õl
from
    ÝÉ as i2 right outer join ¤iîñêr[ as i1 on i2.¤iÔ = i1.¤iÔ
group by
    i1.¤iÔ;

drop view if exists ó¾×îñê;

create view ó¾×îñê as
select
    ó¾×.id,
    óID,
    óú,
    ó¾×.¤iÔ,
    ¤i¼,
    ¤iÚ×,
    case when ó.ítO = 1 then Åàz * (-1) else Åàz end as Åàz,
    case when ó.ítO = 1 then Å²àz * (-1) else Å²àz end as Å²àz,
    case when ó.ítO = 1 then ó¾×.ÅÌP¿ * (-1) else ó¾×.ÅÌP¿ end as ÅÌP¿,
    case when ó.ítO = 1 then ó¾×.ÌP¿ * (-1) else ó¾×.ÌP¿ end as ÌP¿,
    Å¦,
    Ê,
    ó.ítO
from
    ó¾× inner join ó on óID = ó.id inner join ¤iÝÉê on ó¾×.¤iÔ = ¤iÝÉê.¤iÔ;



drop view if exists óîñê;

create view óîñê as
select
    ó.id,
    ó.óú,
    ¼O,
    Ji,
    dbÔ,
    XÖÔ,
    Z,
    ¶v,
    case when ó.ítO = 1 then Åvàz * (-1) else Åvàz end as Åvàz,
    case when ó.ítO = 1 then Åz¿ * (-1) else Åz¿ end as Åz¿,
    case when ó.ítO = 1 then Å²z¿ * (-1) else Å²z¿ end as Å²z¿,
    case when ó.ítO = 1 then Å¿vz * (-1) else Å¿vz end as Å¿vz,
    ó¾×.¤iÔ,
    ¤i¼,
    case when ó.ítO = 1 then ÌP¿ * (-1) else ÌP¿ end as ÌP¿,
    Ê,
    case when ó.ítO = 1 then Åàz * (-1) else Åàz end as Åàz,
    ­ÏÝ,
    üàmFÏÝ,
    ó.ítO,
    ó.XVú,
    ó.õl
from ó¾× left outer join ó on óID = ó.id left outer join ¤iÝÉê on ó¾×.¤iÔ = ¤iÝÉê.¤iÔ left outer join Úqê on ó.OCID = Úqê.OCID;


drop view if exists ã;

create view ã as
select
    ó.óú,
    sum(Åàz) as ¤iÅvàz,
    sum(Åàz + Åz¿) as z,
    sum(Åz¿) as Åz¿,
    sum(Å²z¿) as Å²z¿,
    sum(
        case when ó¾×îñê.Å¦ = 10 then (Åàz - Å²àz) else 0 end
        ) as '10%ÁïÅv',
    sum(
        case when ó¾×îñê.Å¦ = 8 then (Åàz - Å²àz) else 0 end
        ) as '8%ÁïÅv'
from
    ó¾×îñê inner join ó on óID = ó.id inner join ¤iÝÉê on ó¾×îñê.¤iÔ = ¤iÝÉê.¤iÔ
group by
    ó.óú;


drop view if exists ¤iÊã;

create view ¤iÊã as
select
    A.¤iÔ,
    A.¤i¼,
    A.¤iÚ×,
    A.ÌP¿,
    sum(A.Ê) as Ê,
    sum(A.Å²àz) as Å²àz,
    sum(A.Åàz) as Åàz
from
    ó¾×îñê A
where
    exists(
        select
            *
        from
            ó¾×îñê B
        where
            A.¤iÔ = B.¤iÔ
        and
            A.ÌP¿ = B.ÌP¿
        and
            DATE_FORMAT(B.óú, '%Y/%m') = DATE_FORMAT(now(),'%Y/%m')
        )
    and
        DATE_FORMAT(A.óú, '%Y/%m') = DATE_FORMAT(now(),'%Y/%m')
group by
    A.¤iÔ,
    A.ÌP¿
order by
    A.¤iÔ;
