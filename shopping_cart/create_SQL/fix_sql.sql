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

