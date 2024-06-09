#  Apollo


apollo_all_data = dict()


links = {'self': 'http://api.nasa.gov/neo/rest/v1/neo/2001862?api_key=DEMO_KEY'}

id_code = "2001862"

neo_reference_id = "2001862"

name = "1862 Apollo (1932 HA)"

name_limited = "Apollo"

designation = "1862"

nasa_jpl_url = "https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=2001862"

absolute_magnitude_h = 16.08

estimated_diameter = {
    "feet": {'estimated_diameter_min': 5303.2246887282, 'estimated_diameter_max': 11858.3709039515}, 
    "miles": {'estimated_diameter_min': 1.0043982724, 'estimated_diameter_max': 2.2459028136}, 
    "meters": {'estimated_diameter_min': 1616.4228333988, 'estimated_diameter_max': 3614.4313358626}, 
    "kilometers": {'estimated_diameter_min': 1.6164228334, 'estimated_diameter_max': 3.6144313359}, 

}

is_potentially_hazardous_asteroid = True

close_approach_data = {
   "1905-Oct-06 20:28": {
       "close_approach_date": "1905-10-06", 
       "close_approach_date_full": "1905-Oct-06 20:28", 
       "epoch_date_close_approach": -2027129520000, 
       "relative_velocity": {
           "kilometers_per_second": "12.3118751776", 
           "kilometers_per_hour": "44322.7506393308", 
           "miles_per_hour": "27540.4335847553", 
       }, 
       "miss_distance": {
           "astronomical": "0.2670364858", 
           "lunar": "103.8771929762", 
           "kilometers": "39948089.487965246", 
           "miles": "24822591.7689465548", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "1907-Apr-29 12:34": {
       "close_approach_date": "1907-04-29", 
       "close_approach_date_full": "1907-Apr-29 12:34", 
       "epoch_date_close_approach": -1977909960000, 
       "relative_velocity": {
           "kilometers_per_second": "24.2864015732", 
           "kilometers_per_hour": "87431.0456634775", 
           "miles_per_hour": "54326.2516790647", 
       }, 
       "miss_distance": {
           "astronomical": "0.2394713065", 
           "lunar": "93.1543382285", 
           "kilometers": "35824397.378517155", 
           "miles": "22260248.309580539", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "1911-Jan-29 19:13": {
       "close_approach_date": "1911-01-29", 
       "close_approach_date_full": "1911-Jan-29 19:13", 
       "epoch_date_close_approach": -1859431620000, 
       "relative_velocity": {
           "kilometers_per_second": "11.6407199576", 
           "kilometers_per_hour": "41906.5918472117", 
           "miles_per_hour": "26039.1264730633", 
       }, 
       "miss_distance": {
           "astronomical": "0.0657746441", 
           "lunar": "25.5863365549", 
           "kilometers": "9839746.657368067", 
           "miles": "6114135.0566786446", 
       }, 
       "orbiting_body": "Venus", 
   }, 
   "1914-Aug-20 00:36": {
       "close_approach_date": "1914-08-20", 
       "close_approach_date_full": "1914-Aug-20 00:36", 
       "epoch_date_close_approach": -1747265040000, 
       "relative_velocity": {
           "kilometers_per_second": "16.7859807237", 
           "kilometers_per_hour": "60429.5306052318", 
           "miles_per_hour": "37548.5602807897", 
       }, 
       "miss_distance": {
           "astronomical": "0.3733807771", 
           "lunar": "145.2451222919", 
           "kilometers": "55856968.953104777", 
           "miles": "34707911.0802368426", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "1921-Nov-28 19:59": {
       "close_approach_date": "1921-11-28", 
       "close_approach_date_full": "1921-Nov-28 19:59", 
       "epoch_date_close_approach": -1517630460000, 
       "relative_velocity": {
           "kilometers_per_second": "28.1572209572", 
           "kilometers_per_hour": "101365.9954457609", 
           "miles_per_hour": "62984.8875590618", 
       }, 
       "miss_distance": {
           "astronomical": "0.3615124069", 
           "lunar": "140.6283262841", 
           "kilometers": "54081486.050813303", 
           "miles": "33604677.1623894614", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "1923-Jul-05 12:06": {
       "close_approach_date": "1923-07-05", 
       "close_approach_date_full": "1923-Jul-05 12:06", 
       "epoch_date_close_approach": -1467201240000, 
       "relative_velocity": {
           "kilometers_per_second": "14.0368634791", 
           "kilometers_per_hour": "50532.7085246923", 
           "miles_per_hour": "31399.0599163567", 
       }, 
       "miss_distance": {
           "astronomical": "0.3296989486", 
           "lunar": "128.2528910054", 
           "kilometers": "49322260.451799482", 
           "miles": "30647431.5044655716", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "1930-Sep-25 20:54": {
       "close_approach_date": "1930-09-25", 
       "close_approach_date_full": "1930-Sep-25 20:54", 
       "epoch_date_close_approach": -1239159960000, 
       "relative_velocity": {
           "kilometers_per_second": "11.6496413844", 
           "kilometers_per_hour": "41938.7089840139", 
           "miles_per_hour": "26059.0828128724", 
       }, 
       "miss_distance": {
           "astronomical": "0.0862900956", 
           "lunar": "33.5668471884", 
           "kilometers": "12908814.503856372", 
           "miles": "8021165.3863150536", 
       }, 
       "orbiting_body": "Venus", 
   }, 
   "1930-Nov-11 22:54": {
       "close_approach_date": "1930-11-11", 
       "close_approach_date_full": "1930-Nov-11 22:54", 
       "epoch_date_close_approach": -1235091960000, 
       "relative_velocity": {
           "kilometers_per_second": "17.7832028403", 
           "kilometers_per_hour": "64019.5302251866", 
           "miles_per_hour": "39779.2464335333", 
       }, 
       "miss_distance": {
           "astronomical": "0.0282674871", 
           "lunar": "10.9960524819", 
           "kilometers": "4228755.860412477", 
           "miles": "2627627.0469751026", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "1932-May-15 03:59": {
       "close_approach_date": "1932-05-15", 
       "close_approach_date_full": "1932-May-15 03:59", 
       "epoch_date_close_approach": -1187553660000, 
       "relative_velocity": {
           "kilometers_per_second": "15.2930589678", 
           "kilometers_per_hour": "55055.012284166", 
           "miles_per_hour": "34209.0436051253", 
       }, 
       "miss_distance": {
           "astronomical": "0.0750035574", 
           "lunar": "29.1763838286", 
           "kilometers": "11220372.429462738", 
           "miles": "6972016.1309842644", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "1939-Oct-14 15:34": {
       "close_approach_date": "1939-10-14", 
       "close_approach_date_full": "1939-Oct-14 15:34", 
       "epoch_date_close_approach": -953540760000, 
       "relative_velocity": {
           "kilometers_per_second": "11.8104504305", 
           "kilometers_per_hour": "42517.6215497928", 
           "miles_per_hour": "26418.796567981", 
       }, 
       "miss_distance": {
           "astronomical": "0.2424305742", 
           "lunar": "94.3054933638", 
           "kilometers": "36267097.523196954", 
           "miles": "22535329.4238038052", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "1941-May-01 09:44": {
       "close_approach_date": "1941-05-01", 
       "close_approach_date_full": "1941-May-01 09:44", 
       "epoch_date_close_approach": -904745760000, 
       "relative_velocity": {
           "kilometers_per_second": "23.0318466146", 
           "kilometers_per_hour": "82914.6478125161", 
           "miles_per_hour": "51519.9376921714", 
       }, 
       "miss_distance": {
           "astronomical": "0.198457275", 
           "lunar": "77.199879975", 
           "kilometers": "29688785.62600425", 
           "miles": "18447755.95418865", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "1946-Jul-02 17:04": {
       "close_approach_date": "1946-07-02", 
       "close_approach_date_full": "1946-Jul-02 17:04", 
       "epoch_date_close_approach": -741596160000, 
       "relative_velocity": {
           "kilometers_per_second": "11.6479161701", 
           "kilometers_per_hour": "41932.4982124388", 
           "miles_per_hour": "26055.2236809457", 
       }, 
       "miss_distance": {
           "astronomical": "0.0506596809", 
           "lunar": "19.7066158701", 
           "kilometers": "7578580.357519683", 
           "miles": "4709111.4697623054", 
       }, 
       "orbiting_body": "Mars", 
   }, 
   "1948-Aug-30 06:42": {
       "close_approach_date": "1948-08-30", 
       "close_approach_date_full": "1948-Aug-30 06:42", 
       "epoch_date_close_approach": -673377480000, 
       "relative_velocity": {
           "kilometers_per_second": "16.2706184608", 
           "kilometers_per_hour": "58574.2264587659", 
           "miles_per_hour": "36395.7464348926", 
       }, 
       "miss_distance": {
           "astronomical": "0.361872865", 
           "lunar": "140.768544485", 
           "kilometers": "54135409.81479755", 
           "miles": "33638183.83560419", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "1950-Apr-18 20:49": {
       "close_approach_date": "1950-04-18", 
       "close_approach_date_full": "1950-Apr-18 20:49", 
       "epoch_date_close_approach": -621832260000, 
       "relative_velocity": {
           "kilometers_per_second": "31.141289304", 
           "kilometers_per_hour": "112108.6414943201", 
           "miles_per_hour": "69659.9500440679", 
       }, 
       "miss_distance": {
           "astronomical": "0.4669160962", 
           "lunar": "181.6303614218", 
           "kilometers": "69849653.460235094", 
           "miles": "43402562.0566445372", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "1950-Jun-26 15:50": {
       "close_approach_date": "1950-06-26", 
       "close_approach_date_full": "1950-Jun-26 15:50", 
       "epoch_date_close_approach": -615888600000, 
       "relative_velocity": {
           "kilometers_per_second": "13.5220980192", 
           "kilometers_per_hour": "48679.5528690386", 
           "miles_per_hour": "30247.5810590979", 
       }, 
       "miss_distance": {
           "astronomical": "0.009947019", 
           "lunar": "3.869390391", 
           "kilometers": "1488052.85524953", 
           "miles": "924633.168442314", 
       }, 
       "orbiting_body": "Venus", 
   }, 
   "1955-Nov-28 19:53": {
       "close_approach_date": "1955-11-28", 
       "close_approach_date_full": "1955-Nov-28 19:53", 
       "epoch_date_close_approach": -444715620000, 
       "relative_velocity": {
           "kilometers_per_second": "27.6586337453", 
           "kilometers_per_hour": "99571.0814831117", 
           "miles_per_hour": "61869.5978248813", 
       }, 
       "miss_distance": {
           "astronomical": "0.345582897", 
           "lunar": "134.431746933", 
           "kilometers": "51698465.29962939", 
           "miles": "32123936.730449982", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "1957-Jun-26 18:32": {
       "close_approach_date": "1957-06-26", 
       "close_approach_date_full": "1957-Jun-26 18:32", 
       "epoch_date_close_approach": -394954080000, 
       "relative_velocity": {
           "kilometers_per_second": "12.9666967277", 
           "kilometers_per_hour": "46680.1082198431", 
           "miles_per_hour": "29005.2039102686", 
       }, 
       "miss_distance": {
           "astronomical": "0.3082582354", 
           "lunar": "119.9124535706", 
           "kilometers": "46114775.425798598", 
           "miles": "28654392.7277447324", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "1964-Oct-26 03:51": {
       "close_approach_date": "1964-10-26", 
       "close_approach_date_full": "1964-Oct-26 03:51", 
       "epoch_date_close_approach": -163541340000, 
       "relative_velocity": {
           "kilometers_per_second": "12.1717364091", 
           "kilometers_per_hour": "43818.2510727859", 
           "miles_per_hour": "27226.9571735319", 
       }, 
       "miss_distance": {
           "astronomical": "0.1854304162", 
           "lunar": "72.1324319018", 
           "kilometers": "27739995.296733494", 
           "miles": "17236833.7947864572", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "1966-May-02 02:58": {
       "close_approach_date": "1966-05-02", 
       "close_approach_date_full": "1966-May-02 02:58", 
       "epoch_date_close_approach": -115765320000, 
       "relative_velocity": {
           "kilometers_per_second": "22.6578598846", 
           "kilometers_per_hour": "81568.2955846241", 
           "miles_per_hour": "50683.3667759016", 
       }, 
       "miss_distance": {
           "astronomical": "0.1863195766", 
           "lunar": "72.4783152974", 
           "kilometers": "27873011.798661842", 
           "miles": "17319486.4164317396", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "1968-Apr-15 18:27": {
       "close_approach_date": "1968-04-15", 
       "close_approach_date_full": "1968-Apr-15 18:27", 
       "epoch_date_close_approach": -54019980000, 
       "relative_velocity": {
           "kilometers_per_second": "11.6320530644", 
           "kilometers_per_hour": "41875.391031858", 
           "miles_per_hour": "26019.7394997675", 
       }, 
       "miss_distance": {
           "astronomical": "0.0695227204", 
           "lunar": "27.0443382356", 
           "kilometers": "10400450.888445548", 
           "miles": "6462540.5100946424", 
       }, 
       "orbiting_body": "Venus", 
   }, 
   "1973-Aug-03 13:55": {
       "close_approach_date": "1973-08-03", 
       "close_approach_date_full": "1973-Aug-03 13:55", 
       "epoch_date_close_approach": 113234100000, 
       "relative_velocity": {
           "kilometers_per_second": "16.6762104289", 
           "kilometers_per_hour": "60034.3575439234", 
           "miles_per_hour": "37303.0151083339", 
       }, 
       "miss_distance": {
           "astronomical": "0.3748364916", 
           "lunar": "145.8113952324", 
           "kilometers": "56074740.741632892", 
           "miles": "34843228.1948902296", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "1980-Nov-13 17:15": {
       "close_approach_date": "1980-11-13", 
       "close_approach_date_full": "1980-Nov-13 17:15", 
       "epoch_date_close_approach": 342983700000, 
       "relative_velocity": {
           "kilometers_per_second": "18.7763174576", 
           "kilometers_per_hour": "67594.7428472311", 
           "miles_per_hour": "42000.7445208254", 
       }, 
       "miss_distance": {
           "astronomical": "0.0554813695", 
           "lunar": "21.5822527355", 
           "kilometers": "8299894.701882965", 
           "miles": "5157315.419856317", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "1982-May-14 17:13": {
       "close_approach_date": "1982-05-14", 
       "close_approach_date_full": "1982-May-14 17:13", 
       "epoch_date_close_approach": 390244380000, 
       "relative_velocity": {
           "kilometers_per_second": "15.8094104529", 
           "kilometers_per_hour": "56913.8776304191", 
           "miles_per_hour": "35364.070242079", 
       }, 
       "miss_distance": {
           "astronomical": "0.0586981502", 
           "lunar": "22.8335804278", 
           "kilometers": "8781118.242860074", 
           "miles": "5456333.8625500612", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "1986-Jan-22 20:40": {
       "close_approach_date": "1986-01-22", 
       "close_approach_date_full": "1986-Jan-22 20:40", 
       "epoch_date_close_approach": 506810400000, 
       "relative_velocity": {
           "kilometers_per_second": "11.5653998558", 
           "kilometers_per_hour": "41635.4394808494", 
           "miles_per_hour": "25870.64293742", 
       }, 
       "miss_distance": {
           "astronomical": "0.0852798562", 
           "lunar": "33.1738640618", 
           "kilometers": "12757684.841426294", 
           "miles": "7927257.7686350972", 
       }, 
       "orbiting_body": "Venus", 
   }, 
   "1989-Sep-10 14:31": {
       "close_approach_date": "1989-09-10", 
       "close_approach_date_full": "1989-Sep-10 14:31", 
       "epoch_date_close_approach": 621441060000, 
       "relative_velocity": {
           "kilometers_per_second": "15.3278950657", 
           "kilometers_per_hour": "55180.4222366017", 
           "miles_per_hour": "34286.9684725151", 
       }, 
       "miss_distance": {
           "astronomical": "0.3422804817", 
           "lunar": "133.1471073813", 
           "kilometers": "51204431.004893979", 
           "miles": "31816958.0544917502", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "1991-Apr-21 00:26": {
       "close_approach_date": "1991-04-21", 
       "close_approach_date_full": "1991-Apr-21 00:26", 
       "epoch_date_close_approach": 672193560000, 
       "relative_velocity": {
           "kilometers_per_second": "29.9273379135", 
           "kilometers_per_hour": "107738.4164885258", 
           "miles_per_hour": "66944.4621786621", 
       }, 
       "miss_distance": {
           "astronomical": "0.4278624595", 
           "lunar": "166.4384967455", 
           "kilometers": "64007312.594161265", 
           "miles": "39772299.779964857", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "1996-Dec-01 09:29": {
       "close_approach_date": "1996-12-01", 
       "close_approach_date_full": "1996-Dec-01 09:29", 
       "epoch_date_close_approach": 849432540000, 
       "relative_velocity": {
           "kilometers_per_second": "29.6490579416", 
           "kilometers_per_hour": "106736.6085897715", 
           "miles_per_hour": "66321.9777095722", 
       }, 
       "miss_distance": {
           "astronomical": "0.4110714709", 
           "lunar": "159.9068021801", 
           "kilometers": "61495416.464406983", 
           "miles": "38211479.9011150454", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "1998-Jul-09 12:32": {
       "close_approach_date": "1998-07-09", 
       "close_approach_date_full": "1998-Jul-09 12:32", 
       "epoch_date_close_approach": 899987520000, 
       "relative_velocity": {
           "kilometers_per_second": "14.5083741217", 
           "kilometers_per_hour": "52230.146838206", 
           "miles_per_hour": "32453.7820728842", 
       }, 
       "miss_distance": {
           "astronomical": "0.3388135923", 
           "lunar": "131.7984874047", 
           "kilometers": "50685791.735128401", 
           "miles": "31494690.5560018938", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2003-Dec-02 16:05": {
       "close_approach_date": "2003-12-02", 
       "close_approach_date_full": "2003-Dec-02 16:05", 
       "epoch_date_close_approach": 1070381100000, 
       "relative_velocity": {
           "kilometers_per_second": "11.6549157531", 
           "kilometers_per_hour": "41957.6967111089", 
           "miles_per_hour": "26070.8810480776", 
       }, 
       "miss_distance": {
           "astronomical": "0.0893893258", 
           "lunar": "34.7724477362", 
           "kilometers": "13372452.740416046", 
           "miles": "8309256.8275355948", 
       }, 
       "orbiting_body": "Venus", 
   }, 
   "2005-Nov-06 19:15": {
       "close_approach_date": "2005-11-06", 
       "close_approach_date_full": "2005-Nov-06 19:15", 
       "epoch_date_close_approach": 1131304500000, 
       "relative_velocity": {
           "kilometers_per_second": "15.2288441639", 
           "kilometers_per_hour": "54823.8389900454", 
           "miles_per_hour": "34065.4015102313", 
       }, 
       "miss_distance": {
           "astronomical": "0.0752460297", 
           "lunar": "29.2707055533", 
           "kilometers": "11256645.769076739", 
           "miles": "6994555.3390634382", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2007-May-08 15:18": {
       "close_approach_date": "2007-05-08", 
       "close_approach_date_full": "2007-May-08 15:18", 
       "epoch_date_close_approach": 1178637480000, 
       "relative_velocity": {
           "kilometers_per_second": "19.1791137772", 
           "kilometers_per_hour": "69044.8095980482", 
           "miles_per_hour": "42901.7596082983", 
       }, 
       "miss_distance": {
           "astronomical": "0.0714216704", 
           "lunar": "27.7830297856", 
           "kilometers": "10684529.763682048", 
           "miles": "6639058.9378983424", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2014-Aug-21 04:26": {
       "close_approach_date": "2014-08-21", 
       "close_approach_date_full": "2014-Aug-21 04:26", 
       "epoch_date_close_approach": 1408595160000, 
       "relative_velocity": {
           "kilometers_per_second": "16.7835839157", 
           "kilometers_per_hour": "60420.9020964721", 
           "miles_per_hour": "37543.1988609996", 
       }, 
       "miss_distance": {
           "astronomical": "0.3731436407", 
           "lunar": "145.1528762323", 
           "kilometers": "55821493.852765309", 
           "miles": "34685867.8750429042", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2021-Sep-18 13:57": {
       "close_approach_date": "2021-09-18", 
       "close_approach_date_full": "2021-Sep-18 13:57", 
       "epoch_date_close_approach": 1631973420000, 
       "relative_velocity": {
           "kilometers_per_second": "11.8749963119", 
           "kilometers_per_hour": "42749.9867227", 
           "miles_per_hour": "26563.1792500021", 
       }, 
       "miss_distance": {
           "astronomical": "0.0697946543", 
           "lunar": "27.1501205227", 
           "kilometers": "10441131.620666341", 
           "miles": "6487818.3449478658", 
       }, 
       "orbiting_body": "Venus", 
   }, 
   "2021-Nov-22 08:44": {
       "close_approach_date": "2021-11-22", 
       "close_approach_date_full": "2021-Nov-22 08:44", 
       "epoch_date_close_approach": 1637570640000, 
       "relative_velocity": {
           "kilometers_per_second": "23.5545794393", 
           "kilometers_per_hour": "84796.4859814289", 
           "miles_per_hour": "52689.2387477384", 
       }, 
       "miss_distance": {
           "astronomical": "0.2116190659", 
           "lunar": "82.3198166351", 
           "kilometers": "31657761.510029633", 
           "miles": "19671220.8357016154", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2023-May-30 10:16": {
       "close_approach_date": "2023-05-30", 
       "close_approach_date_full": "2023-May-30 10:16", 
       "epoch_date_close_approach": 1685441760000, 
       "relative_velocity": {
           "kilometers_per_second": "11.4187987472", 
           "kilometers_per_hour": "41107.6754898786", 
           "miles_per_hour": "25542.710917586", 
       }, 
       "miss_distance": {
           "astronomical": "0.2128176097", 
           "lunar": "82.7860501733", 
           "kilometers": "31837061.109611339", 
           "miles": "19782632.4406569182", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2030-Oct-04 03:27": {
       "close_approach_date": "2030-10-04", 
       "close_approach_date_full": "2030-Oct-04 03:27", 
       "epoch_date_close_approach": 1917314820000, 
       "relative_velocity": {
           "kilometers_per_second": "12.7071090471", 
           "kilometers_per_hour": "45745.592569574", 
           "miles_per_hour": "28424.5322274667", 
       }, 
       "miss_distance": {
           "astronomical": "0.2793585493", 
           "lunar": "108.6704756777", 
           "kilometers": "41791443.941569991", 
           "miles": "25967999.1131722358", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2032-Apr-26 20:30": {
       "close_approach_date": "2032-04-26", 
       "close_approach_date_full": "2032-Apr-26 20:30", 
       "epoch_date_close_approach": 1966624200000, 
       "relative_velocity": {
           "kilometers_per_second": "25.9362974198", 
           "kilometers_per_hour": "93370.6707113682", 
           "miles_per_hour": "58016.9036984054", 
       }, 
       "miss_distance": {
           "astronomical": "0.2958099347", 
           "lunar": "115.0700645983", 
           "kilometers": "44252536.155959089", 
           "miles": "27497250.9028458682", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2037-Nov-15 23:52": {
       "close_approach_date": "2037-11-15", 
       "close_approach_date_full": "2037-Nov-15 23:52", 
       "epoch_date_close_approach": 2141941920000, 
       "relative_velocity": {
           "kilometers_per_second": "20.8671712485", 
           "kilometers_per_hour": "75121.8164945057", 
           "miles_per_hour": "46677.775365711", 
       }, 
       "miss_distance": {
           "astronomical": "0.1431676288", 
           "lunar": "55.6922076032", 
           "kilometers": "21417572.321430656", 
           "miles": "13308262.3282128128", 
       }, 
       "orbiting_body": "Venus", 
   }, 
   "2039-Jul-17 03:57": {
       "close_approach_date": "2039-07-17", 
       "close_approach_date_full": "2039-Jul-17 03:57", 
       "epoch_date_close_approach": 2194487820000, 
       "relative_velocity": {
           "kilometers_per_second": "12.9032959092", 
           "kilometers_per_hour": "46451.8652730926", 
           "miles_per_hour": "28863.3826192725", 
       }, 
       "miss_distance": {
           "astronomical": "0.0579803347", 
           "lunar": "22.5543501983", 
           "kilometers": "8673734.573007089", 
           "miles": "5389608.7441882682", 
       }, 
       "orbiting_body": "Venus", 
   }, 
   "2039-Jul-26 05:09": {
       "close_approach_date": "2039-07-26", 
       "close_approach_date_full": "2039-Jul-26 05:09", 
       "epoch_date_close_approach": 2195269740000, 
       "relative_velocity": {
           "kilometers_per_second": "16.1277931737", 
           "kilometers_per_hour": "58060.055425293", 
           "miles_per_hour": "36076.2605502328", 
       }, 
       "miss_distance": {
           "astronomical": "0.366852007", 
           "lunar": "142.705430723", 
           "kilometers": "54880278.85242509", 
           "miles": "34101023.993402642", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2046-Nov-13 04:49": {
       "close_approach_date": "2046-11-13", 
       "close_approach_date_full": "2046-Nov-13 04:49", 
       "epoch_date_close_approach": 2425697340000, 
       "relative_velocity": {
           "kilometers_per_second": "17.9824579509", 
           "kilometers_per_hour": "64736.8486230978", 
           "miles_per_hour": "40224.9601902799", 
       }, 
       "miss_distance": {
           "astronomical": "0.0352917495", 
           "lunar": "13.7284905555", 
           "kilometers": "5279570.553773565", 
           "miles": "3280573.019922597", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2048-May-13 23:58": {
       "close_approach_date": "2048-05-13", 
       "close_approach_date_full": "2048-May-13 23:58", 
       "epoch_date_close_approach": 2473027080000, 
       "relative_velocity": {
           "kilometers_per_second": "16.1497801773", 
           "kilometers_per_hour": "58139.2086384258", 
           "miles_per_hour": "36125.443278693", 
       }, 
       "miss_distance": {
           "astronomical": "0.0497605008", 
           "lunar": "19.3568348112", 
           "kilometers": "7444064.929813296", 
           "miles": "4625527.4588276448", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2049-Dec-13 00:24": {
       "close_approach_date": "2049-12-13", 
       "close_approach_date_full": "2049-Dec-13 00:24", 
       "epoch_date_close_approach": 2522967840000, 
       "relative_velocity": {
           "kilometers_per_second": "11.1822791443", 
           "kilometers_per_hour": "40256.2049194181", 
           "miles_per_hour": "25013.6402178462", 
       }, 
       "miss_distance": {
           "astronomical": "0.0611389905", 
           "lunar": "23.7830673045", 
           "kilometers": "9146262.752750235", 
           "miles": "5683224.139953843", 
       }, 
       "orbiting_body": "Mars", 
   }, 
   "2055-Sep-18 02:39": {
       "close_approach_date": "2055-09-18", 
       "close_approach_date_full": "2055-Sep-18 02:39", 
       "epoch_date_close_approach": 2704847940000, 
       "relative_velocity": {
           "kilometers_per_second": "14.6272836348", 
           "kilometers_per_hour": "52658.2210852778", 
           "miles_per_hour": "32719.7707626828", 
       }, 
       "miss_distance": {
           "astronomical": "0.3270693322", 
           "lunar": "127.2299702258", 
           "kilometers": "48928875.439442414", 
           "miles": "30402993.3925327532", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2057-Apr-23 18:50": {
       "close_approach_date": "2057-04-23", 
       "close_approach_date_full": "2057-Apr-23 18:50", 
       "epoch_date_close_approach": 2755277400000, 
       "relative_velocity": {
           "kilometers_per_second": "28.2355236975", 
           "kilometers_per_hour": "101647.8853111696", 
           "miles_per_hour": "63160.0429590431", 
       }, 
       "miss_distance": {
           "astronomical": "0.3719412052", 
           "lunar": "144.6851288228", 
           "kilometers": "55641612.063152924", 
           "miles": "34574094.5139773912", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2057-Jun-06 09:28": {
       "close_approach_date": "2057-06-06", 
       "close_approach_date_full": "2057-Jun-06 09:28", 
       "epoch_date_close_approach": 2759045280000, 
       "relative_velocity": {
           "kilometers_per_second": "11.6017781285", 
           "kilometers_per_hour": "41766.4012625042", 
           "miles_per_hour": "25952.0174955821", 
       }, 
       "miss_distance": {
           "astronomical": "0.0868039423", 
           "lunar": "33.7667335547", 
           "kilometers": "12985684.875682901", 
           "miles": "8068930.4204739938", 
       }, 
       "orbiting_body": "Venus", 
   }, 
   "2064-Jul-25 22:57": {
       "close_approach_date": "2064-07-25", 
       "close_approach_date_full": "2064-Jul-25 22:57", 
       "epoch_date_close_approach": 2984252220000, 
       "relative_velocity": {
           "kilometers_per_second": "16.1403340355", 
           "kilometers_per_hour": "58105.2025279368", 
           "miles_per_hour": "36104.313204095", 
       }, 
       "miss_distance": {
           "astronomical": "0.3663630879", 
           "lunar": "142.5152411931", 
           "kilometers": "54807137.596462773", 
           "miles": "34055576.1243933474", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2071-Nov-17 19:34": {
       "close_approach_date": "2071-11-17", 
       "close_approach_date_full": "2071-Nov-17 19:34", 
       "epoch_date_close_approach": 3215014440000, 
       "relative_velocity": {
           "kilometers_per_second": "20.3379233847", 
           "kilometers_per_hour": "73216.5241848588", 
           "miles_per_hour": "45493.9008191974", 
       }, 
       "miss_distance": {
           "astronomical": "0.1066155268", 
           "lunar": "41.4734399252", 
           "kilometers": "15949455.718207916", 
           "miles": "9910532.2258086008", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2073-May-20 12:48": {
       "close_approach_date": "2073-05-20", 
       "close_approach_date_full": "2073-May-20 12:48", 
       "epoch_date_close_approach": 3262510080000, 
       "relative_velocity": {
           "kilometers_per_second": "13.5791249377", 
           "kilometers_per_hour": "48884.8497755774", 
           "miles_per_hour": "30375.1445730525", 
       }, 
       "miss_distance": {
           "astronomical": "0.1319297392", 
           "lunar": "51.3206685488", 
           "kilometers": "19736407.973975504", 
           "miles": "12263635.2427057952", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2075-May-17 22:47": {
       "close_approach_date": "2075-05-17", 
       "close_approach_date_full": "2075-May-17 22:47", 
       "epoch_date_close_approach": 3325358820000, 
       "relative_velocity": {
           "kilometers_per_second": "14.3167451968", 
           "kilometers_per_hour": "51540.2827085063", 
           "miles_per_hour": "32025.1273307382", 
       }, 
       "miss_distance": {
           "astronomical": "0.0083048366", 
           "lunar": "3.2305814374", 
           "kilometers": "1242385.866058042", 
           "miles": "771982.7798512996", 
       }, 
       "orbiting_body": "Venus", 
   }, 
   "2077-Jan-20 22:01": {
       "close_approach_date": "2077-01-20", 
       "close_approach_date_full": "2077-Jan-20 22:01", 
       "epoch_date_close_approach": 3378405660000, 
       "relative_velocity": {
           "kilometers_per_second": "14.4808956824", 
           "kilometers_per_hour": "52131.2244565241", 
           "miles_per_hour": "32392.3155518885", 
       }, 
       "miss_distance": {
           "astronomical": "0.0586217012", 
           "lunar": "22.8038417668", 
           "kilometers": "8769681.635296444", 
           "miles": "5449227.4841371672", 
       }, 
       "orbiting_body": "Venus", 
   }, 
   "2080-Nov-05 09:15": {
       "close_approach_date": "2080-11-05", 
       "close_approach_date_full": "2080-Nov-05 09:15", 
       "epoch_date_close_approach": 3498023700000, 
       "relative_velocity": {
           "kilometers_per_second": "14.5720439427", 
           "kilometers_per_hour": "52459.3581935411", 
           "miles_per_hour": "32596.2050953145", 
       }, 
       "miss_distance": {
           "astronomical": "0.0979261013", 
           "lunar": "38.0932534057", 
           "kilometers": "14649536.171884231", 
           "miles": "9102799.6747791478", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2082-May-12 11:03": {
       "close_approach_date": "2082-05-12", 
       "close_approach_date_full": "2082-May-12 11:03", 
       "epoch_date_close_approach": 3545809380000, 
       "relative_velocity": {
           "kilometers_per_second": "17.5069802792", 
           "kilometers_per_hour": "63025.1290050322", 
           "miles_per_hour": "39161.3641864879", 
       }, 
       "miss_distance": {
           "astronomical": "0.0333074687", 
           "lunar": "12.9566053243", 
           "kilometers": "4982726.372611669", 
           "miles": "3096122.5988282722", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2087-Jul-23 17:24": {
       "close_approach_date": "2087-07-23", 
       "close_approach_date_full": "2087-Jul-23 17:24", 
       "epoch_date_close_approach": 3709819440000, 
       "relative_velocity": {
           "kilometers_per_second": "12.734649917", 
           "kilometers_per_hour": "45844.7397011266", 
           "miles_per_hour": "28486.1383992917", 
       }, 
       "miss_distance": {
           "astronomical": "0.0777183462", 
           "lunar": "30.2324366718", 
           "kilometers": "11626499.051442594", 
           "miles": "7224371.5120080372", 
       }, 
       "orbiting_body": "Mars", 
   }, 
   "2089-Oct-22 19:12": {
       "close_approach_date": "2089-10-22", 
       "close_approach_date_full": "2089-Oct-22 19:12", 
       "epoch_date_close_approach": 3780846720000, 
       "relative_velocity": {
           "kilometers_per_second": "11.8522453889", 
           "kilometers_per_hour": "42668.0834000105", 
           "miles_per_hour": "26512.2877104121", 
       }, 
       "miss_distance": {
           "astronomical": "0.2094447685", 
           "lunar": "81.4740149465", 
           "kilometers": "31332491.250243095", 
           "miles": "19469107.268400911", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2091-May-06 06:37": {
       "close_approach_date": "2091-05-06", 
       "close_approach_date_full": "2091-May-06 06:37", 
       "epoch_date_close_approach": 3829271820000, 
       "relative_velocity": {
           "kilometers_per_second": "21.1515000361", 
           "kilometers_per_hour": "76145.4001300234", 
           "miles_per_hour": "47313.7904307915", 
       }, 
       "miss_distance": {
           "astronomical": "0.1355424634", 
           "lunar": "52.7260182626", 
           "kilometers": "20276863.819192958", 
           "miles": "12599458.9325725004", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2098-Aug-30 09:53": {
       "close_approach_date": "2098-08-30", 
       "close_approach_date_full": "2098-Aug-30 09:53", 
       "epoch_date_close_approach": 4060230780000, 
       "relative_velocity": {
           "kilometers_per_second": "11.694182388", 
           "kilometers_per_hour": "42099.0565967006", 
           "miles_per_hour": "26158.7165836555", 
       }, 
       "miss_distance": {
           "astronomical": "0.0887057227", 
           "lunar": "34.5065261303", 
           "kilometers": "13270187.172730649", 
           "miles": "8245711.9503909962", 
       }, 
       "orbiting_body": "Venus", 
   }, 
   "2098-Sep-25 10:25": {
       "close_approach_date": "2098-09-25", 
       "close_approach_date_full": "2098-Sep-25 10:25", 
       "epoch_date_close_approach": 4062479100000, 
       "relative_velocity": {
           "kilometers_per_second": "13.8287477148", 
           "kilometers_per_hour": "49783.4917733664", 
           "miles_per_hour": "30933.5257632898", 
       }, 
       "miss_distance": {
           "astronomical": "0.3079602484", 
           "lunar": "119.7965366276", 
           "kilometers": "46070197.205310908", 
           "miles": "28626693.1059822104", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2100-Apr-29 16:01": {
       "close_approach_date": "2100-04-29", 
       "close_approach_date_full": "2100-Apr-29 16:01", 
       "epoch_date_close_approach": 4112697660000, 
       "relative_velocity": {
           "kilometers_per_second": "25.4138818818", 
           "kilometers_per_hour": "91489.9747744134", 
           "miles_per_hour": "56848.312381357", 
       }, 
       "miss_distance": {
           "astronomical": "0.2778655569", 
           "lunar": "108.0897016341", 
           "kilometers": "41568095.458603803", 
           "miles": "25829216.8012783614", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2107-Sep-04 08:58": {
       "close_approach_date": "2107-09-04", 
       "close_approach_date_full": "2107-Sep-04 08:58", 
       "epoch_date_close_approach": 4344569880000, 
       "relative_velocity": {
           "kilometers_per_second": "16.1517085153", 
           "kilometers_per_hour": "58146.1506551232", 
           "miles_per_hour": "36129.7567779014", 
       }, 
       "miss_distance": {
           "astronomical": "0.3578631197", 
           "lunar": "139.2087535633", 
           "kilometers": "53535560.458675039", 
           "miles": "33265454.7293879782", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2109-Apr-22 14:59": {
       "close_approach_date": "2109-04-22", 
       "close_approach_date_full": "2109-Apr-22 14:59", 
       "epoch_date_close_approach": 4396085940000, 
       "relative_velocity": {
           "kilometers_per_second": "30.0485968591", 
           "kilometers_per_hour": "108174.9486926678", 
           "miles_per_hour": "67215.7063140635", 
       }, 
       "miss_distance": {
           "astronomical": "0.4307658045", 
           "lunar": "167.5678979505", 
           "kilometers": "64441646.822036415", 
           "miles": "40042182.554535927", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2116-Aug-14 14:45": {
       "close_approach_date": "2116-08-14", 
       "close_approach_date_full": "2116-Aug-14 14:45", 
       "epoch_date_close_approach": 4626859500000, 
       "relative_velocity": {
           "kilometers_per_second": "16.8982604331", 
           "kilometers_per_hour": "60833.7375591798", 
           "miles_per_hour": "37799.7187628137", 
       }, 
       "miss_distance": {
           "astronomical": "0.3755842367", 
           "lunar": "146.1022680763", 
           "kilometers": "56186601.815895829", 
           "miles": "34912735.4433432802", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2120-Mar-24 04:09": {
       "close_approach_date": "2120-03-24", 
       "close_approach_date_full": "2120-Mar-24 04:09", 
       "epoch_date_close_approach": 4740696540000, 
       "relative_velocity": {
           "kilometers_per_second": "11.6439582509", 
           "kilometers_per_hour": "41918.2497031298", 
           "miles_per_hour": "26046.3702113698", 
       }, 
       "miss_distance": {
           "astronomical": "0.0810313495", 
           "lunar": "31.5211949555", 
           "kilometers": "12122117.288425565", 
           "miles": "7532334.404040197", 
       }, 
       "orbiting_body": "Venus", 
   }, 
   "2123-Dec-05 19:53": {
       "close_approach_date": "2123-12-05", 
       "close_approach_date_full": "2123-Dec-05 19:53", 
       "epoch_date_close_approach": 4857479580000, 
       "relative_velocity": {
           "kilometers_per_second": "30.7110188729", 
           "kilometers_per_hour": "110559.6679425919", 
           "miles_per_hour": "68697.4781168844", 
       }, 
       "miss_distance": {
           "astronomical": "0.4450484985", 
           "lunar": "173.1238659165", 
           "kilometers": "66578307.422298195", 
           "miles": "41369841.887157291", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2125-Jul-24 15:07": {
       "close_approach_date": "2125-07-24", 
       "close_approach_date_full": "2125-Jul-24 15:07", 
       "epoch_date_close_approach": 4909043220000, 
       "relative_velocity": {
           "kilometers_per_second": "15.8757764379", 
           "kilometers_per_hour": "57152.7951765329", 
           "miles_per_hour": "35512.5243139962", 
       }, 
       "miss_distance": {
           "astronomical": "0.3620181406", 
           "lunar": "140.8250566934", 
           "kilometers": "54157142.735120522", 
           "miles": "33651688.0460943236", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2132-Nov-26 22:45": {
       "close_approach_date": "2132-11-26", 
       "close_approach_date_full": "2132-Nov-26 22:45", 
       "epoch_date_close_approach": 5140795500000, 
       "relative_velocity": {
           "kilometers_per_second": "25.4277216326", 
           "kilometers_per_hour": "91539.7978774504", 
           "miles_per_hour": "56879.2705200191", 
       }, 
       "miss_distance": {
           "astronomical": "0.2730122071", 
           "lunar": "106.2017485619", 
           "kilometers": "40842044.666158877", 
           "miles": "25378069.7588194226", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2134-Jun-29 12:52": {
       "close_approach_date": "2134-06-29", 
       "close_approach_date_full": "2134-Jun-29 12:52", 
       "epoch_date_close_approach": 5190871920000, 
       "relative_velocity": {
           "kilometers_per_second": "12.9803356276", 
           "kilometers_per_hour": "46729.2082592243", 
           "miles_per_hour": "29035.7127652941", 
       }, 
       "miss_distance": {
           "astronomical": "0.3079978164", 
           "lunar": "119.8111505796", 
           "kilometers": "46075817.298091068", 
           "miles": "28630185.2697020184", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2141-Oct-10 22:39": {
       "close_approach_date": "2141-10-10", 
       "close_approach_date_full": "2141-Oct-10 22:39", 
       "epoch_date_close_approach": 5420731140000, 
       "relative_velocity": {
           "kilometers_per_second": "11.6504670322", 
           "kilometers_per_hour": "41941.6813159736", 
           "miles_per_hour": "26060.9297043615", 
       }, 
       "miss_distance": {
           "astronomical": "0.0693938485", 
           "lunar": "26.9942070665", 
           "kilometers": "10381171.926702695", 
           "miles": "6450561.118759391", 
       }, 
       "orbiting_body": "Venus", 
   }, 
   "2141-Nov-19 08:49": {
       "close_approach_date": "2141-11-19", 
       "close_approach_date_full": "2141-Nov-19 08:49", 
       "epoch_date_close_approach": 5424137340000, 
       "relative_velocity": {
           "kilometers_per_second": "20.5862541026", 
           "kilometers_per_hour": "74110.5147691926", 
           "miles_per_hour": "46049.3918020019", 
       }, 
       "miss_distance": {
           "astronomical": "0.1143831119", 
           "lunar": "44.4950305291", 
           "kilometers": "17111469.904211653", 
           "miles": "10632574.3594526914", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2143-May-28 07:07": {
       "close_approach_date": "2143-05-28", 
       "close_approach_date_full": "2143-May-28 07:07", 
       "epoch_date_close_approach": 5472083220000, 
       "relative_velocity": {
           "kilometers_per_second": "12.1054164766", 
           "kilometers_per_hour": "43579.4993158234", 
           "miles_per_hour": "27078.6061165459", 
       }, 
       "miss_distance": {
           "astronomical": "0.1847178503", 
           "lunar": "71.8552437667", 
           "kilometers": "27633396.955858861", 
           "miles": "17170596.6572238418", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2150-Nov-10 14:06": {
       "close_approach_date": "2150-11-10", 
       "close_approach_date_full": "2150-Nov-10 14:06", 
       "epoch_date_close_approach": 5707375560000, 
       "relative_velocity": {
           "kilometers_per_second": "15.8510078082", 
           "kilometers_per_hour": "57063.6281093767", 
           "miles_per_hour": "35457.1193660736", 
       }, 
       "miss_distance": {
           "astronomical": "0.0577743517", 
           "lunar": "22.4742228113", 
           "kilometers": "8642919.954950879", 
           "miles": "5370461.4284009702", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2152-May-14 23:28": {
       "close_approach_date": "2152-05-14", 
       "close_approach_date_full": "2152-May-14 23:28", 
       "epoch_date_close_approach": 5755015680000, 
       "relative_velocity": {
           "kilometers_per_second": "16.6822295137", 
           "kilometers_per_hour": "60056.0262492199", 
           "miles_per_hour": "37316.4791991333", 
       }, 
       "miss_distance": {
           "astronomical": "0.0403545029", 
           "lunar": "15.6979016281", 
           "kilometers": "6036947.678748823", 
           "miles": "3751185.3427988374", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2159-Oct-23 18:05": {
       "close_approach_date": "2159-10-23", 
       "close_approach_date_full": "2159-Oct-23 18:05", 
       "epoch_date_close_approach": 5989831500000, 
       "relative_velocity": {
           "kilometers_per_second": "11.8359036245", 
           "kilometers_per_hour": "42609.2530480517", 
           "miles_per_hour": "26475.7328175519", 
       }, 
       "miss_distance": {
           "astronomical": "0.2145634085", 
           "lunar": "83.4651659065", 
           "kilometers": "32098228.891539895", 
           "miles": "19944914.575224751", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2161-May-06 13:45": {
       "close_approach_date": "2161-05-06", 
       "close_approach_date_full": "2161-May-06 13:45", 
       "epoch_date_close_approach": 6038286300000, 
       "relative_velocity": {
           "kilometers_per_second": "21.5529069103", 
           "kilometers_per_hour": "77590.4648770217", 
           "miles_per_hour": "48211.6974676138", 
       }, 
       "miss_distance": {
           "astronomical": "0.1500984687", 
           "lunar": "58.3883043243", 
           "kilometers": "22454411.207781669", 
           "miles": "13952524.1373742722", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2163-Apr-29 13:21": {
       "close_approach_date": "2163-04-29", 
       "close_approach_date_full": "2163-Apr-29 13:21", 
       "epoch_date_close_approach": 6100752060000, 
       "relative_velocity": {
           "kilometers_per_second": "11.9629526737", 
           "kilometers_per_hour": "43066.6296253175", 
           "miles_per_hour": "26759.928835798", 
       }, 
       "miss_distance": {
           "astronomical": "0.0509217334", 
           "lunar": "19.8085542926", 
           "kilometers": "7617782.853347858", 
           "miles": "4733470.7711141204", 
       }, 
       "orbiting_body": "Venus", 
   }, 
   "2165-Jan-04 04:12": {
       "close_approach_date": "2165-01-04", 
       "close_approach_date_full": "2165-Jan-04 04:12", 
       "epoch_date_close_approach": 6153941520000, 
       "relative_velocity": {
           "kilometers_per_second": "19.7074212168", 
           "kilometers_per_hour": "70946.716380413", 
           "miles_per_hour": "44083.5305198183", 
       }, 
       "miss_distance": {
           "astronomical": "0.1351993467", 
           "lunar": "52.5925458663", 
           "kilometers": "20225534.291711529", 
           "miles": "12567564.2431719402", 
       }, 
       "orbiting_body": "Venus", 
   }, 
   "2168-Sep-15 10:06": {
       "close_approach_date": "2168-09-15", 
       "close_approach_date_full": "2168-Sep-15 10:06", 
       "epoch_date_close_approach": 6270602760000, 
       "relative_velocity": {
           "kilometers_per_second": "15.1283259024", 
           "kilometers_per_hour": "54461.973248735", 
           "miles_per_hour": "33840.5522111376", 
       }, 
       "miss_distance": {
           "astronomical": "0.3363260192", 
           "lunar": "130.8308214688", 
           "kilometers": "50313656.097899104", 
           "miles": "31263456.1935074752", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2170-Apr-26 13:16": {
       "close_approach_date": "2170-04-26", 
       "close_approach_date_full": "2170-Apr-26 13:16", 
       "epoch_date_close_approach": 6321417360000, 
       "relative_velocity": {
           "kilometers_per_second": "27.9464865012", 
           "kilometers_per_hour": "100607.3514042077", 
           "miles_per_hour": "62513.4956544645", 
       }, 
       "miss_distance": {
           "astronomical": "0.3626615779", 
           "lunar": "141.0753538031", 
           "kilometers": "54253399.584679073", 
           "miles": "33711499.2789262874", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2177-Aug-16 00:16": {
       "close_approach_date": "2177-08-16", 
       "close_approach_date_full": "2177-Aug-16 00:16", 
       "epoch_date_close_approach": 6551972160000, 
       "relative_velocity": {
           "kilometers_per_second": "16.8986178595", 
           "kilometers_per_hour": "60835.0242942097", 
           "miles_per_hour": "37800.5182899216", 
       }, 
       "miss_distance": {
           "astronomical": "0.3752223481", 
           "lunar": "145.9614934109", 
           "kilometers": "56132464.052158547", 
           "miles": "34879095.7968480686", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2184-Oct-06 20:11": {
       "close_approach_date": "2184-10-06", 
       "close_approach_date_full": "2184-Oct-06 20:11", 
       "epoch_date_close_approach": 6777375060000, 
       "relative_velocity": {
           "kilometers_per_second": "11.5985829768", 
           "kilometers_per_hour": "41754.8987165812", 
           "miles_per_hour": "25944.8702608668", 
       }, 
       "miss_distance": {
           "astronomical": "0.0810126904", 
           "lunar": "31.5139365656", 
           "kilometers": "12119325.926809448", 
           "miles": "7530599.9323604624", 
       }, 
       "orbiting_body": "Venus", 
   }, 
   "2184-Dec-02 23:22": {
       "close_approach_date": "2184-12-02", 
       "close_approach_date_full": "2184-Dec-02 23:22", 
       "epoch_date_close_approach": 6782311320000, 
       "relative_velocity": {
           "kilometers_per_second": "29.0830083692", 
           "kilometers_per_hour": "104698.830129057", 
           "miles_per_hour": "65055.7814210243", 
       }, 
       "miss_distance": {
           "astronomical": "0.3923381564", 
           "lunar": "152.6195428396", 
           "kilometers": "58692952.517166868", 
           "miles": "36470109.5527160584", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2186-Jul-16 20:10": {
       "close_approach_date": "2186-07-16", 
       "close_approach_date_full": "2186-Jul-16 20:10", 
       "epoch_date_close_approach": 6833362200000, 
       "relative_velocity": {
           "kilometers_per_second": "15.0372889841", 
           "kilometers_per_hour": "54134.2403429303", 
           "miles_per_hour": "33636.9117286391", 
       }, 
       "miss_distance": {
           "astronomical": "0.3484757609", 
           "lunar": "135.5570709901", 
           "kilometers": "52131231.577269283", 
           "miles": "32392845.2259227854", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2193-Nov-22 21:28": {
       "close_approach_date": "2193-11-22", 
       "close_approach_date_full": "2193-Nov-22 21:28", 
       "epoch_date_close_approach": 7065437280000, 
       "relative_velocity": {
           "kilometers_per_second": "22.4484739214", 
           "kilometers_per_hour": "80814.5061168928", 
           "miles_per_hour": "50214.9913146882", 
       }, 
       "miss_distance": {
           "astronomical": "0.1750083905", 
           "lunar": "68.0782639045", 
           "kilometers": "26180882.450928235", 
           "miles": "16268045.995690243", 
       }, 
       "orbiting_body": "Earth", 
   }, 
   "2195-Jun-06 08:26": {
       "close_approach_date": "2195-06-06", 
       "close_approach_date_full": "2195-Jun-06 08:26", 
       "epoch_date_close_approach": 7113860760000, 
       "relative_velocity": {
           "kilometers_per_second": "11.1465011964", 
           "kilometers_per_hour": "40127.4043070015", 
           "miles_per_hour": "24933.6085262032", 
       }, 
       "miss_distance": {
           "astronomical": "0.2335162707", 
           "lunar": "90.8378293023", 
           "kilometers": "34933536.707063409", 
           "miles": "21706693.1570326842", 
       }, 
       "orbiting_body": "Earth", 
   }, 

}

orbital_data = {
    "orbit_id": "534", 
    "orbit_determination_date": "2024-02-25 04:47:48", 
    "first_observation_date": "1930-12-13", 
    "last_observation_date": "2024-02-24", 
    "data_arc_in_days": 34041, 
    "observations_used": 3461, 
    "orbit_uncertainty": "0", 
    "minimum_orbit_intersection": ".0258601", 
    "jupiter_tisserand_invariant": "4.414", 
    "epoch_osculation": "2460400.5", 
    "eccentricity": ".5599018486561474", 
    "semi_major_axis": "1.470568609437519", 
    "inclination": "6.352487409745255", 
    "ascending_node_longitude": "35.5558975176406", 
    "orbital_period": "651.367917328339", 
    "perihelion_distance": ".6471945264377521", 
    "perihelion_argument": "286.0393636096748", 
    "aphelion_distance": "2.293942692437287", 
    "perihelion_time": "2460142.994923678358", 
    "mean_anomaly": "142.3186881171835", 
    "mean_motion": ".5526830389138319", 
    "equinox": "J2000", 
    "orbit_class": {
        "orbit_class_type": "APO", 
        "description": "Near-Earth asteroid orbits which cross the Earthfs orbit similar to that of 1862 Apollo", 
        "orbit_class_range": "a (semi-major axis) > 1.0 AU; q (perihelion) < 1.017 AU", 
    }


}

is_sentry_object = False

apollo_all_data["links"] = links
apollo_all_data["id_code"] = id_code
apollo_all_data["neo_reference_id"] = neo_reference_id
apollo_all_data["name"] = name
apollo_all_data["name_limited"] = name_limited
apollo_all_data["designation"] = designation
apollo_all_data["nasa_jpl_url"] = nasa_jpl_url
apollo_all_data["absolute_magnitude_h"] = absolute_magnitude_h
apollo_all_data["estimated_diameter"] = estimated_diameter
apollo_all_data["is_potentially_hazardous_asteroid"] = is_potentially_hazardous_asteroid
apollo_all_data["close_approach_data"] = close_approach_data
apollo_all_data["orbital_data"] = orbital_data
apollo_all_data["is_sentry_object"] = is_sentry_object

