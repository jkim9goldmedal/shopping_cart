drop table if exists `カート`;

create table `カート`(
    `id` int(11) not null auto_increment,
    `商品ID` int(11) unsigned not null,
    `顧客ID` int(11) unsigned not null,
    `数量` int default null,
    `税込価格` int not null,
    `税抜価格` int not null, 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

drop table if exists `商品カテゴリー`;

create table `商品カテゴリー`(
    `id` int(11) not null auto_increment,
    `カテゴリー` varchar(30) not null default '',
    `税率ID` int(11) unsigned not null,
    `カテゴリー割引率` varchar(20) default null,
    `削除フラグ` varchar(10) not null default '0',
    `備考` varchar(200) default null, 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


drop table if exists `受注明細`;

create table `受注明細`(
    `id` int(11) not null auto_increment,
    `受注ID` int(11) unsigned not null,
    `商品ID` int(11) unsigned not null,
    `税込金額` int not null,
    `税抜金額` int not null, 
    `税込販売単価` int not null,
    `販売単価` int not null,
    `数量` int default null,
    `削除フラグ` varchar(10) default '0',
    `備考` varchar(100) default null,
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

drop table if exists `受注`;

create table `受注`(
    `id` int(11) not null auto_increment,
    `受注日` date not null,
    `顧客ID` int(11) unsigned not null,
    `注文合計数` int not null,
    `税込合計金額` int not null,
    `税抜合計金額` int not null, 
    `税込送料込合計額` int not null,
    `税込配送料` int default '0',
    `税抜配送料` int default '0',
    `発送済み`varchar(10) default '0',
    `入金確認済み` varchar(10) default '0',
    `備考` varchar(100) default null,
    `削除フラグ` varchar(10) default '0',
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

drop table if exists `配送料`;

create table `配送料`(
    `id` int(11) not null auto_increment,
    `配送料` int not null,
    `地域` varchar(40) not null,
    `削除フラグ` varchar(10) default '0', 
    `税率ID` int(11) unsigned not null,
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

drop table if exists `税率`;

create table `税率`(
    `id` int(11) not null auto_increment,
    `税率` varchar(30) not null default '',
    `削除フラグ` varchar(10) not null default '0',
    `備考` varchar(200) default null, 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

drop table if exists `在庫`;

create table `在庫`(
    `id` int(11) not null auto_increment,
    `日付` date not null,
    `在庫変動数` int not null,
    `商品ID` int(11) not null,
    `在庫確認フラグ` varchar(10) not null default '0',
    `備考` varchar(200) default null, 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


drop table if exists `顧客`;

create table `顧客`(
    `id` int(11) not null auto_increment,
    `名前` varchar(40) NOT NULL DEFAULT '',
    `カナ` varchar(40) NOT NULL DEFAULT '',
    `郵便番号` varchar(7) NOT NULL,
    `住所` varchar(100) NOT NULL,
    `電話番号` varchar(15) NOT NULL,
    `配送料ID` varchar(11) not null,
    `メールアドレス` varchar(80) not null,
    `ログインパスワード` varchar(30) not null,
    `顧客ランク` varchar(10) not null default '0',
    `削除フラグ` varchar(10) default '0',
    `備考` varchar(200) character set utf8 collate utf8_unicode_ci default '', 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

drop table if exists `商品`;

create table `商品`(
    `id` int(11) not null auto_increment,
    `商品番号` varchar(30) not null default '',
    `商品名` varchar(60)  NOT NULL DEFAULT '',
    `商品詳細` varchar(60) default null,
    `販売単価` mediumint(5) unsigned NOT NULL DEFAULT '0',
    `均一単価` mediumint(5) default null,
    `商品カテゴリーID` int(11) unsigned not null,
    `商品割引率` varchar(20) default null,
    `割引フラグ` varchar(10) not null default '0',
    `削除フラグ` varchar(10) not null default '0',
    `更新日時` datetime not null default current_timestamp,
    `備考` varchar(200) default null, 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

drop view if exists 商品カテゴリー一覧;

create view 商品カテゴリー一覧 as
select 商品カテゴリー.id,カテゴリー,税率,カテゴリー割引率,商品カテゴリー.備考
from 商品カテゴリー inner join 税率 on 税率ID = 税率.id
where 商品カテゴリー.削除フラグ = 0;

drop view if exists 顧客一覧;

create view 顧客一覧 as
select 顧客.id,名前,カナ,郵便番号,住所,電話番号,地域,配送料,メールアドレス,顧客ランク
from 顧客 inner join 配送料 on 配送料ID = 配送料.id
where 顧客.削除フラグ = 0;

drop view if exists 受注明細情報一覧;

create view 受注明細情報一覧 as
select 受注明細.id,受注ID,受注日,商品番号,商品名,商品詳細,税込金額,税抜金額,数量
from 受注明細 inner join 受注 on 受注ID = 受注.id inner join 商品 on 商品ID = 商品.id
where 受注.削除フラグ = 0;

drop view if exists 受注情報一覧;

create view 受注情報一覧 as
select 受注.id,受注日,名前,郵便番号,住所,税込合計金額,税込送料込合計額
from 受注 inner join 顧客 on 顧客ID = 顧客.id
where 受注.削除フラグ = 0;

drop view if exists 配送料一覧;

create view 配送料一覧 as
select id,地域,配送料
from 配送料
where 削除フラグ = 0;

drop view if exists 入出庫履歴;

create view 入出庫履歴 as
select 商品ID,商品番号,商品名,商品詳細,日付,在庫変動数,在庫確認フラグ
from 在庫 inner join 商品 on 商品ID = 商品.id;

drop view if exists 商品一覧;

create view 商品一覧 as 
select 
    在庫.商品ID,
    カテゴリー,
    商品番号,
    商品名,
    商品詳細,
    round(case when 割引フラグ = 0 then 販売単価*(1+(税率/100)) else 0 end) as 税込販売単価,
    case when 割引フラグ = 0 then 販売単価 else 0 end as 税抜販売単価,
    round(case when 割引フラグ = 1 then 販売単価*(1-(商品割引率/100))*(1+(税率/100)) else 0 end) as 税込商品割引価格,
    round(case when 割引フラグ = 1 then 販売単価*(1-(商品割引率/100)) else 0 end) as 税抜商品割引価格,
    round(case when 割引フラグ = 2 then 販売単価*(1-(カテゴリー割引率/100))*(1+(税率/100)) else 0 end) as 税込カテゴリー割引価格,
    round(case when 割引フラグ = 2 then 販売単価*(1-(カテゴリー割引率/100)) else 0 end) as 税抜カテゴリー割引価格,
    round(case when 割引フラグ = 3 then 均一単価*(1+(税率/100)) else 0 end) as 税込均一価格,
    case when 割引フラグ = 3 then 均一単価 else 0 end as 税抜均一単価,
    税率,
    sum(在庫変動数) as 在庫数,
    割引フラグ,商品.
    削除フラグ
from 
    在庫 inner join 商品 on 商品ID = 商品.id inner join 商品カテゴリー on 商品カテゴリーID = 商品カテゴリー.id inner join 税率 on 税率ID = 税率.id
group by 
    在庫.商品ID
having 
    商品.削除フラグ = 0;

drop view if exists 税率一覧;

create view 税率一覧 as
select id,税率,備考
from 税率
where 削除フラグ = 0;


