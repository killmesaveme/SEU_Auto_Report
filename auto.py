import requests
import lxml
from lxml import etree
import time
import execjs
import json
import sys
from datetime import datetime
import getopt

def Autoreport(uname,pwd):
    webheader={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
    }

    with open('encrypt.js','r') as f:
        js=f.read()
    f.close()
    jsdocs=execjs.compile(js)
    form={'WID': '',
          'NEED_CHECKIN_DATE': '2021-08-11',
          'DEPT_CODE': '100488', 'CZR': '', 'CZZXM': '', 'CZRQ': '2021-08-11 00:03:02',
          'CLASS_CODE': '', 'CLASS': '', 'DZ_DQWZ_JD': '', 'DZ_DQWZ_WD': '', 'DZ_DQWZ_SF': '',
          'DZ_DQWZ_CS': '', 'DZ_DQWZ_QX': '', 'USER_NAME_EN': '', 'DZ_XYYYPJG_DISPLAY': '',
          'DZ_XYYYPJG': '2', 'USER_ID': '', 'USER_NAME': '',
          'DEPT_NAME': '', 'GENDER_CODE_DISPLAY': '男', 'GENDER_CODE': '1',
          'PHONE_NUMBER': '', 'IDCARD_NO': '', 'LOCATION_DETAIL': '', 'EMERGENCY_CONTACT_PERSON': '',
          'EMERGENCY_CONTACT_PHONE': '', 'EMERGENCY_CONTACT_NATIVE': '', 'EMERGENCY_CONTACT_HOME': '',
          'HEALTH_STATUS_CODE_DISPLAY': '正常', 'HEALTH_STATUS_CODE': '001', 'HEALTH_UNSUAL_CODE': '',
          'IS_SEE_DOCTOR_DISPLAY': '', 'IS_SEE_DOCTOR': '', 'SAW_DOCTOR_DESC': '',
          'MEMBER_HEALTH_STATUS_CODE_DISPLAY': '', 'MEMBER_HEALTH_STATUS_CODE': '', 'MEMBER_HEALTH_UNSUAL_CODE': '',
          'MENTAL_STATE': '', 'RYSFLB': 'YJS', 'DZ_JSDTCJTW': '36.5', 'DZ_DTWJTW': '', 'DZ_DTWSJCTW': '',
          'DZ_SZWZLX_DISPLAY': '在校内', 'DZ_SZWZLX': '002', 'DZ_SZWZ_GJ_DISPLAY': '', 'DZ_SZWZ_GJ': '', 'DZ_SZWZXX': '',
          'DZ_MQZNJWZ': '', 'DZ_SZXQ_DISPLAY': '九龙湖校区', 'DZ_SZXQ': '002', 'LOCATION_PROVINCE_CODE_DISPLAY': '',
          'LOCATION_PROVINCE_CODE': '', 'LOCATION_CITY_CODE_DISPLAY': '', 'LOCATION_CITY_CODE': '',
          'LOCATION_COUNTY_CODE_DISPLAY': '', 'LOCATION_COUNTY_CODE': '', 'DZ_SFGL_DISPLAY': '否', 'DZ_SFGL': '001',
          'DZ_WD': '', 'DZ_GLKSSJ': '', 'DZ_GLJSSJ': '', 'DZ_GLDQ_DISPLAY': '', 'DZ_GLDQ': '', 'DZ_GLDSF_DISPLAY': '',
          'DZ_GLDSF': '', 'DZ_GLDCS_DISPLAY': '', 'DZ_GLDCS': '', 'DZ_GLSZDQ': '', 'DZ_MQSFWYSBL_DISPLAY': '否',
          'DZ_MQSFWYSBL': '0', 'DZ_YSGLJZSJ': '', 'DZ_YS_GLJZDSF_DISPLAY': '', 'DZ_YS_GLJZDSF': '', 'DZ_YS_GLJZDCS_DISPLAY': '',
          'DZ_YS_GLJZDCS': '', 'DZ_MQSFWQRBL_DISPLAY': '否', 'DZ_MQSFWQRBL': '0', 'DZ_QZGLJZSJ': '', 'DZ_QZ_GLJZDSF_DISPLAY': '',
          'DZ_QZ_GLJZDSF': '', 'DZ_QZ_GLJZDCS_DISPLAY': '', 'DZ_QZ_GLJZDCS': '', 'DZ_SFYJCS1_DISPLAY': '无', 'DZ_SFYJCS1': '0',
          'DZ_ZHLKRQ': '', 'DZ_SFYJCS2_DISPLAY': '无', 'DZ_SFYJCS2': '0', 'DZ_GRYGLSJ1': '', 'DZ_ZHJCGRYSJ1': '',
          'DZ_SFYJCS3_DISPLAY': '无', 'DZ_SFYJCS3': '0', 'DZ_ZHJCGRYSJ2': '', 'DZ_SFYJCS4_DISPLAY': '无',
          'DZ_SFYJCS4': '0', 'DZ_JJXFBSJ': '', 'DZ_JJXFBD_SF_DISPLAY': '', 'DZ_JJXFBD_SF': '', 'DZ_JJXFBD_CS_DISPLAY': '',
          'DZ_JJXFBD_CS': '', 'DZ_BRYWYXFH_DISPLAY': '', 'DZ_BRYWYXFH': '', 'DZ_JCQKSM': '', 'DZ_JRSFFS_DISPLAY': '无',
          'DZ_JRSFFS': '0', 'DZ_TWDS': '', 'DZ_JRSTZK_DISPLAY': '无', 'DZ_JRSTZK': '001', 'DZ_SMJTQK': '',
          'DZ_SFYJCS5_DISPLAY': '无', 'DZ_SFYJCS5': '0', 'DZ_YJZCDDGNRQ': '', 'DZ_SFYJCS7_DISPLAY': '无',
          'DZ_SFYJCS7': '0', 'DZ_ZHJCGGRYSJ': '', 'DZ_SFYJCS8_DISPLAY': '无', 'DZ_SFYJCS8': '0', 'DZ_JTQY_DISPLAY': '',
          'DZ_JTQY': '', 'DZ_SFYJCS9_DISPLAY': '无', 'DZ_SFYJCS9': '0', 'DZ_SFYJCS10_DISPLAY': '无', 'DZ_SFYJCS10': '0',
          'DZ_YWQTXGQK_DISPLAY': '无', 'DZ_YWQTXGQK': '0', 'DZ_QKSM': '', 'DZ_JRSFYXC_DISPLAY': '无', 'DZ_JRSFYXC': '0',
          'DZ_MDDSZSF_DISPLAY': '', 'DZ_MDDSZSF': '', 'DZ_MDDSZCS_DISPLAY': '', 'DZ_MDDSZCS': '', 'DZ_JTFS_DISPLAY': '',
          'DZ_JTFS': '', 'DZ_CCBC': '', 'DZ_SFDXBG_DISPLAY': '', 'DZ_SFDXBG': '', 'DZ_SYJTGJ': '', 'DZ_SDXQ': '',
          'DZ_YMJZRQ1': '2021-04-12', 'DZ_YMJZD1': '', 'DZ_YMJZRQ2': '', 'DZ_YMJZD2': '',
          'DZ_WJZYMYY_DISPLAY': '', 'DZ_WJZYMYY': '', 'DZ_WJZYMQTYY': '', 'REMARK': '',
          'CREATED_AT': '', 'DZ_DBRQ': '', 'DZ_SFYBH': '0', 'DZ_SFLXBXS': '', 'DZ_ZDYPJG': ''}
    url="https://newids.seu.edu.cn/authserver/login?service=https://newids.seu.edu.cn/authserver/login2.jsp"
    widurl="http://ehall.seu.edu.cn/qljfwapp2/sys/lwReportEpidemicSeu/modules/dailyReport/getMyTodayReportWid.do"
    saveurl="http://ehall.seu.edu.cn/qljfwapp2/sys/lwReportEpidemicSeu/modules/dailyReport/T_REPORT_EPIDEMIC_CHECKIN_SAVE.do"
    #url="https://newids.seu.edu.cn/authserver/login?goto=http://my.seu.edu.cn/index.portal"
    sign1="http://ehall.seu.edu.cn/appShow?appId=5821102911870447"
    username=uname#这里输入用户名
    password=pwd#这里输入密码
    req=requests.session()
    response=req.get(url)
    html=etree.HTML(response.text)
    lt=html.xpath('//*[@id="casLoginForm"]/input[1]/@value')
    dllt=html.xpath('//*[@id="casLoginForm"]/input[2]/@value')
    execute=html.xpath('//*[@id="casLoginForm"]/input[3]/@value')
    _eventId=html.xpath('//*[@id="casLoginForm"]/input[4]/@value')
    rmShown=html.xpath('//*[@id="casLoginForm"]/input[5]/@value')
    pwdsalt=html.xpath('//*[@id="casLoginForm"]/input[6]/@value')
    pwdencrypt=jsdocs.call('encryptAES',password,pwdsalt[0])
    data={
        "username":username,
          "rmShown":rmShown,
          "password":pwdencrypt,
          "lt":lt,"execution":execute,
          "dllt":dllt,
          "_eventId":_eventId
          }
    r=req.post(url,headers=webheader,data=data)
    #e=req.post(sign,headers=webheader)
    r2=req.get(sign1,headers=webheader)
    forminfo=etree.HTML(r2.text)
    getwid=req.post(widurl,headers=webheader)
    info=forminfo.xpath('/html/head/script[1]/text()')
    widform=getwid.text
    widform=json.loads(widform)["datas"]["getMyTodayReportWid"]["rows"][0]
    for key,value in widform.items():
        if key in form.keys():
            if value!=None:
                form[key]=value
    form["DZ_JSDTCJTW"]='36.5'
    result=req.post(saveurl,headers=webheader,data=form)
    print(result.text)

    
if __name__=="__main__":
    username="220205149"
    password="Zt152816"
    parameter=sys.argv[1:]
    try:
        opts, args = getopt.getopt(parameter,"hu:p:",["username=","password="])
    except getopt.GetoptError:
        print('AutoReport.py -u <username> -p <password>(or AutoReport.py --username=<username> --password=<password>)')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('AutoReport.py -u <username> -p <password>(or AutoReport.py --username=<username> --password=<password>)')
            sys.exit()
        elif opt in ("-u", "--username"):
            username = arg
        elif opt in ("-p", "--password"):
            password = arg
    date=datetime.today().date()
    is_reported=False

    while True:
        today=datetime.today().date()
        if(today!=date):
            is_reported=False
        now=datetime.now()
        last=datetime.strptime(str(today)+" 23:59:59","%Y-%m-%d %H:%M:%S")
        sleeptime=(last-now).seconds
        if is_reported == False:
            Autoreport(username,password)
            today=datetime.today().date()
            is_reported=True
            date=today
            print(str(today)+"已成功打卡\n")
            time.sleep(sleeptime+60)

        
        
