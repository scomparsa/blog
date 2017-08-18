# -*- coding:utf8 -*-

import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

PROJECT_NAME = 'man-spa'
REQUEST_USER_AGENT = '%s(%s;%s;%s)' % (PROJECT_NAME, PROJECT_NAME, PROJECT_NAME, PROJECT_NAME)

BASE_PATH = os.path.dirname(__file__)                                       
TEMPLATE_PATH = os.path.join(BASE_PATH, '..', 'template')                   
STATIC_PATH = os.path.join(BASE_PATH, '..', 'static')                       

LOG_NAME = '%s.log' % PROJECT_NAME
LOG_FILE = os.path.join(BASE_PATH, '..', 'data/%s' % (LOG_NAME,))

OIL_LIST = [
	{
		'id': 9624935470,
		'cover': 'http://gi1.md.alicdn.com/bao/uploaded/i1/TB1JQcoGFXXXXceXVXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg',
		'title': u'古云草推拿精油 经络疏通精油 肩部颈椎背部腰腿全身按摩精油30ml',
		'desc': u'今日特惠：买2送1。通经活络，能祛除人体风、湿、寒、消除紧张，缓解疲劳。改善亚健康，有效解决颈椎腰椎及全身疼痛，让您经络疏通，一身轻松！美容院10年临床验证，服务超过1.5万人，好评率在98%以上，绿色植物萃取，安全有效，你值得拥有！',
		'link': 'http://redirect.simba.taobao.com/rd?w=unionnojs&f=http%3A%2F%2Fai.taobao.com%2Fauction%2Fedetail.htm%3Fe%3DQ2md8jP9XRQqro%252BR3tKKqNYMbnS7dnxKBRUm14q8OC%252FlL1tPWpvWRP7gvmtLyoa3Dlg3nJM8sR8r%252BELP0FUr3KaMK9XXhU5foYohPO0cOuEz6OTZelcGh23abJM7sDg2KMEPPzOo6XeTAu9Ox2ix7g%253D%253D%26ptype%3D100010%26from%3Dbasic&k=5ccfdb950740ca16&c=un&b=alimm_0&p=mm_107154138_8698851_29286766'
	},
	{
		'id': 13441701815,
		'cover': 'http://gi4.md.alicdn.com/bao/uploaded/i4/TB1gT2sGXXXXXakaXXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg',
		'title': u'古云草肾部保养精油 男士保健 缓解疲劳背部推拿按摩身体30ml',
		'desc': u'肾为“先天之本”、“生命之根”。因此，肾部保养尤为重要！美容院10年临床验证，服务超过2万人，好评率98%以上，绿色植物萃取，安全有效，你值得拥有！',
		'link': 'http://redirect.simba.taobao.com/rd?w=unionnojs&f=http%3A%2F%2Fai.taobao.com%2Fauction%2Fedetail.htm%3Fe%3Da64X%252BsJfHLDghojqVNxKsQsc6LC7BJQFog%252F3K1zSOxCLltG5xFicOdXrTUTgh9sMDPIwxrc30rgx5xFFx04TdaxkXmXxJb3tLWZWiRHBW08v2nsKhkx8L1Rmtaud%252B0v%252ByH5N0TnfPuu9BaVBuoXQGg%253D%253D%26ptype%3D100010%26from%3Dbasic&k=5ccfdb950740ca16&c=un&b=alimm_0&p=mm_107154138_8698851_29286766'
	},
	{
		'id': 9709008610,
		'cover': 'http://gi3.md.alicdn.com/bao/uploaded/i3/TB1tsNUFVXXXXXHXXXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg',
		'title': u'古云草生姜精油 身体按摩洗发护发足浴泡脚驱寒足疗正品单方10ml',
		'desc': u'热销5年，源自天然，健康美丽！',
		'link': 'http://redirect.simba.taobao.com/rd?w=unionnojs&f=http%3A%2F%2Fai.taobao.com%2Fauction%2Fedetail.htm%3Fe%3DftpnSl%252FkXb8qro%252BR3tKKqNquVM0f%252FdE0BRUm14q8OC%252FlL1tPWpvWRP7gvmtLyoa3Dlg3nJM8sR8r%252BELP0FUr3KaMK9XXhU5foYohPO0cOuEz6OTZelcGh23abJM7sDg29xT9nkqZH5KdDV%252FJ%252F%252Fm36w%253D%253D%26ptype%3D100010%26from%3Dbasic&k=5ccfdb950740ca16&c=un&b=alimm_0&p=mm_107154138_8698851_29286766'
	},
	{
		'id': 21357612145,
		'cover': 'http://gi3.md.alicdn.com/bao/uploaded/i3/T1m8IqFsdcXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg',
		'title': u'古云草 薄荷清脑精油 清凉提神净化空气按摩缓解头部不适疲劳10ml',
		'desc': u'感受极致清新、消除疲劳、清醒提神。',
		'link': 'http://redirect.simba.taobao.com/rd?w=unionnojs&f=http%3A%2F%2Fai.taobao.com%2Fauction%2Fedetail.htm%3Fe%3Da8DWDR7AVA3ebLdhAWchHE2OASiperV%252FAdcPAzm7QvSLltG5xFicOdXrTUTgh9sMDPIwxrc30rgx5xFFx04TdaxkXmXxJb3tLWZWiRHBW08v2nsKhkx8L1Rmtaud%252B0v%252BKN5XHsj6XwARpnmnu%252BSpaQ%253D%253D%26ptype%3D100010%26from%3Dbasic&k=5ccfdb950740ca16&c=un&b=alimm_0&p=mm_107154138_8698851_29286766'
	},
	{
		'id': 9626720150,
		'cover': 'http://gi4.md.alicdn.com/bao/uploaded/i4/TB1oLt_GXXXXXXdaXXXXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg',
		'title': u'古云草夫妻情趣精油按摩身体 增进情侣兴奋浪漫全身推油开背30ml',
		'desc': u'源自天然 健康自然 尽享浪漫芳香情趣生活',
		'link': 'http://redirect.simba.taobao.com/rd?w=unionnojs&f=http%3A%2F%2Fai.taobao.com%2Fauction%2Fedetail.htm%3Fe%3DhoPxDoH%252FyUwqro%252BR3tKKqC3RYFccaN6eBRUm14q8OC%252FlL1tPWpvWRP7gvmtLyoa3Dlg3nJM8sR8r%252BELP0FUr3KaMK9XXhU5foYohPO0cOuEz6OTZelcGh23abJM7sDg2k1xMKLSMnCHYOLBZ%252Bet7kQ%253D%253D%26ptype%3D100010%26from%3Dbasic&k=5ccfdb950740ca16&c=un&b=alimm_0&p=mm_107154138_8698851_29286766'
	},
	{
		'id': 40957036910,
		'cover': 'http://gd4.alicdn.com/imgextra/i4/652819646/TB2V8lfapXXXXbwXpXXXXXXXXXX_!!652819646.jpg_400x400.jpg_.webp',
		'title': u'西班牙葡萄籽油基础油护发刮痧按摩香薰精油抗皱保湿补水滋润甘油',
		'desc': u'正品西班牙葡萄籽100ml，搭配精油使用。深层淡化暗沉，全面提亮肌肤! 使用接近肌肤PH的植物性优质胺基酸，能改善肌肤暗沉现象、并温和促进角质代谢，加上Vitamin B3可恢复肌肤白皙，美肌从基础油开始。。更赠送护肤达人推荐10巧妙用法书噢！',
		'link': 'http://redirect.simba.taobao.com/rd?w=unionnojs&f=http%3A%2F%2Fai.taobao.com%2Fauction%2Fedetail.htm%3Fe%3DSkcM84GXCYW6k0Or%252B%252BH4tBgW%252F1tp2ANOtRYUMqm8%252FiGLltG5xFicOdXrTUTgh9sMDPIwxrc30rgx5xFFx04TdaxkXmXxJb3tLWZWiRHBW08v2nsKhkx8L1Rmtaud%252B0v%252BKN5XHsj6XwAJ4suqNWnmZw%253D%253D%26ptype%3D100010%26from%3Dbasic&k=5ccfdb950740ca16&c=un&b=alimm_0&p=mm_107154138_8698851_29286766'
	},
	{
		'id': 9996228366,
		'cover': 'http://gi1.md.alicdn.com/bao/uploaded/i1/T1K1InFvddXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg',
		'title': u'古云草小麦胚芽基础油基底油媒介油美白护肤按摩精油正品30ml',
		'desc': u'源自天然 健康美丽',
		'link': 'http://redirect.simba.taobao.com/rd?w=unionnojs&f=http%3A%2F%2Fai.taobao.com%2Fauction%2Fedetail.htm%3Fe%3Dux2y7pLpRpAqro%252BR3tKKqHR6zNprHH52ZULKeTEAxATlL1tPWpvWRP7gvmtLyoa3Dlg3nJM8sR8r%252BELP0FUr3KaMK9XXhU5foYohPO0cOuEz6OTZelcGh23abJM7sDg28HNdRP1IIHB6yx0izpffvA%253D%253D%26ptype%3D100010%26from%3Dbasic&k=5ccfdb950740ca16&c=un&b=alimm_0&p=mm_107154138_8698851_29286766'
	},
	{
		'id': 15519157612,
		'cover': 'http://gi3.md.alicdn.com/imgextra/i3/14016022278333141/T10_OXXs4iXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg',
		'title': u'香袭人荷荷巴油50ml基础油保湿亮肤抗衰老滋润护肤必按摩精油',
		'desc': u'脸部最佳基底油，富含维他命E，能抗菌，非常容易穿透皮肤，很像皮肤的皮脂腺，尤其是油性肌肤，因为可以溶解皮脂腺所分泌的脂肪，能一起排除阻塞毛孔的污物。也可用于全身，对头发及各种肌肤都适用，可保湿和柔软保护毛孔，是品质最好的油，为高渗性的天然保湿剂。',
		'link': 'http://redirect.simba.taobao.com/rd?w=unionnojs&f=http%3A%2F%2Fai.taobao.com%2Fauction%2Fedetail.htm%3Fe%3DfTLExyy%252F7z3ghojqVNxKsZX%252Fa0rdn9708HgNo8uZfyqLltG5xFicOdXrTUTgh9sMDPIwxrc30rgx5xFFx04TdaxkXmXxJb3tLWZWiRHBW08v2nsKhkx8L1Rmtaud%252B0v%252BKN5XHsj6XwCCQ9qEfvarKQ%253D%253D%26ptype%3D100010%26from%3Dbasic&k=5ccfdb950740ca16&c=un&b=alimm_0&p=mm_107154138_8698851_29286766'
	},
	{
		'id': 17029305750,
		'cover': 'http://gi1.md.alicdn.com/bao/uploaded/i1/T1BrAnFztdXXXXXXXX_!!0-item_pic.jpg_430x430q90.jpg',
		'title': u'古云草乳木果油精油身体按摩基础油基底精油保湿滋养肌肤30ml',
		'desc': u'由于气候及种植业方面的原因，乳木果树只能在热带地区存活。因此，乳木果油极其珍贵。',
		'link': 'http://redirect.simba.taobao.com/rd?w=unionnojs&f=http%3A%2F%2Fai.taobao.com%2Fauction%2Fedetail.htm%3Fe%3DaiDt5n3O43zghojqVNxKsQh2ZF0R%252Fii5HXoLCLLzzT6LltG5xFicOdXrTUTgh9sMDPIwxrc30rgx5xFFx04TdaxkXmXxJb3tLWZWiRHBW08v2nsKhkx8L1Rmtaud%252B0v%252BKN5XHsj6XwCflEMdmtRXtw%253D%253D%26ptype%3D100010%26from%3Dbasic&k=5ccfdb950740ca16&c=un&b=alimm_0&p=mm_107154138_8698851_29286766'
	},
	{
		'id': 36561643895,
		'cover': 'http://img04.taobaocdn.com/bao/uploaded/i4/TB1wqFEHXXXXXcyXXXXXXXXXXXX_!!0-item_pic.jpg_400x400.jpg',
		'title': u'法国进口生姜纯精油10ML 驱寒暖宫生发护发泡脚按摩疏通活络单方',
		'desc': u'对泡脚驱寒暖宫，生发发面效果特别好',
		'link': 'http://redirect.simba.taobao.com/rd?w=unionnojs&f=http%3A%2F%2Fai.taobao.com%2Fauction%2Fedetail.htm%3Fe%3D4cOWy1DBZi4jmraEDZVrLo5huINpz4u4sfSjPqrk7DyLltG5xFicOdXrTUTgh9sMDPIwxrc30rgx5xFFx04TdaxkXmXxJb3tLWZWiRHBW08v2nsKhkx8L1Rmtaud%252B0v%252BKN5XHsj6XwCfKzYQyexnPA%253D%253D%26ptype%3D100010%26from%3Dbasic&k=5ccfdb950740ca16&c=un&b=alimm_0&p=mm_107154138_8698851_29286766'
	},
]