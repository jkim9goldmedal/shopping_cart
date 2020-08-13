drop table if exists `�J�[�g`;

create table `�J�[�g`(
    `id` int(11) not null auto_increment,
    `���i�ԍ�` varchar(30) not null,
    `���O�C��ID` varchar(30) not null,
    `����` int default null,
    `�ō����i` int not null,
    `�Ŕ����i` int not null, 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `�J�[�g` AUTO_INCREMENT = 1;

drop table if exists `���i�J�e�S���[`;

create table `���i�J�e�S���[`(
    `id` int(11) not null auto_increment,
    `�J�e�S���[�ԍ�` int(11) not null,
    `�J�e�S���[` varchar(30) not null default '',
    `�ŗ��Ǘ��ԍ�` int(11) not null,
    `�J�e�S���[������` int(11) default null,
    `�폜�t���O` varchar(10) not null default '0',
    `�X�V����` datetime not null default current_timestamp,
    `���l` varchar(200) default null, 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `���i�J�e�S���[` AUTO_INCREMENT = 1;


drop table if exists `�󒍖���`;

create table `�󒍖���`(
    `id` int(11) not null auto_increment,
    `��ID` int(11) unsigned not null,
    `���i�ԍ�` varchar(30) not null,
    `�ō����z` int not null,
    `�Ŕ����z` int not null, 
    `�ō��̔��P��` int not null,
    `�̔��P��` int not null,
    `����` int default null,
    `�폜�t���O` varchar(10) default '0',
    `���l` varchar(100) default null,
    `�X�V����` datetime default current_timestamp,
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `�󒍖���` AUTO_INCREMENT = 1;

drop table if exists `��`;

create table `��`(
    `id` int(11) not null auto_increment,
    `�󒍓�` date not null,
    `���O�C��ID` varchar(30) not null,
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
    `�X�V����` datetime not null default current_timestamp,
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `��` AUTO_INCREMENT = 1;

drop table if exists `�z����`;

create table `�z����`(
    `id` int(11) not null auto_increment,
    `�z�����Ǘ��ԍ�` int(11) not null,
    `�z����` int not null,
    `�n��` varchar(40) not null,
    `�폜�t���O` varchar(10) default '0', 
    `�ŗ��Ǘ��ԍ�` int(11) not null,
    `�X�V����` datetime not null default current_timestamp,
    `���l` varchar(100) default null,
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `�z����` AUTO_INCREMENT = 1;


drop table if exists `�ŗ�`;

create table `�ŗ�`(
    `id` int(11) not null auto_increment,
    `�ŗ��Ǘ��ԍ�` int(11) not null,
    `�ŗ�` int(11) not null,
    `�폜�t���O` varchar(10) not null default '0',
    `�X�V����` datetime not null default current_timestamp,
    `���l` varchar(200) default null, 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `�ŗ�` AUTO_INCREMENT = 1;


drop table if exists `�݌�`;

create table `�݌�`(
    `id` int(11) not null auto_increment,
    `���t` date not null,
    `�݌ɕϓ���` int not null,
    `���i�ԍ�` varchar(30) not null,
    `�݌Ɋm�F�t���O` varchar(10) not null default '1',
    `���l` varchar(200) default null, 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `�݌�` AUTO_INCREMENT = 1;


drop table if exists `�ڋq`;

create table `�ڋq`(
    `id` int(11) not null auto_increment,
    `���O` varchar(40) NOT NULL DEFAULT '',
    `�J�i` varchar(40) NOT NULL DEFAULT '',
    `�X�֔ԍ�` varchar(7) NOT NULL,
    `�Z��` varchar(100) NOT NULL,
    `�d�b�ԍ�` varchar(15) NOT NULL,
    `�z�����Ǘ��ԍ�` int(11) not null,
    `���[���A�h���X` varchar(80) not null,
    `���O�C��ID` varchar(30) not null,
    `���O�C���p�X���[�h` varchar(30) not null,
    `�ڋq�����N` varchar(10) default '2',
    `�폜�t���O` varchar(10) default '0',
    `�X�V����` datetime not null default current_timestamp,
    `���l` varchar(200) character set utf8 collate utf8_unicode_ci default '', 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `�ڋq` AUTO_INCREMENT = 1;

drop table if exists `���i`;

create table `���i`(
    `id` int(11) not null auto_increment,
    `���i�ԍ�` varchar(30) not null default '',
    `���i��` varchar(60)  NOT NULL DEFAULT '',
    `���i�ڍ�` varchar(60) default '',
    `�̔��P��` mediumint(5) unsigned NOT NULL DEFAULT '0',
    `�ψ�P��` mediumint(5) default null,
    `���i�J�e�S���[�ԍ�` varchar(10) not null,
    `���i������` int(11) default null,
    `�����t���O` varchar(10) not null default '0',
    `�폜�t���O` varchar(10) not null default '0',
    `�X�V����` datetime not null default current_timestamp,
    `���l` varchar(200) default null, 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `���i` AUTO_INCREMENT = 1;

drop view if exists �ŗ��ꗗ;

create view �ŗ��ꗗ as
select
    i1.id,
    i1.�ŗ��Ǘ��ԍ�,
    i1.�ŗ�,
    i1.�X�V����,
    i1.���l
from
    �ŗ� as i1
    inner join(
        select
            �ŗ�.�ŗ��Ǘ��ԍ� as f1,
            max(�ŗ�.id) as f2
        from
            �ŗ�
        group by
            �ŗ�.�ŗ��Ǘ��ԍ�
    ) i2
        on i2.f1 = i1.�ŗ��Ǘ��ԍ�
        and i2.f2 = i1.id;



drop view if exists ���i�J�e�S���[�ꗗ;

create view ���i�J�e�S���[�ꗗ as
select
    i1.id,
    i1.�J�e�S���[�ԍ�,
    i1.�J�e�S���[,
    i1.�ŗ��Ǘ��ԍ�,
    i1.�J�e�S���[������,
    i1.�X�V����,
    i1.���l
from
    ���i�J�e�S���[ as i1
    inner join(
        select
            ���i�J�e�S���[.�J�e�S���[�ԍ� as f1,
            max(���i�J�e�S���[.id) as f2
        from
            ���i�J�e�S���[
        group by
            ���i�J�e�S���[.�J�e�S���[�ԍ�
    ) i2
        on i2.f1 = i1.�J�e�S���[�ԍ�
        and i2.f2 = i1.id;





drop view if exists �ڋq�ꗗ;

create view �ڋq�ꗗ as
select
    i1.id,
    i1.���O,
    i1.�J�i,
    i1.�X�֔ԍ�,
    i1.�Z��,
    i1.�d�b�ԍ�,
    i1.�z�����Ǘ��ԍ�,
    i1.���[���A�h���X,
    i1.���O�C��ID,
    i1.�ڋq�����N,
    i1.�폜�t���O,
    i1.�X�V����,
    i1.���l
from
    �ڋq as i1
    inner join(
        select
            �ڋq.���O�C��ID as f1,
            max(�ڋq.id) as f2
        from
            �ڋq
        group by
            �ڋq.���O�C��ID
    ) i2
        on i2.f1 = i1.���O�C��ID
        and i2.f2 = i1.id;

drop view if exists �y���O�C���p�z�ڋq�ꗗ;

create view �y���O�C���p�z�ڋq�ꗗ as
select
    i1.id,
    i1.���O,
    i1.�J�i,
    i1.�X�֔ԍ�,
    i1.�Z��,
    i1.�d�b�ԍ�,
    i1.�z�����Ǘ��ԍ�,
    i1.���[���A�h���X,
    i1.���O�C��ID,
    i1.���O�C���p�X���[�h,
    i1.�ڋq�����N,
    i1.���l
from
    �ڋq as i1
    inner join(
        select
            �ڋq.���O�C��ID as f1,
            max(�ڋq.id) as f2
        from
            �ڋq
        group by
            �ڋq.���O�C��ID
    ) i2
        on i2.f1 = i1.���O�C��ID
        and i2.f2 = i1.id
where
    i1.�폜�t���O = 0;




drop view if exists �z�����ꗗ;

create view �z�����ꗗ as
select
    i1.id,
    i1.�z�����Ǘ��ԍ�,
    i1.�n��,
    i1.�X�V����,
    i1.�z����,
    i1.�ŗ��Ǘ��ԍ�
from
    �z���� as i1
    inner join(
        select
            �z����.�z�����Ǘ��ԍ� as f1,
            max(�z����.id) as f2
        from
            �z����
        group by
            �z����.�z�����Ǘ��ԍ�
    ) i2
        on i2.f1 = i1.�z�����Ǘ��ԍ�
        and i2.f2 = i1.id;

drop view if exists �y���̓~�X�m�F�p�z���o�ɗ���;

create view �y���̓~�X�m�F�p�z���o�ɗ��� as
select
    ���i.id,
    �݌�.���i�ԍ�,
    ���i��,
    ���i�ڍ�,
    ���t,
    �݌ɕϓ���,
    �݌Ɋm�F�t���O
from �݌� left outer join ���i on �݌�.���i�ԍ� = ���i.���i�ԍ�;

drop view if exists ���o�ɗ���;

create view ���o�ɗ��� as
select
    i1.id,
    i1.���i�ԍ�,
    i1.���i��,
    i1.���i�ڍ�,
    i1.���t,
    i1.�݌ɕϓ���,
    i1.�݌Ɋm�F�t���O
from
    �y���̓~�X�m�F�p�z���o�ɗ��� as i1
    inner join(
        select
            �y���̓~�X�m�F�p�z���o�ɗ���.���i�ԍ� as f1,
            max(�y���̓~�X�m�F�p�z���o�ɗ���.id) as f2
        from
            �y���̓~�X�m�F�p�z���o�ɗ���
        group by
            �y���̓~�X�m�F�p�z���o�ɗ���.���i�ԍ�
    ) i2
        on i2.f1 = i1.���i�ԍ�
        and i2.f2 = i1.id;



drop view if exists �y���̓~�X�m�F�p�z���i�ꗗ;

create view �y���̓~�X�m�F�p�z���i�ꗗ as 
select
    ���i.id,
    ���i.���i�ԍ�,
    ���i�J�e�S���[�ԍ�,
    ���i��,
    ���i�ڍ�,
    round(�̔��P��*(1+(�ŗ�/100))) as �ō��̔��P��,
    �̔��P�� as �Ŕ��̔��P��,
    round(case when �����t���O = 1 then �̔��P��*(1-(���i������/100))*(1+(�ŗ�/100)) else 0 end) as �ō����i�������i,
    round(case when �����t���O = 1 then �̔��P��*(1-(���i������/100)) else 0 end) as �Ŕ����i�������i,
    round(case when �����t���O = 2 then �̔��P��*(1-(�J�e�S���[������/100))*(1+(�ŗ�/100)) else 0 end) as �ō��J�e�S���[�������i,
    round(case when �����t���O = 2 then �̔��P��*(1-(�J�e�S���[������/100)) else 0 end) as �Ŕ��J�e�S���[�������i,
    round(case when �����t���O = 3 then �ψ�P��*(1+(�ŗ�/100)) else 0 end) as �ō��ψꉿ�i,
    case when �����t���O = 3 then �ψ�P�� else 0 end as �Ŕ��ψ�P��,
    �ŗ�,
    �����t���O,
    ���i.�폜�t���O,
    ���i.���l
from 
    ���i left outer join ���i�J�e�S���[�ꗗ on ���i�J�e�S���[�ԍ� = ���i�J�e�S���[�ꗗ.�J�e�S���[�ԍ� left outer join �ŗ��ꗗ on ���i�J�e�S���[�ꗗ.�ŗ��Ǘ��ԍ� = �ŗ��ꗗ.�ŗ��Ǘ��ԍ�
;






drop view if exists ���i���ꗗ�r���[;

create view ���i���ꗗ�r���[ as
select
    i1.id,
    i1.���i�ԍ�,
    i1.���i�J�e�S���[�ԍ�,
    i1.���i��,
    i1.���i�ڍ�,
    i1.�ō��̔��P��,
    i1.�Ŕ��̔��P��,
    i1.�ō����i�������i,
    i1.�Ŕ����i�������i,
    i1.�ō��J�e�S���[�������i,
    i1.�Ŕ��J�e�S���[�������i,
    i1.�ō��ψꉿ�i,
    i1.�Ŕ��ψ�P��,
    i1.�ŗ�,
    i1.�����t���O,
    i1.�폜�t���O,
    i1.���l
from
    �y���̓~�X�m�F�p�z���i�ꗗ as i1
    inner join(
        select
            �y���̓~�X�m�F�p�z���i�ꗗ.���i�ԍ� as f1,
            max(�y���̓~�X�m�F�p�z���i�ꗗ.id) as f2
        from
            �y���̓~�X�m�F�p�z���i�ꗗ
        group by
            �y���̓~�X�m�F�p�z���i�ꗗ.���i�ԍ�
    ) i2
        on i2.f1 = i1.���i�ԍ�
        and i2.f2 = i1.id
group by
    i1.���i�ԍ�;


drop view if exists ���i�݌Ɉꗗ;

create view ���i�݌Ɉꗗ as
select
    i1.id,
    i1.���i�ԍ�,
    i1.���i�J�e�S���[�ԍ�,
    i1.���i��,
    i1.���i�ڍ�,
    i1.�ō��̔��P��,
    i1.�Ŕ��̔��P��,
    i1.�ō����i�������i,
    i1.�Ŕ����i�������i,
    i1.�ō��J�e�S���[�������i,
    i1.�Ŕ��J�e�S���[�������i,
    i1.�ō��ψꉿ�i,
    i1.�Ŕ��ψ�P��,
    i1.�ŗ�,
    sum(�݌ɕϓ���) as �݌ɐ�,
    i1.�����t���O,
    i1.�폜�t���O,
    i1.���l
from
    �݌� as i2 right outer join ���i���ꗗ�r���[ as i1 on i2.���i�ԍ� = i1.���i�ԍ�
group by
    i1.���i�ԍ�;

drop view if exists �󒍖��׏��ꗗ;

create view �󒍖��׏��ꗗ as
select
    �󒍖���.id,
    ��ID,
    �󒍓�,
    �󒍖���.���i�ԍ�,
    ���i��,
    ���i�ڍ�,
    case when ��.�폜�t���O = 1 then �ō����z * (-1) else �ō����z end as �ō����z,
    case when ��.�폜�t���O = 1 then �Ŕ����z * (-1) else �Ŕ����z end as �Ŕ����z,
    case when ��.�폜�t���O = 1 then �󒍖���.�ō��̔��P�� * (-1) else �󒍖���.�ō��̔��P�� end as �ō��̔��P��,
    case when ��.�폜�t���O = 1 then �󒍖���.�̔��P�� * (-1) else �󒍖���.�̔��P�� end as �̔��P��,
    �ŗ�,
    ����,
    ��.�폜�t���O
from
    �󒍖��� inner join �� on ��ID = ��.id inner join ���i�݌Ɉꗗ on �󒍖���.���i�ԍ� = ���i�݌Ɉꗗ.���i�ԍ�;



drop view if exists �󒍏��ꗗ;

create view �󒍏��ꗗ as
select
    ��.id,
    ��.�󒍓�,
    ���O,
    �J�i,
    �d�b�ԍ�,
    �X�֔ԍ�,
    �Z��,
    �������v��,
    case when ��.�폜�t���O = 1 then �ō����v���z * (-1) else �ō����v���z end as �ō����v���z,
    case when ��.�폜�t���O = 1 then �ō��z���� * (-1) else �ō��z���� end as �ō��z����,
    case when ��.�폜�t���O = 1 then �Ŕ��z���� * (-1) else �Ŕ��z���� end as �Ŕ��z����,
    case when ��.�폜�t���O = 1 then �ō����������v�z * (-1) else �ō����������v�z end as �ō����������v�z,
    �󒍖���.���i�ԍ�,
    ���i��,
    case when ��.�폜�t���O = 1 then �̔��P�� * (-1) else �̔��P�� end as �̔��P��,
    ����,
    case when ��.�폜�t���O = 1 then �ō����z * (-1) else �ō����z end as �ō����z,
    �����ς�,
    �����m�F�ς�,
    ��.�폜�t���O,
    ��.�X�V����,
    ��.���l
from �󒍖��� left outer join �� on ��ID = ��.id left outer join ���i�݌Ɉꗗ on �󒍖���.���i�ԍ� = ���i�݌Ɉꗗ.���i�ԍ� left outer join �ڋq�ꗗ on ��.���O�C��ID = �ڋq�ꗗ.���O�C��ID;


drop view if exists ��������;

create view �������� as
select
    ��.�󒍓�,
    sum(�ō����z) as ���i�ō����v���z,
    sum(�ō����z + �ō��z����) as ���z,
    sum(�ō��z����) as �ō��z����,
    sum(�Ŕ��z����) as �Ŕ��z����,
    sum(
        case when �󒍖��׏��ꗗ.�ŗ� = 10 then (�ō����z - �Ŕ����z) else 0 end
        ) as '10%����ō��v',
    sum(
        case when �󒍖��׏��ꗗ.�ŗ� = 8 then (�ō����z - �Ŕ����z) else 0 end
        ) as '8%����ō��v'
from
    �󒍖��׏��ꗗ inner join �� on ��ID = ��.id inner join ���i�݌Ɉꗗ on �󒍖��׏��ꗗ.���i�ԍ� = ���i�݌Ɉꗗ.���i�ԍ�
group by
    ��.�󒍓�;


drop view if exists �������i�ʔ���;

create view �������i�ʔ��� as
select
    A.���i�ԍ�,
    A.���i��,
    A.���i�ڍ�,
    A.�̔��P��,
    sum(A.����) as ����,
    sum(A.�Ŕ����z) as �Ŕ����z,
    sum(A.�ō����z) as �ō����z
from
    �󒍖��׏��ꗗ A
where
    exists(
        select
            *
        from
            �󒍖��׏��ꗗ B
        where
            A.���i�ԍ� = B.���i�ԍ�
        and
            A.�̔��P�� = B.�̔��P��
        and
            DATE_FORMAT(B.�󒍓�, '%Y/%m') = DATE_FORMAT(now(),'%Y/%m')
        )
    and
        DATE_FORMAT(A.�󒍓�, '%Y/%m') = DATE_FORMAT(now(),'%Y/%m')
group by
    A.���i�ԍ�,
    A.�̔��P��
order by
    A.���i�ԍ�;
