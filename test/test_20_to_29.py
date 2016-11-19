# -*- coding: utf-8 -*-

import nlp100


def test_20():
    import hashlib
    import json
    j = nlp100.solve_20()
    content = hashlib.md5(json.dumps(j).encode('utf8')).hexdigest()
    assert content == "458ea1d57b2943bf8639d01beabb3eb3"


def test_21():
    import hashlib
    text = nlp100.solve_21()
    content = hashlib.md5(text.encode('utf8')).hexdigest()
    assert content == 'caa6ac7f8d1e401792d5bf82551f5c2b'


def test_22():
    """solve_22の返り値は1行1カテゴリ形式
    """
    import hashlib
    text = nlp100.solve_22()
    content = hashlib.md5(text.encode('utf8')).hexdigest()
    assert content == '87b90a33575edc0afb56f697f0c3dcf0'


def test_23():
    """solve_23の返り値は行ごとに以下の形式
    セクション名 数字
    """
    import hashlib
    text = nlp100.solve_23()
    content = hashlib.md5(text.encode('utf8')).hexdigest()
    assert content == 'e1926a3844911e2c688743990d0fe169'


def test_24():
    """solve_23の返り値は行ごとに以下の形式
    セクション名 数字
    """
    import hashlib
    text = nlp100.solve_24()
    content = hashlib.md5(text.encode('utf8')).hexdigest()
    assert content == '6b62b0daceb1eb13d6c9b6e3ea472dab'


def test_25():
    right = {
        'GDP統計年元': '2012',
        '確立年月日2': '[[1707年]]',
        '通貨': '[[スターリング・ポンド|UKポンド]] (&pound;)',
        '確立年月日1': '[[927年]]／[[843年]]',
        '国章リンク': '（[[イギリスの国章|国章]]）',
        'GDP値MER': '2兆4337億<ref name="imf-statistics-gdp" />',
        '首相等肩書': '[[イギリスの首相|首相]]',
        '夏時間': '+1',
        '人口順位': '22',
        '時間帯': '±0',
        'GDP値元': '1兆5478億<ref name="imf-statistics-gdp">[http://www.imf.org/external/pubs/ft/weo/2012/02/weodata/weorept.aspx?pr.x=70&pr.y=13&sy=2010&ey=2012&scsm=1&ssd=1&sort=country&ds=.&br=1&c=112&s=NGDP%2CNGDPD%2CPPPGDP%2CPPPPC&grp=0&a= IMF>Data and Statistics>World Economic Outlook Databases>By Countrise>United Kingdom]</ref>',
        '略名': 'イギリス',
        '確立年月日4': '[[1927年]]',
        '面積順位': '76',
        '元首等肩書': '[[イギリスの君主|女王]]',
        'GDP統計年': '2012',
        '面積大きさ': '1 E11',
        '確立形態3': '[[グレートブリテン及びアイルランド連合王国]]建国<br />（[[連合法 (1800年)|1800年連合法]]）',
        '注記': '<references />',
        '国章画像': '[[ファイル:Royal Coat of Arms of the United Kingdom.svg|85px|イギリスの国章]]',
        '元首等氏名': '[[エリザベス2世]]',
        '通貨コード': 'GBP',
        'ccTLD': '[[.uk]] / [[.gb]]<ref>使用は.ukに比べ圧倒的少数。</ref>',
        '位置画像': 'Location_UK_EU_Europe_001.svg',
        '人口密度値': '246',
        '国歌': '[[女王陛下万歳|神よ女王陛下を守り給え]]',
        '人口大きさ': '1 E7',
        '標語': '{{lang|fr|Dieu et mon droit}}<br/>（[[フランス語]]:神と私の権利）',
        'GDP統計年MER': '2012',
        'GDP順位MER': '5',
        '確立形態2': '[[グレートブリテン王国]]建国<br />（[[連合法 (1707年)|1707年連合法]]）',
        '国旗画像': 'Flag of the United Kingdom.svg',
        'GDP値': '2兆3162億<ref name="imf-statistics-gdp" />',
        '首相等氏名': '[[デーヴィッド・キャメロン]]',
        '日本語国名': 'グレートブリテン及び北アイルランド連合王国',
        '確立年月日3': '[[1801年]]', '人口統計年': '2011',
        '確立形態1': '[[イングランド王国]]／[[スコットランド王国]]<br />（両国とも[[連合法 (1707年)|1707年連合法]]まで）',
        '最大都市': 'ロンドン',
        '水面積率': '1.3%',
        '人口値': '63,181,775<ref>[http://esa.un.org/unpd/wpp/Excel-Data/population.htm United Nations Department of Economic and Social Affairs>Population Division>Data>Population>Total Population]</ref>',
        '公用語': '[[英語]]（事実上）',
        '確立形態4': "現在の国号「'''グレートブリテン及び北アイルランド連合王国'''」に変更",
        'GDP順位': '6',
        '面積値': '244,820',
        'GDP/人': '36,727<ref name="imf-statistics-gdp" />',
        '公式国名': '{{lang|en|United Kingdom of Great Britain and Northern Ireland}}<ref>英語以外での正式国名:<br/>',
        '首都': '[[ロンドン]]',
        'ISO 3166-1': 'GB / GBR',
        '建国形態': '建国',
        '国際電話番号': '44'
    }
    ans = nlp100.solve_25()
    for entry in right:
        assert entry in ans
        assert ans[entry] == right[entry]


def test_26():
    ans = nlp100.solve_26()
    entry = '確立形態4'
    assert ans[entry] == "現在の国号「グレートブリテン及び北アイルランド連合王国」に変更"


def test_27():
    ans = nlp100.solve_26()
    entry = '確立形態4'
    assert ans[entry] == "現在の国号「グレートブリテン及び北アイルランド連合王国」に変更"


def test_27():
    right = {
        'GDP/人': '36,727<ref name="imf-statistics-gdp" />',
        'GDP値': '2兆3162億<ref name="imf-statistics-gdp" />',
        'GDP値MER': '2兆4337億<ref name="imf-statistics-gdp" />',
        'GDP値元': '1兆5478億<ref '
        'name="imf-statistics-gdp">[http://www.imf.org/external/pubs/ft/weo/2012/02/weodata/weorept.aspx?pr.x=70&pr.y=13&sy=2010&ey=2012&scsm=1&ssd=1&sort=country&ds=.&br=1&c=112&s=NGDP%2CNGDPD%2CPPPGDP%2CPPPPC&grp=0&a= '
        'IMF>Data and Statistics>World Economic Outlook Databases>By '
        'Countrise>United Kingdom]</ref>',
        'GDP統計年': '2012',
        'GDP統計年MER': '2012',
        'GDP統計年元': '2012',
        'GDP順位': '6',
        'GDP順位MER': '5',
        'ISO 3166-1': 'GB / GBR',
        'ccTLD': '.uk / .gb<ref>使用は.ukに比べ圧倒的少数。</ref>',
        '人口値': '63,181,775<ref>[http://esa.un.org/unpd/wpp/Excel-Data/population.htm '
        'United Nations Department of Economic and Social Affairs>Population '
        'Division>Data>Population>Total Population]</ref>',
        '人口大きさ': '1 E7',
        '人口密度値': '246',
        '人口統計年': '2011',
        '人口順位': '22',
        '位置画像': 'Location_UK_EU_Europe_001.svg',
        '元首等氏名': 'エリザベス2世',
        '元首等肩書': 'イギリスの君主',
        '公式国名': '{{lang|en|United Kingdom of Great Britain and Northern '
                           'Ireland}}<ref>英語以外での正式国名:<br/>',
        '公用語': '英語（事実上）',
        '国旗画像': 'Flag of the United Kingdom.svg',
        '国歌': '女王陛下万歳',
        '国章リンク': '（イギリスの国章）',
        '国章画像': '[[ファイル:Royal Coat of Arms of the United Kingdom.svg|85px|イギリスの国章]]',
        '国際電話番号': '44',
        '夏時間': '+1',
        '建国形態': '建国',
        '日本語国名': 'グレートブリテン及び北アイルランド連合王国',
        '時間帯': '±0',
        '最大都市': 'ロンドン',
        '標語': '{{lang|fr|Dieu et mon droit}}<br/>（フランス語:神と私の権利）',
        '水面積率': '1.3%',
        '注記': '<references />',
        '略名': 'イギリス',
        '確立年月日1': '927年／843年',
        '確立年月日2': '1707年',
        '確立年月日3': '1801年',
        '確立年月日4': '1927年',
        '確立形態1': 'イングランド王国／スコットランド王国<br />（両国とも連合法 (1707年)まで）',
        '確立形態2': 'グレートブリテン王国建国<br />（連合法 (1707年)）',
        '確立形態3': 'グレートブリテン及びアイルランド連合王国建国<br />（連合法 (1800年)）',
        '確立形態4': '現在の国号「グレートブリテン及び北アイルランド連合王国」に変更',
        '通貨': 'スターリング・ポンド (&pound;)',
        '通貨コード': 'GBP',
        '面積値': '244,820',
        '面積大きさ': '1 E11',
        '面積順位': '76',
        '首相等氏名': 'デーヴィッド・キャメロン',
        '首相等肩書': 'イギリスの首相',
        '首都': 'ロンドン'
    }

    ans = nlp100.solve_27()
    for entry in right:
        assert entry in ans
        assert ans[entry] == right[entry]

def test_28():
    right = {
        'GDP/人': '36,727',
        'GDP値': '2兆3162億',
        'GDP値MER': '2兆4337億',
        'GDP値元': '1兆5478億',
        'GDP統計年': '2012',
        'GDP統計年MER': '2012',
        'GDP統計年元': '2012',
        'GDP順位': '6',
        'GDP順位MER': '5',
        'ISO 3166-1': 'GB / GBR',
        'ccTLD': '.uk / .gb',
        '人口値': '63,181,775',
        '人口大きさ': '1 E7',
        '人口密度値': '246',
        '人口統計年': '2011',
        '人口順位': '22',
        '位置画像': 'Location_UK_EU_Europe_001.svg',
        '元首等氏名': 'エリザベス2世',
        '元首等肩書': 'イギリスの君主',
        '公式国名': '英語以外での正式国名:',
        '公用語': '英語（事実上）',
        '国旗画像': 'Flag of the United Kingdom.svg',
        '国歌': '女王陛下万歳',
        '国章リンク': '（イギリスの国章）',
        '国章画像': '',
        '国際電話番号': '44',
        '夏時間': '+1',
        '建国形態': '建国',
        '日本語国名': 'グレートブリテン及び北アイルランド連合王国',
        '時間帯': '±0',
        '最大都市': 'ロンドン',
        '標語': '（フランス語:神と私の権利）',
        '水面積率': '1.3%',
        '注記': '',
        '略名': 'イギリス',
        '確立年月日1': '927年／843年',
        '確立年月日2': '1707年',
        '確立年月日3': '1801年',
        '確立年月日4': '1927年',
        '確立形態1': 'イングランド王国／スコットランド王国（両国とも連合法 (1707年)まで）',
        '確立形態2': 'グレートブリテン王国建国（連合法 (1707年)）',
        '確立形態3': 'グレートブリテン及びアイルランド連合王国建国（連合法 (1800年)）',
        '確立形態4': '現在の国号「グレートブリテン及び北アイルランド連合王国」に変更',
        '通貨': 'スターリング・ポンド (&pound;)',
        '通貨コード': 'GBP',
        '面積値': '244,820',
        '面積大きさ': '1 E11',
        '面積順位': '76',
        '首相等氏名': 'デーヴィッド・キャメロン',
        '首相等肩書': 'イギリスの首相',
        '首都': 'ロンドン'
    }

    ans = nlp100.solve_28()
    for entry in right:
        assert entry in ans
        assert ans[entry] == right[entry]


def test_29():
    url = nlp100.solve_29()
    return url == 'https://ja.wikipedia.org/wiki/ファイル名:Flag_of_the_United_Kingdom.svg'
