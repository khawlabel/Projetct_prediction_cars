import streamlit as st 
import pandas as pd
import pickle




#upload data
data=pickle.load(open(r'C:\khawla\MesProjects\Projetct_prediction_cars\prediction_price_cars.sav','rb'))

#streamlit page

#Layout
st.set_page_config(
    page_title="Car_price",
    layout="wide",
    initial_sidebar_state="expanded")

st.title('Car price prediction')
st.sidebar.header('Car price prediction')
st.sidebar.info('Easy Application for predict pice Car ')
st.image('https://th.bing.com/th/id/R.a0ec66970fb3943634047b96eaf1972a?rik=Kth7%2f88425Nw1g&riu=http%3a%2f%2f2.bp.blogspot.com%2f_dXE63lwcSrk%2fTLly8q4Up9I%2fAAAAAAAAD0Q%2fzzsVFWb6dvU%2fs1600%2fLAMBORGHINI%2bGALLARDO%2bLP570-4%2bBLACK%2bFRONT.jpg&ehk=iGq0wpMkYcxXS8MuXb3cOLl9osjG%2b1KTzSEQGptKmdQ%3d&risl=&pid=ImgRaw&r=0')

#Manufacturer
Manufacturer1=['HONDA', 'FORD', 'HYUNDAI', 'TOYOTA', 'MERCEDES-BENZ',
       'VOLKSWAGEN', 'RENAULT', 'NISSAN', 'CHEVROLET', 'SUBARU', 'DAEWOO',
       'BMW', 'KIA', 'MITSUBISHI', 'SSANGYONG', 'MAZDA', 'GMC', 'FIAT',
       'SUZUKI', 'LEXUS', 'OPEL', 'AUDI', 'CITROEN', 'MINI', 'DODGE',
       'LAND ROVER', 'JEEP', 'ACURA', 'VAZ', 'JAGUAR', 'SKODA',
       'CHRYSLER', 'LINCOLN', 'BUICK', 'PEUGEOT', 'სხვა', 'HAVAL',
       'CADILLAC', 'SCION', 'INFINITI', 'PORSCHE', 'LANCIA', 'MERCURY',
       'SAAB', 'VOLVO', 'ALFA ROMEO', 'SATURN', 'GAZ']

Manufacturer2=[16, 12, 17, 43, 27, 45, 35, 31,  6, 41,  9,  3, 21, 30, 40, 26, 14,
       11, 42, 24, 32,  2,  8, 29, 10, 23, 20,  0, 44, 19, 39,  7, 25,  4,
       33, 47, 15,  5, 38, 18, 34, 22, 28, 36, 46,  1, 37, 13]

manu_mapping=dict(zip(Manufacturer1, Manufacturer2))
manu1=st.selectbox('Manufacturer',Manufacturer1)
Manufacturer=manu_mapping[manu1]

#Model

Model1=['FIT', 'Escape', 'Santa FE', 'Prius', 'Sonata', 'Camry', 'CHR',
       'Elantra', 'E 220', 'H1', 'Jetta', 'Prius C', 'Aqua',
       'Escape Hybrid', 'Civic', 'Megane 1.5CDI', 'E 300', 'Juke',
       'Cruze LT', 'Fusion', 'VOXY', 'A 160', 'Tucson', 'Captiva',
       'Mustang', 'Yaris', 'Cruze', 'Orlando', 'Forester', 'Lacetti',
       '428 Sport Line', 'Genesis', 'Sprinter', 'Focus SE', 'Picanto',
       'Airtrek', 'Korando', '616', 'Serena', 'RAV 4', 'Volt', 'TERRAIN',
       'Hr-v EX', '500', 'Elantra sport limited', 'A 170', 'REXTON',
       'Carnival grand', '1000', 'C 250', 'Vitz funkargo', 'Transit',
       'Vaneo', 'Tacoma', 'Explorer', 'I30', 'Grand Vitara', 'CT 200h',
       'Veloster', 'RAV 4 XLE Sport', 'Sienta', 'Passat',
       'Avalon LIMITED', 'Cerato K3', 'CX-7', 'Astra G', 'Corolla',
       'Rogue', 'GLA 250', 'Sharan', 'Tiida', 'C 300', 'Actyon', 'S 350',
       'RAV 4 Le', 'E 350 ამგ', 'Cr-v', 'Avalon', 'ML 250', 'Colt Lancer',
       'Outlander', 'Camry SE', 'Malibu', 'Insight', 'Altima', 'Vito',
       'GTI', 'Colt', 'C-MAX', 'RAV 4 s p o r t', 'Fusion Titanium',
       'Aveo', 'Aqua S', 'Optima', 'Shuttle', 'Land Cruiser Prado',
       'Equinox', 'Vitz', 'A4 premium', 'Kizashi', '328', 'Element', 'C1',
       'X-Trail', 'RIO', 'Astra', 'Corolla IM', 'CLK 240', 'Fiesta',
       'Cooper', 'Combo', 'A4', 'Corolla verso', 'Q5', 'Odyssey', 'L 200',
       'Insight EX', 'Focus', 'Matiz', 'Mazda 3', 'Scenic', '320',
       'NX 200', 'Spark', 'March', 'HS 250h Hybrid', 'Sonata SPORT',
       'Elantra SE', 'Auris', 'ES 350', 'SOUL', '500C Lounge',
       'Cruze ltz', 'Countryman', 'Corolla 04', 'Rogue SL', 'A6', 'Q3',
       'Accent', 'Grandeur', 'Hr-v', 'Dart Limited', 'CX-9', 'Accord',
       'Fusion TITANIUM', 'Freelander', 'Ist', 'Compass',
       'Transit Connect', 'XV', 'Aqua g soft leather sele', 'Meriva',
       'Prius V', 'Sorento', '114', 'ES 300', 'Sportage', 'Versa',
       'FIT Sport', 'Carnival', 'Step Wagon Pada', 'Dart GT 2.4',
       'Stream', 'TLX', 'A3 PREMIUM', 'kona', 'IS 250', 'Cruze LTZ',
       'ISIS', '1300', 'Transit 350T', 'Outlander 2.0', 'Polo',
       'Cherokee', 'Zafira', '2107', 'XF', 'Camry se', 'Kyron', 'Octavia',
       'Mazda 3 SPORT', 'Ipsum', 'IX35', 'Tiida 2008', 'Sentra',
       'Frontier', 'Smart', 'A 190', 'Jetta სპორტ', 'Corolla LE', '428',
       'X5', 'Transit Connect ბენზინი', 'Elantra limited', 'Camry S',
       'FIT SPORT', 'Ipsum S', 'Cooper S Cabrio R56', 'Mx-5', 'Crafter',
       'A 140', 'Cadenza', 'Sonata 2.0t', 'C 180', 'Sonata S', 'B 170',
       'Cerato', 'Legacy', 'PT Cruiser', 'Sonata blue edition', 'C 200',
       'Sprinter VAN', 'Vectra', 'Civic EX', 'Fuga', 'Viano', 'MKZ',
       'Cruze strocna', 'Countryman S', 'Tiida AXIS', 'Swift',
       'Volt premier', 'HS 250h', 'CT 200h F-sport', 'Outback', 'Atenza',
       'Tiguan', 'Camry Se', 'FIT Hbrid', 'Verso', 'Golf 6', '120',
       'Liana', 'Pajero', 'Alphard', 'ColtPlus', 'A4 S line',
       'Sonata hybrid', 'Century', 'Golf', 'Grandis', 'FIT S', 'Venza',
       'RVR', 'XV LIMITED', 'Premacy', 'Corolla S', 'Demio', 'Jetta GLI',
       'Note', 'CX-5', 'C 220', 'E 200', 'Taurus', 'Fusion phev',
       '500 Abarth', 'CLA 250', '206', 'A4 premium plius', 'Mazda 6',
       'Fred', 'Escape Titanium', 'IVECO DAYLY', 'Camry SPORT', 'Impala',
       'Impreza', 'Hilux', 'Cruze Premier', 'Clio', 'Outlander SPORT',
       '500L LONG', 'Ranger', '200', 'FIT HIBRID', 'H6', 'CC R line',
       'Mazda 6 TOURING', 'Caliber', 'C 230', '320 i', 'Gentra',
       'CC 2.0 T', 'BRZ', 'SX4', '1500', '500 Sport', 'Golf TDI',
       'Camry sport', 'Highlander', 'Demio evropuli', 'X3', 'Equinox LT',
       'Outlander SE', 'Passat R-line', 'Camry XLE', 'Eunos 500', 'A5',
       'Allroad', 'Forester SH', 'Outlander Sport', 'Serena Serea', 'MPV',
       'Cooper S Cabrio', 'Transit S', 'C-MAX HYBRID', 'Transit 135',
       'Caddy', 'Caldina', 'Aqua s', 'Elantra LIMITED', 'Astra H',
       'NEW Beetle', 'Megane GT Line', 'X1', 'Elantra GT', 'Cruze RS',
       'MKZ hybrid', 'CC', 'Prius C Navigation', 'Corsa', 'Sonata HYBRID',
       'Prius V ALPINA', 'RIO lx', 'Jetta SEL', 'Avella',
       'Focus TITANIUM', 'Acadia', 'Forte', 'Accord CL9 type S',
       '500 turbo', 'TSX', 'Aqua L paketi', 'Santa FE Ultimate',
       'Sprinter 311', 'Outlander sport', 'Vito 2.2', '535 Twinturbo',
       'Avensis', 'Sonata Hibrid', 'Prius s', 'RIO lX', 'Prius BLUG-IN',
       'Presage RIDER', 'Yaris IA', '528', 'Micra', 'Getz', '500C',
       'Encore', 'Megane', 'FIT HYBRYD', 'Elantra gt', 'Focus ST',
       'Camry sporti', 'Sonic', 'Cruze LS', 'Camry HYBRID', 'CTS',
       'Lancer', 'Camry LE', '530', 'CT 200h F SPORT', 'Laguna',
       'Elantra Limited', 'S-max', 'RC F', '320 2.0', '328 DIZEL',
       'Impreza G4', 'FIT fit', 'Passat SE', 'iA isti',
       'Elantra GLS / LIMITED', 'Avalon limited', 'Elysion', 'Touran',
       'Corsa Corsa', 'Vectra C', 'Wrangler', 'E 220 cdi', 'Countryman s',
       'Demio 12', '500 46 ml', 'Wish', 'Vitz RS', '500 Lounge', 'Agila',
       'Ioniq', 'Crosstrek', 'Cruze sonic', 'Nubira', 'Axela', 'Scirocco',
       'A3', 'Renegade', 'GONOW', 'Cruze L T', 'C-MAX SEL', 'Aqua G klas',
       'Fusion SE', '328 sulev', 'Sorento SX', 'Corolla Im', 'Kangoo',
       'Aerio SX', 'Murano', 'Highlander 2.4 lit', 'Sonata LPG',
       'Camry Hybrid', 'Kizashi sporti', 'X1 28Xdrive', 'Malibu LT',
       'Focus Fokusi', 'IS 200', 'tC', 'Prius ფლაგინი', 'CX-5 Touring',
       'Edix', 'Veloster R-spec', 'Transit Custom', 'Zafira B',
       'Prius 1.5I', 'Civic Ferio', 'Jetta TDI', 'Optima ECO', '528 i',
       'Sonata Hybrid', 'Verisa', 'Kicks', 'X1 X-Drive', 'Yaris iA',
       'Focus Flexfuel', 'Aqua G', 'Swift Sport', 'Patriot', 'Duster',
       '2121 (Niva)', 'Tourneo Connect', 'Transit Connect Prastoi',
       'FX35', 'Verisa 2007', 'Camry sport se', 'Highlander LIMITED',
       'CLK 230', 'Camry XV50', 'Transit T330', 'Prius ჰიბრიდი',
       'Escape SE', 'Combo TDI', 'Aqua HIBRID', 'Escape მერკური მერინერი',
       'macan', 'Niro', 'E 320', 'RAV 4 SPORT', 'Vectra c', 'CR-Z',
       'Malibu eco', '318', 'EcoSport SE', 'FIT Premiym', 'Legacy Bl5',
       'HHR', 'Prius TSS LIMITED', 'Cooper r50', 'C8', 'Elantra Gt',
       'A3 4X4', '100 NX', 'Focus Titanium', 'Prius S', 'Vitz i.ll',
       'RAV 4 XLE', 'Musa', 'Pathfinder', 'C 250 luxury', 'Passat sport',
       'E 320 4×4', 'Jetta se', '500L', 'X1 4X4', '207', 'Focus se',
       'FIT RS MODELI', 'C 250 1.8 ტურბო', 'Prius C 2013', 'C4',
       'Wingroad', 'Kicks SR', 'Caliber sxt', '4Runner', 'RX 350',
       'Cefiro', 'CR-Z ჰიბრიდი', 'C-MAX PREMIUM', 'Forester XT',
       'Pajero IO', 'Cruze Cruze', 'Tucson Limited', 'Ignis',
       'Corolla ECO', 'Cayman', 'Tiida 15 M', 'Dart', 'Demio mazda2',
       'A4 B6', 'Octavia Scout', 'Mariner', '500 sport', 'Jetta SE',
       'FIT RS', '500 s', 'C5', 'C 230 kompresor', 'Grand Cherokee',
       '09-Mar', 'Hiace', 'Citan', 'ColtPlus Plus', 'Passat RLAINI',
       'E 350', 'Outlander სპორტ', 'Countryman S turbo', 'Prius V HYBRID',
       'Malibu Hybrid', 'Camry sel', 'Elantra 2014', 'Belta',
       'Transit Tourneo', 'Trax', 'Azera', 'C-MAX SE', 'Estima',
       'Demio Sport', 'IS 250 TURBO', 'CX-3', 'Volt Full Packet',
       'Fred HIBRIDI', 'Forester 4x4', 'Juke Nismo RS', 'Lancer GT',
       'ATS', 'Prius 9', 'March Rafeet', '318 რესტაილინგი', 'Juke Nismo',
       'F-pace', 'Lantra', 'X3 SDRIVE', 'FIT RS MUGEN',
       'Forester CrossSport', 'Outback Limited', 'CRX', 'C 250 A.M.G',
       'Optima HYBRID', 'E 250', 'Forester cross sport', 'C 250 AMG',
       'Avenger', 'Legacy bl5', 'C 180 komp', 'Yaris RS', '118',
       'Sportage SX', 'X-Trail NISSAN X TRAIL R', 'Prius prius',
       'Range Rover Evoque 2.0', 'Sonata Limited', 'Tucson Se',
       'Sprinter 313CDI', 'Captur QM3 Samsung', 'Passat 2.0 tfsi',
       'Jetta SPORT', 'Fun Cargo', 'Sonata 2.4L', 'NX 300', 'LATIO',
       'CC sport', 'Prius 11', 'Explorer Turbo japan', 'Fusion Bybrid',
       'Lupo iaponuri', '118 2,0', 'X-Trail NISMO', 'Lantra LIMITED',
       'Veloster Turbo', 'Volt PREMIER', 'Vito 115 CDI', 'Passo',
       'Sonata Sport', 'Matrix XR', 'Presage', 'S60', 'Mazda 2',
       'Edix FR-v', '159', 'Prius plug-in', 'RAV 4 Dizel', 'Astra j',
       'A 200', 'Fabia', 'Prius personna', 'S3', 'Golf 4', '525',
       'Fusion 2015', 'Sportage EX', 'Navara', 'Step Wagon', 'FIT Modulo',
       'Giulietta', 'RX 450 HYBRID', 'Astra CNG', 'Prius C ჰიბრიდი',
       'Noah', 'Mazda 6 Grand touring', 'Sorento EX', 'Camry SPORT PAKET',
       'Teana', 'Fusion HIBRID', 'Sprinter 316', 'Mondeo', 'FIT GP-5',
       'Golf GTI', 'Kangoo Waggon', 'Legacy B4', 'Ceed', 'Sprinter 314',
       '307', '320 Diesel', '500X', 'UP', 'Sonic LT', 'Tucson SE',
       'H1 grandstarex', 'Sportage PRESTIGE', 'Superb', 'Mirage',
       'Megane 1.9CDI', 'Jetta სასწაფოდ', 'Corvette', 'GLK 250',
       'Sprinter 316 CDI', 'Cruze PREMIER', 'Outlander xl',
       'FIT "S"- PAKETI.', 'Fiesta SE', 'H1 GRAND STAREX', 'Tiida Latio',
       'Cr-v LX', 'Sai', '500X Lounge', 'Qashqai Advance CVT',
       'Accent SE', 'Countryman sport', 'Sprinter 313', '323', 'Journey',
       'ES 300 hybrid', 'FIT ex', 'Mariner Hybrid', 'Vito long115',
       'VOXY 2003', 'Vito 113', 'Passat se', 'Ractis', 'Vue',
       'Eclipse ES', 'Fusion 1.6', 'Transit ford', 'Carens',
       'Elantra 2016', 'Crossroad', 'Veloster TURBO', 'A4 S4',
       'Aqua სასწრაფოდ', 'Veloster remix', 'A4 B7', 'Juke nismo',
       'Vitara', 'Escape HYBRID', '508', 'Vito 111 CDI', 'xD',
       'Passat B5', 'XV HYBRID', 'Elantra LIMITEDI', '328 i', 'C 240',
       'Qashqai SPORT', 'Astra GTC 1.9 turbo dies', '400X', 'Jimny',
       'C1 C', '3008', 'B 200', 'Vectra H', 'CLA 250 AMG',
       'Highlander 2,4', 'PT Cruiser pt cruiser', '807',
       'Prius C 80 original', 'Insight LX', 'Patriot 70th anniversary',
       'Camaro', 'E 220 CDI', 'Sprinter 315CDI-XL', 'FIT GP-6',
       'Octavia SCOUT', 'Jetta sport', 'B 200 Turbo', 'Elantra i30',
       'Vanette', 'Prius Plug IN', 'DS 4', 'E-pace',
       '520 d xDrive Luxury', 'Mazda 6 Grand Touring', 'M3', 'Hr-v EXL',
       'Mark X Zio', '220', 'Aqua sport', 'Almera dci', 'Impreza Sport',
       'X4', 'Fusion hybrid', 'Vito 111', '2105', 'Sprinter 308 CDI',
       'Sprinter EURO4', 'Yaris SE', '118 M-sport LCI', '250',
       'CT 200h 1.8', 'Combo 1700', 'Passat tdi sel', 'B 180',
       'Santa FE sport', 'Optima hybrid', 'Sonata sport', 'Vito 115',
       'Sonata SE LIMITED', 'Prius 1.8', 'H1 starixs', 'Accent GS',
       'Corolla se', 'Mazda 5', 'C 250 AMG-PAKET-1,8', 'Niva',
       'B 170 B Class', 'B9 Tribeca', '206 CC', 'Skyline', 'Liberty',
       'E 220 211', 'Sonata LIMITED', 'C 250 1.8', 'Megane 1.9 CDI',
       'LAFESTA', 'E 220 ELEGANCE', 'Rogue SPORT', 'Regal',
       'Prius C hybrid', 'Juke juke', 'FIT Hybrid', 'Juke Juke', 'Galant',
       'V50', 'Caliber journey', '407', 'Camry XSE', '500 sport panorama',
       'B 170 Edition One', 'Fusion HYBRID', 'Crafter 2,5TDI',
       'Volt Premier', 'FIT PREMIUMI', 'Elantra GS', 'Passat SEL',
       'Fusion Hybrid', 'Passat tsi-se', 'Caddy cadi', 'Paceman', 'Rx-8',
       'Micra <DIESEL>', 'i20', 'Prius plagin', 'Punto', 'Prius 3', 'BB',
       'Camry ჰიბრიდი', 'Camry SE HIBRYD', '428 i', 'Juke Turbo', 'i40',
       'Versa s', 'Prius Plug in', 'FIT PREMIUM PAKETI', 'Lancer GTS',
       'Sienna', 'Juke NISMO', 'Jetta s', 'Cooper CLUBMAN', 'E 200 CGI',
       'Golf GOLF 5', 'Integra', 'Impreza WRX/STI LIMITED', 'Corolla 140',
       'Cooper S', 'Cruze LT RS', 'Astra A.H', 'Step Wagon RG2 SPADA',
       'Legacy b4', 'Jetta Hybrid', 'FIT NAVI PREMIUM', 'Civic Hybrid',
       'Jetta 1.4 TURBO', 'Forester L.L.BEAN', 'Sonata SE', 'Fit Aria',
       'INSIGNIA', 'Escape escape', '31105', 'Prius C Hybrid',
       'Sonata სასწრაფოდ', 'Tiguan SE', '500 SPORT', 'Prius C YARIS IA',
       'A 170 Avangard', 'CT 200h F sport', 'Panda', 'Prius C 1.5I',
       'Optima ex', 'GL 320', 'Patriot Latitude', 'Kalos', 'A4 Sline',
       'Prius V HIBRID', 'C 200 2.0', 'Focus SEL', 'Optima k5',
       'Outback 2007', 'Elantra se', 'Fusion HYBRID SE', 'Versa SE',
       'Vito Exstralong', 'Vito Extralong', 'FIT LX',
       'Every Landy NISSAN SEREN']
Model2=[347, 334, 683, 616, 697, 194, 167, 313, 294, 430, 469, 623,  99,
       336, 226, 545, 300, 484, 273, 397, 776,  66, 770, 213, 556, 836,
       269, 577, 383, 504,  37, 416, 725, 377, 611,  94, 499,  63, 689,
       652, 812, 743, 445,  40, 328,  67, 660, 217,   2, 145, 810, 758,
       778, 746, 344, 447, 427, 175, 784, 657, 694, 595, 119, 223, 184,
       112, 245, 672, 411, 691, 751, 152,  91, 676, 654, 304, 263, 118,
       523, 232, 581, 199, 525, 461,  98, 798, 414, 231, 153, 658, 407,
       124, 104, 571, 692, 509, 332, 808,  80, 497,  30, 329, 158, 821,
       661, 109, 249, 171, 371, 239, 235,  74, 254, 649, 570, 501, 462,
       374, 534, 537, 686,  25, 559, 720, 529, 437, 709, 323, 117, 308,
       680,  51, 279, 258, 246, 673,  83, 648,  86, 428, 444, 285, 185,
        89, 406, 393, 468, 238, 761, 833, 105, 549, 636, 717,   3, 306,
       721, 792, 366, 216, 737, 284, 739, 744,  73, 846, 450, 275, 452,
         8, 760, 582, 612, 224, 841,  16, 832, 207, 500, 567, 538, 466,
       454, 753, 688, 394, 696,  69, 481, 251,  36, 831, 763, 326, 198,
       365, 467, 243, 557, 265,  65, 188, 698, 137, 706, 127, 222, 512,
       589, 711, 139, 735, 780, 227, 395, 796, 521, 281, 259, 754, 741,
       816, 436, 179, 578, 116, 749, 203, 353, 795, 422,   7, 517, 592,
        97, 233,  77, 712, 221, 420, 429, 364, 789, 664, 835, 613, 252,
       286, 471, 565, 182, 141, 292, 747, 409,  42, 168,  12,  81, 540,
       391, 338, 453, 201, 456, 457, 443, 277, 230, 584,  53, 669,  11,
       351, 434, 165, 543, 190, 142,  28, 417, 164, 135, 681,   9,  45,
       425, 209, 439, 289, 828, 333, 583, 598, 204, 342,  82,  95, 387,
       585, 690, 524, 242, 765, 154, 759, 186, 189, 106, 320, 114, 558,
       548, 824, 318, 278, 522, 163, 628, 255, 700, 637, 663, 474, 121,
       380,  85, 390,  90,  49, 745, 103, 684, 727, 586, 804,  62, 123,
       701, 644, 662, 622, 615, 837,  59, 550, 418,  50, 331, 544, 352,
       324, 379, 211, 715, 272, 195, 180, 506, 197,  61, 177, 505, 322,
       677, 659,  26,  31, 458, 368, 600, 845, 316, 120, 330, 756, 256,
       781, 820, 298, 261, 287,  41, 819, 809,  43,  93, 465, 268, 280,
       566, 125, 687,  71, 671, 413, 271, 157, 101, 405,  33, 719, 250,
       493,  92, 554, 441, 704, 196, 498, 825, 527, 376, 449, 848, 645,
       183, 311, 785, 764, 842, 617, 228, 476, 572,  60, 702, 790, 495,
       827, 840, 375, 100, 742, 608, 291,  17, 757, 762, 369, 791, 210,
       442, 170, 206, 766, 646, 337, 237, 102, 340, 847, 562, 301, 655,
       783, 172, 528,  23, 310, 360, 514, 435, 635, 244, 162, 319,  72,
         1, 381, 634, 811, 656, 555, 607, 151, 603, 302, 478,  52, 826,
        14, 382, 362, 147, 625, 160, 818, 496, 192,  39, 665, 220, 173,
       155, 388, 593, 270, 771, 455, 248, 218, 752, 283, 290,  75, 569,
       531,  47, 473, 361,  46, 161, 143, 426,   0, 438, 225, 234, 599,
       303, 588, 260, 639, 526, 208, 314, 136, 767, 769, 126, 156, 341,
       288, 451, 181, 813, 392, 384, 488, 507,  84, 621, 530,  24, 487,
       346, 510, 829, 363, 385, 580, 174, 148, 573, 299, 389, 149, 122,
       516, 138, 838,   4, 724, 823, 643, 668, 705, 773, 729, 214, 596,
       475, 396, 699, 560, 503, 166, 619, 345, 400, 519,   5, 822, 511,
       787, 814, 803, 606, 710, 535, 614, 679, 536, 312,  10, 642, 653,
       115,  70, 370, 640, 678, 421,  58, 399, 722, 561, 736, 356, 419,
       666, 111, 631, 564, 542, 718, 202, 748, 401, 732, 553, 349, 424,
       494, 513, 219, 730,  21,  27,  54, 774, 716, 772, 432, 723, 740,
       552, 547, 480, 257, 412, 733, 276, 587, 348, 372, 431, 755, 264,
       682,  55, 650,  88, 262, 728,  29, 483, 307, 367, 532, 807, 777,
       801, 602, 667, 817, 309, 398, 768, 215, 315, 267, 786,  78, 108,
       788,  76, 491, 797, 335,  56, 800, 849, 597, 834, 321,  32, 144,
       651, 113,  34, 482, 159,  20, 131, 782, 169, 440, 590,  64, 626,
       463, 609, 193, 296, 731, 350, 568, 479, 132, 325, 779, 632, 282,
       305,  57, 541, 520, 446, 533,  18, 107,  96, 459, 830, 408, 799,
        15, 726, 734, 839,   6,  19, 176, 236, 604, 130, 685, 575, 713,
       802, 708, 618, 433,  87, 253, 539, 150, 563, 128, 133,  13, 695,
       518, 295, 703, 146, 546, 502, 297, 674, 670, 630, 490, 354, 485,
       415, 775, 191,  35, 205,  48, 129, 402, 266, 815, 359, 317, 601,
       404, 605, 187, 591, 675, 551, 843, 641, 647, 620, 134, 212, 200,
        38, 489, 844, 794, 633, 358, 508, 693, 486, 477, 240, 293, 423,
       464, 460, 247, 241, 274, 110, 738, 515, 472, 357, 229, 470, 386,
       707, 373, 448, 339,  22, 627, 714, 750,  44, 629,  68, 178, 594,
       624, 574, 410, 610, 492,  79, 638, 140, 378, 576, 579, 327, 403,
       793, 805, 806, 355, 343]
manu_mapping_Model=dict(zip(Model1,Model2))
manu_Model=st.selectbox('Model',Model1)
Model=manu_mapping_Model[manu_Model]

#Category
Category1=['Hatchback', 'Jeep', 'Sedan', 'Universal', 'Minivan', 'Cabriolet',
       'Coupe', 'Microbus', 'Goods wagon', 'Pickup']
Category2=[3, 4, 8, 9, 6, 0, 1, 5, 2, 7]
manu_mapping_Category=dict(zip(Category1,Category2))
manu_Category=st.selectbox('Category',Category1)
Category=manu_mapping_Category[manu_Category]

#Leather interior
Leather_interior1=['No', 'Yes']
Leather_interior2=[0, 1]
manu_mapping_Leather_interior=dict(zip(Leather_interior1,Leather_interior2))
manu_Leather_interior=st.selectbox('Leather interior',Leather_interior1)
Leather_interior=manu_mapping_Leather_interior[manu_Leather_interior]

#Fuel type
Fuel_type1=['Petrol', 'Hybrid', 'Diesel', 'Plug-in Hybrid', 'LPG', 'CNG']
Fuel_type2=[4, 2, 1, 5, 3, 0]
manu_mapping_Fuel_type=dict(zip(Fuel_type1,Fuel_type2))
manu_Fuel_type=st.selectbox('Fuel type',Fuel_type1)
Fuel_type=manu_mapping_Fuel_type[manu_Fuel_type]
#Gear box type
Gear_box_type1=['Variator', 'Automatic', 'Tiptronic', 'Manual']
Gear_box_type2=[3, 0, 2, 1]
manu_mapping_Gear_box_type=dict(zip(Gear_box_type1,Gear_box_type2))
manu_Gear_box_type=st.selectbox('Gear box type',Gear_box_type1)
Gear_box_type=manu_mapping_Gear_box_type[manu_Gear_box_type]
#Drive wheel
Drive_wheel1=['Front', '4x4', 'Rear']
Drive_wheel2=[1, 0, 2]
manu_mapping_Drive_wheel=dict(zip(Drive_wheel1,Drive_wheel2))
manu_Drive_wheel=st.selectbox('Drive wheel',Drive_wheel1)
Drive_wheels=manu_mapping_Drive_wheel[manu_Drive_wheel]
#Wheel
Wheel1=['Right-hand drive', 'Left wheel']
Wheel2=[1, 0]
manu_mapping_Wheel=dict(zip(Wheel1,Wheel2))
manu_Wheel=st.selectbox('wheel',Wheel1)
Wheel=manu_mapping_Wheel[manu_Wheel]
#Color
Color1=['Black', 'White', 'Silver', 'Grey', 'Blue', 'Sky blue', 'Red',
       'Orange', 'Green', 'Yellow', 'Brown', 'Golden', 'Beige',
       'Carnelian red', 'Purple', 'Pink']
Color2=[ 1, 14, 12,  7,  2, 13, 11,  8,  6, 15,  3,  5,  0,  4, 10,  9]
manu_mapping_Color=dict(zip(Color1,Color2))
manu_Color=st.selectbox('Color',Color1)
Color=manu_mapping_Color[manu_Color]
#Engine volume'].
Engine_volume1=[1.3, 2.5, 2. , 1.8, 2.4, 1.6, 2.2, 1.5, 1.4, 2.3, 1.2, 1.7, 2.9,
       1.9, 2.7, 3.5, 2.1, 1. , 0.8, 3. , 3.3, 2.8, 3.2, 1.1]
Engine_volume2=[1.3, 2.5, 2. , 1.8, 2.4, 1.6, 2.2, 1.5, 1.4, 2.3, 1.2, 1.7, 2.9,
       1.9, 2.7, 3.5, 2.1, 1. , 0.8, 3. , 3.3, 2.8, 3.2, 1.1]
manu_mapping_Engine_volume=dict(zip(Engine_volume1,Engine_volume2))
manu_Engine_volume=st.selectbox('Engine volume',Engine_volume1)
Engine_volume=manu_mapping_Engine_volume[manu_Engine_volume]
#Cylinders
Cylinders1=[4.]
Cylinders2=[4.]
manu_mapping_Cylinders=dict(zip(Cylinders1,Cylinders2))
manu_Cylinders=st.selectbox('Cylinders',Cylinders1)
Cylinders=manu_mapping_Cylinders[manu_Cylinders]
#Airbags
Airbags1=[ 2,  0,  4, 12,  8, 10,  6,  1, 16,  7,  9,  5, 11,  3, 14, 15, 13]
Airbags2=[ 2,  0,  4, 12,  8, 10,  6,  1, 16,  7,  9,  5, 11,  3, 14, 15, 13]
manu_mapping_Airbags=dict(zip(Airbags1,Airbags2))
manu_Airbags=st.selectbox('Airbags',Airbags1)
Airbags=manu_mapping_Airbags[manu_Airbags]
#Age
Age=st.number_input('Age')
#Levy
Levy=st.number_input('Levy')
#Mileage
Mileage=st.number_input('Mileage')
df=pd.DataFrame({'Manufacturer':Manufacturer,'Model':Model,'Category':Category,'Leather interior':Leather_interior,
                'Fuel type':Fuel_type,'Mileage':Mileage,'Gear box type':Gear_box_type,'Drive wheels':Drive_wheels,
                'Wheel':Wheel,'Color':Color,'Levy':Levy, 'Engine volume':Engine_volume,'Cylinders':Cylinders,
                'Airbags':Airbags,'Age':Age
              },index=[0])
print(df)
# Afficher les types de données de chaque colonne
print(df.dtypes)
button=st.sidebar.button('predict Price')
if button:
    prediction=data.predict(df)
    st.sidebar.write("price is :",prediction)