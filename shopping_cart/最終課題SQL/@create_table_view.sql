drop table if exists `�J�[�g`;

create table `�J�[�g`(
    `id` int(11) not null auto_increment,
    `���iID` int(11) unsigned not null,
    `�ڋqID` int(11) unsigned not null,
    `����` int default null,
    `�ō����i` int not null,
    `�Ŕ����i` int not null, 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

drop table if exists `���i�J�e�S���[`;

create table `���i�J�e�S���[`(
    `id` int(11) not null auto_increment,
    `�J�e�S���[` varchar(30) not null default '',
    `�ŗ�ID` int(11) unsigned not null,
    `�J�e�S���[������` varchar(20) default null,
    `�폜�t���O` varchar(10) not null default '0',
    `���l` varchar(200) default null, 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


drop table if exists `�󒍖���`;

create table `�󒍖���`(
    `id` int(11) not null auto_increment,
    `��ID` int(11) unsigned not null,
    `���iID` int(11) unsigned not null,
    `�ō����z` int not null,
    `�Ŕ����z` int not null, 
    `�ō��̔��P��` int not null,
    `�̔��P��` int not null,
    `����` int default null,
    `�폜�t���O` varchar(10) default '0',
    `���l` varchar(100) default null,
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

drop table if exists `��`;

create table `��`(
    `id` int(11) not null auto_increment,
    `�󒍓�` date not null,
    `�ڋqID` int(11) unsigned not null,
    `�������v��` int not null,
    `�ō����v���z` int not null,
    `�Ŕ����v���z` int not null, 
    `�ō����������v�z` int not null,
    `�ō��z����` int default '0',
    `�Ŕ��z����` int default '0',
    `�����ς�`varchar(10) default '0',
    `�����m�F�ς�` varchar(10) default '0',
    `���l` varchar(100) default null,
    `�폜�t���O` varchar(10) default '0',
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

drop table if exists `�z����`;

create table `�z����`(
    `id` int(11) not null auto_increment,
    `�z����` int not null,
    `�n��` varchar(40) not null,
    `�폜�t���O` varchar(10) default '0', 
    `�ŗ�ID` int(11) unsigned not null,
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

drop table if exists `�ŗ�`;

create table `�ŗ�`(
    `id` int(11) not null auto_increment,
    `�ŗ�` varchar(30) not null default '',
    `�폜�t���O` varchar(10) not null default '0',
    `���l` varchar(200) default null, 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

drop table if exists `�݌�`;

create table `�݌�`(
    `id` int(11) not null auto_increment,
    `���t` date not null,
    `�݌ɕϓ���` int not null,
    `���iID` int(11) not null,
    `�݌Ɋm�F�t���O` varchar(10) not null default '0',
    `���l` varchar(200) default null, 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


drop table if exists `�ڋq`;

create table `�ڋq`(
    `id` int(11) not null auto_increment,
    `���O` varchar(40) NOT NULL DEFAULT '',
    `�J�i` varchar(40) NOT NULL DEFAULT '',
    `�X�֔ԍ�` varchar(7) NOT NULL,
    `�Z��` varchar(100) NOT NULL,
    `�d�b�ԍ�` varchar(15) NOT NULL,
    `�z����ID` varchar(11) not null,
    `���[���A�h���X` varchar(80) not null,
    `���O�C���p�X���[�h` varchar(30) not null,
    `�ڋq�����N` varchar(10) not null default '0',
    `�폜�t���O` varchar(10) default '0',
    `���l` varchar(200) character set utf8 collate utf8_unicode_ci default '', 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

drop table if exists `���i`;

create table `���i`(
    `id` int(11) not null auto_increment,
    `���i�ԍ�` varchar(30) not null default '',
    `���i��` varchar(60)  NOT NULL DEFAULT '',
    `���i�ڍ�` varchar(60) default null,
    `�̔��P��` mediumint(5) unsigned NOT NULL DEFAULT '0',
    `�ψ�P��` mediumint(5) default null,
    `���i�J�e�S���[ID` int(11) unsigned not null,
    `���i������` varchar(20) default null,
    `�����t���O` varchar(10) not null default '0',
    `�폜�t���O` varchar(10) not null default '0',
    `�X�V����` datetime not null default current_timestamp,
    `���l` varchar(200) default null, 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

drop view if exists ���i�J�e�S���[�ꗗ;

create view ���i�J�e�S���[�ꗗ as
select ���i�J�e�S���[.id,�J�e�S���[,�ŗ�,�J�e�S���[������,���i�J�e�S���[.���l
from ���i�J�e�S���[ inner join �ŗ� on �ŗ�ID = �ŗ�.id
where ���i�J�e�S���[.�폜�t���O = 0;

drop view if exists �ڋq�ꗗ;

create view �ڋq�ꗗ as
select �ڋq.id,���O,�J�i,�X�֔ԍ�,�Z��,�d�b�ԍ�,�n��,�z����,���[���A�h���X,�ڋq�����N
from �ڋq inner join �z���� on �z����ID = �z����.id
where �ڋq.�폜�t���O = 0;

drop view if exists �󒍖��׏��ꗗ;

create view �󒍖��׏��ꗗ as
select �󒍖���.id,��ID,�󒍓�,���i�ԍ�,���i��,���i�ڍ�,�ō����z,�Ŕ����z,����
from �󒍖��� inner join �� on ��ID = ��.id inner join ���i on ���iID = ���i.id
where ��.�폜�t���O = 0;

drop view if exists �󒍏��ꗗ;

create view �󒍏��ꗗ as
select ��.id,�󒍓�,���O,�X�֔ԍ�,�Z��,�ō����v���z,�ō����������v�z
from �� inner join �ڋq on �ڋqID = �ڋq.id
where ��.�폜�t���O = 0;

drop view if exists �z�����ꗗ;

create view �z�����ꗗ as
select id,�n��,�z����
from �z����
where �폜�t���O = 0;

drop view if exists ���o�ɗ���;

create view ���o�ɗ��� as
select ���iID,���i�ԍ�,���i��,���i�ڍ�,���t,�݌ɕϓ���,�݌Ɋm�F�t���O
from �݌� inner join ���i on ���iID = ���i.id;

drop view if exists ���i�ꗗ;

create view ���i�ꗗ as 
select 
    �݌�.���iID,
    �J�e�S���[,
    ���i�ԍ�,
    ���i��,
    ���i�ڍ�,
    round(case when �����t���O = 0 then �̔��P��*(1+(�ŗ�/100)) else 0 end) as �ō��̔��P��,
    case when �����t���O = 0 then �̔��P�� else 0 end as �Ŕ��̔��P��,
    round(case when �����t���O = 1 then �̔��P��*(1-(���i������/100))*(1+(�ŗ�/100)) else 0 end) as �ō����i�������i,
    round(case when �����t���O = 1 then �̔��P��*(1-(���i������/100)) else 0 end) as �Ŕ����i�������i,
    round(case when �����t���O = 2 then �̔��P��*(1-(�J�e�S���[������/100))*(1+(�ŗ�/100)) else 0 end) as �ō��J�e�S���[�������i,
    round(case when �����t���O = 2 then �̔��P��*(1-(�J�e�S���[������/100)) else 0 end) as �Ŕ��J�e�S���[�������i,
    round(case when �����t���O = 3 then �ψ�P��*(1+(�ŗ�/100)) else 0 end) as �ō��ψꉿ�i,
    case when �����t���O = 3 then �ψ�P�� else 0 end as �Ŕ��ψ�P��,
    �ŗ�,
    sum(�݌ɕϓ���) as �݌ɐ�,
    �����t���O,���i.
    �폜�t���O
from 
    �݌� inner join ���i on ���iID = ���i.id inner join ���i�J�e�S���[ on ���i�J�e�S���[ID = ���i�J�e�S���[.id inner join �ŗ� on �ŗ�ID = �ŗ�.id
group by 
    �݌�.���iID
having 
    ���i.�폜�t���O = 0;

drop view if exists �ŗ��ꗗ;

create view �ŗ��ꗗ as
select id,�ŗ�,���l
from �ŗ�
where �폜�t���O = 0;


