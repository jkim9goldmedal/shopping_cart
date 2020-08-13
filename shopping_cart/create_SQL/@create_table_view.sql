drop table if exists `カート`;

create table `カート`(
    `id` int(11) not null auto_increment,
    `商品番号` varchar(30) not null,
    `ログインID` varchar(30) not null,
    `数量` int default null,
    `税込価格` int not null,
    `税抜価格` int not null, 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `カート` AUTO_INCREMENT = 1;

drop table if exists `商品カテゴリー`;

create table `商品カテゴリー`(
    `id` int(11) not null auto_increment,
    `カテゴリー番号` int(11) not null,
    `カテゴリー` varchar(30) not null default '',
    `税率管理番号` int(11) not null,
    `カテゴリー割引率` int(11) default null,
    `削除フラグ` varchar(10) not null default '0',
    `更新日時` datetime not null default current_timestamp,
    `備考` varchar(200) default null, 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `商品カテゴリー` AUTO_INCREMENT = 1;


drop table if exists `受注明細`;

create table `受注明細`(
    `id` int(11) not null auto_increment,
    `受注ID` int(11) unsigned not null,
    `商品番号` varchar(30) not null,
    `税込金額` int not null,
    `税抜金額` int not null, 
    `税込販売単価` int not null,
    `販売単価` int not null,
    `数量` int default null,
    `削除フラグ` varchar(10) default '0',
    `備考` varchar(100) default null,
    `更新日時` datetime default current_timestamp,
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `受注明細` AUTO_INCREMENT = 1;

drop table if exists `受注`;

create table `受注`(
    `id` int(11) not null auto_increment,
    `受注日` date not null,
    `ログインID` varchar(30) not null,
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
    `更新日時` datetime not null default current_timestamp,
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `受注` AUTO_INCREMENT = 1;

drop table if exists `配送料`;

create table `配送料`(
    `id` int(11) not null auto_increment,
    `配送料管理番号` int(11) not null,
    `配送料` int not null,
    `地域` varchar(40) not null,
    `削除フラグ` varchar(10) default '0', 
    `税率管理番号` int(11) not null,
    `更新日時` datetime not null default current_timestamp,
    `備考` varchar(100) default null,
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `配送料` AUTO_INCREMENT = 1;


drop table if exists `税率`;

create table `税率`(
    `id` int(11) not null auto_increment,
    `税率管理番号` int(11) not null,
    `税率` int(11) not null,
    `削除フラグ` varchar(10) not null default '0',
    `更新日時` datetime not null default current_timestamp,
    `備考` varchar(200) default null, 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `税率` AUTO_INCREMENT = 1;


drop table if exists `在庫`;

create table `在庫`(
    `id` int(11) not null auto_increment,
    `日付` date not null,
    `在庫変動数` int not null,
    `商品番号` varchar(30) not null,
    `在庫確認フラグ` varchar(10) not null default '1',
    `備考` varchar(200) default null, 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `在庫` AUTO_INCREMENT = 1;


drop table if exists `顧客`;

create table `顧客`(
    `id` int(11) not null auto_increment,
    `名前` varchar(40) NOT NULL DEFAULT '',
    `カナ` varchar(40) NOT NULL DEFAULT '',
    `郵便番号` varchar(7) NOT NULL,
    `住所` varchar(100) NOT NULL,
    `電話番号` varchar(15) NOT NULL,
    `配送料管理番号` int(11) not null,
    `メールアドレス` varchar(80) not null,
    `ログインID` varchar(30) not null,
    `ログインパスワード` varchar(30) not null,
    `顧客ランク` varchar(10) default '2',
    `削除フラグ` varchar(10) default '0',
    `更新日時` datetime not null default current_timestamp,
    `備考` varchar(200) character set utf8 collate utf8_unicode_ci default '', 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `顧客` AUTO_INCREMENT = 1;

drop table if exists `商品`;

create table `商品`(
    `id` int(11) not null auto_increment,
    `商品番号` varchar(30) not null default '',
    `商品名` varchar(60)  NOT NULL DEFAULT '',
    `商品詳細` varchar(60) default '',
    `販売単価` mediumint(5) unsigned NOT NULL DEFAULT '0',
    `均一単価` mediumint(5) default null,
    `商品カテゴリー番号` varchar(10) not null,
    `商品割引率` int(11) default null,
    `割引フラグ` varchar(10) not null default '0',
    `削除フラグ` varchar(10) not null default '0',
    `更新日時` datetime not null default current_timestamp,
    `備考` varchar(200) default null, 
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `商品` AUTO_INCREMENT = 1;

drop view if exists 税率一覧;

create view 税率一覧 as
select
    i1.id,
    i1.税率管理番号,
    i1.税率,
    i1.更新日時,
    i1.備考
from
    税率 as i1
    inner join(
        select
            税率.税率管理番号 as f1,
            max(税率.id) as f2
        from
            税率
        group by
            税率.税率管理番号
    ) i2
        on i2.f1 = i1.税率管理番号
        and i2.f2 = i1.id;



drop view if exists 商品カテゴリー一覧;

create view 商品カテゴリー一覧 as
select
    i1.id,
    i1.カテゴリー番号,
    i1.カテゴリー,
    i1.税率管理番号,
    i1.カテゴリー割引率,
    i1.更新日時,
    i1.備考
from
    商品カテゴリー as i1
    inner join(
        select
            商品カテゴリー.カテゴリー番号 as f1,
            max(商品カテゴリー.id) as f2
        from
            商品カテゴリー
        group by
            商品カテゴリー.カテゴリー番号
    ) i2
        on i2.f1 = i1.カテゴリー番号
        and i2.f2 = i1.id;





drop view if exists 顧客一覧;

create view 顧客一覧 as
select
    i1.id,
    i1.名前,
    i1.カナ,
    i1.郵便番号,
    i1.住所,
    i1.電話番号,
    i1.配送料管理番号,
    i1.メールアドレス,
    i1.ログインID,
    i1.顧客ランク,
    i1.削除フラグ,
    i1.更新日時,
    i1.備考
from
    顧客 as i1
    inner join(
        select
            顧客.ログインID as f1,
            max(顧客.id) as f2
        from
            顧客
        group by
            顧客.ログインID
    ) i2
        on i2.f1 = i1.ログインID
        and i2.f2 = i1.id;

drop view if exists 【ログイン用】顧客一覧;

create view 【ログイン用】顧客一覧 as
select
    i1.id,
    i1.名前,
    i1.カナ,
    i1.郵便番号,
    i1.住所,
    i1.電話番号,
    i1.配送料管理番号,
    i1.メールアドレス,
    i1.ログインID,
    i1.ログインパスワード,
    i1.顧客ランク,
    i1.備考
from
    顧客 as i1
    inner join(
        select
            顧客.ログインID as f1,
            max(顧客.id) as f2
        from
            顧客
        group by
            顧客.ログインID
    ) i2
        on i2.f1 = i1.ログインID
        and i2.f2 = i1.id
where
    i1.削除フラグ = 0;




drop view if exists 配送料一覧;

create view 配送料一覧 as
select
    i1.id,
    i1.配送料管理番号,
    i1.地域,
    i1.更新日時,
    i1.配送料,
    i1.税率管理番号
from
    配送料 as i1
    inner join(
        select
            配送料.配送料管理番号 as f1,
            max(配送料.id) as f2
        from
            配送料
        group by
            配送料.配送料管理番号
    ) i2
        on i2.f1 = i1.配送料管理番号
        and i2.f2 = i1.id;

drop view if exists 【入力ミス確認用】入出庫履歴;

create view 【入力ミス確認用】入出庫履歴 as
select
    商品.id,
    在庫.商品番号,
    商品名,
    商品詳細,
    日付,
    在庫変動数,
    在庫確認フラグ
from 在庫 left outer join 商品 on 在庫.商品番号 = 商品.商品番号;

drop view if exists 入出庫履歴;

create view 入出庫履歴 as
select
    i1.id,
    i1.商品番号,
    i1.商品名,
    i1.商品詳細,
    i1.日付,
    i1.在庫変動数,
    i1.在庫確認フラグ
from
    【入力ミス確認用】入出庫履歴 as i1
    inner join(
        select
            【入力ミス確認用】入出庫履歴.商品番号 as f1,
            max(【入力ミス確認用】入出庫履歴.id) as f2
        from
            【入力ミス確認用】入出庫履歴
        group by
            【入力ミス確認用】入出庫履歴.商品番号
    ) i2
        on i2.f1 = i1.商品番号
        and i2.f2 = i1.id;



drop view if exists 【入力ミス確認用】商品一覧;

create view 【入力ミス確認用】商品一覧 as 
select
    商品.id,
    商品.商品番号,
    商品カテゴリー番号,
    商品名,
    商品詳細,
    round(販売単価*(1+(税率/100))) as 税込販売単価,
    販売単価 as 税抜販売単価,
    round(case when 割引フラグ = 1 then 販売単価*(1-(商品割引率/100))*(1+(税率/100)) else 0 end) as 税込商品割引価格,
    round(case when 割引フラグ = 1 then 販売単価*(1-(商品割引率/100)) else 0 end) as 税抜商品割引価格,
    round(case when 割引フラグ = 2 then 販売単価*(1-(カテゴリー割引率/100))*(1+(税率/100)) else 0 end) as 税込カテゴリー割引価格,
    round(case when 割引フラグ = 2 then 販売単価*(1-(カテゴリー割引率/100)) else 0 end) as 税抜カテゴリー割引価格,
    round(case when 割引フラグ = 3 then 均一単価*(1+(税率/100)) else 0 end) as 税込均一価格,
    case when 割引フラグ = 3 then 均一単価 else 0 end as 税抜均一単価,
    税率,
    割引フラグ,
    商品.削除フラグ,
    商品.備考
from 
    商品 left outer join 商品カテゴリー一覧 on 商品カテゴリー番号 = 商品カテゴリー一覧.カテゴリー番号 left outer join 税率一覧 on 商品カテゴリー一覧.税率管理番号 = 税率一覧.税率管理番号
;






drop view if exists 商品情報一覧ビュー;

create view 商品情報一覧ビュー as
select
    i1.id,
    i1.商品番号,
    i1.商品カテゴリー番号,
    i1.商品名,
    i1.商品詳細,
    i1.税込販売単価,
    i1.税抜販売単価,
    i1.税込商品割引価格,
    i1.税抜商品割引価格,
    i1.税込カテゴリー割引価格,
    i1.税抜カテゴリー割引価格,
    i1.税込均一価格,
    i1.税抜均一単価,
    i1.税率,
    i1.割引フラグ,
    i1.削除フラグ,
    i1.備考
from
    【入力ミス確認用】商品一覧 as i1
    inner join(
        select
            【入力ミス確認用】商品一覧.商品番号 as f1,
            max(【入力ミス確認用】商品一覧.id) as f2
        from
            【入力ミス確認用】商品一覧
        group by
            【入力ミス確認用】商品一覧.商品番号
    ) i2
        on i2.f1 = i1.商品番号
        and i2.f2 = i1.id
group by
    i1.商品番号;


drop view if exists 商品在庫一覧;

create view 商品在庫一覧 as
select
    i1.id,
    i1.商品番号,
    i1.商品カテゴリー番号,
    i1.商品名,
    i1.商品詳細,
    i1.税込販売単価,
    i1.税抜販売単価,
    i1.税込商品割引価格,
    i1.税抜商品割引価格,
    i1.税込カテゴリー割引価格,
    i1.税抜カテゴリー割引価格,
    i1.税込均一価格,
    i1.税抜均一単価,
    i1.税率,
    sum(在庫変動数) as 在庫数,
    i1.割引フラグ,
    i1.削除フラグ,
    i1.備考
from
    在庫 as i2 right outer join 商品情報一覧ビュー as i1 on i2.商品番号 = i1.商品番号
group by
    i1.商品番号;

drop view if exists 受注明細情報一覧;

create view 受注明細情報一覧 as
select
    受注明細.id,
    受注ID,
    受注日,
    受注明細.商品番号,
    商品名,
    商品詳細,
    case when 受注.削除フラグ = 1 then 税込金額 * (-1) else 税込金額 end as 税込金額,
    case when 受注.削除フラグ = 1 then 税抜金額 * (-1) else 税抜金額 end as 税抜金額,
    case when 受注.削除フラグ = 1 then 受注明細.税込販売単価 * (-1) else 受注明細.税込販売単価 end as 税込販売単価,
    case when 受注.削除フラグ = 1 then 受注明細.販売単価 * (-1) else 受注明細.販売単価 end as 販売単価,
    税率,
    数量,
    受注.削除フラグ
from
    受注明細 inner join 受注 on 受注ID = 受注.id inner join 商品在庫一覧 on 受注明細.商品番号 = 商品在庫一覧.商品番号;



drop view if exists 受注情報一覧;

create view 受注情報一覧 as
select
    受注.id,
    受注.受注日,
    名前,
    カナ,
    電話番号,
    郵便番号,
    住所,
    注文合計数,
    case when 受注.削除フラグ = 1 then 税込合計金額 * (-1) else 税込合計金額 end as 税込合計金額,
    case when 受注.削除フラグ = 1 then 税込配送料 * (-1) else 税込配送料 end as 税込配送料,
    case when 受注.削除フラグ = 1 then 税抜配送料 * (-1) else 税抜配送料 end as 税抜配送料,
    case when 受注.削除フラグ = 1 then 税込送料込合計額 * (-1) else 税込送料込合計額 end as 税込送料込合計額,
    受注明細.商品番号,
    商品名,
    case when 受注.削除フラグ = 1 then 販売単価 * (-1) else 販売単価 end as 販売単価,
    数量,
    case when 受注.削除フラグ = 1 then 税込金額 * (-1) else 税込金額 end as 税込金額,
    発送済み,
    入金確認済み,
    受注.削除フラグ,
    受注.更新日時,
    受注.備考
from 受注明細 left outer join 受注 on 受注ID = 受注.id left outer join 商品在庫一覧 on 受注明細.商品番号 = 商品在庫一覧.商品番号 left outer join 顧客一覧 on 受注.ログインID = 顧客一覧.ログインID;


drop view if exists 月次売上;

create view 月次売上 as
select
    受注.受注日,
    sum(税込金額) as 商品税込合計金額,
    sum(税込金額 + 税込配送料) as 総額,
    sum(税込配送料) as 税込配送料,
    sum(税抜配送料) as 税抜配送料,
    sum(
        case when 受注明細情報一覧.税率 = 10 then (税込金額 - 税抜金額) else 0 end
        ) as '10%消費税合計',
    sum(
        case when 受注明細情報一覧.税率 = 8 then (税込金額 - 税抜金額) else 0 end
        ) as '8%消費税合計'
from
    受注明細情報一覧 inner join 受注 on 受注ID = 受注.id inner join 商品在庫一覧 on 受注明細情報一覧.商品番号 = 商品在庫一覧.商品番号
group by
    受注.受注日;


drop view if exists 月次商品別売上;

create view 月次商品別売上 as
select
    A.商品番号,
    A.商品名,
    A.商品詳細,
    A.販売単価,
    sum(A.数量) as 数量,
    sum(A.税抜金額) as 税抜金額,
    sum(A.税込金額) as 税込金額
from
    受注明細情報一覧 A
where
    exists(
        select
            *
        from
            受注明細情報一覧 B
        where
            A.商品番号 = B.商品番号
        and
            A.販売単価 = B.販売単価
        and
            DATE_FORMAT(B.受注日, '%Y/%m') = DATE_FORMAT(now(),'%Y/%m')
        )
    and
        DATE_FORMAT(A.受注日, '%Y/%m') = DATE_FORMAT(now(),'%Y/%m')
group by
    A.商品番号,
    A.販売単価
order by
    A.商品番号;
