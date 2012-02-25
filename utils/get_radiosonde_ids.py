import re

regex = re.compile(".+s\('([0-9]+)")

list = """<AREA COORDS="223,24,5" SHAPE="CIRCLE" HREF="javascript:g('01241')" onMouseOver="return s('01241  Orland (ENOL)')">
<AREA COORDS="178,99,5" SHAPE="CIRCLE" HREF="javascript:g('01400')" onMouseOver="return s('01400  Ekofisk')">
<AREA COORDS="197,75,5" SHAPE="CIRCLE" HREF="javascript:g('01415')" onMouseOver="return s('01415  Stavanger/Sola (ENZV)')">
<AREA COORDS="262,36,5" SHAPE="CIRCLE" HREF="javascript:g('02365')" onMouseOver="return s('02365  Sundsvall-Harnosand Fpl')">
<AREA COORDS="271,90,5" SHAPE="CIRCLE" HREF="javascript:g('02591')" onMouseOver="return s('02591  Visby Aerologiska Stn (ESQV)')">
<AREA COORDS="295,51,5" SHAPE="CIRCLE" HREF="javascript:g('02963')" onMouseOver="return s('02963  Jokioinen')">
<AREA COORDS="161,54,5" SHAPE="CIRCLE" HREF="javascript:g('03005')" onMouseOver="return s('03005  Lerwick')">
<AREA COORDS="132,151,5" SHAPE="CIRCLE" HREF="javascript:g('03743')" onMouseOver="return s('03743  Larkhill')">
<AREA COORDS="104,155,5" SHAPE="CIRCLE" HREF="javascript:g('03808')" onMouseOver="return s('03808  Camborne')">
<AREA COORDS="77,123,5" SHAPE="CIRCLE" HREF="javascript:g('03953')" onMouseOver="return s('03953  Valentia Observatory')">
<AREA COORDS="139,25,5" SHAPE="CIRCLE" HREF="javascript:g('06011')" onMouseOver="return s('06011  Torshavn')">
<AREA COORDS="183,151,5" SHAPE="CIRCLE" HREF="javascript:g('06260')" onMouseOver="return s('06260  De Bilt (EHDB)')">
<AREA COORDS="189,214,5" SHAPE="CIRCLE" HREF="javascript:g('06610')" onMouseOver="return s('06610  Payerne (LSMP)')">
<AREA COORDS="104,177,5" SHAPE="CIRCLE" HREF="javascript:g('07110')" onMouseOver="return s('07110  Brest (LFRB)')">
<AREA COORDS="154,186,5" SHAPE="CIRCLE" HREF="javascript:g('07145')" onMouseOver="return s('07145  Trappes')">
<AREA COORDS="122,227,5" SHAPE="CIRCLE" HREF="javascript:g('07510')" onMouseOver="return s('07510  Bordeaux Merignac (LFBD)')">
<AREA COORDS="163,247,5" SHAPE="CIRCLE" HREF="javascript:g('07645')" onMouseOver="return s('07645  Nimes-Courbessac (LFME)')">
<AREA COORDS="200,276,5" SHAPE="CIRCLE" HREF="javascript:g('07761')" onMouseOver="return s('07761  Ajaccio (LFKJ)')">
<AREA COORDS="52,224,5" SHAPE="CIRCLE" HREF="javascript:g('08001')" onMouseOver="return s('08001  La Coruna')">
<AREA COORDS="91,236,5" SHAPE="CIRCLE" HREF="javascript:g('08023')" onMouseOver="return s('08023  Santander')">
<AREA COORDS="110,264,5" SHAPE="CIRCLE" HREF="javascript:g('08160')" onMouseOver="return s('08160  Zaragoza/Aeropuerto (LEZG)')">
<AREA COORDS="139,271,5" SHAPE="CIRCLE" HREF="javascript:g('08190')" onMouseOver="return s('08190  Barcelona')">
<AREA COORDS="82,272,5" SHAPE="CIRCLE" HREF="javascript:g('08221')" onMouseOver="return s('08221  Madrid/Barajas (LEMD)')">
<AREA COORDS="139,297,5" SHAPE="CIRCLE" HREF="javascript:g('08302')" onMouseOver="return s('08302  Palma De Mallorca')">
<AREA COORDS="97,309,5" SHAPE="CIRCLE" HREF="javascript:g('08430')" onMouseOver="return s('08430  Murcia')">
<AREA COORDS="49,320,5" SHAPE="CIRCLE" HREF="javascript:g('08495')" onMouseOver="return s('08495  Gibraltar (LXGB)')">
<AREA COORDS="24,275,5" SHAPE="CIRCLE" HREF="javascript:g('08579')" onMouseOver="return s('08579  Lisboa/Gago Coutinho')">
<AREA COORDS="216,126,5" SHAPE="CIRCLE" HREF="javascript:g('10035')" onMouseOver="return s('10035  Schleswig')">
<AREA COORDS="199,134,5" SHAPE="CIRCLE" HREF="javascript:g('10113')" onMouseOver="return s('10113  Norderney')">
<AREA COORDS="242,132,5" SHAPE="CIRCLE" HREF="javascript:g('10184')" onMouseOver="return s('10184  Greifswald')">
<AREA COORDS="218,146,5" SHAPE="CIRCLE" HREF="javascript:g('10238')" onMouseOver="return s('10238  Bergen (ETGB)')">
<AREA COORDS="247,153,5" SHAPE="CIRCLE" HREF="javascript:g('10393')" onMouseOver="return s('10393  Lindenberg')">
<AREA COORDS="195,160,5" SHAPE="CIRCLE" HREF="javascript:g('10410')" onMouseOver="return s('10410  Essen (EDZE)')">
<AREA COORDS="219,172,5" SHAPE="CIRCLE" HREF="javascript:g('10548')" onMouseOver="return s('10548  Meiningen')">
<AREA COORDS="196,181,5" SHAPE="CIRCLE" HREF="javascript:g('10618')" onMouseOver="return s('10618  Idar-Oberstein (ETGI)')">
<AREA COORDS="209,192,5" SHAPE="CIRCLE" HREF="javascript:g('10739')" onMouseOver="return s('10739  Stuttgart/Schnarrenberg')">
<AREA COORDS="231,186,5" SHAPE="CIRCLE" HREF="javascript:g('10771')" onMouseOver="return s('10771  Kuemmersbruck (ETGK)')">
<AREA COORDS="228,200,5" SHAPE="CIRCLE" HREF="javascript:g('10868')" onMouseOver="return s('10868  Muenchen-Oberschlssheim')">
<AREA COORDS="266,199,5" SHAPE="CIRCLE" HREF="javascript:g('11035')" onMouseOver="return s('11035  Wien/Hohe Warte')">
<AREA COORDS="250,179,5" SHAPE="CIRCLE" HREF="javascript:g('11520')" onMouseOver="return s('11520  Praha-Libus')">
<AREA COORDS="271,185,5" SHAPE="CIRCLE" HREF="javascript:g('11747')" onMouseOver="return s('11747  Prostejov')">
<AREA COORDS="296,187,5" SHAPE="CIRCLE" HREF="javascript:g('11952')" onMouseOver="return s('11952  Poprad-Ganovce')">
<AREA COORDS="269,123,5" SHAPE="CIRCLE" HREF="javascript:g('12120')" onMouseOver="return s('12120  Leba')">
<AREA COORDS="295,147,5" SHAPE="CIRCLE" HREF="javascript:g('12374')" onMouseOver="return s('12374  Legionowo')">
<AREA COORDS="267,157,5" SHAPE="CIRCLE" HREF="javascript:g('12425')" onMouseOver="return s('12425  Wroclaw I')">
<AREA COORDS="303,238,5" SHAPE="CIRCLE" HREF="javascript:g('13275')" onMouseOver="return s('13275  Beograd/Kosutnjak')">
<AREA COORDS="265,229,5" SHAPE="CIRCLE" HREF="javascript:g('14240')" onMouseOver="return s('14240  Zagreb/Maksimir (LDDD)')">
<AREA COORDS="260,250,5" SHAPE="CIRCLE" HREF="javascript:g('14430')" onMouseOver="return s('14430  Zadar')">
<AREA COORDS="352,232,5" SHAPE="CIRCLE" HREF="javascript:g('15420')" onMouseOver="return s('15420  Bucuresti Inmh-Banesa (LRBS)')">
<AREA COORDS="333,259,5" SHAPE="CIRCLE" HREF="javascript:g('15614')" onMouseOver="return s('15614  Sofia (Observ) (LBSF)')">
<AREA COORDS="241,227,5" SHAPE="CIRCLE" HREF="javascript:g('16044')" onMouseOver="return s('16044  Udine/Campoformido (LIPD)')">
<AREA COORDS="207,233,5" SHAPE="CIRCLE" HREF="javascript:g('16080')" onMouseOver="return s('16080  Milano/Linate (LIML)')">
<AREA COORDS="192,243,5" SHAPE="CIRCLE" HREF="javascript:g('16113')" onMouseOver="return s('16113  Cuneo-Levaldigi')">
<AREA COORDS="234,280,5" SHAPE="CIRCLE" HREF="javascript:g('16245')" onMouseOver="return s('16245  Pratica Di Mare (LIRE)')">
<AREA COORDS="286,291,5" SHAPE="CIRCLE" HREF="javascript:g('16320')" onMouseOver="return s('16320  Brindisi (LIBR)')">
<AREA COORDS="234,328,5" SHAPE="CIRCLE" HREF="javascript:g('16429')" onMouseOver="return s('16429  Trapani/Birgi (LICT)')">
<AREA COORDS="200,309,5" SHAPE="CIRCLE" HREF="javascript:g('16560')" onMouseOver="return s('16560  Cagliari/Elmas (LIEE)')">
<AREA COORDS="347,318,5" SHAPE="CIRCLE" HREF="javascript:g('16716')" onMouseOver="return s('16716  Athinai (Airport) (LGAT)')">
<AREA COORDS="452,241,5" SHAPE="CIRCLE" HREF="javascript:g('17030')" onMouseOver="return s('17030  Samsun')">
<AREA COORDS="389,268,5" SHAPE="CIRCLE" HREF="javascript:g('17062')" onMouseOver="return s('17062  Istanbul/Goztepe')">
<AREA COORDS="428,269,5" SHAPE="CIRCLE" HREF="javascript:g('17130')" onMouseOver="return s('17130  Ankara/Central')">
<AREA COORDS="380,304,5" SHAPE="CIRCLE" HREF="javascript:g('17220')" onMouseOver="return s('17220  Izmir/Guzelyali')">
<AREA COORDS="415,303,5" SHAPE="CIRCLE" HREF="javascript:g('17240')" onMouseOver="return s('17240  Isparta (LTBM)')">
<AREA COORDS="465,295,5" SHAPE="CIRCLE" HREF="javascript:g('17351')" onMouseOver="return s('17351  Adana/Bolge')">
<AREA COORDS="447,334,5" SHAPE="CIRCLE" HREF="javascript:g('17600')" onMouseOver="return s('17600  Paphos Airport (LCPH)')">
<AREA COORDS="454,325,5" SHAPE="CIRCLE" HREF="javascript:g('17607')" onMouseOver="return s('17607  Athalassa (LCNC)')">
<AREA COORDS="458,327,5" SHAPE="CIRCLE" HREF="javascript:g('17609')" onMouseOver="return s('17609  Larnaca Airport (LCLK)')">
<AREA COORDS="347,25,5" SHAPE="CIRCLE" HREF="javascript:g('22820')" onMouseOver="return s('22820  Petrozavodsk, LE')">
<AREA COORDS="371,18,5" SHAPE="CIRCLE" HREF="javascript:g('22845')" onMouseOver="return s('22845  Kargopol, AR')">
<AREA COORDS="336,50,5" SHAPE="CIRCLE" HREF="javascript:g('26063')" onMouseOver="return s('26063  St.Petersburg(Voejkovo), LE (ULLI)')">
<AREA COORDS="362,66,5" SHAPE="CIRCLE" HREF="javascript:g('26298')" onMouseOver="return s('26298  Bologoe, LE')">
<AREA COORDS="348,89,5" SHAPE="CIRCLE" HREF="javascript:g('26477')" onMouseOver="return s('26477  Velikie Luki, LE (ULOL)')">
<AREA COORDS="362,103,5" SHAPE="CIRCLE" HREF="javascript:g('26781')" onMouseOver="return s('26781  Smolensk, MI')">
<AREA COORDS="439,14,5" SHAPE="CIRCLE" HREF="javascript:g('27199')" onMouseOver="return s('27199  Kirov, MS')">
<AREA COORDS="425,55,5" SHAPE="CIRCLE" HREF="javascript:g('27459')" onMouseOver="return s('27459  Niznij Novgorod, MS')">
<AREA COORDS="457,43,5" SHAPE="CIRCLE" HREF="javascript:g('27595')" onMouseOver="return s('27595  Kazan, MS')">
<AREA COORDS="386,103,5" SHAPE="CIRCLE" HREF="javascript:g('27707')" onMouseOver="return s('27707  Suhinici, MS')">
<AREA COORDS="410,85,5" SHAPE="CIRCLE" HREF="javascript:g('27730')" onMouseOver="return s('27730  Rjazan, MS')">
<AREA COORDS="449,83,5" SHAPE="CIRCLE" HREF="javascript:g('27962')" onMouseOver="return s('27962  Penza, MS (UWPP)')">
<AREA COORDS="476,67,5" SHAPE="CIRCLE" HREF="javascript:g('27995')" onMouseOver="return s('27995  Samara (Bezencuk), MS')">
<AREA COORDS="364,131,5" SHAPE="CIRCLE" HREF="javascript:g('33041')" onMouseOver="return s('33041  Gomel, MI')">
<AREA COORDS="368,155,5" SHAPE="CIRCLE" HREF="javascript:g('33345')" onMouseOver="return s('33345  Kyiv, KI (UKKK)')">
<AREA COORDS="397,174,5" SHAPE="CIRCLE" HREF="javascript:g('33791')" onMouseOver="return s('33791  Kryvyi Rih, KI')">
<AREA COORDS="401,125,5" SHAPE="CIRCLE" HREF="javascript:g('34009')" onMouseOver="return s('34009  Kursk, MS')">
<AREA COORDS="422,117,5" SHAPE="CIRCLE" HREF="javascript:g('34122')" onMouseOver="return s('34122  Voronez, MS (UUOO)')">
<AREA COORDS="465,94,5" SHAPE="CIRCLE" HREF="javascript:g('34172')" onMouseOver="return s('34172  Saratov, MS')">
<AREA COORDS="440,124,5" SHAPE="CIRCLE" HREF="javascript:g('34247')" onMouseOver="return s('34247  Kalac, MS')">
<AREA COORDS="472,128,5" SHAPE="CIRCLE" HREF="javascript:g('34560')" onMouseOver="return s('34560  Volgograd, TB (URWW)')">
<AREA COORDS="449,162,5" SHAPE="CIRCLE" HREF="javascript:g('34731')" onMouseOver="return s('34731  Rostov-Na-Donu, TB (URRR)')">
<AREA COORDS="460,199,5" SHAPE="CIRCLE" HREF="javascript:g('37018')" onMouseOver="return s('37018  Tuapse, TB')">
<AREA COORDS="137,335,5" SHAPE="CIRCLE" HREF="javascript:g('60390')" onMouseOver="return s('60390  Dar-El-Beida (DAAG)')">
<AREA COORDS="210,341,5" SHAPE="CIRCLE" HREF="javascript:g('60715')" onMouseOver="return s('60715  Tunis-Carthage (DTTA)')">
<AREA COORDS="568,3,5" SHAPE="CIRCLE" HREF="javascript:g('03953')" onMouseOver="return s('03953  Valentia Observatory')">
<AREA COORDS="414,27,5" SHAPE="CIRCLE" HREF="javascript:g('04220')" onMouseOver="return s('04220  Aasiaat (Egedesminde) (BGEM)')">
<AREA COORDS="457,53,5" SHAPE="CIRCLE" HREF="javascript:g('04270')" onMouseOver="return s('04270  Narsarsuaq (BGBW)')">
<AREA COORDS="456,19,5" SHAPE="CIRCLE" HREF="javascript:g('04360')" onMouseOver="return s('04360  Tasiilaq (Ammassalik) (BGAM)')">
<AREA COORDS="591,97,5" SHAPE="CIRCLE" HREF="javascript:g('08508')" onMouseOver="return s('08508  Lajes/Santa Rita')">
<AREA COORDS="195,14,5" SHAPE="CIRCLE" HREF="javascript:g('70026')" onMouseOver="return s('70026  Barrow/W. Post W.Rogers, AK (PABR)')">
<AREA COORDS="168,29,5" SHAPE="CIRCLE" HREF="javascript:g('70133')" onMouseOver="return s('70133  Kotzebue, Ralph Wien, AK (PAOT)')">
<AREA COORDS="153,36,5" SHAPE="CIRCLE" HREF="javascript:g('70200')" onMouseOver="return s('70200  Nome, AK (PAOM)')">
<AREA COORDS="147,60,5" SHAPE="CIRCLE" HREF="javascript:g('70219')" onMouseOver="return s('70219  Bethel/Bethel Airport, AK (PABE)')">
<AREA COORDS="169,59,5" SHAPE="CIRCLE" HREF="javascript:g('70231')" onMouseOver="return s('70231  Mcgrath, AK (PAMC)')">
<AREA COORDS="192,60,5" SHAPE="CIRCLE" HREF="javascript:g('70261')" onMouseOver="return s('70261  Fairbanks/Int, AK (PAFA)')">
<AREA COORDS="177,77,5" SHAPE="CIRCLE" HREF="javascript:g('70273')" onMouseOver="return s('70273  Anchorage/Int, AK (PANC)')">
<AREA COORDS="114,60,5" SHAPE="CIRCLE" HREF="javascript:g('70308')" onMouseOver="return s('70308  St. Paul, AK (PASN)')">
<AREA COORDS="125,84,5" SHAPE="CIRCLE" HREF="javascript:g('70316')" onMouseOver="return s('70316  Cold Bay, AK (PACD)')">
<AREA COORDS="152,79,5" SHAPE="CIRCLE" HREF="javascript:g('70326')" onMouseOver="return s('70326  King Salmon, AK (PAKN)')">
<AREA COORDS="160,90,5" SHAPE="CIRCLE" HREF="javascript:g('70350')" onMouseOver="return s('70350  Kodiak, AK (PADQ)')">
<AREA COORDS="200,98,5" SHAPE="CIRCLE" HREF="javascript:g('70361')" onMouseOver="return s('70361  Yakutat, AK (PAYA)')">
<AREA COORDS="215,131,5" SHAPE="CIRCLE" HREF="javascript:g('70398')" onMouseOver="return s('70398  Annette Island, AK (PANT)')">
<AREA COORDS="244,77,5" SHAPE="CIRCLE" HREF="javascript:g('71043')" onMouseOver="return s('71043  Norman Wells Ua, NT (YVQ)')">
<AREA COORDS="354,54,5" SHAPE="CIRCLE" HREF="javascript:g('71081')" onMouseOver="return s('71081  Hall Beach, NT (YUX)')">
<AREA COORDS="222,158,5" SHAPE="CIRCLE" HREF="javascript:g('71109')" onMouseOver="return s('71109  Port Hardy, BC (YZT)')">
<AREA COORDS="269,151,5" SHAPE="CIRCLE" HREF="javascript:g('71119')" onMouseOver="return s('71119  Edmonton Stony Plain, AB (WSE)')">
<AREA COORDS="248,168,5" SHAPE="CIRCLE" HREF="javascript:g('71203')" onMouseOver="return s('71203  Kelowna Apt, BC (WLW)')">
<AREA COORDS="470,161,5" SHAPE="CIRCLE" HREF="javascript:g('71600')" onMouseOver="return s('71600  Sable Island, NS (WSA)')">
<AREA COORDS="449,173,5" SHAPE="CIRCLE" HREF="javascript:g('71603')" onMouseOver="return s('71603  Yarmouth, NS (YQI)')">
<AREA COORDS="408,174,5" SHAPE="CIRCLE" HREF="javascript:g('71722')" onMouseOver="return s('71722  Maniwaki, QB (WMW)')">
<AREA COORDS="483,130,5" SHAPE="CIRCLE" HREF="javascript:g('71802')" onMouseOver="return s('71802  Mt Pearl, NF (AYT)')">
<AREA COORDS="433,141,5" SHAPE="CIRCLE" HREF="javascript:g('71811')" onMouseOver="return s('71811  Sept-Iles, QB (YZV)')">
<AREA COORDS="462,137,5" SHAPE="CIRCLE" HREF="javascript:g('71815')" onMouseOver="return s('71815  Stephenville, NF (YJT)')">
<AREA COORDS="444,117,5" SHAPE="CIRCLE" HREF="javascript:g('71816')" onMouseOver="return s('71816  Goose Bay, NF (YYR)')">
<AREA COORDS="402,133,5" SHAPE="CIRCLE" HREF="javascript:g('71823')" onMouseOver="return s('71823  La Grande Iv, QB (YAH)')">
<AREA COORDS="384,153,5" SHAPE="CIRCLE" HREF="javascript:g('71836')" onMouseOver="return s('71836  Moosonee, ON (YMO)')">
<AREA COORDS="351,160,5" SHAPE="CIRCLE" HREF="javascript:g('71845')" onMouseOver="return s('71845  Pickle Lake, ON (WPL)')">
<AREA COORDS="313,150,5" SHAPE="CIRCLE" HREF="javascript:g('71867')" onMouseOver="return s('71867  The Pas, MB (YQD)')">
<AREA COORDS="408,104,5" SHAPE="CIRCLE" HREF="javascript:g('71906')" onMouseOver="return s('71906  Kuujjuaq, QB (YVP)')">
<AREA COORDS="380,112,5" SHAPE="CIRCLE" HREF="javascript:g('71907')" onMouseOver="return s('71907  Inukjuak, QB (WPH)')">
<AREA COORDS="241,144,5" SHAPE="CIRCLE" HREF="javascript:g('71908')" onMouseOver="return s('71908  Prince George, PE (ZXS)')">
<AREA COORDS="395,73,5" SHAPE="CIRCLE" HREF="javascript:g('71909')" onMouseOver="return s('71909  Iqaluit, NT (YFB)')">
<AREA COORDS="333,121,5" SHAPE="CIRCLE" HREF="javascript:g('71913')" onMouseOver="return s('71913  Churchill, MB (YYQ)')">
<AREA COORDS="356,83,5" SHAPE="CIRCLE" HREF="javascript:g('71915')" onMouseOver="return s('71915  Coral Harbour, NT (YZS)')">
<AREA COORDS="318,21,5" SHAPE="CIRCLE" HREF="javascript:g('71924')" onMouseOver="return s('71924  Resolute, NT (YRB)')">
<AREA COORDS="300,59,5" SHAPE="CIRCLE" HREF="javascript:g('71925')" onMouseOver="return s('71925  Cambridge Bay, NT (YCB)')">
<AREA COORDS="323,88,5" SHAPE="CIRCLE" HREF="javascript:g('71926')" onMouseOver="return s('71926  Baker Lake, NT (YBK)')">
<AREA COORDS="279,114,5" SHAPE="CIRCLE" HREF="javascript:g('71934')" onMouseOver="return s('71934  Fort Smith, NT (YSM)')">
<AREA COORDS="247,117,5" SHAPE="CIRCLE" HREF="javascript:g('71945')" onMouseOver="return s('71945  Fort Nelson, BC (YYE)')">
<AREA COORDS="234,54,5" SHAPE="CIRCLE" HREF="javascript:g('71957')" onMouseOver="return s('71957  Inuvik, NT (YEV)')">
<AREA COORDS="215,97,5" SHAPE="CIRCLE" HREF="javascript:g('71964')" onMouseOver="return s('71964  Whitehorse, YT (YXY)')">
<AREA COORDS="418,297,5" SHAPE="CIRCLE" HREF="javascript:g('72201')" onMouseOver="return s('72201  Key West/Int, FL (EYW)')">
<AREA COORDS="423,289,5" SHAPE="CIRCLE" HREF="javascript:g('72202')" onMouseOver="return s('72202  Miami, FL (MFL)')">
<AREA COORDS="410,265,5" SHAPE="CIRCLE" HREF="javascript:g('72206')" onMouseOver="return s('72206  Jacksonville Intl, FL (JAX)')">
<AREA COORDS="414,250,5" SHAPE="CIRCLE" HREF="javascript:g('72208')" onMouseOver="return s('72208  Charleston/Muni, SC (CHS)')">
<AREA COORDS="411,281,5" SHAPE="CIRCLE" HREF="javascript:g('72210')" onMouseOver="return s('72210  Tampa Bay Area, FL (TBW)')">
<AREA COORDS="398,268,5" SHAPE="CIRCLE" HREF="javascript:g('72214')" onMouseOver="return s('72214  Tallahassee Fsu, FL (TLH)')">
<AREA COORDS="393,253,5" SHAPE="CIRCLE" HREF="javascript:g('72215')" onMouseOver="return s('72215  Peachtree City, GA (FFC)')">
<AREA COORDS="383,256,5" SHAPE="CIRCLE" HREF="javascript:g('72230')" onMouseOver="return s('72230  Shelby County Airport, AL (BMX)')">
<AREA COORDS="372,274,5" SHAPE="CIRCLE" HREF="javascript:g('72233')" onMouseOver="return s('72233  Slidell Muni, LA (LIX)')">
<AREA COORDS="369,264,5" SHAPE="CIRCLE" HREF="javascript:g('72235')" onMouseOver="return s('72235  Jackson Thompson Fld, MS (JAN)')">
<AREA COORDS="356,278,5" SHAPE="CIRCLE" HREF="javascript:g('72240')" onMouseOver="return s('72240  Lake Charles/Muni, LA (LCH)')">
<AREA COORDS="352,265,5" SHAPE="CIRCLE" HREF="javascript:g('72248')" onMouseOver="return s('72248  Shreveport Reg, LA (SHV)')">
<AREA COORDS="335,265,5" SHAPE="CIRCLE" HREF="javascript:g('72249')" onMouseOver="return s('72249  Ft Worth, TX (FWD)')">
<AREA COORDS="338,303,5" SHAPE="CIRCLE" HREF="javascript:g('72250')" onMouseOver="return s('72250  Brownsville Intl, TX (BRO)')">
<AREA COORDS="337,293,5" SHAPE="CIRCLE" HREF="javascript:g('72251')" onMouseOver="return s('72251  Corpus Christi Intl, TX (CRP)')">
<AREA COORDS="320,285,5" SHAPE="CIRCLE" HREF="javascript:g('72261')" onMouseOver="return s('72261  Del Rio/Int, TX (DRT)')">
<AREA COORDS="313,271,5" SHAPE="CIRCLE" HREF="javascript:g('72265')" onMouseOver="return s('72265  Midland/Midland Reg, TX (MAF)')">
<AREA COORDS="272,269,5" SHAPE="CIRCLE" HREF="javascript:g('72274')" onMouseOver="return s('72274  Tucson, AZ (TUS)')">
<AREA COORDS="244,263,5" SHAPE="CIRCLE" HREF="javascript:g('72293')" onMouseOver="return s('72293  San Diego/Miramar, CA (NKX)')">
<AREA COORDS="425,236,5" SHAPE="CIRCLE" HREF="javascript:g('72305')" onMouseOver="return s('72305  Newport, NC (MHX)')">
<AREA COORDS="409,233,5" SHAPE="CIRCLE" HREF="javascript:g('72317')" onMouseOver="return s('72317  Greensboro/High Pt, NC (GSO)')">
<AREA COORDS="406,228,5" SHAPE="CIRCLE" HREF="javascript:g('72318')" onMouseOver="return s('72318  Blacksburg, VA (RNK)')">
<AREA COORDS="381,239,5" SHAPE="CIRCLE" HREF="javascript:g('72327')" onMouseOver="return s('72327  Nashville, TN (BNA)')">
<AREA COORDS="357,251,5" SHAPE="CIRCLE" HREF="javascript:g('72340')" onMouseOver="return s('72340  North Little Rock, AR (LZK)')">
<AREA COORDS="334,252,5" SHAPE="CIRCLE" HREF="javascript:g('72357')" onMouseOver="return s('72357  Norman/Westheimer, OK (OUN)')">
<AREA COORDS="315,253,5" SHAPE="CIRCLE" HREF="javascript:g('72363')" onMouseOver="return s('72363  Amarillo Arpt(Awos), TX (AMA)')">
<AREA COORDS="292,272,5" SHAPE="CIRCLE" HREF="javascript:g('72364')" onMouseOver="return s('72364  Santa Teresa, NM (EPZ)')">
<AREA COORDS="292,254,5" SHAPE="CIRCLE" HREF="javascript:g('72365')" onMouseOver="return s('72365  Albuquerque/Int, NM (ABQ)')">
<AREA COORDS="269,252,5" SHAPE="CIRCLE" HREF="javascript:g('72376')" onMouseOver="return s('72376  Flagstaff, AZ (FGZ)')">
<AREA COORDS="242,251,5" SHAPE="CIRCLE" HREF="javascript:g('72381')" onMouseOver="return s('72381  Edwards Afb, CA (EDW)')">
<AREA COORDS="255,246,5" SHAPE="CIRCLE" HREF="javascript:g('72388')" onMouseOver="return s('72388  Las Vegas, NV (VEF)')">
<AREA COORDS="230,250,5" SHAPE="CIRCLE" HREF="javascript:g('72393')" onMouseOver="return s('72393  Vandenberg Afb, Vandenberg Afb, CA (VBG)')">
<AREA COORDS="425,217,5" SHAPE="CIRCLE" HREF="javascript:g('72402')" onMouseOver="return s('72402  Wallops Island, VA (WAL)')">
<AREA COORDS="415,215,5" SHAPE="CIRCLE" HREF="javascript:g('72403')" onMouseOver="return s('72403  Sterling, VA (IAD)')">
<AREA COORDS="388,220,5" SHAPE="CIRCLE" HREF="javascript:g('72426')" onMouseOver="return s('72426  Wilmington, OH (ILN)')">
<AREA COORDS="350,239,5" SHAPE="CIRCLE" HREF="javascript:g('72440')" onMouseOver="return s('72440  Springfield/Muno., MO (SGF)')">
<AREA COORDS="321,239,5" SHAPE="CIRCLE" HREF="javascript:g('72451')" onMouseOver="return s('72451  Dodge City(Awos), KS (DDC)')">
<AREA COORDS="339,230,5" SHAPE="CIRCLE" HREF="javascript:g('72456')" onMouseOver="return s('72456  Topeka/Billard Muni, KS (TOP)')">
<AREA COORDS="300,228,5" SHAPE="CIRCLE" HREF="javascript:g('72469')" onMouseOver="return s('72469  Denver/Stapleton, CO (DNR)')">
<AREA COORDS="285,232,5" SHAPE="CIRCLE" HREF="javascript:g('72476')" onMouseOver="return s('72476  Grand Junction/Walker, CO (GJT)')">
<AREA COORDS="238,224,5" SHAPE="CIRCLE" HREF="javascript:g('72489')" onMouseOver="return s('72489  Reno, NV (REV)')">
<AREA COORDS="226,232,5" SHAPE="CIRCLE" HREF="javascript:g('72493')" onMouseOver="return s('72493  Oakland Int, CA (OAK)')">
<AREA COORDS="430,199,5" SHAPE="CIRCLE" HREF="javascript:g('72501')" onMouseOver="return s('72501  Upton, NY (OKX)')">
<AREA COORDS="423,191,5" SHAPE="CIRCLE" HREF="javascript:g('72518')" onMouseOver="return s('72518  Albany, NY (ALB)')">
<AREA COORDS="401,210,5" SHAPE="CIRCLE" HREF="javascript:g('72520')" onMouseOver="return s('72520  Pittsburgh/Moon, PA (PIT)')">
<AREA COORDS="404,196,5" SHAPE="CIRCLE" HREF="javascript:g('72528')" onMouseOver="return s('72528  Buffalo Int, NY (BUF)')">
<AREA COORDS="335,218,5" SHAPE="CIRCLE" HREF="javascript:g('72558')" onMouseOver="return s('72558  Omaha/Valley, NE (OAX)')">
<AREA COORDS="318,221,5" SHAPE="CIRCLE" HREF="javascript:g('72562')" onMouseOver="return s('72562  North Platte/Lee Bird, NE (LBF)')">
<AREA COORDS="271,222,5" SHAPE="CIRCLE" HREF="javascript:g('72572')" onMouseOver="return s('72572  Salt Lake City/Intnl, UT (SLC)')">
<AREA COORDS="255,220,5" SHAPE="CIRCLE" HREF="javascript:g('72582')" onMouseOver="return s('72582  Elko, NV (LKN)')">
<AREA COORDS="228,207,5" SHAPE="CIRCLE" HREF="javascript:g('72597')" onMouseOver="return s('72597  Medford/Jackson, OR (MFR)')">
<AREA COORDS="386,202,5" SHAPE="CIRCLE" HREF="javascript:g('72632')" onMouseOver="return s('72632  White Lake, MI (DTX)')">
<AREA COORDS="378,191,5" SHAPE="CIRCLE" HREF="javascript:g('72634')" onMouseOver="return s('72634  Gaylord, MI (APX)')">
<AREA COORDS="365,196,5" SHAPE="CIRCLE" HREF="javascript:g('72645')" onMouseOver="return s('72645  Green Bay/Straubel, WI (GRB)')">
<AREA COORDS="344,198,5" SHAPE="CIRCLE" HREF="javascript:g('72649')" onMouseOver="return s('72649  Chanhassen, MN (MPX)')">
<AREA COORDS="325,196,5" SHAPE="CIRCLE" HREF="javascript:g('72659')" onMouseOver="return s('72659  Aberdeen/Reg, SD (ABR)')">
<AREA COORDS="307,205,5" SHAPE="CIRCLE" HREF="javascript:g('72662')" onMouseOver="return s('72662  Rapid City, SD (RAP)')">
<AREA COORDS="286,210,5" SHAPE="CIRCLE" HREF="javascript:g('72672')" onMouseOver="return s('72672  Riverton, WY (RIW)')">
<AREA COORDS="255,205,5" SHAPE="CIRCLE" HREF="javascript:g('72681')" onMouseOver="return s('72681  Boise/Mun, ID (BOI)')">
<AREA COORDS="230,193,5" SHAPE="CIRCLE" HREF="javascript:g('72694')" onMouseOver="return s('72694  Salem/Mcnary, OR (SLE)')">
<AREA COORDS="435,161,5" SHAPE="CIRCLE" HREF="javascript:g('72712')" onMouseOver="return s('72712  Caribou/Mun, ME (CAR)')">
<AREA COORDS="342,177,5" SHAPE="CIRCLE" HREF="javascript:g('72747')" onMouseOver="return s('72747  Int.Falls/Falls Int, MN (INL)')">
<AREA COORDS="316,190,5" SHAPE="CIRCLE" HREF="javascript:g('72764')" onMouseOver="return s('72764  Bismarck/Mun, ND (BIS)')">
<AREA COORDS="294,182,5" SHAPE="CIRCLE" HREF="javascript:g('72768')" onMouseOver="return s('72768  Glasgow/Int, MT (GGW)')">
<AREA COORDS="276,185,5" SHAPE="CIRCLE" HREF="javascript:g('72776')" onMouseOver="return s('72776  Great Falls, MT (TFX)')">
<AREA COORDS="253,182,5" SHAPE="CIRCLE" HREF="javascript:g('72786')" onMouseOver="return s('72786  Spokane, WA (OTX)')">
<AREA COORDS="228,176,5" SHAPE="CIRCLE" HREF="javascript:g('72797')" onMouseOver="return s('72797  Quillayute, WA (UIL)')">
<AREA COORDS="434,179,5" SHAPE="CIRCLE" HREF="javascript:g('74389')" onMouseOver="return s('74389  Gray, ME (GYX)')">
<AREA COORDS="358,214,5" SHAPE="CIRCLE" HREF="javascript:g('74455')" onMouseOver="return s('74455  Davenport, IA (DVN)')">
<AREA COORDS="439,190,5" SHAPE="CIRCLE" HREF="javascript:g('74494')" onMouseOver="return s('74494  Chatham, MA (CHH)')">
<AREA COORDS="365,221,5" SHAPE="CIRCLE" HREF="javascript:g('74560')" onMouseOver="return s('74560  Lincoln, IL (ILX)')">
<AREA COORDS="333,244,5" SHAPE="CIRCLE" HREF="javascript:g('74646')" onMouseOver="return s('74646  Lamont Oklahoma, OK (LMN)')">
<AREA COORDS="418,274,5" SHAPE="CIRCLE" HREF="javascript:g('74794')" onMouseOver="return s('74794  Cape Kennedy, FL (XMR)')">
<AREA COORDS="397,323,5" SHAPE="CIRCLE" HREF="javascript:g('76595')" onMouseOver="return s('76595  Cancun')">
<AREA COORDS="481,227,5" SHAPE="CIRCLE" HREF="javascript:g('78016')" onMouseOver="return s('78016  Bermuda Nvl Stn Kindley (TXKF)')">
<AREA COORDS="439,288,5" SHAPE="CIRCLE" HREF="javascript:g('78073')" onMouseOver="return s('78073  Nassau Airport (MYNN)')">
<AREA COORDS="428,326,5" SHAPE="CIRCLE" HREF="javascript:g('78384')" onMouseOver="return s('78384  Owen Roberts Arpt (MWCR)')">
<AREA COORDS="455,326,5" SHAPE="CIRCLE" HREF="javascript:g('78397')" onMouseOver="return s('78397  Kingston/Norman Manley (MKJP)')">
<AREA COORDS="509,301,5" SHAPE="CIRCLE" HREF="javascript:g('78526')" onMouseOver="return s('78526  San Juan/Int (TJSJ)')">
<AREA COORDS="393,344,5" SHAPE="CIRCLE" HREF="javascript:g('78583')" onMouseOver="return s('78583  Phillip Goldston Intl. (MZBZ)')">
<AREA COORDS="525,296,5" SHAPE="CIRCLE" HREF="javascript:g('78866')" onMouseOver="return s('78866  Juliana Airport (TNCM)')">
<AREA COORDS="538,301,5" SHAPE="CIRCLE" HREF="javascript:g('78897')" onMouseOver="return s('78897  Le Raizet, Guadeloupe (TFFR)')">
<AREA COORDS="555,331,5" SHAPE="CIRCLE" HREF="javascript:g('78970')" onMouseOver="return s('78970  Piarco Int. Airport (TTPP)')">
<AREA COORDS="509,342,5" SHAPE="CIRCLE" HREF="javascript:g('78988')" onMouseOver="return s('78988  Hato Airport, Curacao (TNCC)')">
<AREA COORDS="437,365,5" SHAPE="CIRCLE" HREF="javascript:g('80001')" onMouseOver="return s('80001  San Andres Isl (SKSP)')">
<AREA COORDS="496,398,5" SHAPE="CIRCLE" HREF="javascript:g('80222')" onMouseOver="return s('80222  Bogota/Eldorado (SKBO)')">
<AREA COORDS="582,373,5" SHAPE="CIRCLE" HREF="javascript:g('82022')" onMouseOver="return s('82022  Boa Vista (SBBV)')">
<AREA COORDS="28,241,5" SHAPE="CIRCLE" HREF="javascript:g('91165')" onMouseOver="return s('91165  Lihue, HI (PHLI)')">
<AREA COORDS="40,265,5" SHAPE="CIRCLE" HREF="javascript:g('91285')" onMouseOver="return s('91285  Hilo/Gen, HI (PHTO)')">
<AREA COORDS="129,25,5" SHAPE="CIRCLE" HREF="javascript:g('78970')" onMouseOver="return s('78970  Piarco Int. Airport (TTPP)')">
<AREA COORDS="94,17,5" SHAPE="CIRCLE" HREF="javascript:g('78988')" onMouseOver="return s('78988  Hato Airport, Curacao (TNCC)')">
<AREA COORDS="34,15,5" SHAPE="CIRCLE" HREF="javascript:g('80001')" onMouseOver="return s('80001  San Andres Isl (SKSP)')">
<AREA COORDS="69,52,5" SHAPE="CIRCLE" HREF="javascript:g('80222')" onMouseOver="return s('80222  Bogota/Eldorado (SKBO)')">
<AREA COORDS="64,71,5" SHAPE="CIRCLE" HREF="javascript:g('80371')" onMouseOver="return s('80371  Tres Esquinas (SKTQ)')">
<AREA COORDS="171,52,5" SHAPE="CIRCLE" HREF="javascript:g('81405')" onMouseOver="return s('81405  Rochambeau (SOCA)')">
<AREA COORDS="132,61,5" SHAPE="CIRCLE" HREF="javascript:g('82022')" onMouseOver="return s('82022  Boa Vista (SBBV)')">
<AREA COORDS="177,74,5" SHAPE="CIRCLE" HREF="javascript:g('82099')" onMouseOver="return s('82099  Macapa (SBMQ)')">
<AREA COORDS="189,80,5" SHAPE="CIRCLE" HREF="javascript:g('82193')" onMouseOver="return s('82193  Belem (Aeroporto) (SBBE)')">
<AREA COORDS="135,89,5" SHAPE="CIRCLE" HREF="javascript:g('82332')" onMouseOver="return s('82332  Manaus (Aeroporto) (SBMN)')">
<AREA COORDS="234,91,5" SHAPE="CIRCLE" HREF="javascript:g('82397')" onMouseOver="return s('82397  Fortaleza')">
<AREA COORDS="263,92,5" SHAPE="CIRCLE" HREF="javascript:g('82400')" onMouseOver="return s('82400  Fernando De Noronha (SBFN)')">
<AREA COORDS="250,101,5" SHAPE="CIRCLE" HREF="javascript:g('82599')" onMouseOver="return s('82599  Natal Aeroporto (SBNT)')">
<AREA COORDS="214,105,5" SHAPE="CIRCLE" HREF="javascript:g('82678')" onMouseOver="return s('82678  Floriano')">
<AREA COORDS="76,109,5" SHAPE="CIRCLE" HREF="javascript:g('82705')" onMouseOver="return s('82705  Cruzerio Do Sul')">
<AREA COORDS="193,108,5" SHAPE="CIRCLE" HREF="javascript:g('82765')" onMouseOver="return s('82765  Carolina')">
<AREA COORDS="117,115,5" SHAPE="CIRCLE" HREF="javascript:g('82824')" onMouseOver="return s('82824  Porto Velho (Aeroporto) (SBPV)')">
<AREA COORDS="153,120,5" SHAPE="CIRCLE" HREF="javascript:g('82965')" onMouseOver="return s('82965  Alta Floresta (Aero) (SBAT)')">
<AREA COORDS="226,118,5" SHAPE="CIRCLE" HREF="javascript:g('82983')" onMouseOver="return s('82983  Petrolina')">
<AREA COORDS="135,133,5" SHAPE="CIRCLE" HREF="javascript:g('83208')" onMouseOver="return s('83208  Vilhena (Aeroporto) (SBVH)')">
<AREA COORDS="212,136,5" SHAPE="CIRCLE" HREF="javascript:g('83288')" onMouseOver="return s('83288  Bom Jesus Da Lapa (SBLP)')">
<AREA COORDS="153,148,5" SHAPE="CIRCLE" HREF="javascript:g('83362')" onMouseOver="return s('83362  Cuiaba (Aeroporto) (SBCY)')">
<AREA COORDS="191,149,5" SHAPE="CIRCLE" HREF="javascript:g('83378')" onMouseOver="return s('83378  Brasilia (Aeroporto) (SBBR)')">
<AREA COORDS="231,158,5" SHAPE="CIRCLE" HREF="javascript:g('83498')" onMouseOver="return s('83498  Caravelas')">
<AREA COORDS="211,167,5" SHAPE="CIRCLE" HREF="javascript:g('83566')" onMouseOver="return s('83566  Confis Intnl Arpt')">
<AREA COORDS="160,171,5" SHAPE="CIRCLE" HREF="javascript:g('83612')" onMouseOver="return s('83612  Campo Grande (Aero) (SBCG)')">
<AREA COORDS="227,170,5" SHAPE="CIRCLE" HREF="javascript:g('83649')" onMouseOver="return s('83649  Vitoria')">
<AREA COORDS="213,183,5" SHAPE="CIRCLE" HREF="javascript:g('83746')" onMouseOver="return s('83746  Galeao (SBGL)')">
<AREA COORDS="197,186,5" SHAPE="CIRCLE" HREF="javascript:g('83779')" onMouseOver="return s('83779  Marte Civ/Mil (SBMT)')">
<AREA COORDS="160,196,5" SHAPE="CIRCLE" HREF="javascript:g('83827')" onMouseOver="return s('83827  Foz Do Iguacu (Aero) (SBFI)')">
<AREA COORDS="188,208,5" SHAPE="CIRCLE" HREF="javascript:g('83899')" onMouseOver="return s('83899  Florianopolis (SBFL)')">
<AREA COORDS="185,196,5" SHAPE="CIRCLE" HREF="javascript:g('83840')" onMouseOver="return s('83840  Curitiba (Aeroporto) (SBCT)')">
<AREA COORDS="149,219,5" SHAPE="CIRCLE" HREF="javascript:g('83928')" onMouseOver="return s('83928  Uruguaniana (SBUG)')">
<AREA COORDS="164,218,5" SHAPE="CIRCLE" HREF="javascript:g('83937')" onMouseOver="return s('83937  Santa Maria (SBSM)')">
<AREA COORDS="87,186,5" SHAPE="CIRCLE" HREF="javascript:g('85442')" onMouseOver="return s('85442  Antofagasta (SCFA)')">
<AREA COORDS="81,240,5" SHAPE="CIRCLE" HREF="javascript:g('85586')" onMouseOver="return s('85586  Santo Domingo (SCSN)')">
<AREA COORDS="74,286,5" SHAPE="CIRCLE" HREF="javascript:g('85799')" onMouseOver="return s('85799  Puerto Montt (SCTE)')">
<AREA COORDS="85,365,5" SHAPE="CIRCLE" HREF="javascript:g('85934')" onMouseOver="return s('85934  Punta Arenas (SCCI)')">
<AREA COORDS="36,37,5" SHAPE="CIRCLE" HREF="javascript:g('45004')" onMouseOver="return s('45004  Kings Park')">
<AREA COORDS="107,6,5" SHAPE="CIRCLE" HREF="javascript:g('47909')" onMouseOver="return s('47909  Naze/Funchatoge')">
<AREA COORDS="82,27,5" SHAPE="CIRCLE" HREF="javascript:g('47918')" onMouseOver="return s('47918  Ishigakijima (ROIG)')">
<AREA COORDS="115,19,5" SHAPE="CIRCLE" HREF="javascript:g('47945')" onMouseOver="return s('47945  Minamidaitojima (ROMD)')">
<AREA COORDS="166,12,5" SHAPE="CIRCLE" HREF="javascript:g('47971')" onMouseOver="return s('47971  Chichijima (RJAO)')">
<AREA COORDS="220,27,5" SHAPE="CIRCLE" HREF="javascript:g('47991')" onMouseOver="return s('47991  Minamitorishima (RJAM)')">
<AREA COORDS="8,68,5" SHAPE="CIRCLE" HREF="javascript:g('48855')" onMouseOver="return s('48855  Da Nang (VVDN)')">
<AREA COORDS="1,93,5" SHAPE="CIRCLE" HREF="javascript:g('48900')" onMouseOver="return s('48900  Ho Chi Minh (VVTS)')">
<AREA COORDS="0,0,5" SHAPE="CIRCLE" HREF="javascript:g('57516')" onMouseOver="return s('57516  Chongqing, CD (ZUCK)')">
<AREA COORDS="31,7,5" SHAPE="CIRCLE" HREF="javascript:g('57679')" onMouseOver="return s('57679  Changsha, HK (ZGCS)')">
<AREA COORDS="16,10,5" SHAPE="CIRCLE" HREF="javascript:g('57749')" onMouseOver="return s('57749  Huaihua, HK')">
<AREA COORDS="1,16,5" SHAPE="CIRCLE" HREF="javascript:g('57816')" onMouseOver="return s('57816  Guiyang, CD (ZUGY)')">
<AREA COORDS="18,21,5" SHAPE="CIRCLE" HREF="javascript:g('57957')" onMouseOver="return s('57957  Guilin, GZ (ZGKL)')">
<AREA COORDS="30,19,5" SHAPE="CIRCLE" HREF="javascript:g('57972')" onMouseOver="return s('57972  Chenzhou, HK')">
<AREA COORDS="39,19,5" SHAPE="CIRCLE" HREF="javascript:g('57993')" onMouseOver="return s('57993  Ganzhou, HK (ZSGZ)')">
<AREA COORDS="44,4,5" SHAPE="CIRCLE" HREF="javascript:g('58606')" onMouseOver="return s('58606  Nanchang, HK (ZSCN)')">
<AREA COORDS="57,3,5" SHAPE="CIRCLE" HREF="javascript:g('58633')" onMouseOver="return s('58633  Qu Xian, SH')">
<AREA COORDS="69,4,5" SHAPE="CIRCLE" HREF="javascript:g('58665')" onMouseOver="return s('58665  Hongjia, SH')">
<AREA COORDS="51,11,5" SHAPE="CIRCLE" HREF="javascript:g('58725')" onMouseOver="return s('58725  Shaowu, SH')">
<AREA COORDS="59,18,5" SHAPE="CIRCLE" HREF="javascript:g('58847')" onMouseOver="return s('58847  Fuzhou, SH (ZSFZ)')">
<AREA COORDS="54,26,5" SHAPE="CIRCLE" HREF="javascript:g('59134')" onMouseOver="return s('59134  Xiamen, SH (ZSAM)')">
<AREA COORDS="1,29,5" SHAPE="CIRCLE" HREF="javascript:g('59211')" onMouseOver="return s('59211  Baise, GZ')">
<AREA COORDS="22,31,5" SHAPE="CIRCLE" HREF="javascript:g('59265')" onMouseOver="return s('59265  Wuzhou, GZ')">
<AREA COORDS="30,30,5" SHAPE="CIRCLE" HREF="javascript:g('59280')" onMouseOver="return s('59280  Qing Yuan, GZ')">
<AREA COORDS="47,32,5" SHAPE="CIRCLE" HREF="javascript:g('59316')" onMouseOver="return s('59316  Shantou, GZ (ZGOW)')">
<AREA COORDS="8,35,5" SHAPE="CIRCLE" HREF="javascript:g('59431')" onMouseOver="return s('59431  Nanning, GZ (ZGNN)')">
<AREA COORDS="18,48,5" SHAPE="CIRCLE" HREF="javascript:g('59758')" onMouseOver="return s('59758  Haikou, GZ (ZGHK)')">
<AREA COORDS="27,64,5" SHAPE="CIRCLE" HREF="javascript:g('59981')" onMouseOver="return s('59981  Xisha Dao, GZ')">
<AREA COORDS="437,38,5" SHAPE="CIRCLE" HREF="javascript:g('91165')" onMouseOver="return s('91165  Lihue, HI (PHLI)')">
<AREA COORDS="178,80,5" SHAPE="CIRCLE" HREF="javascript:g('91212')" onMouseOver="return s('91212  Guam Intl Arpt (PGUM)')">
<AREA COORDS="457,50,5" SHAPE="CIRCLE" HREF="javascript:g('91285')" onMouseOver="return s('91285  Hilo/Gen, HI (PHTO)')">
<AREA COORDS="210,108,5" SHAPE="CIRCLE" HREF="javascript:g('91334')" onMouseOver="return s('91334  Truk (PTKK)')">
<AREA COORDS="240,111,5" SHAPE="CIRCLE" HREF="javascript:g('91348')" onMouseOver="return s('91348  Ponape (PTPN)')">
<AREA COORDS="301,110,5" SHAPE="CIRCLE" HREF="javascript:g('91376')" onMouseOver="return s('91376  Majuro/Marshall Is (PKMJ)')">
<AREA COORDS="130,109,5" SHAPE="CIRCLE" HREF="javascript:g('91408')" onMouseOver="return s('91408  Koror, Palau Is (PTRO)')">
<AREA COORDS="147,99,5" SHAPE="CIRCLE" HREF="javascript:g('91413')" onMouseOver="return s('91413  Yap (PTYA)')">
<AREA COORDS="280,145,5" SHAPE="CIRCLE" HREF="javascript:g('91532')" onMouseOver="return s('91532  Republic Of Nauru(Arcs2)')">
<AREA COORDS="278,249,5" SHAPE="CIRCLE" HREF="javascript:g('91592')" onMouseOver="return s('91592  Noumea (Nlle-Caledonie) (NWWN)')">
<AREA COORDS="329,227,5" SHAPE="CIRCLE" HREF="javascript:g('91680')" onMouseOver="return s('91680  Nadi Airport (NFFN)')">
<AREA COORDS="384,210,5" SHAPE="CIRCLE" HREF="javascript:g('91765')" onMouseOver="return s('91765  Pago Pago/Int.Airp. (NSTU)')">
<AREA COORDS="190,153,5" SHAPE="CIRCLE" HREF="javascript:g('92044')" onMouseOver="return s('92044  Momote W.O.')">
<AREA COORDS="113,201,5" SHAPE="CIRCLE" HREF="javascript:g('94120')" onMouseOver="return s('94120  Darwin Airport, NT (YPDN)')">
<AREA COORDS="141,200,5" SHAPE="CIRCLE" HREF="javascript:g('94150')" onMouseOver="return s('94150  Gove Airport, NT (YDGV)')">
<AREA COORDS="73,228,5" SHAPE="CIRCLE" HREF="javascript:g('94203')" onMouseOver="return s('94203  Broome Amo, WE (YBRM)')">
<AREA COORDS="182,222,5" SHAPE="CIRCLE" HREF="javascript:g('94287')" onMouseOver="return s('94287  Cairns Airport, QU (YBCS)')">
<AREA COORDS="187,234,5" SHAPE="CIRCLE" HREF="javascript:g('94294')" onMouseOver="return s('94294  Townsville Aero, QU (YBTL)')">
<AREA COORDS="202,220,5" SHAPE="CIRCLE" HREF="javascript:g('94299')" onMouseOver="return s('94299  Willis Island, QU')">
<AREA COORDS="35,249,5" SHAPE="CIRCLE" HREF="javascript:g('94302')" onMouseOver="return s('94302  Learmonth Airport, WE (YPLM)')">
<AREA COORDS="175,255,5" SHAPE="CIRCLE" HREF="javascript:g('94346')" onMouseOver="return s('94346  Longreach Amo, QU (YBLR)')">
<AREA COORDS="204,255,5" SHAPE="CIRCLE" HREF="javascript:g('94374')" onMouseOver="return s('94374  Rockhampton Aero, QU (YBRK)')">
<AREA COORDS="101,263,5" SHAPE="CIRCLE" HREF="javascript:g('94461')" onMouseOver="return s('94461  Giles, WE')">
<AREA COORDS="185,270,5" SHAPE="CIRCLE" HREF="javascript:g('94510')" onMouseOver="return s('94510  Charleville Amo, QU (YBCV)')">
<AREA COORDS="216,275,5" SHAPE="CIRCLE" HREF="javascript:g('94578')" onMouseOver="return s('94578  Brisbane Airport Aero, QU (YBBN)')">
<AREA COORDS="44,299,5" SHAPE="CIRCLE" HREF="javascript:g('94610')" onMouseOver="return s('94610  Perth Airport, WE (YPPH)')">
<AREA COORDS="71,310,5" SHAPE="CIRCLE" HREF="javascript:g('94638')" onMouseOver="return s('94638  Esperance Mo, WE')">
<AREA COORDS="149,316,5" SHAPE="CIRCLE" HREF="javascript:g('94672')" onMouseOver="return s('94672  Adelaide Airport, SA (YPAD)')">
<AREA COORDS="165,312,5" SHAPE="CIRCLE" HREF="javascript:g('94693')" onMouseOver="return s('94693  Mildura Airport, VC (YMMI)')">
<AREA COORDS="207,310,5" SHAPE="CIRCLE" HREF="javascript:g('94767')" onMouseOver="return s('94767  Sydney Airport Amo Aws, NW (YSSY)')">
<AREA COORDS="178,332,5" SHAPE="CIRCLE" HREF="javascript:g('94866')" onMouseOver="return s('94866  Melbourne Airport, VC (YMML)')">
<AREA COORDS="190,363,5" SHAPE="CIRCLE" HREF="javascript:g('94975')" onMouseOver="return s('94975  Hobart Airport, TA (YMHB)')">
<AREA COORDS="285,284,5" SHAPE="CIRCLE" HREF="javascript:g('94996')" onMouseOver="return s('94996  Norfolk Island Aero (YSNF)')">
<AREA COORDS="9,125,5" SHAPE="CIRCLE" HREF="javascript:g('96147')" onMouseOver="return s('96147  Ranai (WION)')">
<AREA COORDS="6,156,5" SHAPE="CIRCLE" HREF="javascript:g('96249')" onMouseOver="return s('96249  Tanjung Pandan/Buluh (WIKD)')">
<AREA COORDS="39,120,5" SHAPE="CIRCLE" HREF="javascript:g('96315')" onMouseOver="return s('96315  Brunei Airport (WBSB)')">
<AREA COORDS="18,136,5" SHAPE="CIRCLE" HREF="javascript:g('96413')" onMouseOver="return s('96413  Kuching (WBGG)')">
<AREA COORDS="30,128,5" SHAPE="CIRCLE" HREF="javascript:g('96441')" onMouseOver="return s('96441  Bintulu (WBGB)')">
<AREA COORDS="44,115,5" SHAPE="CIRCLE" HREF="javascript:g('96471')" onMouseOver="return s('96471  Kota Kinabalu (WBKK)')">
<AREA COORDS="53,123,5" SHAPE="CIRCLE" HREF="javascript:g('96481')" onMouseOver="return s('96481  Tawau (WBKW)')">
<AREA COORDS="51,128,5" SHAPE="CIRCLE" HREF="javascript:g('96509')" onMouseOver="return s('96509  Tarakan/Juwata (WRLR)')">
<AREA COORDS="51,133,5" SHAPE="CIRCLE" HREF="javascript:g('96529')" onMouseOver="return s('96529  Tanjung Redep/Kalimarau (WRLK)')">
<AREA COORDS="14,144,5" SHAPE="CIRCLE" HREF="javascript:g('96581')" onMouseOver="return s('96581  Pontianak/Supadio (WIOO)')">
<AREA COORDS="39,147,5" SHAPE="CIRCLE" HREF="javascript:g('96595')" onMouseOver="return s('96595  Muara Teweh/Beringin (WRBM)')">
<AREA COORDS="50,146,5" SHAPE="CIRCLE" HREF="javascript:g('96607')" onMouseOver="return s('96607  Samarinda/Temindung (WRLS)')">
<AREA COORDS="48,149,5" SHAPE="CIRCLE" HREF="javascript:g('96633')" onMouseOver="return s('96633  Balikpapan/Sepinggan (WRLL)')">
<AREA COORDS="29,156,5" SHAPE="CIRCLE" HREF="javascript:g('96645')" onMouseOver="return s('96645  Pangkalan Bun/Iskandar (WRBI)')">
<AREA COORDS="38,159,5" SHAPE="CIRCLE" HREF="javascript:g('96685')" onMouseOver="return s('96685  Banjarmasin/Syamsudin (WRBB)')">
<AREA COORDS="1,171,5" SHAPE="CIRCLE" HREF="javascript:g('96749')" onMouseOver="return s('96749  Jakarta/Soekarno-Hatta (WIII)')">
<AREA COORDS="8,174,5" SHAPE="CIRCLE" HREF="javascript:g('96791')" onMouseOver="return s('96791  Cirebon/Jatiwangi')">
<AREA COORDS="12,175,5" SHAPE="CIRCLE" HREF="javascript:g('96797')" onMouseOver="return s('96797  Tegal')">
<AREA COORDS="18,175,5" SHAPE="CIRCLE" HREF="javascript:g('96839')" onMouseOver="return s('96839  Semarang/Ahmad Yani (WIIS)')">
<AREA COORDS="29,170,5" SHAPE="CIRCLE" HREF="javascript:g('96925')" onMouseOver="return s('96925  Sangkapura (Bawean Is.)')">
<AREA COORDS="29,177,5" SHAPE="CIRCLE" HREF="javascript:g('96935')" onMouseOver="return s('96935  Surabaya/Juanda (WRSJ)')">
<AREA COORDS="88,126,5" SHAPE="CIRCLE" HREF="javascript:g('97008')" onMouseOver="return s('97008  Naha/Tahuna (WAMH)')">
<AREA COORDS="86,136,5" SHAPE="CIRCLE" HREF="javascript:g('97014')" onMouseOver="return s('97014  Menado/ Sam Ratulangi (WAMM)')">
<AREA COORDS="61,146,5" SHAPE="CIRCLE" HREF="javascript:g('97072')" onMouseOver="return s('97072  Palu/Mutiara (WAML)')">
<AREA COORDS="76,147,5" SHAPE="CIRCLE" HREF="javascript:g('97086')" onMouseOver="return s('97086  Luwuk/Bubung (WAMW)')">
<AREA COORDS="58,155,5" SHAPE="CIRCLE" HREF="javascript:g('97120')" onMouseOver="return s('97120  Majene')">
<AREA COORDS="61,167,5" SHAPE="CIRCLE" HREF="javascript:g('97180')" onMouseOver="return s('97180  Ujung Pandang/Hasanuddin (WAAA)')">
<AREA COORDS="40,184,5" SHAPE="CIRCLE" HREF="javascript:g('97230')" onMouseOver="return s('97230  Denpasar/Ngurah Rai (WRRR)')">
<AREA COORDS="44,183,5" SHAPE="CIRCLE" HREF="javascript:g('97240')" onMouseOver="return s('97240  Mataram/Selaparang (WRRA)')">
<AREA COORDS="73,183,5" SHAPE="CIRCLE" HREF="javascript:g('97300')" onMouseOver="return s('97300  Maumere/Wai Oti (WRKC)')">
<AREA COORDS="64,188,5" SHAPE="CIRCLE" HREF="javascript:g('97340')" onMouseOver="return s('97340  Waingapu/Mau Hau (WRRW)')">
<AREA COORDS="80,190,5" SHAPE="CIRCLE" HREF="javascript:g('97372')" onMouseOver="return s('97372  Kupang/Eltari (WRKK)')">
<AREA COORDS="97,139,5" SHAPE="CIRCLE" HREF="javascript:g('97430')" onMouseOver="return s('97430  Ternate/Babullah (WAMT)')">
<AREA COORDS="114,147,5" SHAPE="CIRCLE" HREF="javascript:g('97502')" onMouseOver="return s('97502  Sorong/Jefman (WASS)')">
<AREA COORDS="137,148,5" SHAPE="CIRCLE" HREF="javascript:g('97560')" onMouseOver="return s('97560  Biak/Frans Kaisiepo (WABB)')">
<AREA COORDS="100,160,5" SHAPE="CIRCLE" HREF="javascript:g('97724')" onMouseOver="return s('97724  Ambon/Pattimura (WAPP)')">
<AREA COORDS="113,161,5" SHAPE="CIRCLE" HREF="javascript:g('97748')" onMouseOver="return s('97748  Geser')">
<AREA COORDS="122,169,5" SHAPE="CIRCLE" HREF="javascript:g('97810')" onMouseOver="return s('97810  Tual/Dumatubun')">
<AREA COORDS="115,180,5" SHAPE="CIRCLE" HREF="javascript:g('97900')" onMouseOver="return s('97900  Saumlaki/Olilit (WAPI)')">
<AREA COORDS="157,182,5" SHAPE="CIRCLE" HREF="javascript:g('97980')" onMouseOver="return s('97980  Merauke/Mopah (WAKK)')">
<AREA COORDS="65,57,5" SHAPE="CIRCLE" HREF="javascript:g('98223')" onMouseOver="return s('98223  Laoag (RPLI)')">
<AREA COORDS="69,75,5" SHAPE="CIRCLE" HREF="javascript:g('98433')" onMouseOver="return s('98433  Tanay')">
<AREA COORDS="80,82,5" SHAPE="CIRCLE" HREF="javascript:g('98444')" onMouseOver="return s('98444  Legaspi (RPMP)')">
<AREA COORDS="57,98,5" SHAPE="CIRCLE" HREF="javascript:g('98618')" onMouseOver="return s('98618  Puerto Princesa (RPVP)')">
<AREA COORDS="134,49,5" SHAPE="CIRCLE" HREF="javascript:g('89002')" onMouseOver="return s('89002  Neumayer')">
<AREA COORDS="149,149,5" SHAPE="CIRCLE" HREF="javascript:g('89009')" onMouseOver="return s('89009  Amundsen-Scott')">
<AREA COORDS="115,81,5" SHAPE="CIRCLE" HREF="javascript:g('89022')" onMouseOver="return s('89022  Halley')">
<AREA COORDS="219,64,5" SHAPE="CIRCLE" HREF="javascript:g('89532')" onMouseOver="return s('89532  Syowa')">
<AREA COORDS="254,95,5" SHAPE="CIRCLE" HREF="javascript:g('89564')" onMouseOver="return s('89564  Mawson')">
<AREA COORDS="259,126,5" SHAPE="CIRCLE" HREF="javascript:g('89571')" onMouseOver="return s('89571  Davis')">
<AREA COORDS="266,193,5" SHAPE="CIRCLE" HREF="javascript:g('89611')" onMouseOver="return s('89611  Casey')">
<AREA COORDS="164,211,5" SHAPE="CIRCLE" HREF="javascript:g('89664')" onMouseOver="return s('89664  Mcmurdo')">
<AREA COORDS="298,214,5" SHAPE="CIRCLE" HREF="javascript:g('01001')" onMouseOver="return s('01001  Jan Mayen (ENJA)')">
<AREA COORDS="256,187,5" SHAPE="CIRCLE" HREF="javascript:g('01004')" onMouseOver="return s('01004  Ny-Alesund Ii (ENAS)')">
<AREA COORDS="276,173,5" SHAPE="CIRCLE" HREF="javascript:g('01028')" onMouseOver="return s('01028  Bjornoya (ENBJ)')">
<AREA COORDS="315,169,5" SHAPE="CIRCLE" HREF="javascript:g('01152')" onMouseOver="return s('01152  Bodo (ENBO)')">
<AREA COORDS="336,176,5" SHAPE="CIRCLE" HREF="javascript:g('01241')" onMouseOver="return s('01241  Orland (ENOL)')">
<AREA COORDS="378,189,5" SHAPE="CIRCLE" HREF="javascript:g('01400')" onMouseOver="return s('01400  Ekofisk')">
<AREA COORDS="364,183,5" SHAPE="CIRCLE" HREF="javascript:g('01415')" onMouseOver="return s('01415  Stavanger/Sola (ENZV)')">
<AREA COORDS="338,155,5" SHAPE="CIRCLE" HREF="javascript:g('02365')" onMouseOver="return s('02365  Sundsvall-Harnosand Fpl')">
<AREA COORDS="363,145,5" SHAPE="CIRCLE" HREF="javascript:g('02591')" onMouseOver="return s('02591  Visby Aerologiska Stn (ESQV)')">
<AREA COORDS="305,146,5" SHAPE="CIRCLE" HREF="javascript:g('02836')" onMouseOver="return s('02836  Sodankyla (EFSO)')">
<AREA COORDS="341,137,5" SHAPE="CIRCLE" HREF="javascript:g('02963')" onMouseOver="return s('02963  Jokioinen')">
<AREA COORDS="358,202,5" SHAPE="CIRCLE" HREF="javascript:g('03005')" onMouseOver="return s('03005  Lerwick')">
<AREA COORDS="267,288,5" SHAPE="CIRCLE" HREF="javascript:g('04220')" onMouseOver="return s('04220  Aasiaat (Egedesminde) (BGEM)')">
<AREA COORDS="306,308,5" SHAPE="CIRCLE" HREF="javascript:g('04270')" onMouseOver="return s('04270  Narsarsuaq (BGBW)')">
<AREA COORDS="264,221,5" SHAPE="CIRCLE" HREF="javascript:g('04320')" onMouseOver="return s('04320  Danmarkshavn (BGDH)')">
<AREA COORDS="294,237,5" SHAPE="CIRCLE" HREF="javascript:g('04339')" onMouseOver="return s('04339  Ittoqqortoormiit (BGSC)')">
<AREA COORDS="301,278,5" SHAPE="CIRCLE" HREF="javascript:g('04360')" onMouseOver="return s('04360  Tasiilaq (Ammassalik) (BGAM)')">
<AREA COORDS="346,216,5" SHAPE="CIRCLE" HREF="javascript:g('06011')" onMouseOver="return s('06011  Torshavn')">
<AREA COORDS="387,167,5" SHAPE="CIRCLE" HREF="javascript:g('10035')" onMouseOver="return s('10035  Schleswig')">
<AREA COORDS="393,175,5" SHAPE="CIRCLE" HREF="javascript:g('10113')" onMouseOver="return s('10113  Norderney')">
<AREA COORDS="387,154,5" SHAPE="CIRCLE" HREF="javascript:g('10184')" onMouseOver="return s('10184  Greifswald')">
<AREA COORDS="396,164,5" SHAPE="CIRCLE" HREF="javascript:g('10238')" onMouseOver="return s('10238  Bergen (ETGB)')">
<AREA COORDS="397,149,5" SHAPE="CIRCLE" HREF="javascript:g('10393')" onMouseOver="return s('10393  Lindenberg')">
<AREA COORDS="379,142,5" SHAPE="CIRCLE" HREF="javascript:g('12120')" onMouseOver="return s('12120  Leba')">
<AREA COORDS="388,127,5" SHAPE="CIRCLE" HREF="javascript:g('12374')" onMouseOver="return s('12374  Legionowo')">
<AREA COORDS="396,139,5" SHAPE="CIRCLE" HREF="javascript:g('12425')" onMouseOver="return s('12425  Wroclaw I')">
<AREA COORDS="225,158,5" SHAPE="CIRCLE" HREF="javascript:g('20046')" onMouseOver="return s('20046  Polargmo Im. Krenkelja, DK')">
<AREA COORDS="183,137,5" SHAPE="CIRCLE" HREF="javascript:g('20292')" onMouseOver="return s('20292  Gmo Im.E.K. Fedorova, DK')">
<AREA COORDS="213,114,5" SHAPE="CIRCLE" HREF="javascript:g('20674')" onMouseOver="return s('20674  Ostrov Dikson, DK')">
<AREA COORDS="255,126,5" SHAPE="CIRCLE" HREF="javascript:g('20744')" onMouseOver="return s('20744  Malye Karmakuly, DK')">
<AREA COORDS="145,150,5" SHAPE="CIRCLE" HREF="javascript:g('21432')" onMouseOver="return s('21432  Ostrov Kotelnyj, DK')">
<AREA COORDS="138,124,5" SHAPE="CIRCLE" HREF="javascript:g('21824')" onMouseOver="return s('21824  Tiksi, TK')">
<AREA COORDS="113,145,5" SHAPE="CIRCLE" HREF="javascript:g('21946')" onMouseOver="return s('21946  Chokurdah, TK')">
<AREA COORDS="291,139,5" SHAPE="CIRCLE" HREF="javascript:g('22113')" onMouseOver="return s('22113  Murmansk, AR (ULMM)')">
<AREA COORDS="301,135,5" SHAPE="CIRCLE" HREF="javascript:g('22217')" onMouseOver="return s('22217  Kandalaksa, AR')">
<AREA COORDS="282,118,5" SHAPE="CIRCLE" HREF="javascript:g('22271')" onMouseOver="return s('22271  Sojna, AR')">
<AREA COORDS="308,124,5" SHAPE="CIRCLE" HREF="javascript:g('22522')" onMouseOver="return s('22522  Kem, LE')">
<AREA COORDS="322,115,5" SHAPE="CIRCLE" HREF="javascript:g('22820')" onMouseOver="return s('22820  Petrozavodsk, LE')">
<AREA COORDS="317,104,5" SHAPE="CIRCLE" HREF="javascript:g('22845')" onMouseOver="return s('22845  Kargopol, AR')">
<AREA COORDS="270,105,5" SHAPE="CIRCLE" HREF="javascript:g('23205')" onMouseOver="return s('23205  Narjan-Mar, AR')">
<AREA COORDS="248,85,5" SHAPE="CIRCLE" HREF="javascript:g('23330')" onMouseOver="return s('23330  Salehard, NO')">
<AREA COORDS="270,89,5" SHAPE="CIRCLE" HREF="javascript:g('23418')" onMouseOver="return s('23418  Pechora, AR')">
<AREA COORDS="204,71,5" SHAPE="CIRCLE" HREF="javascript:g('23472')" onMouseOver="return s('23472  Turuhansk, NO')">
<AREA COORDS="294,82,5" SHAPE="CIRCLE" HREF="javascript:g('23804')" onMouseOver="return s('23804  Syktyvkar, AR (UUYY)')">
<AREA COORDS="199,48,5" SHAPE="CIRCLE" HREF="javascript:g('23884')" onMouseOver="return s('23884  Bor, NO')">
<AREA COORDS="276,64,5" SHAPE="CIRCLE" HREF="javascript:g('23921')" onMouseOver="return s('23921  Ivdel, SV')">
<AREA COORDS="254,55,5" SHAPE="CIRCLE" HREF="javascript:g('23933')" onMouseOver="return s('23933  Hanty-Mansijsk, NO (USHH)')">
<AREA COORDS="232,45,5" SHAPE="CIRCLE" HREF="javascript:g('23955')" onMouseOver="return s('23955  Aleksandrovskoe, NO')">
<AREA COORDS="156,95,5" SHAPE="CIRCLE" HREF="javascript:g('24125')" onMouseOver="return s('24125  Olenek, HA')">
<AREA COORDS="118,113,5" SHAPE="CIRCLE" HREF="javascript:g('24266')" onMouseOver="return s('24266  Verhojansk, HA')">
<AREA COORDS="132,97,5" SHAPE="CIRCLE" HREF="javascript:g('24343')" onMouseOver="return s('24343  Zhigansk, HA')">
<AREA COORDS="175,65,5" SHAPE="CIRCLE" HREF="javascript:g('24507')" onMouseOver="return s('24507  Tura, NO')">
<AREA COORDS="126,81,5" SHAPE="CIRCLE" HREF="javascript:g('24641')" onMouseOver="return s('24641  Viljujsk, HA')">
<AREA COORDS="86,114,5" SHAPE="CIRCLE" HREF="javascript:g('24688')" onMouseOver="return s('24688  Ojmjakon, HA')">
<AREA COORDS="140,66,5" SHAPE="CIRCLE" HREF="javascript:g('24726')" onMouseOver="return s('24726  Mirnvy, HB')">
<AREA COORDS="166,45,5" SHAPE="CIRCLE" HREF="javascript:g('24908')" onMouseOver="return s('24908  Vanavara, NO')">
<AREA COORDS="119,63,5" SHAPE="CIRCLE" HREF="javascript:g('24944')" onMouseOver="return s('24944  Olekminsk, HA')">
<AREA COORDS="104,85,5" SHAPE="CIRCLE" HREF="javascript:g('24959')" onMouseOver="return s('24959  Jakutsk, HA (UEEE)')">
<AREA COORDS="93,163,5" SHAPE="CIRCLE" HREF="javascript:g('25123')" onMouseOver="return s('25123  Cherskij, HA')">
<AREA COORDS="87,137,5" SHAPE="CIRCLE" HREF="javascript:g('25400')" onMouseOver="return s('25400  Zyrjanka, HA')">
<AREA COORDS="76,155,5" SHAPE="CIRCLE" HREF="javascript:g('25428')" onMouseOver="return s('25428  Omolon, HB')">
<AREA COORDS="72,133,5" SHAPE="CIRCLE" HREF="javascript:g('25703')" onMouseOver="return s('25703  Sejmchan, HA')">
<AREA COORDS="58,120,5" SHAPE="CIRCLE" HREF="javascript:g('25913')" onMouseOver="return s('25913  Magadan, HA (UHMM)')">
<AREA COORDS="336,117,5" SHAPE="CIRCLE" HREF="javascript:g('26063')" onMouseOver="return s('26063  St.Petersburg(Voejkovo), LE (ULLI)')">
<AREA COORDS="341,103,5" SHAPE="CIRCLE" HREF="javascript:g('26298')" onMouseOver="return s('26298  Bologoe, LE')">
<AREA COORDS="354,107,5" SHAPE="CIRCLE" HREF="javascript:g('26477')" onMouseOver="return s('26477  Velikie Luki, LE (ULOL)')">
<AREA COORDS="359,99,5" SHAPE="CIRCLE" HREF="javascript:g('26781')" onMouseOver="return s('26781  Smolensk, MI')">
<AREA COORDS="307,72,5" SHAPE="CIRCLE" HREF="javascript:g('27199')" onMouseOver="return s('27199  Kirov, MS')">
<AREA COORDS="329,74,5" SHAPE="CIRCLE" HREF="javascript:g('27459')" onMouseOver="return s('27459  Niznij Novgorod, MS')">
<AREA COORDS="319,59,5" SHAPE="CIRCLE" HREF="javascript:g('27595')" onMouseOver="return s('27595  Kazan, MS')">
<AREA COORDS="356,87,5" SHAPE="CIRCLE" HREF="javascript:g('27707')" onMouseOver="return s('27707  Suhinici, MS')">
<AREA COORDS="345,78,5" SHAPE="CIRCLE" HREF="javascript:g('27730')" onMouseOver="return s('27730  Rjazan, MS')">
<AREA COORDS="339,59,5" SHAPE="CIRCLE" HREF="javascript:g('27962')" onMouseOver="return s('27962  Penza, MS (UWPP)')">
<AREA COORDS="329,48,5" SHAPE="CIRCLE" HREF="javascript:g('27995')" onMouseOver="return s('27995  Samara (Bezencuk), MS')">
<AREA COORDS="294,57,5" SHAPE="CIRCLE" HREF="javascript:g('28225')" onMouseOver="return s('28225  Perm, SV')">
<AREA COORDS="262,41,5" SHAPE="CIRCLE" HREF="javascript:g('28275')" onMouseOver="return s('28275  Tobolsk, NO')">
<AREA COORDS="285,43,5" SHAPE="CIRCLE" HREF="javascript:g('28445')" onMouseOver="return s('28445  Verhnee Dubrovo, SV')">
<AREA COORDS="276,31,5" SHAPE="CIRCLE" HREF="javascript:g('28661')" onMouseOver="return s('28661  Kurgan, SV')">
<AREA COORDS="253,19,5" SHAPE="CIRCLE" HREF="javascript:g('28698')" onMouseOver="return s('28698  Omsk, NO')">
<AREA COORDS="305,42,5" SHAPE="CIRCLE" HREF="javascript:g('28722')" onMouseOver="return s('28722  Ufa, SV')">
<AREA COORDS="220,31,5" SHAPE="CIRCLE" HREF="javascript:g('29231')" onMouseOver="return s('29231  Kolpasevo, NO')">
<AREA COORDS="193,31,5" SHAPE="CIRCLE" HREF="javascript:g('29263')" onMouseOver="return s('29263  Enisejsk, NO (UNII)')">
<AREA COORDS="177,32,5" SHAPE="CIRCLE" HREF="javascript:g('29282')" onMouseOver="return s('29282  Bogucany, NO')">
<AREA COORDS="191,18,5" SHAPE="CIRCLE" HREF="javascript:g('29572')" onMouseOver="return s('29572  Emeljanovo, NO')">
<AREA COORDS="236,17,5" SHAPE="CIRCLE" HREF="javascript:g('29612')" onMouseOver="return s('29612  Barabinsk, NO')">
<AREA COORDS="222,13,5" SHAPE="CIRCLE" HREF="javascript:g('29634')" onMouseOver="return s('29634  Novosibirsk, NO (UNNN)')">
<AREA COORDS="169,13,5" SHAPE="CIRCLE" HREF="javascript:g('29698')" onMouseOver="return s('29698  Nizhneudinsk, NO (UINN)')">
<AREA COORDS="195,4,5" SHAPE="CIRCLE" HREF="javascript:g('29862')" onMouseOver="return s('29862  Hakasskaja, NO')">
<AREA COORDS="137,49,5" SHAPE="CIRCLE" HREF="javascript:g('30054')" onMouseOver="return s('30054  Vitim, HA')">
<AREA COORDS="146,35,5" SHAPE="CIRCLE" HREF="javascript:g('30230')" onMouseOver="return s('30230  Kirensk, IR (UIKK)')">
<AREA COORDS="162,22,5" SHAPE="CIRCLE" HREF="javascript:g('30309')" onMouseOver="return s('30309  Bratsk, IR')">
<AREA COORDS="115,43,5" SHAPE="CIRCLE" HREF="javascript:g('30372')" onMouseOver="return s('30372  Chara, IR')">
<AREA COORDS="123,24,5" SHAPE="CIRCLE" HREF="javascript:g('30554')" onMouseOver="return s('30554  Bagdarin, IR')">
<AREA COORDS="135,13,5" SHAPE="CIRCLE" HREF="javascript:g('30635')" onMouseOver="return s('30635  Ust-Barguzin, IR')">
<AREA COORDS="102,30,5" SHAPE="CIRCLE" HREF="javascript:g('30673')" onMouseOver="return s('30673  Mogoca, IR')">
<AREA COORDS="151,3,5" SHAPE="CIRCLE" HREF="javascript:g('30715')" onMouseOver="return s('30715  Angarsk, IR')">
<AREA COORDS="118,11,5" SHAPE="CIRCLE" HREF="javascript:g('30758')" onMouseOver="return s('30758  Chita, IR (UIAA)')">
<AREA COORDS="103,7,5" SHAPE="CIRCLE" HREF="javascript:g('30965')" onMouseOver="return s('30965  Borzja, IR')">
<AREA COORDS="102,63,5" SHAPE="CIRCLE" HREF="javascript:g('31004')" onMouseOver="return s('31004  Aldan, HA')">
<AREA COORDS="68,101,5" SHAPE="CIRCLE" HREF="javascript:g('31088')" onMouseOver="return s('31088  Ohotsk, HA')">
<AREA COORDS="65,79,5" SHAPE="CIRCLE" HREF="javascript:g('31168')" onMouseOver="return s('31168  Ajan, HA')">
<AREA COORDS="81,44,5" SHAPE="CIRCLE" HREF="javascript:g('31300')" onMouseOver="return s('31300  Zeja, HA')">
<AREA COORDS="46,73,5" SHAPE="CIRCLE" HREF="javascript:g('31369')" onMouseOver="return s('31369  Nikolaevsk-Na-Amure, HA')">
<AREA COORDS="69,30,5" SHAPE="CIRCLE" HREF="javascript:g('31510')" onMouseOver="return s('31510  Blagovescensk, HA')">
<AREA COORDS="39,40,5" SHAPE="CIRCLE" HREF="javascript:g('31736')" onMouseOver="return s('31736  Habarovsk, HA')">
<AREA COORDS="32,25,5" SHAPE="CIRCLE" HREF="javascript:g('31873')" onMouseOver="return s('31873  Dalnerechensk, HA')">
<AREA COORDS="27,8,5" SHAPE="CIRCLE" HREF="javascript:g('31977')" onMouseOver="return s('31977  Vladivostok (Sad Gorod), HA')">
<AREA COORDS="32,69,5" SHAPE="CIRCLE" HREF="javascript:g('32061')" onMouseOver="return s('32061  Aleksandrovsk-Sahalnskij, HA')">
<AREA COORDS="22,66,5" SHAPE="CIRCLE" HREF="javascript:g('32098')" onMouseOver="return s('32098  Poronajsk, HA')">
<AREA COORDS="12,57,5" SHAPE="CIRCLE" HREF="javascript:g('32150')" onMouseOver="return s('32150  Juzhno-Sahalinsk, HA (UHSS)')">
<AREA COORDS="5,113,5" SHAPE="CIRCLE" HREF="javascript:g('32215')" onMouseOver="return s('32215  Severo-Kurilsk, HA')">
<AREA COORDS="29,140,5" SHAPE="CIRCLE" HREF="javascript:g('32389')" onMouseOver="return s('32389  Kljuchi, HA')">
<AREA COORDS="14,126,5" SHAPE="CIRCLE" HREF="javascript:g('32540')" onMouseOver="return s('32540  Kamchatskij, HA (UHPP)')">
<AREA COORDS="373,95,5" SHAPE="CIRCLE" HREF="javascript:g('33041')" onMouseOver="return s('33041  Gomel, MI')">
<AREA COORDS="383,90,5" SHAPE="CIRCLE" HREF="javascript:g('33345')" onMouseOver="return s('33345  Kyiv, KI (UKKK)')">
<AREA COORDS="390,74,5" SHAPE="CIRCLE" HREF="javascript:g('33791')" onMouseOver="return s('33791  Kryvyi Rih, KI')">
<AREA COORDS="366,77,5" SHAPE="CIRCLE" HREF="javascript:g('34009')" onMouseOver="return s('34009  Kursk, MS')">
<AREA COORDS="359,68,5" SHAPE="CIRCLE" HREF="javascript:g('34122')" onMouseOver="return s('34122  Voronez, MS (UUOO)')">
<AREA COORDS="343,50,5" SHAPE="CIRCLE" HREF="javascript:g('34172')" onMouseOver="return s('34172  Saratov, MS')">
<AREA COORDS="361,58,5" SHAPE="CIRCLE" HREF="javascript:g('34247')" onMouseOver="return s('34247  Kalac, MS')">
<AREA COORDS="359,43,5" SHAPE="CIRCLE" HREF="javascript:g('34560')" onMouseOver="return s('34560  Volgograd, TB (URWW)')">
<AREA COORDS="378,50,5" SHAPE="CIRCLE" HREF="javascript:g('34731')" onMouseOver="return s('34731  Rostov-Na-Donu, TB (URRR)')">
<AREA COORDS="374,34,5" SHAPE="CIRCLE" HREF="javascript:g('34858')" onMouseOver="return s('34858  Divnoe, TB')">
<AREA COORDS="359,22,5" SHAPE="CIRCLE" HREF="javascript:g('34880')" onMouseOver="return s('34880  Astrahan, TB')">
<AREA COORDS="317,29,5" SHAPE="CIRCLE" HREF="javascript:g('35121')" onMouseOver="return s('35121  Orenburg, AL')">
<AREA COORDS="316,18,5" SHAPE="CIRCLE" HREF="javascript:g('35229')" onMouseOver="return s('35229  Aktjubinsk, AL (UATT)')">
<AREA COORDS="343,15,5" SHAPE="CIRCLE" HREF="javascript:g('35700')" onMouseOver="return s('35700  Atyran, AL')">
<AREA COORDS="245,1,5" SHAPE="CIRCLE" HREF="javascript:g('36003')" onMouseOver="return s('36003  Pavlodar, AL')">
<AREA COORDS="395,40,5" SHAPE="CIRCLE" HREF="javascript:g('37018')" onMouseOver="return s('37018  Tuapse, TB')">
<AREA COORDS="383,27,5" SHAPE="CIRCLE" HREF="javascript:g('37054')" onMouseOver="return s('37054  Mineralnye Vody, TB (URMM)')">
<AREA COORDS="8,48,5" SHAPE="CIRCLE" HREF="javascript:g('47401')" onMouseOver="return s('47401  Wakkanai')">
<AREA COORDS="89,7,5" SHAPE="CIRCLE" HREF="javascript:g('50527')" onMouseOver="return s('50527  Hailar, SY')">
<AREA COORDS="71,18,5" SHAPE="CIRCLE" HREF="javascript:g('50557')" onMouseOver="return s('50557  Nenjiang, SY')">
<AREA COORDS="54,20,5" SHAPE="CIRCLE" HREF="javascript:g('50774')" onMouseOver="return s('50774  Yichun, SY')">
<AREA COORDS="54,5,5" SHAPE="CIRCLE" HREF="javascript:g('50953')" onMouseOver="return s('50953  Harbin, SY')">
<AREA COORDS="109,238,5" SHAPE="CIRCLE" HREF="javascript:g('70026')" onMouseOver="return s('70026  Barrow/W. Post W.Rogers, AK (PABR)')">
<AREA COORDS="83,235,5" SHAPE="CIRCLE" HREF="javascript:g('70133')" onMouseOver="return s('70133  Kotzebue, Ralph Wien, AK (PAOT)')">
<AREA COORDS="69,233,5" SHAPE="CIRCLE" HREF="javascript:g('70200')" onMouseOver="return s('70200  Nome, AK (PAOM)')">
<AREA COORDS="52,247,5" SHAPE="CIRCLE" HREF="javascript:g('70219')" onMouseOver="return s('70219  Bethel/Bethel Airport, AK (PABE)')">
<AREA COORDS="69,258,5" SHAPE="CIRCLE" HREF="javascript:g('70231')" onMouseOver="return s('70231  Mcgrath, AK (PAMC)')">
<AREA COORDS="86,270,5" SHAPE="CIRCLE" HREF="javascript:g('70261')" onMouseOver="return s('70261  Fairbanks/Int, AK (PAFA)')">
<AREA COORDS="66,275,5" SHAPE="CIRCLE" HREF="javascript:g('70273')" onMouseOver="return s('70273  Anchorage/Int, AK (PANC)')">
<AREA COORDS="26,229,5" SHAPE="CIRCLE" HREF="javascript:g('70308')" onMouseOver="return s('70308  St. Paul, AK (PASN)')">
<AREA COORDS="21,254,5" SHAPE="CIRCLE" HREF="javascript:g('70316')" onMouseOver="return s('70316  Cold Bay, AK (PACD)')">
<AREA COORDS="46,265,5" SHAPE="CIRCLE" HREF="javascript:g('70326')" onMouseOver="return s('70326  King Salmon, AK (PAKN)')">
<AREA COORDS="46,278,5" SHAPE="CIRCLE" HREF="javascript:g('70350')" onMouseOver="return s('70350  Kodiak, AK (PADQ)')">
<AREA COORDS="75,304,5" SHAPE="CIRCLE" HREF="javascript:g('70361')" onMouseOver="return s('70361  Yakutat, AK (PAYA)')">
<AREA COORDS="75,339,5" SHAPE="CIRCLE" HREF="javascript:g('70398')" onMouseOver="return s('70398  Annette Island, AK (PANT)')">
<AREA COORDS="121,303,5" SHAPE="CIRCLE" HREF="javascript:g('71043')" onMouseOver="return s('71043  Norman Wells Ua, NT (YVQ)')">
<AREA COORDS="216,309,5" SHAPE="CIRCLE" HREF="javascript:g('71081')" onMouseOver="return s('71081  Hall Beach, NT (YUX)')">
<AREA COORDS="217,234,5" SHAPE="CIRCLE" HREF="javascript:g('71082')" onMouseOver="return s('71082  Alert, NT (WLT)')">
<AREA COORDS="70,368,5" SHAPE="CIRCLE" HREF="javascript:g('71109')" onMouseOver="return s('71109  Port Hardy, BC (YZT)')">
<AREA COORDS="119,378,5" SHAPE="CIRCLE" HREF="javascript:g('71119')" onMouseOver="return s('71119  Edmonton Stony Plain, AB (WSE)')">
<AREA COORDS="92,388,5" SHAPE="CIRCLE" HREF="javascript:g('71203')" onMouseOver="return s('71203  Kelowna Apt, BC (WLW)')">
<AREA COORDS="339,383,5" SHAPE="CIRCLE" HREF="javascript:g('71802')" onMouseOver="return s('71802  Mt Pearl, NF (AYT)')">
<AREA COORDS="286,396,5" SHAPE="CIRCLE" HREF="javascript:g('71811')" onMouseOver="return s('71811  Sept-Iles, QB (YZV)')">
<AREA COORDS="316,391,5" SHAPE="CIRCLE" HREF="javascript:g('71815')" onMouseOver="return s('71815  Stephenville, NF (YJT)')">
<AREA COORDS="297,371,5" SHAPE="CIRCLE" HREF="javascript:g('71816')" onMouseOver="return s('71816  Goose Bay, NF (YYR)')">
<AREA COORDS="254,386,5" SHAPE="CIRCLE" HREF="javascript:g('71823')" onMouseOver="return s('71823  La Grande Iv, QB (YAH)')">
<AREA COORDS="162,389,5" SHAPE="CIRCLE" HREF="javascript:g('71867')" onMouseOver="return s('71867  The Pas, MB (YQD)')">
<AREA COORDS="262,357,5" SHAPE="CIRCLE" HREF="javascript:g('71906')" onMouseOver="return s('71906  Kuujjuaq, QB (YVP)')">
<AREA COORDS="234,364,5" SHAPE="CIRCLE" HREF="javascript:g('71907')" onMouseOver="return s('71907  Inukjuak, QB (WPH)')">
<AREA COORDS="94,362,5" SHAPE="CIRCLE" HREF="javascript:g('71908')" onMouseOver="return s('71908  Prince George, PE (ZXS)')">
<AREA COORDS="250,328,5" SHAPE="CIRCLE" HREF="javascript:g('71909')" onMouseOver="return s('71909  Iqaluit, NT (YFB)')">
<AREA COORDS="187,365,5" SHAPE="CIRCLE" HREF="javascript:g('71913')" onMouseOver="return s('71913  Churchill, MB (YYQ)')">
<AREA COORDS="215,334,5" SHAPE="CIRCLE" HREF="javascript:g('71915')" onMouseOver="return s('71915  Coral Harbour, NT (YZS)')">
<AREA COORDS="203,251,5" SHAPE="CIRCLE" HREF="javascript:g('71917')" onMouseOver="return s('71917  Eureka, NT (WEU)')">
<AREA COORDS="192,279,5" SHAPE="CIRCLE" HREF="javascript:g('71924')" onMouseOver="return s('71924  Resolute, NT (YRB)')">
<AREA COORDS="171,305,5" SHAPE="CIRCLE" HREF="javascript:g('71925')" onMouseOver="return s('71925  Cambridge Bay, NT (YCB)')">
<AREA COORDS="185,334,5" SHAPE="CIRCLE" HREF="javascript:g('71926')" onMouseOver="return s('71926  Baker Lake, NT (YBK)')">
<AREA COORDS="140,347,5" SHAPE="CIRCLE" HREF="javascript:g('71934')" onMouseOver="return s('71934  Fort Smith, NT (YSM)')">
<AREA COORDS="110,339,5" SHAPE="CIRCLE" HREF="javascript:g('71945')" onMouseOver="return s('71945  Fort Nelson, BC (YYE)')">
<AREA COORDS="120,282,5" SHAPE="CIRCLE" HREF="javascript:g('71957')" onMouseOver="return s('71957  Inuvik, NT (YEV)')">
<AREA COORDS="89,309,5" SHAPE="CIRCLE" HREF="javascript:g('71964')" onMouseOver="return s('71964  Whitehorse, YT (YXY)')">
<AREA COORDS="69,387,5" SHAPE="CIRCLE" HREF="javascript:g('72797')" onMouseOver="return s('72797  Quillayute, WA (UIL)')">
<AREA COORDS="141,8,5" SHAPE="CIRCLE" HREF="javascript:g('08430')" onMouseOver="return s('08430  Murcia')">
<AREA COORDS="121,19,5" SHAPE="CIRCLE" HREF="javascript:g('08495')" onMouseOver="return s('08495  Gibraltar (LXGB)')">
<AREA COORDS="21,4,5" SHAPE="CIRCLE" HREF="javascript:g('08508')" onMouseOver="return s('08508  Lajes/Santa Rita')">
<AREA COORDS="68,39,5" SHAPE="CIRCLE" HREF="javascript:g('08522')" onMouseOver="return s('08522  Funchal')">
<AREA COORDS="104,4,5" SHAPE="CIRCLE" HREF="javascript:g('08579')" onMouseOver="return s('08579  Lisboa/Gago Coutinho')">
<AREA COORDS="204,9,5" SHAPE="CIRCLE" HREF="javascript:g('16429')" onMouseOver="return s('16429  Trapani/Birgi (LICT)')">
<AREA COORDS="188,1,5" SHAPE="CIRCLE" HREF="javascript:g('16560')" onMouseOver="return s('16560  Cagliari/Elmas (LIEE)')">
<AREA COORDS="256,9,5" SHAPE="CIRCLE" HREF="javascript:g('16716')" onMouseOver="return s('16716  Athinai (Airport) (LGAT)')">
<AREA COORDS="272,6,5" SHAPE="CIRCLE" HREF="javascript:g('17220')" onMouseOver="return s('17220  Izmir/Guzelyali')">
<AREA COORDS="288,10,5" SHAPE="CIRCLE" HREF="javascript:g('17240')" onMouseOver="return s('17240  Isparta (LTBM)')">
<AREA COORDS="332,11,5" SHAPE="CIRCLE" HREF="javascript:g('17281')" onMouseOver="return s('17281  Diyarbakir')">
<AREA COORDS="310,14,5" SHAPE="CIRCLE" HREF="javascript:g('17351')" onMouseOver="return s('17351  Adana/Bolge')">
<AREA COORDS="297,27,5" SHAPE="CIRCLE" HREF="javascript:g('17600')" onMouseOver="return s('17600  Paphos Airport (LCPH)')">
<AREA COORDS="301,25,5" SHAPE="CIRCLE" HREF="javascript:g('17607')" onMouseOver="return s('17607  Athalassa (LCNC)')">
<AREA COORDS="302,26,5" SHAPE="CIRCLE" HREF="javascript:g('17609')" onMouseOver="return s('17609  Larnaca Airport (LCLK)')">
<AREA COORDS="308,42,5" SHAPE="CIRCLE" HREF="javascript:g('40179')" onMouseOver="return s('40179  Bet Dagan')">
<AREA COORDS="316,62,5" SHAPE="CIRCLE" HREF="javascript:g('40375')" onMouseOver="return s('40375  Tabuk (OETB)')">
<AREA COORDS="340,67,5" SHAPE="CIRCLE" HREF="javascript:g('40394')" onMouseOver="return s('40394  Hail (OEHL)')">
<AREA COORDS="377,72,5" SHAPE="CIRCLE" HREF="javascript:g('40417')" onMouseOver="return s('40417  K.F.I.A.-Dammam (OEDF)')">
<AREA COORDS="330,81,5" SHAPE="CIRCLE" HREF="javascript:g('40430')" onMouseOver="return s('40430  Al-Madinah (OEMA)')">
<AREA COORDS="363,80,5" SHAPE="CIRCLE" HREF="javascript:g('40437')" onMouseOver="return s('40437  King Khaled Intl Arpt (OERK)')">
<AREA COORDS="369,57,5" SHAPE="CIRCLE" HREF="javascript:g('40582')" onMouseOver="return s('40582  Kuwait Intl Arpt (OKBK)')">
<AREA COORDS="423,18,5" SHAPE="CIRCLE" HREF="javascript:g('40745')" onMouseOver="return s('40745  Mashhad (OIMM)')">
<AREA COORDS="384,22,5" SHAPE="CIRCLE" HREF="javascript:g('40754')" onMouseOver="return s('40754  Tehran-Mehrabad (OIII)')">
<AREA COORDS="365,30,5" SHAPE="CIRCLE" HREF="javascript:g('40766')" onMouseOver="return s('40766  Kermanshah (OICC)')">
<AREA COORDS="421,37,5" SHAPE="CIRCLE" HREF="javascript:g('40809')" onMouseOver="return s('40809  Birjand (OIMB)')">
<AREA COORDS="410,52,5" SHAPE="CIRCLE" HREF="javascript:g('40841')" onMouseOver="return s('40841  Kerman (OIKK)')">
<AREA COORDS="452,45,5" SHAPE="CIRCLE" HREF="javascript:g('40990')" onMouseOver="return s('40990  Kandahar Airport (OAKN)')">
<AREA COORDS="328,96,5" SHAPE="CIRCLE" HREF="javascript:g('41024')" onMouseOver="return s('41024  Jeddah (King Abdul Aziz) (OEJN)')">
<AREA COORDS="344,113,5" SHAPE="CIRCLE" HREF="javascript:g('41112')" onMouseOver="return s('41112  Abha (OEAB)')">
<AREA COORDS="400,82,5" SHAPE="CIRCLE" HREF="javascript:g('41217')" onMouseOver="return s('41217  Abu Dhabi Inter Arpt (OMAA)')">
<AREA COORDS="433,79,5" SHAPE="CIRCLE" HREF="javascript:g('41756')" onMouseOver="return s('41756  Jiwani (OPJI)')">
<AREA COORDS="458,80,5" SHAPE="CIRCLE" HREF="javascript:g('41780')" onMouseOver="return s('41780  Karachi Airport (OPKC)')">
<AREA COORDS="70,61,5" SHAPE="CIRCLE" HREF="javascript:g('60018')" onMouseOver="return s('60018  Guimar-Tenerife')">
<AREA COORDS="161,16,5" SHAPE="CIRCLE" HREF="javascript:g('60390')" onMouseOver="return s('60390  Dar-El-Beida (DAAG)')">
<AREA COORDS="136,45,5" SHAPE="CIRCLE" HREF="javascript:g('60571')" onMouseOver="return s('60571  Bechar (DAOR)')">
<AREA COORDS="158,68,5" SHAPE="CIRCLE" HREF="javascript:g('60630')" onMouseOver="return s('60630  In-Salah')">
<AREA COORDS="108,65,5" SHAPE="CIRCLE" HREF="javascript:g('60656')" onMouseOver="return s('60656  Tindouf (DAOF)')">
<AREA COORDS="171,90,5" SHAPE="CIRCLE" HREF="javascript:g('60680')" onMouseOver="return s('60680  Tamanrasset')">
<AREA COORDS="194,15,5" SHAPE="CIRCLE" HREF="javascript:g('60715')" onMouseOver="return s('60715  Tunis-Carthage (DTTA)')">
<AREA COORDS="184,32,5" SHAPE="CIRCLE" HREF="javascript:g('60760')" onMouseOver="return s('60760  Tozeur (DTTZ)')">
<AREA COORDS="183,119,5" SHAPE="CIRCLE" HREF="javascript:g('61024')" onMouseOver="return s('61024  Agadez (DRZA)')">
<AREA COORDS="156,136,5" SHAPE="CIRCLE" HREF="javascript:g('61052')" onMouseOver="return s('61052  Niamey-Aero (DRRN)')">
<AREA COORDS="127,131,5" SHAPE="CIRCLE" HREF="javascript:g('61265')" onMouseOver="return s('61265  Mopti (GAMB)')">
<AREA COORDS="65,130,5" SHAPE="CIRCLE" HREF="javascript:g('61641')" onMouseOver="return s('61641  Dakar/Yoff (GOOY)')">
<AREA COORDS="120,274,5" SHAPE="CIRCLE" HREF="javascript:g('61901')" onMouseOver="return s('61901  St. Helena Is.')">
<AREA COORDS="404,298,5" SHAPE="CIRCLE" HREF="javascript:g('61980')" onMouseOver="return s('61980  Saint-Denis/Gillot (FMEE)')">
<AREA COORDS="292,54,5" SHAPE="CIRCLE" HREF="javascript:g('62378')" onMouseOver="return s('62378  Helwan')">
<AREA COORDS="298,73,5" SHAPE="CIRCLE" HREF="javascript:g('62403')" onMouseOver="return s('62403  South Of Valley Univ')">
<AREA COORDS="276,69,5" SHAPE="CIRCLE" HREF="javascript:g('62423')" onMouseOver="return s('62423  Farafra')">
<AREA COORDS="232,179,5" SHAPE="CIRCLE" HREF="javascript:g('64650')" onMouseOver="return s('64650  Bangui (FEFF)')">
<AREA COORDS="216,142,5" SHAPE="CIRCLE" HREF="javascript:g('64700')" onMouseOver="return s('64700  Ndjamena (FTTJ)')">
<AREA COORDS="191,180,5" SHAPE="CIRCLE" HREF="javascript:g('64910')" onMouseOver="return s('64910  Douala R.S. (FKKD)')">
<AREA COORDS="139,141,5" SHAPE="CIRCLE" HREF="javascript:g('65503')" onMouseOver="return s('65503  Ouagadougou (DFFD)')">
<AREA COORDS="361,273,5" SHAPE="CIRCLE" HREF="javascript:g('67027')" onMouseOver="return s('67027  Majunga (FMNM)')">
<AREA COORDS="366,288,5" SHAPE="CIRCLE" HREF="javascript:g('67083')" onMouseOver="return s('67083  Antananarivo/Ivato (FMMI)')">
<AREA COORDS="375,284,5" SHAPE="CIRCLE" HREF="javascript:g('67095')" onMouseOver="return s('67095  Tamatave (FMMT)')">
<AREA COORDS="364,319,5" SHAPE="CIRCLE" HREF="javascript:g('67197')" onMouseOver="return s('67197  Fort-Dauphin (FMSD)')">
<AREA COORDS="268,340,5" SHAPE="CIRCLE" HREF="javascript:g('68442')" onMouseOver="return s('68442  Bloemfontein Airport (FABL)')">
<AREA COORDS="203,2,5" SHAPE="CIRCLE" HREF="javascript:g('29862')" onMouseOver="return s('29862  Hakasskaja, NO')">
<AREA COORDS="277,5,5" SHAPE="CIRCLE" HREF="javascript:g('30635')" onMouseOver="return s('30635  Ust-Barguzin, IR')">
<AREA COORDS="255,13,5" SHAPE="CIRCLE" HREF="javascript:g('30715')" onMouseOver="return s('30715  Angarsk, IR')">
<AREA COORDS="297,12,5" SHAPE="CIRCLE" HREF="javascript:g('30758')" onMouseOver="return s('30758  Chita, IR (UIAA)')">
<AREA COORDS="278,26,5" SHAPE="CIRCLE" HREF="javascript:g('30935')" onMouseOver="return s('30935  Krasnyj Chikoj, IR')">
<AREA COORDS="312,21,5" SHAPE="CIRCLE" HREF="javascript:g('30965')" onMouseOver="return s('30965  Borzja, IR')">
<AREA COORDS="359,8,5" SHAPE="CIRCLE" HREF="javascript:g('31510')" onMouseOver="return s('31510  Blagovescensk, HA')">
<AREA COORDS="396,9,5" SHAPE="CIRCLE" HREF="javascript:g('31736')" onMouseOver="return s('31736  Habarovsk, HA')">
<AREA COORDS="397,29,5" SHAPE="CIRCLE" HREF="javascript:g('31873')" onMouseOver="return s('31873  Dalnerechensk, HA')">
<AREA COORDS="396,48,5" SHAPE="CIRCLE" HREF="javascript:g('31977')" onMouseOver="return s('31977  Vladivostok (Sad Gorod), HA')">
<AREA COORDS="433,4,5" SHAPE="CIRCLE" HREF="javascript:g('32150')" onMouseOver="return s('32150  Juzhno-Sahalinsk, HA (UHSS)')">
<AREA COORDS="120,14,5" SHAPE="CIRCLE" HREF="javascript:g('35394')" onMouseOver="return s('35394  Karaganda, AL')">
<AREA COORDS="92,19,5" SHAPE="CIRCLE" HREF="javascript:g('35671')" onMouseOver="return s('35671  Zhezkazgan, AL')">
<AREA COORDS="141,2,5" SHAPE="CIRCLE" HREF="javascript:g('36003')" onMouseOver="return s('36003  Pavlodar, AL')">
<AREA COORDS="215,18,5" SHAPE="CIRCLE" HREF="javascript:g('36096')" onMouseOver="return s('36096  Kyzyl, NO')">
<AREA COORDS="98,57,5" SHAPE="CIRCLE" HREF="javascript:g('38341')" onMouseOver="return s('38341  Zhambyl, AL')">
<AREA COORDS="23,75,5" SHAPE="CIRCLE" HREF="javascript:g('40745')" onMouseOver="return s('40745  Mashhad (OIMM)')">
<AREA COORDS="11,95,5" SHAPE="CIRCLE" HREF="javascript:g('40809')" onMouseOver="return s('40809  Birjand (OIMB)')">
<AREA COORDS="42,120,5" SHAPE="CIRCLE" HREF="javascript:g('40990')" onMouseOver="return s('40990  Kandahar Airport (OAKN)')">
<AREA COORDS="1,151,5" SHAPE="CIRCLE" HREF="javascript:g('41756')" onMouseOver="return s('41756  Jiwani (OPJI)')">
<AREA COORDS="32,165,5" SHAPE="CIRCLE" HREF="javascript:g('41780')" onMouseOver="return s('41780  Karachi Airport (OPKC)')">
<AREA COORDS="101,160,5" SHAPE="CIRCLE" HREF="javascript:g('42182')" onMouseOver="return s('42182  New Delhi/Safdarjung (VIDD)')">
<AREA COORDS="200,204,5" SHAPE="CIRCLE" HREF="javascript:g('42623')" onMouseOver="return s('42623  Imphal (VEIM)')">
<AREA COORDS="94,310,5" SHAPE="CIRCLE" HREF="javascript:g('43418')" onMouseOver="return s('43418  Trincomalee (VCCT)')">
<AREA COORDS="80,321,5" SHAPE="CIRCLE" HREF="javascript:g('43466')" onMouseOver="return s('43466  Colombo')">
<AREA COORDS="89,329,5" SHAPE="CIRCLE" HREF="javascript:g('43497')" onMouseOver="return s('43497  Hambantota')">
<AREA COORDS="204,29,5" SHAPE="CIRCLE" HREF="javascript:g('44212')" onMouseOver="return s('44212  Ulaan-Gom')">
<AREA COORDS="271,44,5" SHAPE="CIRCLE" HREF="javascript:g('44292')" onMouseOver="return s('44292  Ulaan-Baator')">
<AREA COORDS="261,74,5" SHAPE="CIRCLE" HREF="javascript:g('44373')" onMouseOver="return s('44373  Dalanzadgad')">
<AREA COORDS="333,215,5" SHAPE="CIRCLE" HREF="javascript:g('45004')" onMouseOver="return s('45004  Kings Park')">
<AREA COORDS="390,87,5" SHAPE="CIRCLE" HREF="javascript:g('47090')" onMouseOver="return s('47090  Sokcho')">
<AREA COORDS="370,95,5" SHAPE="CIRCLE" HREF="javascript:g('47102')" onMouseOver="return s('47102  Baengnyeongdo')">
<AREA COORDS="385,97,5" SHAPE="CIRCLE" HREF="javascript:g('47122')" onMouseOver="return s('47122  Osan Ab (RKSO)')">
<AREA COORDS="399,100,5" SHAPE="CIRCLE" HREF="javascript:g('47138')" onMouseOver="return s('47138  Pohang')">
<AREA COORDS="388,110,5" SHAPE="CIRCLE" HREF="javascript:g('47158')" onMouseOver="return s('47158  Kwangju Ab (RKJJ)')">
<AREA COORDS="388,124,5" SHAPE="CIRCLE" HREF="javascript:g('47185')" onMouseOver="return s('47185  Cheju Upper/Radar')">
<AREA COORDS="433,16,5" SHAPE="CIRCLE" HREF="javascript:g('47401')" onMouseOver="return s('47401  Wakkanai')">
<AREA COORDS="439,31,5" SHAPE="CIRCLE" HREF="javascript:g('47412')" onMouseOver="return s('47412  Sapporo')">
<AREA COORDS="446,45,5" SHAPE="CIRCLE" HREF="javascript:g('47580')" onMouseOver="return s('47580  Misawa Ab (RJSM)')">
<AREA COORDS="443,54,5" SHAPE="CIRCLE" HREF="javascript:g('47582')" onMouseOver="return s('47582  Akita')">
<AREA COORDS="434,76,5" SHAPE="CIRCLE" HREF="javascript:g('47600')" onMouseOver="return s('47600  Wajima')">
<AREA COORDS="454,77,5" SHAPE="CIRCLE" HREF="javascript:g('47646')" onMouseOver="return s('47646  Tateno')">
<AREA COORDS="461,96,5" SHAPE="CIRCLE" HREF="javascript:g('47678')" onMouseOver="return s('47678  Hachijyojima/Omure')">
<AREA COORDS="446,91,5" SHAPE="CIRCLE" HREF="javascript:g('47681')" onMouseOver="return s('47681  Hamamatsu Ab (RJNH)')">
<AREA COORDS="439,103,5" SHAPE="CIRCLE" HREF="javascript:g('47778')" onMouseOver="return s('47778  Shionomisaki')">
<AREA COORDS="410,114,5" SHAPE="CIRCLE" HREF="javascript:g('47807')" onMouseOver="return s('47807  Fukuoka')">
<AREA COORDS="416,127,5" SHAPE="CIRCLE" HREF="javascript:g('47827')" onMouseOver="return s('47827  Kagoshima')">
<AREA COORDS="417,150,5" SHAPE="CIRCLE" HREF="javascript:g('47909')" onMouseOver="return s('47909  Naze/Funchatoge')">
<AREA COORDS="394,187,5" SHAPE="CIRCLE" HREF="javascript:g('47918')" onMouseOver="return s('47918  Ishigakijima (ROIG)')">
<AREA COORDS="433,163,5" SHAPE="CIRCLE" HREF="javascript:g('47945')" onMouseOver="return s('47945  Minamidaitojima (ROMD)')">
<AREA COORDS="232,248,5" SHAPE="CIRCLE" HREF="javascript:g('48327')" onMouseOver="return s('48327  Chiang Mai (VTCC)')">
<AREA COORDS="259,258,5" SHAPE="CIRCLE" HREF="javascript:g('48354')" onMouseOver="return s('48354  Udon Thani (VTUD)')">
<AREA COORDS="241,263,5" SHAPE="CIRCLE" HREF="javascript:g('48378')" onMouseOver="return s('48378  Phitsanulok (VTPS)')">
<AREA COORDS="274,273,5" SHAPE="CIRCLE" HREF="javascript:g('48407')" onMouseOver="return s('48407  Ubon Ratchathani (VTUU)')">
<AREA COORDS="254,276,5" SHAPE="CIRCLE" HREF="javascript:g('48431')" onMouseOver="return s('48431  Nakhon Ratchasima (VTUN)')">
<AREA COORDS="246,294,5" SHAPE="CIRCLE" HREF="javascript:g('48477')" onMouseOver="return s('48477  Sattahip')">
<AREA COORDS="255,294,5" SHAPE="CIRCLE" HREF="javascript:g('48480')" onMouseOver="return s('48480  Chanthaburi (VTBC)')">
<AREA COORDS="238,300,5" SHAPE="CIRCLE" HREF="javascript:g('48500')" onMouseOver="return s('48500  Prachuap Khirikhan (VTBP)')">
<AREA COORDS="234,321,5" SHAPE="CIRCLE" HREF="javascript:g('48551')" onMouseOver="return s('48551  Surat Thani (VTSB)')">
<AREA COORDS="226,329,5" SHAPE="CIRCLE" HREF="javascript:g('48565')" onMouseOver="return s('48565  Phuket Airport (VTSP)')">
<AREA COORDS="244,336,5" SHAPE="CIRCLE" HREF="javascript:g('48568')" onMouseOver="return s('48568  Songkhla (VTSH)')">
<AREA COORDS="241,352,5" SHAPE="CIRCLE" HREF="javascript:g('48601')" onMouseOver="return s('48601  Penang/Bayan Lepas (WMKP)')">
<AREA COORDS="257,345,5" SHAPE="CIRCLE" HREF="javascript:g('48615')" onMouseOver="return s('48615  Kota Bharu (WMKC)')">
<AREA COORDS="253,373,5" SHAPE="CIRCLE" HREF="javascript:g('48650')" onMouseOver="return s('48650  Sepang')">
<AREA COORDS="265,364,5" SHAPE="CIRCLE" HREF="javascript:g('48657')" onMouseOver="return s('48657  Kuantan (WMKD)')">
<AREA COORDS="273,384,5" SHAPE="CIRCLE" HREF="javascript:g('48698')" onMouseOver="return s('48698  Singapore/Changi Arpt (WSSS)')">
<AREA COORDS="278,231,5" SHAPE="CIRCLE" HREF="javascript:g('48820')" onMouseOver="return s('48820  Ha Noi (VVNB)')">
<AREA COORDS="298,266,5" SHAPE="CIRCLE" HREF="javascript:g('48855')" onMouseOver="return s('48855  Da Nang (VVDN)')">
<AREA COORDS="290,306,5" SHAPE="CIRCLE" HREF="javascript:g('48900')" onMouseOver="return s('48900  Ho Chi Minh (VVTS)')">
<AREA COORDS="328,26,5" SHAPE="CIRCLE" HREF="javascript:g('50527')" onMouseOver="return s('50527  Hailar, SY')">
<AREA COORDS="352,20,5" SHAPE="CIRCLE" HREF="javascript:g('50557')" onMouseOver="return s('50557  Nenjiang, SY')">
<AREA COORDS="371,25,5" SHAPE="CIRCLE" HREF="javascript:g('50774')" onMouseOver="return s('50774  Yichun, SY')">
<AREA COORDS="366,41,5" SHAPE="CIRCLE" HREF="javascript:g('50953')" onMouseOver="return s('50953  Harbin, SY')">
<AREA COORDS="184,43,5" SHAPE="CIRCLE" HREF="javascript:g('51076')" onMouseOver="return s('51076  Altay, UQ')">
<AREA COORDS="147,63,5" SHAPE="CIRCLE" HREF="javascript:g('51431')" onMouseOver="return s('51431  Yining, UQ (ZWYN)')">
<AREA COORDS="178,69,5" SHAPE="CIRCLE" HREF="javascript:g('51463')" onMouseOver="return s('51463  Urumqi, UQ')">
<AREA COORDS="152,79,5" SHAPE="CIRCLE" HREF="javascript:g('51644')" onMouseOver="return s('51644  Kuqa, UQ')">
<AREA COORDS="113,86,5" SHAPE="CIRCLE" HREF="javascript:g('51709')" onMouseOver="return s('51709  Kashi, UQ (ZWSH)')">
<AREA COORDS="176,102,5" SHAPE="CIRCLE" HREF="javascript:g('51777')" onMouseOver="return s('51777  Ruoqiang, UQ')">
<AREA COORDS="130,107,5" SHAPE="CIRCLE" HREF="javascript:g('51828')" onMouseOver="return s('51828  Hotan, UQ (ZWTN)')">
<AREA COORDS="145,110,5" SHAPE="CIRCLE" HREF="javascript:g('51839')" onMouseOver="return s('51839  Minfeng, UQ')">
<AREA COORDS="206,79,5" SHAPE="CIRCLE" HREF="javascript:g('52203')" onMouseOver="return s('52203  Hami, UQ (ZWHM)')">
<AREA COORDS="244,86,5" SHAPE="CIRCLE" HREF="javascript:g('52267')" onMouseOver="return s('52267  Ejin Qi, LZ')">
<AREA COORDS="224,87,5" SHAPE="CIRCLE" HREF="javascript:g('52323')" onMouseOver="return s('52323  Mazong Shan, LZ')">
<AREA COORDS="211,98,5" SHAPE="CIRCLE" HREF="javascript:g('52418')" onMouseOver="return s('52418  Dunhuang, LZ')">
<AREA COORDS="231,101,5" SHAPE="CIRCLE" HREF="javascript:g('52533')" onMouseOver="return s('52533  Jiuquan, LZ (ZLJQ)')">
<AREA COORDS="255,109,5" SHAPE="CIRCLE" HREF="javascript:g('52681')" onMouseOver="return s('52681  Minqin, LZ')">
<AREA COORDS="211,123,5" SHAPE="CIRCLE" HREF="javascript:g('52818')" onMouseOver="return s('52818  Golmud, LZ')">
<AREA COORDS="228,125,5" SHAPE="CIRCLE" HREF="javascript:g('52836')" onMouseOver="return s('52836  Dulan, LZ')">
<AREA COORDS="249,122,5" SHAPE="CIRCLE" HREF="javascript:g('52866')" onMouseOver="return s('52866  Xining, LZ (ZLXN)')">
<AREA COORDS="262,127,5" SHAPE="CIRCLE" HREF="javascript:g('52983')" onMouseOver="return s('52983  Yu Zhong, LZ')">
<AREA COORDS="298,70,5" SHAPE="CIRCLE" HREF="javascript:g('53068')" onMouseOver="return s('53068  Erenhot, BJ')">
<AREA COORDS="299,90,5" SHAPE="CIRCLE" HREF="javascript:g('53463')" onMouseOver="return s('53463  Hohhot, BJ (ZBHH)')">
<AREA COORDS="277,93,5" SHAPE="CIRCLE" HREF="javascript:g('53513')" onMouseOver="return s('53513  Linhe, BJ')">
<AREA COORDS="272,109,5" SHAPE="CIRCLE" HREF="javascript:g('53614')" onMouseOver="return s('53614  Yinchuan, LZ (ZLIC)')">
<AREA COORDS="307,110,5" SHAPE="CIRCLE" HREF="javascript:g('53772')" onMouseOver="return s('53772  Taiyuan, BJ (ZBYN)')">
<AREA COORDS="291,120,5" SHAPE="CIRCLE" HREF="javascript:g('53845')" onMouseOver="return s('53845  Yan An, LZ (ZLYA)')">
<AREA COORDS="276,129,5" SHAPE="CIRCLE" HREF="javascript:g('53915')" onMouseOver="return s('53915  Pingliang, LZ')">
<AREA COORDS="318,65,5" SHAPE="CIRCLE" HREF="javascript:g('54102')" onMouseOver="return s('54102  Xilin Hot, BJ')">
<AREA COORDS="348,61,5" SHAPE="CIRCLE" HREF="javascript:g('54135')" onMouseOver="return s('54135  Tongliao, SY')">
<AREA COORDS="362,55,5" SHAPE="CIRCLE" HREF="javascript:g('54161')" onMouseOver="return s('54161  Changchun, SY (ZYCC)')">
<AREA COORDS="334,74,5" SHAPE="CIRCLE" HREF="javascript:g('54218')" onMouseOver="return s('54218  Chifeng, SY')">
<AREA COORDS="384,55,5" SHAPE="CIRCLE" HREF="javascript:g('54292')" onMouseOver="return s('54292  Yanji, SY')">
<AREA COORDS="357,72,5" SHAPE="CIRCLE" HREF="javascript:g('54342')" onMouseOver="return s('54342  Shenyang, SY (ZYYY)')">
<AREA COORDS="375,67,5" SHAPE="CIRCLE" HREF="javascript:g('54374')" onMouseOver="return s('54374  Linjiang, SY')">
<AREA COORDS="324,92,5" SHAPE="CIRCLE" HREF="javascript:g('54511')" onMouseOver="return s('54511  Beijing, BJ (ZBAA)')">
<AREA COORDS="353,93,5" SHAPE="CIRCLE" HREF="javascript:g('54662')" onMouseOver="return s('54662  Dalian, BJ (ZYTL)')">
<AREA COORDS="351,114,5" SHAPE="CIRCLE" HREF="javascript:g('54857')" onMouseOver="return s('54857  Qingdao, BJ (ZSQD)')">
<AREA COORDS="192,156,5" SHAPE="CIRCLE" HREF="javascript:g('55299')" onMouseOver="return s('55299  Nagqu, CD')">
<AREA COORDS="185,168,5" SHAPE="CIRCLE" HREF="javascript:g('55591')" onMouseOver="return s('55591  Lhasa, CD (ZULS)')">
<AREA COORDS="222,147,5" SHAPE="CIRCLE" HREF="javascript:g('56029')" onMouseOver="return s('56029  Yushu, LZ')">
<AREA COORDS="255,133,5" SHAPE="CIRCLE" HREF="javascript:g('56080')" onMouseOver="return s('56080  Hezuo, LZ')">
<AREA COORDS="222,160,5" SHAPE="CIRCLE" HREF="javascript:g('56137')" onMouseOver="return s('56137  Qamdo, CD')">
<AREA COORDS="239,157,5" SHAPE="CIRCLE" HREF="javascript:g('56146')" onMouseOver="return s('56146  Garze, CD')">
<AREA COORDS="253,183,5" SHAPE="CIRCLE" HREF="javascript:g('56571')" onMouseOver="return s('56571  Xichang, CD')">
<AREA COORDS="266,190,5" SHAPE="CIRCLE" HREF="javascript:g('56691')" onMouseOver="return s('56691  Weining, CD')">
<AREA COORDS="229,203,5" SHAPE="CIRCLE" HREF="javascript:g('56739')" onMouseOver="return s('56739  Tengchong, CD')">
<AREA COORDS="256,203,5" SHAPE="CIRCLE" HREF="javascript:g('56778')" onMouseOver="return s('56778  Kunming, CD (ZPPP)')">
<AREA COORDS="245,219,5" SHAPE="CIRCLE" HREF="javascript:g('56964')" onMouseOver="return s('56964  Simao, CD')">
<AREA COORDS="261,215,5" SHAPE="CIRCLE" HREF="javascript:g('56985')" onMouseOver="return s('56985  Mengzi, CD')">
<AREA COORDS="316,130,5" SHAPE="CIRCLE" HREF="javascript:g('57083')" onMouseOver="return s('57083  Zhengzhou, BJ (ZHCC)')">
<AREA COORDS="280,146,5" SHAPE="CIRCLE" HREF="javascript:g('57127')" onMouseOver="return s('57127  Hanzhong, LZ')">
<AREA COORDS="312,142,5" SHAPE="CIRCLE" HREF="javascript:g('57178')" onMouseOver="return s('57178  Nanyang, BJ')">
<AREA COORDS="296,163,5" SHAPE="CIRCLE" HREF="javascript:g('57447')" onMouseOver="return s('57447  Enshi, HK')">
<AREA COORDS="306,159,5" SHAPE="CIRCLE" HREF="javascript:g('57461')" onMouseOver="return s('57461  Yichang, HK')">
<AREA COORDS="323,157,5" SHAPE="CIRCLE" HREF="javascript:g('57494')" onMouseOver="return s('57494  Wuhan, HK (ZHHH)')">
<AREA COORDS="278,170,5" SHAPE="CIRCLE" HREF="javascript:g('57516')" onMouseOver="return s('57516  Chongqing, CD (ZUCK)')">
<AREA COORDS="319,175,5" SHAPE="CIRCLE" HREF="javascript:g('57679')" onMouseOver="return s('57679  Changsha, HK (ZGCS)')">
<AREA COORDS="301,182,5" SHAPE="CIRCLE" HREF="javascript:g('57749')" onMouseOver="return s('57749  Huaihua, HK')">
<AREA COORDS="281,191,5" SHAPE="CIRCLE" HREF="javascript:g('57816')" onMouseOver="return s('57816  Guiyang, CD (ZUGY)')">
<AREA COORDS="305,197,5" SHAPE="CIRCLE" HREF="javascript:g('57957')" onMouseOver="return s('57957  Guilin, GZ (ZGKL)')">
<AREA COORDS="322,192,5" SHAPE="CIRCLE" HREF="javascript:g('57972')" onMouseOver="return s('57972  Chenzhou, HK')">
<AREA COORDS="334,189,5" SHAPE="CIRCLE" HREF="javascript:g('57993')" onMouseOver="return s('57993  Ganzhou, HK (ZSGZ)')">
<AREA COORDS="336,129,5" SHAPE="CIRCLE" HREF="javascript:g('58027')" onMouseOver="return s('58027  Xuzhou, SH')">
<AREA COORDS="354,129,5" SHAPE="CIRCLE" HREF="javascript:g('58150')" onMouseOver="return s('58150  Sheyang, SH')">
<AREA COORDS="330,140,5" SHAPE="CIRCLE" HREF="javascript:g('58203')" onMouseOver="return s('58203  Fuyang, HK')">
<AREA COORDS="349,143,5" SHAPE="CIRCLE" HREF="javascript:g('58238')" onMouseOver="return s('58238  Nanjing, SH (ZSNJ)')">
<AREA COORDS="365,143,5" SHAPE="CIRCLE" HREF="javascript:g('58362')" onMouseOver="return s('58362  Shanghai, SH')">
<AREA COORDS="340,155,5" SHAPE="CIRCLE" HREF="javascript:g('58424')" onMouseOver="return s('58424  Anqing, HK')">
<AREA COORDS="359,153,5" SHAPE="CIRCLE" HREF="javascript:g('58457')" onMouseOver="return s('58457  Hangzhou, SH (ZSHC)')">
<AREA COORDS="336,169,5" SHAPE="CIRCLE" HREF="javascript:g('58606')" onMouseOver="return s('58606  Nanchang, HK (ZSCN)')">
<AREA COORDS="353,163,5" SHAPE="CIRCLE" HREF="javascript:g('58633')" onMouseOver="return s('58633  Qu Xian, SH')">
<AREA COORDS="369,162,5" SHAPE="CIRCLE" HREF="javascript:g('58665')" onMouseOver="return s('58665  Hongjia, SH')">
<AREA COORDS="347,176,5" SHAPE="CIRCLE" HREF="javascript:g('58725')" onMouseOver="return s('58725  Shaowu, SH')">
<AREA COORDS="360,183,5" SHAPE="CIRCLE" HREF="javascript:g('58847')" onMouseOver="return s('58847  Fuzhou, SH (ZSFZ)')">
<AREA COORDS="355,195,5" SHAPE="CIRCLE" HREF="javascript:g('59134')" onMouseOver="return s('59134  Xiamen, SH (ZSAM)')">
<AREA COORDS="282,210,5" SHAPE="CIRCLE" HREF="javascript:g('59211')" onMouseOver="return s('59211  Baise, GZ')">
<AREA COORDS="313,210,5" SHAPE="CIRCLE" HREF="javascript:g('59265')" onMouseOver="return s('59265  Wuzhou, GZ')">
<AREA COORDS="324,207,5" SHAPE="CIRCLE" HREF="javascript:g('59280')" onMouseOver="return s('59280  Qing Yuan, GZ')">
<AREA COORDS="348,205,5" SHAPE="CIRCLE" HREF="javascript:g('59316')" onMouseOver="return s('59316  Shantou, GZ (ZGOW)')">
<AREA COORDS="293,218,5" SHAPE="CIRCLE" HREF="javascript:g('59431')" onMouseOver="return s('59431  Nanning, GZ (ZGNN)')">
<AREA COORDS="309,235,5" SHAPE="CIRCLE" HREF="javascript:g('59758')" onMouseOver="return s('59758  Haikou, GZ (ZGHK)')">
<AREA COORDS="326,256,5" SHAPE="CIRCLE" HREF="javascript:g('59981')" onMouseOver="return s('59981  Xisha Dao, GZ')">
<AREA COORDS="216,352,5" SHAPE="CIRCLE" HREF="javascript:g('96009')" onMouseOver="return s('96009  Lhokseumawe/Malikussaleh (WITM)')">
<AREA COORDS="202,349,5" SHAPE="CIRCLE" HREF="javascript:g('96011')" onMouseOver="return s('96011  Banda Aceh/Blang Bintang (WITT)')">
<AREA COORDS="228,366,5" SHAPE="CIRCLE" HREF="javascript:g('96035')" onMouseOver="return s('96035  Medan/Polonia (WIMM)')">
<AREA COORDS="230,383,5" SHAPE="CIRCLE" HREF="javascript:g('96073')" onMouseOver="return s('96073  Sibolga/Pinangsori (WIMS)')">
<AREA COORDS="219,383,5" SHAPE="CIRCLE" HREF="javascript:g('96075')" onMouseOver="return s('96075  Gunung Sitoli/Binaka (WIMB)')">
<AREA COORDS="278,387,5" SHAPE="CIRCLE" HREF="javascript:g('96091')" onMouseOver="return s('96091  Tanjung Pinang/Kijang (WIKN)')">
<AREA COORDS="251,392,5" SHAPE="CIRCLE" HREF="javascript:g('96109')" onMouseOver="return s('96109  Pekan Baru/Simpangtiga (WIBB)')">
<AREA COORDS="308,360,5" SHAPE="CIRCLE" HREF="javascript:g('96147')" onMouseOver="return s('96147  Ranai (WION)')">
<AREA COORDS="242,404,5" SHAPE="CIRCLE" HREF="javascript:g('96163')" onMouseOver="return s('96163  Padang/Tabing (WIMG)')">
<AREA COORDS="279,399,5" SHAPE="CIRCLE" HREF="javascript:g('96179')" onMouseOver="return s('96179  Singkep/Dabo (WIKS)')">
<AREA COORDS="271,409,5" SHAPE="CIRCLE" HREF="javascript:g('96195')" onMouseOver="return s('96195  Jambi/Sultan Taha (WIPA)')">
<AREA COORDS="281,420,5" SHAPE="CIRCLE" HREF="javascript:g('96221')" onMouseOver="return s('96221  Palembang/St. Badarudin (WIPP)')">
<AREA COORDS="293,413,5" SHAPE="CIRCLE" HREF="javascript:g('96237')" onMouseOver="return s('96237  Pangkal Pinang (WIKK)')">
<AREA COORDS="308,417,5" SHAPE="CIRCLE" HREF="javascript:g('96249')" onMouseOver="return s('96249  Tanjung Pandan/Buluh (WIKD)')">
<AREA COORDS="260,430,5" SHAPE="CIRCLE" HREF="javascript:g('96253')" onMouseOver="return s('96253  Bengkulu/Padang Kemiling (WIPL)')">
<AREA COORDS="286,440,5" SHAPE="CIRCLE" HREF="javascript:g('96295')" onMouseOver="return s('96295  Tanjung Karang/Radin (WIIT)')">
<AREA COORDS="360,345,5" SHAPE="CIRCLE" HREF="javascript:g('96315')" onMouseOver="return s('96315  Brunei Airport (WBSB)')">
<AREA COORDS="326,378,5" SHAPE="CIRCLE" HREF="javascript:g('96413')" onMouseOver="return s('96413  Kuching (WBGG)')">
<AREA COORDS="347,361,5" SHAPE="CIRCLE" HREF="javascript:g('96441')" onMouseOver="return s('96441  Bintulu (WBGB)')">
<AREA COORDS="367,335,5" SHAPE="CIRCLE" HREF="javascript:g('96471')" onMouseOver="return s('96471  Kota Kinabalu (WBKK)')">
<AREA COORDS="384,346,5" SHAPE="CIRCLE" HREF="javascript:g('96481')" onMouseOver="return s('96481  Tawau (WBKW)')">
<AREA COORDS="383,354,5" SHAPE="CIRCLE" HREF="javascript:g('96509')" onMouseOver="return s('96509  Tarakan/Juwata (WRLR)')">
<AREA COORDS="384,364,5" SHAPE="CIRCLE" HREF="javascript:g('96529')" onMouseOver="return s('96529  Tanjung Redep/Kalimarau (WRLK)')">
<AREA COORDS="320,393,5" SHAPE="CIRCLE" HREF="javascript:g('96581')" onMouseOver="return s('96581  Pontianak/Supadio (WIOO)')">
<AREA COORDS="368,393,5" SHAPE="CIRCLE" HREF="javascript:g('96595')" onMouseOver="return s('96595  Muara Teweh/Beringin (WRBM)')">
<AREA COORDS="386,387,5" SHAPE="CIRCLE" HREF="javascript:g('96607')" onMouseOver="return s('96607  Samarinda/Temindung (WRLS)')">
<AREA COORDS="385,393,5" SHAPE="CIRCLE" HREF="javascript:g('96633')" onMouseOver="return s('96633  Balikpapan/Sepinggan (WRLL)')">
<AREA COORDS="351,412,5" SHAPE="CIRCLE" HREF="javascript:g('96645')" onMouseOver="return s('96645  Pangkalan Bun/Iskandar (WRBI)')">
<AREA COORDS="370,415,5" SHAPE="CIRCLE" HREF="javascript:g('96685')" onMouseOver="return s('96685  Banjarmasin/Syamsudin (WRBB)')">
<AREA COORDS="300,448,5" SHAPE="CIRCLE" HREF="javascript:g('96749')" onMouseOver="return s('96749  Jakarta/Soekarno-Hatta (WIII)')">
<AREA COORDS="315,453,5" SHAPE="CIRCLE" HREF="javascript:g('96791')" onMouseOver="return s('96791  Cirebon/Jatiwangi')">
<AREA COORDS="324,453,5" SHAPE="CIRCLE" HREF="javascript:g('96797')" onMouseOver="return s('96797  Tegal')">
<AREA COORDS="335,453,5" SHAPE="CIRCLE" HREF="javascript:g('96839')" onMouseOver="return s('96839  Semarang/Ahmad Yani (WIIS)')">
<AREA COORDS="355,440,5" SHAPE="CIRCLE" HREF="javascript:g('96925')" onMouseOver="return s('96925  Sangkapura (Bawean Is.)')">
<AREA COORDS="358,454,5" SHAPE="CIRCLE" HREF="javascript:g('96935')" onMouseOver="return s('96935  Surabaya/Juanda (WRSJ)')">
<AREA COORDS="446,336,5" SHAPE="CIRCLE" HREF="javascript:g('97008')" onMouseOver="return s('97008  Naha/Tahuna (WAMH)')">
<AREA COORDS="447,354,5" SHAPE="CIRCLE" HREF="javascript:g('97014')" onMouseOver="return s('97014  Menado/ Sam Ratulangi (WAMM)')">
<AREA COORDS="408,383,5" SHAPE="CIRCLE" HREF="javascript:g('97072')" onMouseOver="return s('97072  Palu/Mutiara (WAML)')">
<AREA COORDS="435,379,5" SHAPE="CIRCLE" HREF="javascript:g('97086')" onMouseOver="return s('97086  Luwuk/Bubung (WAMW)')">
<AREA COORDS="406,400,5" SHAPE="CIRCLE" HREF="javascript:g('97120')" onMouseOver="return s('97120  Majene')">
<AREA COORDS="415,421,5" SHAPE="CIRCLE" HREF="javascript:g('97180')" onMouseOver="return s('97180  Ujung Pandang/Hasanuddin (WAAA)')">
<AREA COORDS="382,463,5" SHAPE="CIRCLE" HREF="javascript:g('97230')" onMouseOver="return s('97230  Denpasar/Ngurah Rai (WRRR)')">
<AREA COORDS="390,460,5" SHAPE="CIRCLE" HREF="javascript:g('97240')" onMouseOver="return s('97240  Mataram/Selaparang (WRRA)')">
<AREA COORDS="448,448,5" SHAPE="CIRCLE" HREF="javascript:g('97300')" onMouseOver="return s('97300  Maumere/Wai Oti (WRKC)')">
<AREA COORDS="432,462,5" SHAPE="CIRCLE" HREF="javascript:g('97340')" onMouseOver="return s('97340  Waingapu/Mau Hau (WRRW)')">
<AREA COORDS="464,459,5" SHAPE="CIRCLE" HREF="javascript:g('97372')" onMouseOver="return s('97372  Kupang/Eltari (WRKK)')">
<AREA COORDS="468,354,5" SHAPE="CIRCLE" HREF="javascript:g('97430')" onMouseOver="return s('97430  Ternate/Babullah (WAMT)')">
<AREA COORDS="381,236,5" SHAPE="CIRCLE" HREF="javascript:g('98223')" onMouseOver="return s('98223  Laoag (RPLI)')">
<AREA COORDS="393,261,5" SHAPE="CIRCLE" HREF="javascript:g('98433')" onMouseOver="return s('98433  Tanay')">
<AREA COORDS="413,267,5" SHAPE="CIRCLE" HREF="javascript:g('98444')" onMouseOver="return s('98444  Legaspi (RPMP)')">
<AREA COORDS="382,301,5" SHAPE="CIRCLE" HREF="javascript:g('98618')" onMouseOver="return s('98618  Puerto Princesa (RPVP)')">
<AREA COORDS="0,15,5" SHAPE="CIRCLE" HREF="javascript:g('12374')" onMouseOver="return s('12374  Legionowo')">
<AREA COORDS="47,88,5" SHAPE="CIRCLE" HREF="javascript:g('15420')" onMouseOver="return s('15420  Bucuresti Inmh-Banesa (LRBS)')">
<AREA COORDS="22,105,5" SHAPE="CIRCLE" HREF="javascript:g('15614')" onMouseOver="return s('15614  Sofia (Observ) (LBSF)')">
<AREA COORDS="25,149,5" SHAPE="CIRCLE" HREF="javascript:g('16716')" onMouseOver="return s('16716  Athinai (Airport) (LGAT)')">
<AREA COORDS="142,118,5" SHAPE="CIRCLE" HREF="javascript:g('17030')" onMouseOver="return s('17030  Samsun')">
<AREA COORDS="175,118,5" SHAPE="CIRCLE" HREF="javascript:g('17095')" onMouseOver="return s('17095  Erzurum (ERZM)')">
<AREA COORDS="75,121,5" SHAPE="CIRCLE" HREF="javascript:g('17062')" onMouseOver="return s('17062  Istanbul/Goztepe')">
<AREA COORDS="110,130,5" SHAPE="CIRCLE" HREF="javascript:g('17130')" onMouseOver="return s('17130  Ankara/Central')">
<AREA COORDS="57,144,5" SHAPE="CIRCLE" HREF="javascript:g('17220')" onMouseOver="return s('17220  Izmir/Guzelyali')">
<AREA COORDS="88,150,5" SHAPE="CIRCLE" HREF="javascript:g('17240')" onMouseOver="return s('17240  Isparta (LTBM)')">
<AREA COORDS="177,152,5" SHAPE="CIRCLE" HREF="javascript:g('17281')" onMouseOver="return s('17281  Diyarbakir')">
<AREA COORDS="133,158,5" SHAPE="CIRCLE" HREF="javascript:g('17351')" onMouseOver="return s('17351  Adana/Bolge')">
<AREA COORDS="106,179,5" SHAPE="CIRCLE" HREF="javascript:g('17600')" onMouseOver="return s('17600  Paphos Airport (LCPH)')">
<AREA COORDS="115,174,5" SHAPE="CIRCLE" HREF="javascript:g('17607')" onMouseOver="return s('17607  Athalassa (LCNC)')">
<AREA COORDS="117,177,5" SHAPE="CIRCLE" HREF="javascript:g('17609')" onMouseOver="return s('17609  Larnaca Airport (LCLK)')">
<AREA COORDS="222,8,5" SHAPE="CIRCLE" HREF="javascript:g('27962')" onMouseOver="return s('27962  Penza, MS (UWPP)')">
<AREA COORDS="263,9,5" SHAPE="CIRCLE" HREF="javascript:g('27995')" onMouseOver="return s('27995  Samara (Bezencuk), MS')">
<AREA COORDS="92,15,5" SHAPE="CIRCLE" HREF="javascript:g('33041')" onMouseOver="return s('33041  Gomel, MI')">
<AREA COORDS="88,33,5" SHAPE="CIRCLE" HREF="javascript:g('33345')" onMouseOver="return s('33345  Kyiv, KI (UKKK)')">
<AREA COORDS="113,55,5" SHAPE="CIRCLE" HREF="javascript:g('33791')" onMouseOver="return s('33791  Kryvyi Rih, KI')">
<AREA COORDS="140,21,5" SHAPE="CIRCLE" HREF="javascript:g('34009')" onMouseOver="return s('34009  Kursk, MS')">
<AREA COORDS="169,22,5" SHAPE="CIRCLE" HREF="javascript:g('34122')" onMouseOver="return s('34122  Voronez, MS (UUOO)')">
<AREA COORDS="232,22,5" SHAPE="CIRCLE" HREF="javascript:g('34172')" onMouseOver="return s('34172  Saratov, MS')">
<AREA COORDS="186,33,5" SHAPE="CIRCLE" HREF="javascript:g('34247')" onMouseOver="return s('34247  Kalac, MS')">
<AREA COORDS="216,48,5" SHAPE="CIRCLE" HREF="javascript:g('34560')" onMouseOver="return s('34560  Volgograd, TB (URWW)')">
<AREA COORDS="174,62,5" SHAPE="CIRCLE" HREF="javascript:g('34731')" onMouseOver="return s('34731  Rostov-Na-Donu, TB (URRR)')">
<AREA COORDS="207,75,5" SHAPE="CIRCLE" HREF="javascript:g('34858')" onMouseOver="return s('34858  Divnoe, TB')">
<AREA COORDS="250,71,5" SHAPE="CIRCLE" HREF="javascript:g('34880')" onMouseOver="return s('34880  Astrahan, TB')">
<AREA COORDS="316,21,5" SHAPE="CIRCLE" HREF="javascript:g('35121')" onMouseOver="return s('35121  Orenburg, AL')">
<AREA COORDS="335,34,5" SHAPE="CIRCLE" HREF="javascript:g('35229')" onMouseOver="return s('35229  Aktjubinsk, AL (UATT)')">
<AREA COORDS="286,64,5" SHAPE="CIRCLE" HREF="javascript:g('35700')" onMouseOver="return s('35700  Atyran, AL')">
<AREA COORDS="167,92,5" SHAPE="CIRCLE" HREF="javascript:g('37018')" onMouseOver="return s('37018  Tuapse, TB')">
<AREA COORDS="205,91,5" SHAPE="CIRCLE" HREF="javascript:g('37054')" onMouseOver="return s('37054  Mineralnye Vody, TB (URMM)')">
<AREA COORDS="128,204,5" SHAPE="CIRCLE" HREF="javascript:g('40179')" onMouseOver="return s('40179  Bet Dagan')">
<AREA COORDS="144,237,5" SHAPE="CIRCLE" HREF="javascript:g('40375')" onMouseOver="return s('40375  Tabuk (OETB)')">
<AREA COORDS="191,246,5" SHAPE="CIRCLE" HREF="javascript:g('40394')" onMouseOver="return s('40394  Hail (OEHL)')">
<AREA COORDS="267,255,5" SHAPE="CIRCLE" HREF="javascript:g('40417')" onMouseOver="return s('40417  K.F.I.A.-Dammam (OEDF)')">
<AREA COORDS="173,273,5" SHAPE="CIRCLE" HREF="javascript:g('40430')" onMouseOver="return s('40430  Al-Madinah (OEMA)')">
<AREA COORDS="238,269,5" SHAPE="CIRCLE" HREF="javascript:g('40437')" onMouseOver="return s('40437  King Khaled Intl Arpt (OERK)')">
<AREA COORDS="250,229,5" SHAPE="CIRCLE" HREF="javascript:g('40582')" onMouseOver="return s('40582  Kuwait Intl Arpt (OKBK)')">
<AREA COORDS="358,164,5" SHAPE="CIRCLE" HREF="javascript:g('40745')" onMouseOver="return s('40745  Mashhad (OIMM)')">
<AREA COORDS="281,170,5" SHAPE="CIRCLE" HREF="javascript:g('40754')" onMouseOver="return s('40754  Tehran-Mehrabad (OIII)')">
<AREA COORDS="242,183,5" SHAPE="CIRCLE" HREF="javascript:g('40766')" onMouseOver="return s('40766  Kermanshah (OICC)')">
<AREA COORDS="354,196,5" SHAPE="CIRCLE" HREF="javascript:g('40809')" onMouseOver="return s('40809  Birjand (OIMB)')">
<AREA COORDS="333,220,5" SHAPE="CIRCLE" HREF="javascript:g('40841')" onMouseOver="return s('40841  Kerman (OIKK)')">
<AREA COORDS="168,299,5" SHAPE="CIRCLE" HREF="javascript:g('41024')" onMouseOver="return s('41024  Jeddah (King Abdul Aziz) (OEJN)')">
<AREA COORDS="200,331,5" SHAPE="CIRCLE" HREF="javascript:g('41112')" onMouseOver="return s('41112  Abha (OEAB)')">
<AREA COORDS="312,274,5" SHAPE="CIRCLE" HREF="javascript:g('41217')" onMouseOver="return s('41217  Abu Dhabi Inter Arpt (OMAA)')">
<AREA COORDS="378,268,5" SHAPE="CIRCLE" HREF="javascript:g('41756')" onMouseOver="return s('41756  Jiwani (OPJI)')">
<AREA COORDS="96,223,5" SHAPE="CIRCLE" HREF="javascript:g('62378')" onMouseOver="return s('62378  Helwan')">
<AREA COORDS="109,257,5" SHAPE="CIRCLE" HREF="javascript:g('62403')" onMouseOver="return s('62403  South Of Valley Univ')">
<AREA COORDS="64,249,5" SHAPE="CIRCLE" HREF="javascript:g('62423')" onMouseOver="return s('62423  Farafra')">
"""

print regex.findall(list)
