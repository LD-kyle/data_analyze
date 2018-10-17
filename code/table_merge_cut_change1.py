import pandas as pd
import re

def get_supplier_name_unify(string):
    list=['合普动力','NISSAN','中海龙能源科技','Continental Automotive (Germany)','御捷车业','电驱动','德洋电子科技',
          '尤奈特电机','比亚迪','大地和','新大洋机电','东风','江铃集团新能源汽车','众泰汽车','瑞驰汽车','德沃仕',
          '银隆电器','巨一','斯科若','博格华纳','华域汽车电动系统','道一动力','大陆汽车系统','裕成雅科电机',
          '方正电机','富奥汽车','兰德新能源汽车','和鑫','金坛绿能','乐金汽车','长安','杰能动力','东风汽车','伯坦动力','创驱',
          '精进','英搏尔','奇瑞','福田','绿控传动','北京新能源汽车','微特利','蔚然','阳光电动力','意谱电动','联合汽车电子',
          '大郡动力','卧龙','莱姆斯特','HYUNDAI MOBIS','捷欧大地和','蓝博威','蓝狐','中科深江','湘电莱特','北京汽车新能源汽车',
          '百转','中华汽车','金龙客车','乐创世纪','伯坦科技工程','索尔达动力','海博瑞德','永力新能源动力','杰诺瑞','都凌','富临精工',
          '汇川技术','新动力电机','德沃士','万向','百隆','江南汽车制造','中慈','勋迪','海马','锐伊恩','市普世','东道新能源科技',
          '泰锋','大郡晟誉','格至控智能','湖北天运','富特','云迪','福瑞德','北方凯达','UQM技术','General Motor','AC Propulsion Inc.',
          'BMW AG','Magna E-Car System','九龙','三峻','巴斯巴','休普','绿巨能','Remy International Inc','金华青年',
          '众达','依思普林','圣代电机','中智远','亿马先锋','现代MOBIS','清源','台达电子工业','英威腾','茂宏电机','中车时代','汉腾',
          '鸿创','精骏','南车时代','南车','宇通','潍柴','通宇','合康','大连电机','POSCO TMC Co.LTD',
          '松正','海格','越博','蓝海华腾','金龙联合','威康','安凯','中车','创为','博能上饶','万润','英康汇通','特百佳','联腾',
          '东湖科技','亚南','力信','申龙','五洲龙','佩特来','民富沃能','中通','冠龙','金龙','江西特种电机','泰丰','鑫国','梅花',
          '众联能创','江铃集团晶马','联孚','福工','中德世纪','南洋','野马','奕控','成都客车','阳光电源','宇清','极能','西门子',
          '逸卡','三新','航天万源','天厦精控','四川新纪元','大郡','中瑞蓝科','德威利','普林亿威','吉利','玉柴机器','熙斯特',
          '泓凯','重汽集团济南豪沃客车','万象','华夏','瑞华','旭利','南车电车','采埃孚','中力汇通','泓凯','融浦益达','创源天地',
          '凯博易控','凯马百路佳','中材高新','西虎','五菱','正华','北京机械设备研究所','佳木斯','三立','铭马','襄樊特种电机',
          '华创','科斯特','恒通','银通','申沃','大洋','卡威','力久','易动','维特利','阳光','融智天骏','铭马','捷创','神马',
          '捷远','天元','牡丹','北京汽车','华盛源通','航天新长征','博尊','聚能','鸿源','常隆','汇元','永济新时速','钱潮轴承',
          '栋霖','亿纬赛恩斯','华宸','东莞电机','佩特莱','纽贝耳','华盛源通','奥地特','智能控制','中铜','新福达','蓝海节能',
          '航天新长征','雅骏','索尔','宏达允捷','少林客','九州车业','闽东','启特','澳特卡','华英','东方电气','科远','丰电安弗森',
          '奥思源','哈尔滨电机厂','星美','普拉格','耐力','一汽','壹品电子','挚云电气','金泰德胜电机','速达交通',
          '恒润','中九','众泰','领途','东元','优力仕']
    supplier_name_unify = ''
    for x in list:
        if x in string:
            supplier_name_unify=x
            break
    return supplier_name_unify

def get_unify(name,list):
    if name in list:
        name= list[0]
    return name

def get_company_name_unify(string):
    list=['江铃','东风','华晨鑫源','东风雷诺','长江乘用车','御捷车业','云度新能源','豪情汽车','一汽海马','通家汽车',
          '江南汽车','长安','江淮','力帆','比亚迪','知豆','广州汽车','金龙客车','奇瑞','北汽福田',
          '北京汽车','北京新能源','上汽大通','上汽通用五菱','东南','日产','长城','上海汽车','一汽夏利','广汽丰田',
          '海马','金华青年','北京现代','野马汽车','一汽吉林','九龙','吉利','潍柴','猎豹','华晨','宝沃','成功',
          '北汽新能源','黄海','昌河','北汽银翔','荣成华泰','北汽','卡威','昌河铃木','中国第一汽车','汉腾','中兴',
          '凯翼','上汽大众','广汽本田','红星','飞碟','上汽通用','广汽吉奥','新龙马','广汽吉奥','一汽丰田','一汽-大众',
          '上海大众','哈飞','华普','上海通用','前途','广汽三菱','威马','合众','安达尔','一汽客车','广通','宇通','中博',
          '亚星','华奥','中车时代','沂星','中汽宏远','源正','陆地方舟','金龙联合','申龙客车','五洲龙','南京汽车','安凯',
          '博能上饶客车','万象','金龙旅行车','国宏','山西新能源','广通','北方华德尼奥普兰客车','亚星','扬子江汽车','大运',
          '四川省客车','北奔重型','舒驰','中通','五龙','中植一客','华策','长江','万向','大汉','南京市公共交通车辆厂','天洋',
          '镇江汽车','豪沃','重汽','武汉客车','新福达','宜春','中航爱维客','成都客车','梅花','新筑通工','通联','中车电车',
          '少林','皇城相府宇航','常隆','飞驰','贵航云马','航天神州','恒通','星凯龙','乾丰','华龙','牡丹','西虎','申沃',
          '恩驰','跃迪','新楚风','陕西汽车','九州','之信','上汽唐山客车','登达','南车电车','友谊','安源','龙华','秦星',
          '北车','凯马百路佳','穗通','桂林客车','吉姆西','原野','冀东华夏','京华','越西','云山','中威','现代','四川汽车',
          '南车时代','中骐','齐鲁','益茂','顺达','紫金江发','神马','宝龙集团湛江万里','中植','昆明客车','陕西汉中','中车',
          '中集凌宇','中上','森源艾思特福','衡山','龙江','沃尔沃','克莱斯勒','恒润','领途']
    company_name_unify=''
    for x in list:
        if x in string:
            company_name_unify=x
            break
    company_name_unify=get_unify(company_name_unify,['上汽大众','上海大众'])
    company_name_unify = get_unify(company_name_unify, ['上汽通用', '上海通用'])
    company_name_unify = get_unify(company_name_unify, ['北京汽车', '北汽','北京新能源','北汽新能源','北汽银翔'])
    company_name_unify = get_unify(company_name_unify, ['吉利', '豪情汽车'])
    company_name_unify = get_unify(company_name_unify, ['一汽', '中国第一汽车','一汽吉林'])
    company_name_unify = get_unify(company_name_unify, ['海马', '一汽海马'])
    return company_name_unify

def write_fail(data,filename):
    d = {'企业名': data}
    df = pd.DataFrame(data=d)
    df.to_csv(filename, encoding='gbk')


def write_name(data,filename):
    supplier_name, index_motor, company_name, index_company = [[], [], [], [], []], [], [], []
    for z in range(1, 6):
        for x in range(0, len(data['电机供应商' + str(z) + '_G'])):
            supplier_name[z - 1].append(get_supplier_name_unify(data['电机供应商' + str(z) + '_G'][x]))
            if get_supplier_name_unify(data['电机供应商' + str(z) + '_G'][x]) == '' and data['电机供应商' + str(z) + '_G'][x] != '':
                index_motor.append(data['电机供应商' + str(z) + '_G'][x])
    for x in range(0, len(data['企业名称_G'])):
        company_name.append(get_company_name_unify(data['企业名称_G'][x]))
        if get_company_name_unify(data['企业名称_G'][x]) == '':
            index_company.append(data['企业名称_G'][x])
    for i in range(1, 6):
        data['电机供应商{}企业简称_G'.format(i)] = supplier_name[i - 1]
    data['整车厂企业简称_G'] = company_name
    data = data.set_index('企业名称_G')
    data.to_csv(filename[:-4]+'_change.csv')
    data.to_excel(filename[:-4]+'_change.xlsx')#output excel
    write_fail(index_motor, filename[:-4]+'supplier_name_unify_fail.csv')
    write_fail(index_company, filename[:-4]+'company_name_unify_fail.csv')

def get_front_place(detail,a,x):
    list1=[]
    if x==0:
        content=['/', '：', ':', ',', '，', '；', ';', '.', '。','为','、',')','）','用']
    else:
        content=['/', '：', ':', ',', '，', '；', ';', '.', '。','为','、']
    for i in range(1, len(detail[:a])):
        if detail[a - i] in content:
            list1.append(a - i)
        elif i==len(detail[:a])-1:
            list1.append(0)
    b=max(list1)
    return b

def get_behind_place(detail,a):
    list1=[]
    for i in range(a, len(detail)):
        if detail[i] in ['/', '：', ':', ',', '，', '；', ';', '.', '。','、']:
            list1.append(i)

        elif i==len(detail)-1:
            list1.append(len(detail)-1)
    c=min(list1)
    return c

def get_d(detail):
    list0,list1=[],['ABS','电机','ESC','选']
    for x in list1:
       if  x in detail:
           list0.append(detail.index(x))
       else:
           list0.append(len(detail))
    d=min(list0)
    return d

def get_cut(string):
    list1=['/', '：', ':', ',', '，', '；', ';', '.', '。']
    for x in list1:
       if x in string:
           index1=get_behind_place(string,0)
           index2=get_front_place(string,len(string)-1,1)
           string=string[0:index1+1]+string[index2+1:]

    return string

def get_sign(detail):
    list1 = ['动力蓄电池主电源种类/型号/生产企业','电池种类/型号/生产企业','电池类型及厂家','电池生产企业','本车的动力装置配置','蓄电池生产厂家','储能装置','电池种类/生产企业',
             '电池采用','电池种类/型号','该车采用','电池为','装配','配装','采用','动力电池', '动力蓄电池','蓄电池', '单体型号', '电池']
    index = 'nothing'
    for x in list1:
        if x in detail:
            index = x
            break
    return index

def get_battary(string):
    index = 'nothing'
    list1=['金属氢化物镍','锂离子', '磷酸铁', '镍钴锰酸', '三元锂', '复合锂','钛酸锂','磷酸锂','锂离力', '锰酸', '镍钴锰',
           '三元动力电池','LT-IFP-60AH','LF105','超级电容器','101-0020-02','IFP20100140A','超级电容','磷铁锂','HGL-1','三元材料',
          '三元聚合物', '三元能量型','铅酸','锰钴镍酸','镍锰','镍氢','磷酸亚铁','NMC锂三元系二次','三元电池','三元蓄电池',
           'AGM蓄电池','功率型','D34/78','锂电池','KMBNF82100202R','SPIM11245190',
           'BCAP3000 K2系列/BMOD0165','MV07203127MPP','CEVYNB1']
    for i in list1:
        if i in string:
            index = i
            break
    if index =='nothing':
        battary=''
    else:
       a = string.index(index)
       b = get_front_place(string, a,0)
       c = get_behind_place(string, a)
       battary = string[b + 1:c]
    return battary

def get_motor(data):
    content = []
    list1 = data.replace('/', '').split('公司')
    if len(list1) > 1 and len(list1) < 6:
        for i in range(0, len(list1) - 1):
            content.append(list1[i] + '公司')
        for i in range(len(list1) - 1, 5):
            content.append('')
    else:
        content.append(list1[0])
        for i in range(1, 5):
            content.append('')
    return content

def get_company(data):
  item,item1,item2,motor=[[],[]],[],[],[[], [], [], [], []]
  for x in range(0,len(data)):
        detail = data['其它_G'][x]
        try:
            battary=get_battary(detail)
            if battary=='':
                item2.append(x)
            index=get_sign(detail)
            a=detail.index(index)
            detail=detail[a:]
            index='nothing'
            list1=['LEJ,储能装置总成生产企业Samsung','LG Chem,Ltd','Johnson Matthey Battery Systems',
                   'SAMSUNG SDI ENERGY MALAYSIA SDN. BHD.','Hitachi Automotive Systems,Ltd.',
                   '美国活塞汽车','Automotive Energy Supply','Hitachi Automotive Systems Americas.',
                   'Blue Energy Co., Ltd.','GM Subsystems Manufacturing, LLC','PRIMEARTH EV','GM','Ford Motor',
                   'Deutsche ACCUmotive','PRIMEARTHEVENERGYCO.,LTD.','HITACHI','LG Chem, Ltd',
                   'XALT','MaxwellTechnologies ,Inc','MaxwellTechnologiesInc','Maxwell Technologies ,Inc',
                   'Maxwell techonolgies.Inc','Maxwell Technologies Inc','麦克斯威科技公司','LS Mtron Ltd','院','会社','股份','公司']
            for i in list1:
                if i in detail:
                    index=i
                    break
            a=detail.index(index)
            b=get_front_place(detail,a,1)
            d=get_d(detail)
            content=detail[a+2:d]
            if '公司'in content:
                    f = content.index('公司')+2+a
            else:
                    f = a
            c=get_behind_place(detail,f)
            detail=get_cut(detail[b+1:c])
            content=get_motor(data['发动机企业_G'][x])
            for i in range(0,len(content)):
                motor[i].append(content[i])
            item[0].append(detail)
            item[1].append(battary)
        except Exception as e:
            item[0].append('')
            item[1].append('')
            for i in range(0,5):
                motor[i].append('')
            item1.append(x)
  return  item,item1,item2,motor

def get_other(list1,data,filename):
    df = data.iloc[list1]
    df = df.set_index('企业名称_G')
    df.to_csv(filename, encoding='utf8')
    if len(list1) ==0:
        print('finish')

def get_data_max(data,column):
  for x in column:
     content = []
     for i in range(0, len(data)):
        if data.loc[i,x] == '' :
            content.append('')
        else:
             value=re.findall(r'\d+\.?\d*',data.loc[i,x])
             if len(value)==0:
                 content.append('')
             else:
                content.append(max([float(y) for y in value]))
     data[x+'_Max']=content
  return data


def get_data_min(data,column):
  for x in column:
     content = []
     for i in range(0, len(data)):
        if data[x][i] == '':
            content.append('')
        else: 
            value=re.findall(r'\d+\.?\d*',data.loc[i,x])
            content.append(min([float(y) for y in value]))
     data[x+'_Min']=content
  return data


def get_data_power(df):
    p_max, content0, n_max,t_max = [], [], [],[]
    for j in range(0, len(df)):
        detail = df.loc[j,'驱动电机峰值功率/转速/转矩(kW /r/min/N.m)_X']
        number=len(df.loc[j,'车辆基本信_X'].split(','))
        if detail=='':
            p_max.append('')
            content0.append('')
            n_max.append('')
            t_max.append('')
        else:
            if (':'  in detail)|('：' in detail):
                if '/' in detail:
                    s=re.findall(r'(\d+\.?\d+/+\d+\.?\d+/+\d+\.?\d*)', detail)
                elif '、' in detail:
                    s=re.findall(r'(\d+\.?\d+、+\d+\.?\d+、+\d+\.?\d*)', detail)
                s=','.join(s)
                s=re.findall(r'(\d+\.?\d*)', s)
            else:
                s=re.findall(r'(\d+\.?\d*)', detail)
            if len(s)%number==0:
                if len(s)/number==3:
                    p_max.append(max([float(s[x]) for x in range(0,len(s),3)]))
                    n_max.append(max([float(s[x]) for x in range(1,len(s),3)]))
                    t_max.append(max([float(s[x]) for x in range(2,len(s),3)]))
                    content0.append('单')
                elif  len(s)/number>3:
                    long=len(s)//number
                    p_max.append(max([sum([float(s[x]) for x in range(y*long,long+y*long,3)])  for y in range(0,number)]))
                    n_max.append(max([float(s[x]) for x in range(1,len(s),3)]))
                    t_max.append(max([sum([float(s[x]) for x in range(y*long+2,long+y*long,3)])  for y in range(0,number)]))
                    content0.append('多')
                else:
                     p_max.append('')
                     content0.append('')
                     n_max.append('')
                     t_max.append('')
                     print(j,detail)
    df['最大电机总功率_X']=p_max
    df['电机单_多_X']=content0
    df['电机最大转速_X'] = n_max
    df['电机最大转矩_X'] =t_max 
    return df

def get_phev_cut_change(filename_read,column_max,column_min):
    data = pd.read_csv(filename_read, encoding='utf8').astype(str)
    data = data.replace(to_replace=re.compile(r'.*nan.*'), value='')
    data = get_data_max(data, column_max)
    data = get_data_min(data, column_min)
    #data = get_data_power(data)

    item, item1, item2, motor = get_company(data)
    get_other(item1, data, filename_read[:-4]+'battary_supplier_fail_get.csv')
    get_other(item2, data, filename_read[:-4]+'battary_type_fail_get.csv')
    data['电池供应商_G'], data['电池种类_G'] = item[0], item[1]
    data = data.set_index('企业名称_G')
    data.to_csv(filename_read[:-4] +'_change.csv')
    data.to_excel(filename_read[:-4] +'_change.xlsx')#output excel
    

def get_ev_cut_change(filename_read,column_max,column_min):
    data = pd.read_csv(filename_read, encoding='utf8').astype(str)
    data = data.replace(to_replace=re.compile(r'.*nan.*'), value='')
    data = get_data_max(data, column_max)
    data = get_data_min(data, column_min)
    #data = get_data_power(data)

    item, item1, item2, motor = get_company(data)
    get_other(item1, data, filename_read[:-4]+'battary_supplier_fail_get.csv')
    get_other(item2, data, filename_read[:-4]+'battary_type_fail_get.csv')
    data['电池供应商_G'], data['电池种类_G'] = item[0], item[1]
    data['电机供应商1_G'],data['电机供应商2_G'],data['电机供应商3_G'],data['电机供应商4_G'],data['电机供应商5_G']=motor[0],motor[1],motor[2],motor[3],motor[4]
    write_name(data,filename_read)


def main():
   filename_phevs=[]
   filename_evs=['table_announce_ev.csv']
   column_max=['总质量(kg)_G','整备质量(kg)_G','额定载客(含驾驶员)(座位数)_G','整车长_G','轴距(mm)_G',
        '整车宽_G','整车高_G','货厢长_G','货厢宽_G','货厢高_G','前轮距_G','后轮距_G']
   column_min=[]
   for filename_ev in filename_evs:
       get_ev_cut_change('data/'+filename_ev, column_max, column_min)
   for filename_phev in filename_phevs:
       get_phev_cut_change('data/'+filename_phev, column_max, column_min)
   
if __name__ == '__main__':
    main()