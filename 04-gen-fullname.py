# -*- coding: UTF-8 -*-

# Filename : 04-gen-fullname.py
# author by : （学员ID)

# 目的:
# 掌握函数

import random

# 练习一
# 建立一个函数，可以随机产生一个中国人的姓
def pick_family_name():

    family_names = ( \
    "赵","钱","孙","李","周","吴","郑","王","冯","陈","褚","卫","蒋","沈","韩","杨","朱","秦","尤","许","何","吕","施","张", \
    "孔","曹","严","华","金","魏","陶","姜","戚","谢","邹","喻","柏","水","窦","章","云","苏","潘","葛","奚","范","彭","郎", \
    "鲁","韦","昌","马","苗","凤","花","方","俞","任","袁","柳","酆","鲍","史","唐","费","廉","岑","薛","雷","贺","倪","汤", \
    "滕","殷","罗","毕","郝","邬","安","常","乐","于","时","傅","皮","卞","齐","康","伍","余","元","卜","顾","孟","平","黄", \
    "和","穆","萧","尹","姚","邵","湛","汪","祁","毛","禹","狄","米","贝","明","臧","计","伏","成","戴","谈","宋","茅","庞", \
    "熊","纪","舒","屈","项","祝","董","梁","杜","阮","蓝","闵","席","季","麻","强","贾","路","娄","危","江","童","颜","郭", \
    "梅","盛","林","刁","钟","徐","邱","骆","高","夏","蔡","田","樊","胡","凌","霍","虞","万","支","柯","昝","管","卢","莫", \
    "经","房","裘","缪","干","解","应","宗","丁","宣","贲","邓","郁","单","杭","洪","包","诸","左","石","崔","吉","钮","龚", \
    "程","嵇","邢","滑","裴","陆","荣","翁","荀","羊","於","惠","甄","曲","家","封","芮","羿","储","靳","汲","邴","糜","松", \
    "井","段","富","巫","乌","焦","巴","弓","牧","隗","山","谷","车","侯","宓","蓬","全","郗","班","仰","秋","仲","伊","宫", \
    "宁","仇","栾","暴","甘","钭","厉","戎","祖","武","符","刘","景","詹","束","龙","叶","幸","司","韶","郜","黎","蓟","薄", \
    "印","宿","白","怀","蒲","邰","从","鄂","索","咸","籍","赖","卓","蔺","屠","蒙","池","乔","阴","鬱","胥","能","苍","双", \
    "闻","莘","党","翟","谭","贡","劳","逄","姬","申","扶","堵","冉","宰","郦","雍","卻","璩","桑","桂","濮","牛","寿","通", \
    "边","扈","燕","冀","郏","浦","尚","农","温","别","庄","晏","柴","瞿","阎","充","慕","连","茹","习","宦","艾","鱼","容", \
    "向","古","易","慎","戈","廖","庾","终","暨","居","衡","步","都","耿","满","弘","匡","国","文","寇","广","禄","阙","东", \
    "欧","殳","沃","利","蔚","越","夔","隆","师","巩","厍","聂","晁","勾","敖","融","冷","訾","辛","阚","那","简","饶","空", \
    "曾","毋","沙","乜","养","鞠","须","丰","巢","关","蒯","相","查","后","荆","红","游","竺","权","逯","盖","益","桓","公", \
    "万俟","司马","上官","欧阳","夏侯","诸葛","闻人","东方", \
    "赫连","皇甫","尉迟","公羊","澹台","公冶","宗政","濮阳", \
    "淳于","单于","太叔","申屠","公孙","仲孙","轩辕","令狐", \
    "钟离","宇文","长孙","慕容","鲜于","闾丘","司徒","司空", \
    "丌官","司寇","仉督","子车","颛孙","端木","巫马","公西", \
    "漆","雕","乐正","壤","驷","公良","拓跋","夹谷","宰父","谷梁", \
    "晋","楚","闫","法","汝","鄢","涂","钦","段干","百里","东郭","南门", \
    "呼延","归","海","羊舌","微","生","岳","帅","缑","亢","况","郈","有","琴", \
    "梁丘","左丘","东门","西门","商","牟","佘","佴","伯赏","南宫", \
    "墨","哈","谯","笪","年","爱","阳","佟","第五","言","福" \
    )

    one_name = random.choice(family_names)
    return one_name

# -------------  调用函数 ---------------------------
'''
for i in range(10):
    picked_name = pick_family_name()
    print("(%d)- %s" % (i, picked_name))
'''

# 练习二
# 建立一个函数，可以随机产生一个中国人的名称（ 1=男孩， 2=女孩）
def pick_given_name( is_boy ):
    # 男孩们的单字名
    boys_given_words1 = ( \
		'潮','彻','郴','琛','澈','臣','辰','晨','承','盛','程','池','炽','冲','重','崇','绸','畴','酬','筹', \
		'楚','处','棰','锤','淳','赐','聪','璁','丛','淙','琮','璀','村','达','大','代','岱','玳','单','郸', \
		'石','当','铛','党','祷','道','得','德','地','灯','登','迪','狄','笛','柢','递','谛','滇','巅','典', \
		'淀','雕','顶','鼎','东','栋','笃','度','端','缎','煅','锻','敦','铎','恩','发','法','凯','志','明', \
		'伟','嘉','建','文','子','云','杰','兴','友','才','振','航','鹏','宇','衡','佳','强','宁','丰','波', \
		'森','学','民','永','翔','鸿','海','军','贵','藏','操','焯','晁','朝','驰','川','义','生','凡','连', \
		'良','乐','勇','辉','龙','宏','安','岩','中','茂','进','林','有','诚','先','敬','震','正','涛','超', \
		'周','勋','元','哲','俊','博','彬','富','顺','信','昌','豪','邦','绍','浩','泽','涵','思','家','魄', \
		'檗','卜','步','埔','瓿','材','财','参','灿','策','曾','差','察','长','昶','畅','倡','绰','帆','藩', \
		'杠','巩','贡','钩','加','见','将','飞','斐','奋','风','枫','峰','烽','锋','逢','福','阜','复','奖', \
		'金','津','竟','靖','镜','镌','赋','盖','溉','概','甘','刚','岗','钢','罡','港','高','诰','革','葛', \
		'铬','根','庚','耿','功','宫','恭','构','故','顾','观','冠','莞','管','光','广','归','圭','桂','过', \
		'纪','技','系','季','际','继','绩','稷','谦','霆','玉','智','名','聚','兵','忠','廷','江','政','君', \
		'恒','礼','磊','阳','洋','迅','胜','传','创','存','锉','宕','导','岛','砥','斗','督','顿','瀚','瑞', \
		'朔','荣','为','斌','庆','成','可','健','英','锦','立','平','旭','同','全','源','向','雄','利','希', \
		'奇','易','来','启','坤','昊','朋','和','艺','昭','映','威','奎','帅','星','春','章','伦','城','钊', \
		'洲','晗','景','珂','皓','棠','越','语','钧','亿','基','理','纶','维','瑜','齐','毅','谊','贤','逸', \
		'卫','万','臻','儒','洁','霖','隆','远','耀','誉','岚','康','天','甲','价','驾','架','稼','尖','坚', \
		'间','俭','检','简','饯','剑','漳','谏','践','鉴','键','交','佼','皎','觉','教','阶','节','解','介', \
		'界','近','劲','晋','京','经','荆','径','竞','炯','赳','九','韭','居','驹','枸','举','巨','炬','隽', \
		'决','诀','均','郡','峻','浚','骏','竣','羽','韦'
    )
    # 男孩们的双字名
    boys_given_words2 = ( \
        '致浩','明云','浩烨','兆忠','予忻','顺雨','尚扬','俊祥','语禅','予浩','童兆','可然','业尚','抒霄','如海','聿彦','德容','政斌','羽凡','沛林', \
        '毅宾','晖予','运川','志双','程涵','英资','曦傲','誉冉','翊暄','兆博','梓楚','祖翰','轩睿','梓哲','偌宸','炜晁','宜书','以诺','睿思','开浩', \
        '峥延','灿烨','煜萧','亿鑫','家容','冬抒','谊言','凌宏','江哲','苛弈','名轩','涵蓄','卫洋','洪生','鸿森','霖祥','浩广','睿才','宇琪','华瑞', \
        '子櫲','羽希','梓灵','渤驰','圣彭','岩辉','寅升','思宇','艺喧','艳秋','汇然','楷荣','宁彦','韵沅','君戎','学竣','宇笑','俊曦','宸源','岳楠', \
        '予抒','尚寅','烨赫','宏旷','呈熙','祺然','俊麟','心逸','雨桐','晖尚','炳鑫','睿炯','智笙','毓珲','廷希','章宸','玉庭','震晗','梓瑾','文悦', \
        '士元','禹浩','凯文','兴睿','抒淯','煜烨','家燊','宏扬','笑书','烨毅','潇育','思博','德懿','慕鑫','意佳','子烨','奕洋','华铭','旭滕','昶旭', \
        '宇聪','鑫宇','桦烨','士忠','会钧','泓宁','名宁','子予','杰呈','懿敏','旭鸣','景森','钦瑞','萧宸','国欣','亭钧','恩曦','雄智','天叙','君昊', \
        '启纬','菁眙','龙辰','皓予','誉浛','华阳','成笑','鸣逸','阳越','疏鸣','巍续','瑞奇','羽翰','岳阳','秋智','永春','苛意','欣诺','铭亿','羽盈', \
        '有聪','珈毓','夙宸','致彬','佩誉','含烨','羽儒','志利','艺蕴','羽纤','世方','朗贤','睿芯','语阳','硕育','彦淳','美轩','峪含','浩玮','益含', \
        '泣涵','俊言','凇伯','梦熙','峻熙','胥宸','舞轩','书懿','智邦','源彬','炯抒','宇齐','睿珅','晨杰','高明','雨益','尚悦','晔尚','茗钦','雪山'  \
    )
    # 女孩们的单字名
    girls_given_words1 = ( \
        '叶','璐','娅','琦','晶','妍','瑶','毓','茜','秋','珊','莎','锦','黛','青','倩','婷','姣','婉','娴', \
        '颖','露','怡','婵','雁','蓓','纨','仪','荷','丹','蓉','眉','君','琴','蕊','薇','菁','岚','苑','婕', \
        '瑗','琰','韵','融','园','艺','咏','卿','聪','澜','纯','悦','昭','冰','爽','琬','茗','羽','希','宁', \
        '瑾','馨','欣','飘','育','滢','馥','筠','竹','霭','凝','晓','欢','霄','枫','芸','菲','寒','伊','亚', \
        '宜','可','柔','思','糖','雅','钰','嘉','芯','楚','沁','妃','岑','雯','允','萌','姿','予','卉','舒', \
        '诗','佳','姬','影','荔','枝','丽','秀','娟','英','华','慧','巧','美','娜','静','淑','惠','珠','翠', \
        '芝','玉','萍','红','娥','玲','芬','芳','燕','彩','春','菊','勤','珍','贞','莉','兰','凤','洁','梅', \
        '琳','素','云','莲','真','环','雪','荣','爱','妹','霞','香','月','莺','媛','艳','瑞','凡','琼','桂', \
        '娣','璧','梦'
    )
    # 女孩们的双名
    girls_given_words2 = ( \
        '倩雪','美琳','欢馨','优璇','雨嘉','娅楠','明美','诗涵','黛滢','嫦曦', \
        '静香','凌薇','雅静','雪丽','依娜','婉玗','书怡','诗茵','灵静','睿婕','婉婷'
    )

    # 随机生成名的字数 1-2
    given_name_num = random.randint(1, 2)

    # 第二种方法： 直接用 sample
    # 男孩的话选用 男字库
    if is_boy == 1:
        # 80% 选用单字双组合， 20% 选用双字
        if random.random() > 0.2:
            picked_word = random.sample(boys_given_words1, given_name_num)
        else:
            picked_word = random.sample(boys_given_words2, 1)
    else:
        # 90% 选用单字双组合， 10% 选用双字
        if random.random() > 0.1:
            picked_word = random.sample(girls_given_words1, given_name_num)
        else:
            picked_word = random.sample(girls_given_words2, 1)

    picked_name =""
    for word in picked_word:
        picked_name += word

    return picked_name

# -------------  调用函数 ---------------------------
"""
#定义选取次数
pick_times = 5
print("选取 (%d) 个男生的名，分别是：" %(pick_times), end="")
for i in range(pick_times):
    print("%s " % (pick_given_name(1)), end="")

print("\n")
print("选取 (%d) 个女生的名，分别是：" %(pick_times), end="")
for i in range(pick_times):
    print("%s " % (pick_given_name(2)), end="")
"""

# 练习三
# 函数说明： 自动生成一个中国人的全名
def get_full_name():

    # 随机挑选姓氏
    family_name = pick_family_name()

    # 随机产生性别
    sex = random.randint(1, 2)

    # 随机挑选名
    given_name = pick_given_name(sex)

    # 组成全名
    full_name = family_name + " " + given_name

    return full_name

# -------------  调用函数 ---------------------------
# 定义选取次数
pick_times = 10
# 定义人名列表
character_names = []
# 开始循环
for i in range(pick_times):

    # 组成全名
    full_name = get_full_name()

    # 输出全名及性别
    print("No.(%d) 个人,姓名是(%s)" % (i+1, full_name))
    character_names.append(full_name)

print("\n-------华丽分割线-----")
print ("所有人名一次性输出为：", character_names)
