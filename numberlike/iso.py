# -*- coding: utf-8 -*-
from numberlike.checksum import Luhn
from numberlike.nonarithmetic import nonarithmetic

try:
    string = basestring
except:
    string = str


class iso3166(nonarithmetic, int):
    """Numeric ISO 3166 country code.

    Notice that some ranges are specifically marked as reserved for user
    assigned purposes:

    * numeric: 900-999
    * alpha2: AA, QM-QZ, XA-XZ, ZZ
    * alpha3: AAA-AAZ, QMA-QZZ, XAA-XZZ, ZZA-ZZZ

    To use these, simply define them in the iso3166._known mapping.
    """

    _known = {
        4:   ('AF', 'AFG', "Afghanistan"),
        8:   ('AL', 'ALB', "Albania, People's Socialist Republic of"),
        12:  ('DZ', 'DZA', "Algeria, People's Democratic Republic of"),
        16:  ('AS', 'ASM', "American Samoa"),
        20:  ('AD', 'AND', "Andorra, Principality of"),
        24:  ('AO', 'AGO', "Angola, Republic of"),
        660: ('AI', 'AIA', "Anguilla"),
        10:  ('AQ', 'ATA', "Antarctica (the territory South of 60 deg S)"),
        28:  ('AG', 'ATG', "Antigua and Barbuda"),
        32:  ('AR', 'ARG', "Argentina, Argentine Republic"),
        51:  ('AM', 'ARM', "Armenia"),
        533: ('AW', 'ABW', "Aruba"),
        36:  ('AU', 'AUS', "Australia, Commonwealth of"),
        40:  ('AT', 'AUT', "Austria, Republic of"),
        31:  ('AZ', 'AZE', "Azerbaijan, Republic of"),
        44:  ('BS', 'BHS', "Bahamas, Commonwealth of the"),
        48:  ('BH', 'BHR', "Bahrain, Kingdom of"),
        50:  ('BD', 'BGD', "Bangladesh, People's Republic of"),
        52:  ('BB', 'BRB', "Barbados"),
        112: ('BY', 'BLR', "Belarus"),
        56:  ('BE', 'BEL', "Belgium, Kingdom of"),
        84:  ('BZ', 'BLZ', "Belize"),
        204: ('BJ', 'BEN', "Benin, People's Republic of"),
        60:  ('BM', 'BMU', "Bermuda"),
        64:  ('BT', 'BTN', "Bhutan, Kingdom of"),
        68:  ('BO', 'BOL', "Bolivia, Republic of"),
        70:  ('BA', 'BIH', "Bosnia and Herzegovina"),
        72:  ('BW', 'BWA', "Botswana, Republic of"),
        74:  ('BV', 'BVT', "Bouvet Island (Bouvetoya)"),
        76:  ('BR', 'BRA', "Brazil, Federative Republic of"),
        86:  ('IO', 'IOT', "British Indian Ocean Territory, Chagos"),
        92:  ('VG', 'VGB', "British Virgin Islands"),
        96:  ('BN', 'BRN', "Brunei Darussalam"),
        100: ('BG', 'BGR', "Bulgaria, People's Republic of"),
        854: ('BF', 'BFA', "Burkina Faso"),
        108: ('BI', 'BDI', "Burundi, Republic of"),
        116: ('KH', 'KHM', "Cambodia, Kingdom of"),
        120: ('CM', 'CMR', "Cameroon, United Republic of"),
        124: ('CA', 'CAN', "Canada"),
        132: ('CV', 'CPV', "Cape Verde, Republic of"),
        136: ('KY', 'CYM', "Cayman Islands"),
        140: ('CF', 'CAF', "Central African Republic"),
        148: ('TD', 'TCD', "Chad, Republic of"),
        152: ('CL', 'CHL', "Chile, Republic of"),
        156: ('CN', 'CHN', "China, People's Republic of"),
        162: ('CX', 'CXR', "Christmas Island"),
        166: ('CC', 'CCK', "Cocos (Keeling) Islands"),
        170: ('CO', 'COL', "Colombia, Republic of"),
        174: ('KM', 'COM', "Comoros, Union of the"),
        180: ('CD', 'COD', "Congo, Democratic Republic of"),
        178: ('CG', 'COG', "Congo, People's Republic of"),
        184: ('CK', 'COK', "Cook Islands"),
        188: ('CR', 'CRI', "Costa Rica, Republic of"),
        384: ('CI', 'CIV', "Cote D'Ivoire, Ivory Coast, Republic of the"),
        192: ('CU', 'CUB', "Cuba, Republic of"),
        196: ('CY', 'CYP', "Cyprus, Republic of"),
        200: ('CS', 'CSK', "Czechoslovak Socialist Republic"),
        203: ('CZ', 'CZE', "Czech Republic"),
        208: ('DK', 'DNK', "Denmark, Kingdom of"),
        262: ('DJ', 'DJI', "Djibouti, Republic of"),
        212: ('DM', 'DMA', "Dominica, Commonwealth of"),
        214: ('DO', 'DOM', "Dominican Republic"),
        218: ('EC', 'ECU', "Ecuador, Republic of"),
        818: ('EG', 'EGY', "Egypt, Arab Republic of"),
        222: ('SV', 'SLV', "El Salvador, Republic of"),
        226: ('GQ', 'GNQ', "Equatorial Guinea, Republic of"),
        232: ('ER', 'ERI', "Eritrea"),
        233: ('EE', 'EST', "Estonia"),
        231: ('ET', 'ETH', "Ethiopia"),
        234: ('FO', 'FRO', "Faroe Islands"),
        238: ('FK', 'FLK', "Falkland Islands (Malvinas)"),
        242: ('FJ', 'FJI', "Fiji, Republic of the Fiji Islands"),
        246: ('FI', 'FIN', "Finland, Republic of"),
        250: ('FR', 'FRA', "France, French Republic"),
        254: ('GF', 'GUF', "French Guiana"),
        258: ('PF', 'PYF', "French Polynesia"),
        260: ('TF', 'ATF', "French Southern Territories"),
        266: ('GA', 'GAB', "Gabon, Gabonese Republic"),
        270: ('GM', 'GMB', "Gambia, Republic of the"),
        268: ('GE', 'GEO', "Georgia"),
        278: ('DD', 'DDR', "German Democratic Republic"),
        276: ('DE', 'DEU', "Germany"),
        288: ('GH', 'GHA', "Ghana, Republic of"),
        292: ('GI', 'GIB', "Gibraltar"),
        300: ('GR', 'GRC', "Greece, Hellenic Republic"),
        304: ('GL', 'GRL', "Greenland"),
        308: ('GD', 'GRD', "Grenada"),
        312: ('GP', 'GLP', "Guadaloupe"),
        316: ('GU', 'GUM', "Guam"),
        320: ('GT', 'GTM', "Guatemala, Republic of"),
        831: ('GG', 'GGY', "Guernsey"),
        624: ('GW', 'GNB', "Guinea-Bissau, Republic of"),
        324: ('GN', 'GIN', "Guinea, Revolutionary People's Republic of"),
        328: ('GY', 'GUY', "Guyana, Republic of"),
        332: ('HT', 'HTI', "Haiti, Republic of"),
        334: ('HM', 'HMD', "Heard and McDonald Islands"),
        336: ('VA', 'VAT', "Holy See (Vatican City State)"),
        340: ('HN', 'HND', "Honduras, Republic of"),
        344: ('HK', 'HKG', "Hong Kong, Special Admin Region of China"),
        191: ('HR', 'HRV', "Hrvatska (Croatia)"),
        348: ('HU', 'HUN', "Hungary, Hungarian People's Republic"),
        352: ('IS', 'ISL', "Iceland, Republic of"),
        356: ('IN', 'IND', "India, Republic of"),
        360: ('ID', 'IDN', "Indonesia, Republic of"),
        364: ('IR', 'IRN', "Iran, Islamic Republic of"),
        368: ('IQ', 'IRQ', "Iraq, Republic of"),
        372: ('IE', 'IRL', "Ireland"),
        376: ('IL', 'ISR', "Israel, State of"),
        380: ('IT', 'ITA', "Italy, Italian Republic"),
        388: ('JM', 'JAM', "Jamaica"),
        392: ('JP', 'JPN', "Japan"),
        832: ('JE', 'JEY', "Jersey"),
        400: ('JO', 'JOR', "Jordan, Hashemite Kingdom of"),
        398: ('KZ', 'KAZ', "Kazakhstan, Republic of"),
        404: ('KE', 'KEN', "Kenya, Republic of"),
        296: ('KI', 'KIR', "Kiribati, Republic of"),
        408: ('KP', 'PRK', "Korea, Democratic People's Republic of"),
        410: ('KR', 'KOR', "Korea, Republic of"),
        414: ('KW', 'KWT', "Kuwait, State of"),
        417: ('KG', 'KGZ', "Kyrgyz Republic"),
        418: ('LA', 'LAO', "Lao People's Democratic Republic"),
        428: ('LV', 'LVA', "Latvia"),
        422: ('LB', 'LBN', "Lebanon, Lebanese Republic"),
        426: ('LS', 'LSO', "Lesotho, Kingdom of"),
        430: ('LR', 'LBR', "Liberia, Republic of"),
        434: ('LY', 'LBY', "Libyan Arab Jamahiriya"),
        438: ('LI', 'LIE', "Liechtenstein, Principality of"),
        440: ('LT', 'LTU', "Lithuania"),
        442: ('LU', 'LUX', "Luxembourg, Grand Duchy of"),
        446: ('MO', 'MAC', "Macao, Special Administrative Region of China"),
        807: ('MK', 'MKD', "Macedonia, the former Yugoslav Republic of"),
        450: ('MG', 'MDG', "Madagascar, Republic of"),
        454: ('MW', 'MWI', "Malawi, Republic of"),
        458: ('MY', 'MYS', "Malaysia"),
        462: ('MV', 'MDV', "Maldives, Republic of"),
        466: ('ML', 'MLI', "Mali, Republic of"),
        470: ('MT', 'MLT', "Malta, Republic of"),
        584: ('MH', 'MHL', "Marshall Islands"),
        474: ('MQ', 'MTQ', "Martinique"),
        478: ('MR', 'MRT', "Mauritania, Islamic Republic of"),
        480: ('MU', 'MUS', "Mauritius"),
        175: ('YT', 'MYT', "Mayotte"),
        484: ('MX', 'MEX', "Mexico, United Mexican States"),
        583: ('FM', 'FSM', "Micronesia, Federated States of"),
        498: ('MD', 'MDA', "Moldova, Republic of"),
        492: ('MC', 'MCO', "Monaco, Principality of"),
        496: ('MN', 'MNG', "Mongolia, Mongolian People's Republic"),
        499: ('ME', 'MNE', "Montenegro"),
        500: ('MS', 'MSR', "Montserrat"),
        504: ('MA', 'MAR', "Morocco, Kingdom of"),
        508: ('MZ', 'MOZ', "Mozambique, People's Republic of"),
        104: ('MM', 'MMR', "Myanmar"),
        516: ('NA', 'NAM', "Namibia"),
        520: ('NR', 'NRU', "Nauru, Republic of"),
        524: ('NP', 'NPL', "Nepal, Kingdom of"),
        530: ('AN', 'ANT', "Netherlands Antilles"),
        528: ('NL', 'NLD', "Netherlands, Kingdom of the"),
        540: ('NC', 'NCL', "New Caledonia"),
        554: ('NZ', 'NZL', "New Zealand"),
        558: ('NI', 'NIC', "Nicaragua, Republic of"),
        566: ('NG', 'NGA', "Nigeria, Federal Republic of"),
        562: ('NE', 'NER', "Niger, Republic of the"),
        570: ('NU', 'NIU', "Niue, Republic of"),
        574: ('NF', 'NFK', "Norfolk Island"),
        580: ('MP', 'MNP', "Northern Mariana Islands"),
        578: ('NO', 'NOR', "Norway, Kingdom of"),
        512: ('OM', 'OMN', "Oman, Sultanate of"),
        586: ('PK', 'PAK', "Pakistan, Islamic Republic of"),
        585: ('PW', 'PLW', "Palau"),
        275: ('PS', 'PSE', "Palestinian Territory, Occupied"),
        590: ('PA', 'PAN', "Panama"),
        598: ('PG', 'PNG', "Papua New Guinea"),
        600: ('PY', 'PRY', "Paraguay, Republic of"),
        720: ('YD', 'YMD', "People's Democratic Republic of Yemen"),
        604: ('PE', 'PER', "Peru, Republic of"),
        608: ('PH', 'PHL', "Philippines, Republic of the"),
        612: ('PN', 'PCN', "Pitcairn Island"),
        616: ('PL', 'POL', "Poland, Polish People's Republic"),
        620: ('PT', 'PRT', "Portugal, Portuguese Republic"),
        630: ('PR', 'PRI', "Puerto Rico"),
        634: ('QA', 'QAT', "Qatar, State of"),
        638: ('RE', 'REU', "Reunion"),
        642: ('RO', 'ROU', "Romania, Socialist Republic of"),
        643: ('RU', 'RUS', "Russian Federation"),
        646: ('RW', 'RWA', "Rwanda, Rwandese Republic"),
        652: ('BL', 'BLM', "Saint Barthélemy"),
        663: ('MF', 'MAF', "Saint Martin"),
        882: ('WS', 'WSM', "Samoa, Independent State of"),
        674: ('SM', 'SMR', "San Marino, Republic of"),
        678: ('ST', 'STP', "Sao Tome and Principe, Democratic Republic of"),
        682: ('SA', 'SAU', "Saudi Arabia, Kingdom of"),
        686: ('SN', 'SEN', "Senegal, Republic of"),
        688: ('RS', 'SRB', "Serbia"),
        690: ('SC', 'SYC', "Seychelles, Republic of"),
        694: ('SL', 'SLE', "Sierra Leone, Republic of"),
        702: ('SG', 'SGP', "Singapore, Republic of"),
        703: ('SK', 'SVK', "Slovakia (Slovak Republic)"),
        705: ('SI', 'SVN', "Slovenia"),
        90:  ('SB', 'SLB', "Solomon Islands"),
        706: ('SO', 'SOM', "Somalia, Somali Republic"),
        710: ('ZA', 'ZAF', "South Africa, Republic of"),
        239: ('GS', 'SGS', "South Georgia and the South Sandwich Islands"),
        724: ('ES', 'ESP', "Spain, Spanish State"),
        144: ('LK', 'LKA', "Sri Lanka, Democratic Socialist Republic of"),
        654: ('SH', 'SHN', "St. Helena"),
        659: ('KN', 'KNA', "St. Kitts and Nevis"),
        662: ('LC', 'LCA', "St. Lucia"),
        666: ('PM', 'SPM', "St. Pierre and Miquelon"),
        670: ('VC', 'VCT', "St. Vincent and the Grenadines"),
        736: ('SD', 'SDN', "Sudan, Democratic Republic of the"),
        740: ('SR', 'SUR', "Suriname, Republic of"),
        744: ('SJ', 'SJM', "Svalbard & Jan Mayen Islands"),
        748: ('SZ', 'SWZ', "Swaziland, Kingdom of"),
        752: ('SE', 'SWE', "Sweden, Kingdom of"),
        756: ('CH', 'CHE', "Switzerland, Swiss Confederation"),
        760: ('SY', 'SYR', "Syrian Arab Republic"),
        158: ('TW', 'TWN', "Taiwan, Province of China"),
        762: ('TJ', 'TJK', "Tajikistan"),
        834: ('TZ', 'TZA', "Tanzania, United Republic of"),
        764: ('TH', 'THA', "Thailand, Kingdom of"),
        626: ('TL', 'TLS', "Timor-Leste, Democratic Republic of"),
        768: ('TG', 'TGO', "Togo, Togolese Republic"),
        772: ('TK', 'TKL', "Tokelau (Tokelau Islands)"),
        776: ('TO', 'TON', "Tonga, Kingdom of"),
        780: ('TT', 'TTO', "Trinidad and Tobago, Republic of"),
        788: ('TN', 'TUN', "Tunisia, Republic of"),
        792: ('TR', 'TUR', "Turkey, Republic of"),
        795: ('TM', 'TKM', "Turkmenistan"),
        796: ('TC', 'TCA', "Turks and Caicos Islands"),
        798: ('TV', 'TUV', "Tuvalu"),
        800: ('UG', 'UGA', "Uganda, Republic of"),
        804: ('UA', 'UKR', "Ukraine"),
        784: ('AE', 'ARE', "United Arab Emirates"),
        826: ('GB', 'GBR', "United Kingdom of Great Britain & N. Ireland"),
        581: ('UM', 'UMI', "United States Minor Outlying Islands"),
        840: ('US', 'USA', "United States of America"),
        858: ('UY', 'URY', "Uruguay, Eastern Republic of"),
        810: ('SU', 'SUN', "U.S.S.R."),
        850: ('VI', 'VIR', "US Virgin Islands"),
        860: ('UZ', 'UZB', "Uzbekistan"),
        876: ('WF', 'WLF', "Wallis and Futuna Islands"),
        548: ('VU', 'VUT', "Vanuatu"),
        862: ('VE', 'VEN', "Venezuela, Bolivarian Republic of"),
        732: ('EH', 'ESH', "Western Sahara"),
        704: ('VN', 'VNM', "Viet Nam, Socialist Republic of"),
        887: ('YE', 'YEM', "Yemen"),
        894: ('ZM', 'ZMB', "Zambia, Republic of"),
        716: ('ZW', 'ZWE', "Zimbabwe"),
        248: ('AX', 'ALA', "Åland Islands"),
        }

    def __new__(cls, x):
        if isinstance(x, string):
            for k, v in cls._known.items():
                if x in v:
                    x = k
                    break
            else:
                x = int(x)

        if x not in cls._known:
            raise RuntimeError('Unknown %s code %s' % (cls.__name__, x), x)

        return super(iso3166, cls).__new__(cls, x)

    name = property(lambda s: s._known[int(s)][2],
                    doc="Plain country name string")
    short = property(lambda s: s.name.split(',')[0],
                     doc="Short name extracted from name")
    alpha2 = property(lambda s: s._known[int(s)][0], doc="Alpha2 code")
    alpha3 = property(lambda s: s._known[int(s)][1], doc="Alpha2 code")

    def formal():
        def get_formal(self):
            n = self.name
            if ',' in n:
                if 'of' in n:
                    return ' '.join(reversed(n.split(', ', 1)))
                else:
                    return n.split(', ', 1)[-1]
            else:
                return n

        return property(get_formal, doc="Formal name extracted from name")

    formal = formal()

    def __str__(self):
        return "%d" % self

    def __repr__(self):
        return "%s(%d)" % (self.__class__.__name__, self)


class iso7812(nonarithmetic, long):
    """ISO/IEC 7812 Identification card numbers.

    Leading zero numbers are not accepted.
    """

    _mii = {
        0: "ISO/TC 68 and other future industry assignments",
        1: "Airlines",
        2: "Airlines and other future industry assignments",
        3: "Travel and entertainment and banking/financial",
        4: "Banking and financial",
        5: "Banking and financial",
        6: "Merchandising and banking/financial",
        7: "Petroleum and other future industry assignments",
        8: "Healthcare, telecoms and other future industry assignments",
        9: "National assignment",
        }

    def __new__(cls, x):
        if not Luhn.verify(x):
            raise ValueError('Luhn checksum failed')

        if x < 10000000:
            raise ValueError('Number too short')

        if x > 9999999999999999999L:
            raise ValueError('Number too long')

        return super(iso7812, cls).__new__(cls, x)

    mii = property(lambda self: self._mii[int(str(int(self))[0])],
                   doc="Major industry identifier")

    iin = property(lambda self: int(str(int(self))[:6]),
                   doc="Issuer identifier number")

    account = property(lambda self: int(str(int(self))[6:-1]),
                       doc="Individual account number")

    check = property(lambda self: int(self) % 10,
                     doc="Luhn check digit")

    def country():
        def country_get(self):
            s = str(int(self))
            if s[0] == '9':
                return iso3166(int(s[1:4]))
        return property(country_get, doc="Country code, if national card")

    country = country()
