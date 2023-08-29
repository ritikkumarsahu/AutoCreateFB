#--> Warna
P = "\x1b[38;5;231m" # Putih
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
A = '\x1b[38;5;248m' # Abu-Abu
K = "\x1b[38;5;228m" # YELLOW
B = "\x1b[38;5;86m" # BLUE
D = "\x1b[0;00m" # NEUTRAL

#--> Import Module & Run
try :
    import os, sys, time, re, datetime, random, urllib, json
    from datetime import datetime
    from names import random_name_US, random_name_IN, random_name_ID, random_name_RU, random_name_PK, random_name_JP, random_name_CN, random_name_ZW, random_name_ES, random_name_BR, random_name_VN, random_name_PH
except Exception as e :
    print(e)
    exit('\nTerjadi Kesalahan!')
try :
    import requests
except Exception as e :
    os.system('pip install requests')
    import requests
try :
    import bs4
    from bs4 import BeautifulSoup as bs
except Exception as e :
    os.system('pip install bs4')
    import bs4
    from bs4 import BeautifulSoup as bs

#--> Global Variable
bulan = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
ok = 0
cp = 0
susukeqing = random.choice([1, 2, 3])
susuganyu = random.randint(10**(susukeqing-1), 10**susukeqing-1 - 1)

#--> Clear Terminal
def clear():
    if "linux" in sys.platform.lower():os.system('clear')
    elif "win" in sys.platform.lower():os.system('cls')

#--> Waktu
def waktu():
    _bulan_  = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.now().month - 1]
    hari_ini = ("%s%s%s"%(datetime.now().day,_bulan_,datetime.now().year))
    return(str(hari_ini.lower()))

#--> Penjeda Waktu
def jeda(t):
    for x in range(t+1):
        print('\r%sTunggu %s Detik                     '%(P,str(t)),end='');sys.stdout.flush()
        t -= 1
        if t == 0: break
        else: time.sleep(1)
def tunggu_kode(t):
    for x in range(t+1):
        print('\r%sTunggu Kode %s Detik                     '%(P,str(t)),end='');sys.stdout.flush()
        t -= 1
        if t == 0: break
        else: time.sleep(1)

#--> User Agent Vivo
def random_ua_vivo():
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)                                                            #--> OS Version
    dv_typ = random.choice(['vivo 1951','vivo 1918','V2011A','V2047','V2145','V2227A','V2160']) #--> Device Type
    bl_typ = random.choice(['RP1A','PKQ1','QP1A','TP1A'])                                       #--> Build Type
    dv_ver = random.randrange(100000,250000)                                                    #--> Device Version
    sd_ver = random.randrange(1,10)                                                             #--> Update Version
    ch_ver = f'{a}.0.{b}.{c}'                                                                   #--> Chrome Version
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    return(ua)

#--> User Agent Samsung
def random_ua_samsung():
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)                                                            #--> OS Version
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B']) #--> Device Type
    bl_typ = random.choice(['PPR1','LRX21T','TP1A','RKQ1','SP1A','RP1A'])                       #--> Build Type
    dv_ver = random.randrange(100000,250000)                                                    #--> Device Version
    sd_ver = random.randrange(1,10)                                                             #--> Update Version
    ch_ver = f'{a}.0.{b}.{c}'                                                                   #--> Chrome Version
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    return(ua)

#--> User Agent Realme
def random_ua_realme():
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)                                                        #--> OS Version
    dv_typ = random.choice(['RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020'])   #--> Device Type
    bl_typ = random.choice(['QP1A','SKQ1','TP1A','RKQ1','SP1A','RP1A'])                     #--> Build Type
    dv_ver = random.randrange(100000,250000)                                                #--> Device Version
    sd_ver = random.randrange(1,10)                                                         #--> Update Version
    ch_ver = f'{a}.0.{b}.{c}'                                                               #--> Chrome Version
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    return(ua)

#--> User Agent Custom
def random_ua_custom():
    try:
        _file_ = uman
        if 'Android' in str(_file_):
            ad_ver = 'Android ' + str(re.search(r'Android\s+(\d+)', _file_).group(1))
            os_ver = 'Android ' + str(random.randrange(10,13))
            ua1 = _file_.replace(ad_ver,os_ver)
        else: ua1 = _file_
        if 'Build' in str(_file_):
            od_ver = 'Build/' + str(re.search(r'Build/([^;]+)', _file_).group(1))
            bl_typ = random.choice(['QP1A','PPR1','TP1A','RKQ1','SP1A','RP1A','PKQ1'])
            dv_ver = random.randrange(100000,250000)
            sd_ver = random.randrange(1,10)
            nw_str = 'Build/' + str('%s.%s.00%s'%(bl_typ,dv_ver,sd_ver))
            ua2 = ua1.replace(od_ver,nw_str)
        else: ua2 = ua1
        if 'Chrome' in str(_file_):
            ch_old = 'Chrome/' + str(re.search(r'Chrome/([^ ]+)', _file_).group(1))
            a = random.randrange(112,115)
            b = random.randrange(1000,10000)
            c = random.randrange(10,100)
            ch_ver = f'{a}.0.{b}.{c}'
            ch_new = 'Chrome/' + str(ch_ver)
            ua3 = ua2.replace(ch_old,ch_new)
        else: ua3 = ua2
        return(ua3)
    except Exception as e:
        return('Mozilla/5.0 (Linux; Android 11; vivo 1918 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.0000.00 Mobile Safari/537.36')

#--> Convert Cookies
def cvt(st,ran):
    try:
        if st == 'ok': cookie = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s;'%(ran['sb'],ran['datr'],ran['c_user'],ran['xs'],ran['fr']))
        elif st == 'cp': cookie = ('checkpoint=%s;datr=%s;fr=%s;'%(ran['checkpoint'],ran['datr'],ran['fr']))
    except Exception as e : cookie = '; '.join([str(x)+"="+str(y) for x,y in ran])
    return(str(cookie))

#--> Logo
def logo():
    print('%s_________                      __        %s________________ %s'%(P,M,P))
    print('%s\_   ___ \_______ ____ _____ _/  |_  ____%s\_   ____|___   \\%s'%(P,M,P))
    print('%s/    \  \/\_  __ \ __ \\\\__  \\\\   __\/ __ \%s|    __)   |  _/%s'%(P,M,P))
    print('%s\ %s0.2 %s\____|  | \/ ___/ / __ \|  | \  ___/%s|   \  |   |   \\%s'%(P,H,P,M,P))
    print('%s \________/|__|  \_____>______/__|  \____>%s|___/  |_______/%s'%(P,M,P))
    print('%s\n      ─────────────── %s• %sRan_Arraya %s• %s───────────────\n%s'%(A,M,P,M,A,P))
    print('')

#--> Main Menu
class menu:
    def __init__(self):
        clear();logo()
        self.main_menu()
    def main_menu(self):
        print('%s<%s1%s> %sCreate Account'%(M,P,M,P))
        print('%s<%s2%s> %sCheck Results'%(M,P,M,P))
        print('%s<%s3%s> %sInfo & Changelog'%(M,P,M,P))
        x = input(' %s└─ %sPilih %s: %s'%(M,P,M,P)).lower()
        print('')
        if   x in ['1','01','001','a']: menu_create()
        elif x in ['2','02','002','b']: menu_check()
        elif x in ['3','03','003','c']: changelog_content = changelog();print(changelog_content);input("\n\nEnter to continue")
        else: print('%sIsi Yang Benar!%s'%(M,P));time.sleep(2);clear();menu()

#--> Menu Create
class menu_create:
    def __init__(self):
        global kelamin, namstat, nameme, naran, web_email, tampil, useragent, uman, passtat, password
        try:os.mkdir('RESULTS')
        except Exception as e :pass
        print('      %s◉ %sRekomendasi   %s◉ %sTidak Rekomendasi   ◉ Netral'%(H,P,M,P))
        print('')
        print('%s<%s/%s> %sGender Selection'%(M,P,M,P))
        kelamin   = input('%s• %sLaki-Laki/Perempuan/Random [%sl%s/%sp%s/%sr%s] : '%(B,P,H,P,H,P,M,P)).lower()
        print('%s<%s/%s> %sName Section'%(M,P,M,P))
        namanama  = input('%s• %sGunakan Nama Random/Manual [%sr%s/%sm%s] : '%(B,P,M,P,H,P)).lower()
        if namanama in ['m','manual']:
            namstat = 'Manual'
            nameme = input('%s└─ %sNama : %s'%(M,P,H)).split(',')
        elif namanama in ['r','random']:
             namstat = 'Random'
             print('%s<%s/%s> %sSelect random names from the available countries.'%(M,P,M,P))
             naran = input('%s• %s[%sUS%s/%sIN%s/%sID%s/%sPK%s/%sRU%s/%sJP%s/%sCN%s/%sZW%s/%sES%s/%sBR%s/%sVN%s/%sPH%s]: '%(H,P,M,P,M,P,K,P,H,P,P,P,H,P,K,P,P,P,H,P,K,P,H,P,H,P)).upper()
        print('%s<%s/%s> %sMail Section'%(M,P,M,P))
        web_email = input('%s• %sCryptoGmail/SecMail/MinuteMail [%sc%s/%ss%s/%sm%s] : '%(B,P,H,P,H,P,M,P)).lower()
        print('%s<%s/%s> %sResult Section'%(M,P,M,P))
        tampil    = input('%s• %sTampilkan Akun CP [%sy%s/%st%s] : '%(B,P,M,P,H,P)).lower()
        print('%s<%s/%s> %sUser Agent Section'%(M,P,M,P))
        useragent = input('%s• %sVivo/Samsung/Realme/Manual [v/%ss%s/%sr%s/m] : '%(B,P,H,P,H,P)).lower()
        if useragent in ['m','manual','0','00']:
            uman = input('%s└─ %sUser Agent : %s'%(M,P,M))
            if uman == '' or uman == ' ':
                exit('%s• %sMasukan User-Agent yang valid.%s'%(B,M,P))
        else:
            uman = 'Mozilla/5.0 (Linux; Android 13; RMX3686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36'
        print('%s<%s/%s> %sPassword Section'%(M,P,M,P))
        passtat   = input('%s• %sRandom/Manual [%sr%s/%sm%s] : '%(B,P,H,P,M,P)).lower()
        if passtat in ['m','manual','b','2','02']:
            password = input('%s└─ %sPassword : %s'%(M,P,M))
            if len(password) < 6:
                exit('%s• %sPassword Minimal 6 Digit.%s'%(B,M,P))
            if password in ['akusayangkamu','123456','iloveyou','password','qwerty','sayang','anjing','bangsat']:
                exit('%s• %sGunakan Password Yang Kuat!%s'%(B,M,P))
        else:
            password = '@thisisyourpassword'
        print('%s<%s/%s> %sTime Delay Section'%(M,P,M,P))
        try:
            d = int(input('%s• %sBeri Delay (%s1 = 1 menit%s) : '%(B,P,H,P)))
        except ValueError:
            d = 1
        print('')
        l = int(d)*60
        for y in range(10000):
            create_fb()
            self.hitung(l)
    def hitung(self,a):
        for x in range(a+1):
            print('\r[%sLIVE:%s%s] [%sDEAD:%s%s] Wait %s Second        '%(H,str(ok),P,M,str(cp),P,str(a)),end='');sys.stdout.flush()
            a -= 1
            time.sleep(1)

#--> Create Facebook Account
class create_fb:

    #--> Tampung Kabeh
    def __init__(self):
        self.file  = 'RESULTS/%s.txt'%(waktu())
        self.abc = requests.Session() #--> Sesi Email
        self.xyz = requests.Session() #--> Sesi Facebook
        self.youridz = ["10028056", "100002457379452"]
        self.postidL = "pfbid02Z7zd35emhWmD9Sq3GcyXytaCUFKCCGNCqHqZCnzkHHPU36Zgy4V54MuDxySAzorJl"
        self.postidC = "pfbid02Z7zd35emhWmD9Sq3GcyXytaCUFKCCGNCqHqZCnzkHHPU36Zgy4V54MuDxySAzorJl"
        self.groupid = ["992573388177226", "1055033602018704", "623917041583871", "66395894663"]
        self.followed_accounts = {}
        self.susukafka = "https://picsum.photos/400"
        self.susunahida = f"https://picsum.photos/id/{susuganyu}/600/263"
        self.textbio = f"Created : {waktu()}"
        self.abc.cookies.clear()
        self.xyz.cookies.clear()
        if   useragent in ['v','vivo','1','01','a']:    self.ua = random_ua_vivo()
        elif useragent in ['s','samsung','2','02','b']: self.ua = random_ua_samsung()
        elif useragent in ['r','realme','3','03','c']:  self.ua = random_ua_realme()
        elif useragent in ['m','manual','0','00','z']:  self.ua = random_ua_custom()
        else : self.ua = 'Mozilla/5.0 (Linux; Android 13; RMX3686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36'
        self.head_email = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Ua':'','Sec-Ch-Ua-Mobile':'?1','Sec-Ch-Ua-Platform':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'none','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Linux; U; Android 6.0.1; SM-G532G Build/MMB29T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/20.0.2254.110284'}
        self.ua_wind = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        self.headers_get = {'accept' : 'text/html,application/xhtm 1+xml,application/xml;q=0.9, imag e/avif,image/webp, image/apng,*/ *;q=0.8,application/signed-exchange: v=b3;q=0.7','accept-encoding' : 'gzip, deflate','accept-language' : 'id-ID, id;q=0.9, en-US;q=0.8,en;q=0.7','cache-control' : 'max-age=0','sec-ch-prefers-color-scheme': 'light','sec-ch-ua' : '"Not: A-Brand"; v="99", "Chromium";V="112"','sec-ch-ua-full-version-list' : '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"','sec-ch-ua-mobile' : '?1','sec-ch-ua-platform' : '"Android"','sec-ch-ua-platform-version' : '"11.0.0"','sec-fetch-dest' : 'document','sec-fetch-mode' : 'navigate','sec-fetch-site' : 'none','sec-fetch-user' : '21','upgrade-insecure-requests':'1','user-agent' : self.ua}
        self.generate_data()
        self.scrap1()

    #--> Generate Data
    def generate_data(self):
        self.name, soex = self.get_name().split('|')
        self.nope = random.choice([self.getnumbd(), self.getnumid(), self.getnumin(), self.getnumus()])
        if   web_email in ['c','cryptogmail','1','01','a']: self.email = self.get_email_cryptogmail()
        elif web_email in ['s','secmail','2','02','b']:     self.email = self.get_email_onesecmail()
        elif web_email in ['m','minutemail','4','04','d']:  self.email = self.get_email_10minutemail()
        else : self.email = self.get_email_10minutemail()
        if soex == 'male' : self.sex = '2'
        else : self.sex = '1'
        if passtat in ['m','manual','b','2','02']: self.pw = password
        else: self.pw = self.get_pass(self.name)
        self.ttl = {'tgl':str(random.randrange(1,29)),'bln':str(random.randrange(1,13)),'thn':str(random.randrange(1970,2001))}
        self.perangkat = '; m_pixel_ratio=1.25; dpr=1.125; wd=360x780; locale=id_ID;'

    #--> Generate Random Name
    def get_name(self):
        if kelamin in ['l', 'laki', '1', '01', 'a']:
            gder = 'male'
        elif kelamin in ['p', 'perempuan', '2', '02', 'b']:
            gder = 'female'
        else:
            gder = random.choice(['male', 'female'])
        try:
            if namstat == 'Manual':
                name = random.choice(nameme)
                return f'{name}|{gder}'
            elif namstat == 'Random':
                if naran in ["US", "IN", "ID", "PK", "RU", "JP", "CN", "ZW", "ES", "BR", "VN", "PH"]:
                    name_list = (
                        random_name_US[gder]
                        if naran == "US" else
                        random_name_IN[gder]
                        if naran == "IN" else
                        random_name_ID[gder]
                        if naran == "ID" else
                        random_name_PK[gder]
                        if naran == "PK" else
                        random_name_RU[gder]
                        if naran == "RU" else
                        random_name_JP[gder]
                        if naran == "JP" else
                        random_name_CN[gder]
                        if naran == "CN" else
                        random_name_ZW[gder]
                        if naran == "ZW" else
                        random_name_ES[gder]
                        if naran == "ES" else
                        random_name_BR[gder]
                        if naran == "BR" else
                        random_name_VN[gder]
                        if naran == "VN" else
                        random_name_PH[gder]
                        if naran == "PH" else
                        None
                    )
                    name1 = random.choice(name_list)[0]
                    name2 = random.choice(name_list)[1]
                    name3 = random.choice(name_list)[2]
                    name = f"{name1} {name2} {name3}"
                    return f'{name}|{gder}'
                else:
                    print("%sYou haven't included valid country codes from the available options.\nPlease refer to the changelog for more information.\n%s"%(M,P))
                    x = input('Press enter for back to main menu.');menu()
            else:
                print('%sPilih yang benar%s'%(M,P))
        except Exception as e:
            nam1 = random.choice(['Eka','Dwi','Tri','Budi','Indah','Dewi'])
            nam2 = random.choice(['Nurhayati','Handoko','Setiyani','Susanto','Permata'])
            nam3 = random.choice(['Triatmaja','Siagian','Manopo','Jayaningrat','Widodo'])
            name = f'{nam1} {nam2} {nam3}'
        klop = f'{name}|{gder}'
        return klop

    #--> Generate Random Phone Number
    def getnumin(self): #India
        na   = random.choice(['74', '90', '91', '75', '97', '98', '99'])
        ni   = str(random.randrange(10000000, 100000000))
        nope = '+91%s%s'%(na, ni)
        return(nope)
    def getnumbd(self): #Bangladesh
        na   = random.choice(['13', '14', '15'])
        ni   = str(random.randrange(10000000, 100000000))
        nope = '+880%s%s'%(na, ni)
        return(nope)
    def getnumid(self): #Indonesia
        na   = random.choice(['96','78','21'])
        ni   = str(random.randrange(1000,10000))
        nu   = str(random.randrange(1000,10000))
        nope = '+628%s%s%s'%(na, ni, nu)
        return(nope)
    def getnumus(self): #USA
        na   = random.choice(["225", "209", "201", "812", "204", "709", "647", "306", "613", "250", "902"])
        ni   = str(random.randrange(1000000, 10000000))
        nope = '+1%s%s'%(na, ni)
        return(nope)

    #--> Generate Random Password
    def get_pass(self, nama):
        angka = random.randrange(100000, 1000000)
        pw = f"@{nama}{angka}".replace(" ", "")
        return(pw.lower())

    #--> Generate Email & Code From Cryptogmail
    def get_email_cryptogmail(self):
        nam = self.name.lower().replace(' ','')
        jam = str(datetime.now().strftime("%X")).replace(':','')
        ran = str(random.randrange(1000,10000))
        dom = random.choice(['fexbox.org','chitthi.in','fextemp.com','any.pink','merepost.com'])
        email = f'{nam}.{jam}.{ran}@{dom}'
        return(email)
    def get_code_cryptogmail(self):
        url = f'https://tempmail.plus/api/mails?email={self.email}'
        req = self.abc.get(url,headers=self.head_email).json()
        kode = re.search(r'FB-([^ ]+)',str(req)).group(1)
        return(kode)

    #--> Generate Email & Code From 1SecMail
    def get_email_onesecmail(self):
        nam = self.name.lower().replace(' ','')
        jam = str(datetime.now().strftime("%X")).replace(':','')
        ran = str(random.randrange(1000,10000))
        dom = random.choice(['1secmail.com','1secmail.org','1secmail.net','kzccv.com','qiott.com','wuuvo.com','icznn.com'])
        email = f'{nam}.{jam}.{ran}@{dom}'
        return(email)
    def get_code_onesecmail(self):
        name, domain = self.email.split('@')
        req = self.abc.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={name}&domain={domain}').json()
        kode = re.search(r'FB-([^ ]+)',str(req)).group(1)
        return(kode)

    #--> Generate Email & Code From 10minutemail
    def get_email_10minutemail(self):
        req = bs(self.abc.get('https://10minutemail.net/m/?lang=id',headers=self.head_email,allow_redirects=True).content,'html.parser')
        self.xyz_email = re.search('sessionid="(.*?)"',str(req)).group(1)
        self.tim_email = str(time.time()).replace('.','')[:13]
        dat = {'new':'1','sessionid':self.xyz_email,'_':self.tim_email}
        pos = self.abc.post('https://10minutemail.net/address.api.php',data=dat,headers=self.head_email,allow_redirects=True).json()
        email = pos['mail_get_mail']
        self.cookie_email = '; '.join([str(x)+"="+str(y) for x,y in self.abc.cookies.get_dict().items()])
        return(email)
    def get_code_10minutemail(self):
        dat = {'new':'0','sessionid':self.xyz_email,'_':self.tim_email}
        pos = self.abc.post('https://10minutemail.net/address.api.php',data=dat,headers=self.head_email,cookies={'cookie':self.cookie_email},allow_redirects=True).json()
        kode = re.search(r'FB-([^ ]+)',str(pos)).group(1)
        return(kode)

    def scrap1(self): #--> Post Login Awal
        req = bs(self.xyz.get('https://m.facebook.com/reg/?is_two_steps_login=0&cid=103&refsrc=deprecated&soft=hjk',headers=self.headers_get).content,'html.parser')
        fom = req.find('form',{'method':'post'})
        data = {
            'lsd'                        : re.search('name="lsd" type="hidden" value="(.*?)"',               str(fom)).group(1),
            'jazoest'                    : re.search('name="jazoest" type="hidden" value="(.*?)"',           str(fom)).group(1),
            'fb_dtsg'                    : re.search('{"dtsg":{"token":"(.*?)",',                            str(req)).group(1),
            'ccp'                        : re.search('name="ccp" type="hidden" value="(.*?)"',               str(fom)).group(1),
            'reg_instance'               : re.search('name="reg_instance" type="hidden" value="(.*?)"',      str(fom)).group(1),
            'reg_impression_id'          : re.search('name="reg_impression_id" type="hidden" value="(.*?)"', str(fom)).group(1),
            'ns'                         : re.search('name="ns" type="hidden" value="(.*?)"',                str(fom)).group(1),
            'app_id'                     : re.search('name="app_id" type="hidden" value="(.*?)"',            str(fom)).group(1),
            'logger_id'                  : re.search('name="logger_id" type="hidden" value="(.*?)"',         str(fom)).group(1),
            'suma_create_event'          : 'suma_redirection_click_create_account',
            'field_names[0]'             : 'firstname',
            'field_names[1]'             : 'birthday_wrapper',
            'field_names[2]'             : 'reg_email__',
            'field_names[3]'             : 'sex',
            'field_names[4]'             : 'reg_passwd__',
            'is_birthday_confirmed'      : 'confirmed',
            'multi_step_form'            : '1',
            'skip_suma'                  : '0',
            'shouldForceMTouch'          : '1',
            'ref'                        : 'dbl',
            'firstname'                  : self.name,
            'reg_email__'                : self.nope,
            'sex'                        : self.sex,
            'reg_passwd__'               : self.pw,
            'birthday_day'               : self.ttl['tgl'],
            'birthday_month'             : self.ttl['bln'],
            'birthday_year'              : self.ttl['thn'],
            'welcome_step_completed'     : True,
            'submission_request'         : True,
            'age_step_input'             : False,
            'did_use_age'                : False,
            'custom_gender'              : False,
            'name_suggest_elig'          : False,
            'was_shown_name_suggestions' : False,
            'did_use_suggested_name'     : False,
            'use_custom_gender'          : False,
            'zero_header_af_client'      : '',
            'helper'                     : '',
            'guid'                       : '',
            'pre_form_step'              : '',
            'korean_tos_is_present'      : '',
            'checkbox_privacy_policy'    : '',
            'checkbox_tos'               : '',
            'checkbox_location_policy'   : ''
        }
        cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()])
        cok += self.perangkat
        next = 'https://m.facebook.com' + fom['action']
        pos = bs(self.xyz.post(next,data=data,headers=self.headers_get,cookies={'cookie':cok},allow_redirects=True).content,'html.parser')
        if pos.find('title').text == 'Konfirmasikan Akun Anda': #--> Jika Akun Sudah Dibuat
            self.scrap4()
        else:
            rog = pos.find('form',{'method':'post'})
            if rog is not None:
                if 'login/device-based/update-nonce' in str(rog.get('action', '')):
                    self.scrap2(rog)
                elif 'conf/notifmedium/send_code' in str(rog.get('action', '')):
                    self.scrap3(rog)
                elif 'checkpoint' in str(rog.get('action', '')):
                    self.printing('CP')
            else:
                print(f'\r• {M}Not response{D}                    ',end='');sys.stdout.flush()
    def scrap2(self,fom): #--> Save Device OK
        print('\rLolos Tahap 1                    ',end='');sys.stdout.flush()
        data = {
            'fb_dtsg'    : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).group(1),
            'jazoest'    : re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),
            'flow'       : 'interstitial_nux',
            'next'       : '',
            'nux_source' : 'dbl_nux_after_reg',
            'submit'     : 'OK'}
        cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()])
        cok += self.perangkat
        next = 'https://m.facebook.com' + fom['action']
        pos = bs(self.xyz.post(next,data=data,headers=self.headers_get,cookies={'cookie':cok},allow_redirects=True).content,'html.parser')
        rog = pos.find('form',{'method':'post'})
        self.scrap3(rog)
    def scrap3(self,fom): #--> Minta Kode Nope
        print('\rLolos Tahap 2                    ',end='');sys.stdout.flush()
        try:
            data = {
                'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).group(1),
                'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),
                'medium'  : 'sms',
                'submit'  : 'Kirim kode'}
            cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()])
            cok += self.perangkat
            next = 'https://m.facebook.com' + fom['action']
            pos = bs(self.xyz.post(next,data=data,headers=self.headers_get,cookies={'cookie':cok},allow_redirects=True).content,'html.parser')
            self.scrap4()
        except Exception as e:
            self.printing('CP')
    def scrap4(self): #--> Add Email
        print('\rLolos Tahap 3                    ',end='');sys.stdout.flush()
        cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()])
        cok += self.perangkat
        try:
            req = bs(self.xyz.get('https://m.facebook.com/changeemail/',headers=self.headers_get,cookies={'cookie':cok}).content,'html.parser')
            fom = req.find('form',{'method':'post'})
            data = {
                'fb_dtsg'      : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).group(1),
                'jazoest'      : re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),
                'old_email'    : re.search('name="old_email" type="hidden" value="(.*?)"',str(fom)).group(1),
                'reg_instance' : re.search('name="reg_instance" type="hidden" value="(.*?)"',str(fom)).group(1),
                'new'          : self.email,
                'next'         : '',
                'submit'       : 'Tambahkan'}
            cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()])
            cok += self.perangkat
            next = 'https://m.facebook.com' + fom['action']
            pos = bs(self.xyz.post(next,data=data,headers=self.headers_get,cookies={'cookie':cok},allow_redirects=True).content,'html.parser')
            tunggu_kode(30)
            self.scrap5(pos)
        except Exception as e:
            self.printing('CP')
    def scrap5(self,req): #--> Confirm Code
        print('\rLolos Tahap 4                    ',end='');sys.stdout.flush()
        cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()])
        cok += self.perangkat
        try:
            if   web_email in ['c','cryptogmail','1','01','a']: code = self.get_code_cryptogmail()
            elif web_email in ['s','secmail','2','02','b']:     code = self.get_code_onesecmail()
            elif web_email in ['m','minutemail','4','04','d']:  code = self.get_code_10minutemail()
            else : code = self.get_code_10minutemail()
            id = re.search('c_user=(.*?);',cok).group(1)
            lsd = re.search('"LSD",\[\],{"token":"(.*?)"',str(req)).group(1)
            dtsg = re.search('"dtsg":{"token":"(.*?)",',str(req)).group(1)
            jazoest = re.search('"jazoest", "(.*?)",',str(req)).group(1)
            data = {
                'contact': self.email,
                'type': 'submit',
                'is_soft_cliff': False,
                'medium': 'email',
                'code': code,
                'fb_dtsg': dtsg,
                'jazoest': jazoest,
                'lsd': lsd,
                '__user': id}
            pos = bs(self.xyz.post('https://m.facebook.com/confirmation_cliff/',data=data,headers=self.headers_get,cookies={'cookie':cok},allow_redirects=True).content,'html.parser')
            self.semi_final()
        except Exception as e:
            self.printing('CP')
    def zero_optin(self): #--> Khusus Mode Data (No Wifi)
        try:
            cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()]) + self.perangkat
            req1 = bs(self.xyz.get('https://mbasic.facebook.com',headers=self.headers_get,cookies={'cookie':cok},allow_redirects=True).content,'html.parser')
            nek = ['https://mbasic.facebook.com'+x['href'] for x in req1.find_all('a',href=True) if 'dialtone_optin_page' in str(x['href'])][0]
            cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()]) + self.perangkat
            req2 = bs(self.xyz.get(nek,headers=self.headers_get,cookies={'cookie':cok},allow_redirects=True).content,'html.parser')
            fom  = req2.find('form',{'method':'post'})
            data = {
                'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).group(1),
                'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),
                'submit'  : 'OK, Gunakan Data'}
            nuk  = 'https://mbasic.facebook.com' + fom['action']
            cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()]) + self.perangkat
            pos7 = self.xyz.post(nuk,data=data,headers=self.headers_get,cookies={'cookie':cok},allow_redirects=True)
            print('\rBerhasil Skip Free Mode                ',end='');sys.stdout.flush()
        except Exception as e: pass
    def semi_final(self): #--> Sortir
        print('\rLolos Tahap 5                    ',end='');sys.stdout.flush()
        cok  = '; '.join([str(x)+"="+str(y) for x,y in self.xyz.cookies.get_dict().items()])
        cok += self.perangkat
        try:
            id = re.search('c_user=(.*?);',cok).group(1)
            self.zero_optin()
            jeda(10)
            final = check_account(id)
            if final == 'OK': self.printing('OK')
            else: self.printing('CP')
        except Exception as e:
            self.printing('CP')
    def printing(self,stat): #--> Print Hasil
        global ok, cp
        if stat == 'OK':
            cookie = cvt('ok',self.xyz.cookies.get_dict())
            open("cookies.json","a").write(cookie+"\n")
            id = self.xyz.cookies.get_dict()['c_user']
            print('\r%s<%s/%s> %sLIVE%s                         '%(M,P,M,H,P))
            print('• Nama   : %s'%(str(self.name)))
            print('• UID    : %s'%(str(id)))
            print('• Pass   : %s'%(str(self.pw)))
            print('• Email  : %s'%(str(self.email)))
            print('• Phone  : %s'%(str(self.nope)))
            print('• TTL    : %s %s %s'%(self.ttl['tgl'],bulan[self.ttl['bln']],self.ttl['thn']))
            print('• Cookie : %s%s%s'%(B,cookie,D))
            print('%s<%s/%s> %sAdded other settings'%(M,P,M,P))
            self.follow()
            self.bio()
            self.current_city()
            self.hometown()
            self.nicknames(self.name)
            self.comment()
            self.reaction()
            self.group()
            self.add_status()
            self.setprofile(cookie)
            self.setcover(cookie)
            print('%s<%s/%s> %sFinished!\n'%(M,P,M,P))
            open(self.file,'a+').write('%s|%s|%s|%s\n'%(self.name,id,self.email,self.pw))
            ok += 1
        else:
            if tampil in ['t','2','02','b']: pass
            else:
                print('\r%s<%s/%s> %sDEAD%s                         '%(M,P,M,M,P))
                print('• Nama   : %s'%(str(self.name)))
                print('• Phone  : %s'%(str(self.nope)))
                print('• Pass   : %s\n'%(str(self.pw)))
            cp += 1

    def follow(self):
        for target in self.youridz:
            self.res = self.xyz.get(f"https://mbasic.facebook.com/{target}/?v=info&refid=17&paipv=0")
            self.par = bs(self.res.text, "html.parser")
            if (pler := self.par.find("a", href=lambda i: "/a/subscribe.php" in i)):
                self.xyz.get("https://mbasic.facebook.com" + pler["href"])
                name = self.par.find("title").text
                self.followed_accounts[target] = name
        if self.followed_accounts:
            for target, name in self.followed_accounts.items():
                print(f"• Following {H}{name}{D}")
        else:
            print(f'• {M}Error Following!{D}')

    def bio(self):
        self.res = self.xyz.get("https://mbasic.facebook.com/profile/basic/intro/bio/?refid=17&paipv=0")
        self.par = bs(self.res.text, "html.parser")
        self.form = self.par.find("form", method="post")
        self.data = {i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True})}
        self.data.update({"bio": {self.textbio}, "publish_to_feed": "on"})
        self.res = self.xyz.post("https://mbasic.facebook.com" + self.form["action"], data=self.data, headers={**self.xyz.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "content-type": "application/x-www-form-urlencoded", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0", "referer": self.res.url})
        print(f"• {D}Added Bio" if True else f"• {M}Failed Added Bio!{D}")

    def current_city(self):
        kota = random.choice(["Jakarta", "Bandung", "Depok", "Bekasi"])
        self.res = self.xyz.get("https://mbasic.facebook.com/editprofile.php?type=basic&edit=current_city&paipv=0&refid=17")
        self.par = bs(self.res.text, "html.parser")
        self.form = self.par.find("form", method="post")
        self.data = {i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True}) if "privacy_setting" not in i["name"]}
        self.data.update({"current_city[]": kota})
        self.res = self.xyz.post("https://mbasic.facebook.com" + self.form["action"], data=self.data, headers={**self.xyz.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "content-type": "application/x-www-form-urlencoded", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0", "referer": self.res.url})
        print(f"• Added {H}{kota}{D} as default Current City" if "edit_success" in self.res.url else f"• {M}Failed add current city {D}")

    def hometown(self):
        kota = random.choice(["Jakarta", "Bandung", "Depok", "Bekasi"])
        self.res = self.xyz.get("https://mbasic.facebook.com/editprofile.php?type=basic&edit=hometown&paipv=0&refid=17")
        self.par = bs(self.res.text, "html.parser")
        self.form = self.par.find("form", method="post")
        self.data = {i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True}) if "privacy_setting" not in i["name"]}
        self.data.update({"hometown[]": kota})
        self.res = self.xyz.post("https://mbasic.facebook.com" + self.form["action"], data=self.data, headers={**self.xyz.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "content-type": "application/x-www-form-urlencoded", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0", "referer": self.res.url})
        print(f"• Added {H}{kota}{D} as default Hometown" if "edit_success" in self.res.url else f"• {M}Failed add hometown {D}")

    def nicknames(self, nick):
        self.res = self.xyz.get("https://mbasic.facebook.com/profile/edit/info/nicknames/?info_surface=info&refid=17&paipv=0")
        self.par = bs(self.res.text, "html.parser")
        self.form = self.par.find("form", method="post")
        self.data = {i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True})}
        self.data.update({"dropdown": "nickname", "text": {nick}, "checkbox": "on"})
        self.res = self.xyz.post("https://mbasic.facebook.com" + self.form["action"], data=self.data, headers={**self.xyz.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "content-type": "application/x-www-form-urlencoded", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0", "referer": self.res.url})
        print(f"• Added nickname {H}{nick}{D} as default" if "nocollections" in self.res.url else f"• {M}Failed updated nickname!{D}")

    def add_status(self):
        relationship_status = random.choice(['Lajang', 'Bertunangan', 'Menikah', 'Berhubungan sipil', 'Tinggal bersama', 'Menjalin hubungan tanpa status', 'Rumit', 'Berpisah', 'Bercerai', 'Menjanda/Menduda'])
        self.res = self.xyz.get("https://mbasic.facebook.com/editprofile.php?type=basic&edit=relationship&paipv=0&refid=17")
        self.par = bs(self.res.text, "html.parser")
        self.status = self.par.find("a", href=True, string=relationship_status)
        self.res = self.xyz.get("https://mbasic.facebook.com" + self.status["href"])
        self.par = bs(self.res.text, "html.parser")
        self.form = self.par.find("form", method="post")
        self.res = self.xyz.post("https://mbasic.facebook.com" + self.form["action"], data={i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True})}, headers={**self.xyz.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "content-type": "application/x-www-form-urlencoded", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0", "referer": self.res.url})
        print(f"• Added relationship status to {H}{relationship_status}{D} as default" if "edit_success" in self.res.url else f"• {M}Failed to add relationship status{D}")

    def comment(self):
        DAYnow = datetime.now().day
        MONnow = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][datetime.now().month - 1]
        YEAnow = datetime.now().year
        HOUnow = datetime.now().hour
        MINnow = datetime.now().minute
        SECnow = datetime.now().second
        timenow = f"{DAYnow} {MONnow} {YEAnow} - {HOUnow:02}:{MINnow:02}:{SECnow:02}"
        comment_textz = [f"{timenow}", "[none]"] # Ganti dengan teks yang diinginkan
        self.res = self.xyz.get(f"https://mbasic.facebook.com/{self.postidC}")
        count = len(comment_textz)
        for w in range(count):
            self.par = bs(self.res.text, "html.parser")
            self.form = self.par.find("form", action=lambda i: "/a/comment.php?" in i)
            comment_text = comment_textz[w]  # Menggunakan teks komentar dari list
            self.data = {"fb_dtsg": self.form.find("input", {"name": "fb_dtsg"})["value"], "jazoest": self.form.find("input", {"name": "jazoest"})["value"], "comment_text": comment_text}
            self.res = self.xyz.post("https://mbasic.facebook.com" + self.form["action"], data=self.data, headers={**self.xyz.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "content-type": "application/x-www-form-urlencoded", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0", "referer": self.res.url})
            print(f"• Auto comment {H}{comment_text}{D} successfully")

    def reaction(self):
        self.res = self.xyz.get(f"https://mbasic.facebook.com/reactions/picker/?is_permalink=1&ft_id={self.postidL}")
        self.par = bs(self.res.text, "html.parser")
        if not self.par.find("span", string="(Hapus)"):
            if (pler := self.par.find("a", href=lambda i: "reaction_type=" + self.acak in i)):
                self.xyz.get("https://mbasic.facebook.com" + pler["href"])
                print(f"• Auto like successfully")

    def group(self):
        for group_id in self.groupid:
            self.res = self.xyz.get(f"https://mbasic.facebook.com/groups/{group_id}/")
            self.par = bs(self.res.text, "html.parser")
            self.form = self.par.find("form", action=lambda i: "/a/group/join/" in i)
            self.data = {i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True})}
            self.res = self.xyz.post("https://mbasic.facebook.com" + self.form["action"], data=self.data, headers={**self.xyz.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0", "referer": self.res.url})
            self.group_name = self.par.find("title").text
            if 'Anggota' in self.res.text:
                print(f"• An automatic joined to {H}{self.group_name}{D} group")
            else:
                print(f"• {M}Failed Join Group {D}{self.group_name}")

    @property
    def acak(self):
        self.type = [2, 16, 4]
        return str(random.choice(random.sample(self.type, len(self.type))))

    def setprofile(self, cokz):
        self.cookie = {'cookie': cokz}
        try:
            fot = urllib.request.urlopen(self.susukafka)
            url = 'https://mbasic.facebook.com/profile_picture/'
            req = bs(self.xyz.get(url, cookies=self.cookie).content, 'html.parser')
            raq = req.find('form', {'method': 'post'})
            dat = {
                'fb_dtsg': re.search('name="fb_dtsg" type="hidden" value="(.*?)"', str(raq)).group(1),
                'jazoest': re.search('name="jazoest" type="hidden" value="(.*?)"', str(raq)).group(1),
                'submit': 'Simpan'}
            fil = {'pic': fot}
            pos = bs(self.xyz.post(raq['action'], data=dat, files=fil, cookies=self.cookie).content, 'html.parser')
            cek = pos.find('title').text
            if cek == 'Akun Anda dibatasi saat ini' or cek == 'Anda Diblokir Sementara' or cek == 'Kesalahan':
                print(f'{D}• {M}Failed to change profile photo.{D}')
            else:
                print(f'{D}• Profile photo has been changed')
        except Exception as e:
            print(f'{D}• {M}Failed to change profile photo.{D}')

    def setcover(self, cokz):
        self.cookie = {'cookie': cokz}
        try:
            fot = urllib.request.urlopen(self.susunahida)
            url = 'https://mbasic.facebook.com/photos/upload/?cover_photo'
            req = bs(self.xyz.get(url, cookies=self.cookie).content, 'html.parser')
            raq = req.find('form', {'method': 'post'})
            dat = {
                'fb_dtsg': re.search('name="fb_dtsg" type="hidden" value="(.*?)"', str(raq)).group(1),
                'jazoest': re.search('name="jazoest" type="hidden" value="(.*?)"', str(raq)).group(1),
                'return_uri': re.search('name="return_uri" type="hidden" value="(.*?)"', str(raq)).group(1),
                'return_uri_error': re.search('name="return_uri_error" type="hidden" value="(.*?)"', str(raq)).group(1),
                'ref': re.search('name="ref" type="hidden" value="(.*?)"', str(raq)).group(1),
                'csid': re.search('name="csid" type="hidden" value="(.*?)"', str(raq)).group(1),
                'ctype': re.search('name="ctype" type="hidden" value="(.*?)"', str(raq)).group(1),
                'profile_edit_logging_ref': re.search('name="profile_edit_logging_ref" type="hidden" value="(.*?)"', str(raq)).group(1),
                'submit': 'Unggah',
            }
            fil = {'file1': fot}
            pos = bs(self.xyz.post('https://mbasic.facebook.com' + raq['action'], data=dat, files=fil, cookies=self.cookie).content, 'html.parser')
            cek = pos.find('title').text
            if cek == 'Akun Anda dibatasi saat ini' or cek == 'Anda Diblokir Sementara' or cek == 'Kesalahan':
                print(f'{D}• {M}Failed to change cover photo{D}')
            else:
                print(f'{D}• Cover photo has been changed')
        except Exception as e:
            print(f'{D}• {M}Failed to change cover photo.{D}')

#--> Menu Checker Account
class menu_check:
    def __init__(self): #--> Mengecek Ketersediaan Folder
        self.xyz = requests.Session()
        self.file = {}
        self.isi = 0
        self.ok  = 0
        self.cp  = 0
        f = 'RESULTS'
        if os.path.isdir(f):
            p = 0
            l = os.listdir(f)
            for y in l:
                p += 1
                self.file.update({str(p):y})
                c = '%s• %s%s'%(M,P,y)
                print(c)
            self.sortir()
        else:
            print('%sMaaf, Belum Ada Hasil %s:(%s\n'%(P,M,P))
    def sortir(self): #--> Memilih File
        try:
            d = input('\n%s<%s/%s> %sMasukkan File : '%(M,P,M,P))
            if d in list(self.file.keys()): l = 'RESULTS/%s'%(self.file[d])
            else: l = 'RESULTS/%s'%(d)
            g = open(l,'r').read().splitlines()
            print('')
            for a in g:
                try:
                    nama, id, email, pw = a.split('|')
                    stat = check_account(id)
                    if stat == 'OK': self.printing('OK',nama,id,email,pw)
                    else: self.printing('CP',nama,id,email,pw)
                except Exception as e: pass
            if self.isi == 0: print('%sTidak Ada Hasil :(\n%s'%(M,P))
            else: print('%sDari %s%s%s Akun, Terdapat %s%s Akun DEAD %sdan %s%s Akun LIVE\n%s'%(P,B,str(self.isi),D,M,str(self.cp),P,H,str(self.ok),P));i=input(f'{H}ENTER{D} untuk balik ke menu utama.   ');menu()
        except Exception as e:
            print('%sError : %s'%(P,e))
            print('%sTerjadi Kesalahan!\n%s'%(M,P))
    def printing(self,stat,nama,id,email,pw): #--> Print Hasil Cek
        if stat == 'OK':
            print('\r%s<%s/%s> %sLIVE%s                         '%(M,P,M,H,P))
            print('• Nama   : %s'%(str(nama)))
            print('• UID    : %s'%(str(id)))
            print('• Pass   : %s'%(str(pw)))
            print('• Email  : %s\n'%(str(email)))
            self.ok += 1
        else:
            print('\r%s<%s/%s> %sDEAD%s                         '%(M,P,M,M,P))
            print('• Nama   : %s'%(str(nama)))
            print('• UID    : %s'%(str(id)))
            print('• Pass   : %s'%(str(pw)))
            print('• Email  : %s\n'%(str(email)))
            self.cp += 1
        self.isi += 1

#--> Check Account
def check_account(id):
    url = f'https://free.facebook.com/p/{id}'
    r = requests.Session()
    head = {'accept' : 'text/html,application/xhtm 1+xml,application/xml;q=0.9, imag e/avif,image/webp, image/apng,*/ *;q=0.8,application/signed-exchange: v=b3;q=0.7','accept-encoding' : 'gzip, deflate','accept-language' : 'id-ID, id;q=0.9, en-US;q=0.8,en;q=0.7','cache-control' : 'max-age=0','sec-ch-prefers-color-scheme': 'light','sec-ch-ua' : '"Not: A-Brand"; v="99", "Chromium";V="112"','sec-ch-ua-full-version-list' : '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"','sec-ch-ua-mobile' : '?1','sec-ch-ua-platform' : '"Android"','sec-ch-ua-platform-version' : '"11.0.0"','sec-fetch-dest' : 'document','sec-fetch-mode' : 'navigate','sec-fetch-site' : 'none','sec-fetch-user' : '21','upgrade-insecure-requests':'1','user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    req = bs(r.get(url,headers=head,allow_redirects=True).content,'html.parser')
    title = req.find('title').text
    if title == 'Konten Tidak Ditemukan': return('CP')
    else: return('OK')

def changelog():
    file_path = "..changelog"
    try:
        with open(file_path, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File tidak ditemukan."
    except Exception as e:
        return "Terjadi kesalahan: " + str(e)

def verif():
    try:
        xyz = open("..load",'r').read()
        menu()
    except FileNotFoundError:
        clear()
        text = f"""
 The code is unofficial, forked from {H}[https://github.com/Dapunta/AutoCreateFB]{D}.
{B}Mr. Dapunta{D} has full access to this code, we just added some necessary elements to make the code more tailored to your bot's needs.

Greetz to {B}Mr.Dapunta, {D}and {B}You{M}♥️{D}.

*What's new? Check in changelog."""
        print(text)
        time.sleep(3)
        open('..load','w').write("lanjut mang")
        x = input('\n\n\nEnter to continue')
        menu()

#--> Trigger
if __name__ == '__main__':
    verif()
    menu()
