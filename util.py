from config import *

# For crawl courses:

TIMEOUT_STR = '用户登陆超时或访问内容不存在。请重试，如访问仍然失败，请与系统管理员联系。'
FREQ_STR = '操作过于频繁，请重新登录。'

if TRY_LOGIN:
	COOKIES = {}
else:
	COOKIES = {
		'serverid': SERVERID,
		'JSESSIONID': JSESSIONID,
	}

COOKIES_FILE = 'cookies.pkl'

URL = 'http://zhjwxk.cic.tsinghua.edu.cn/xkYjs.vxkYjsXkbBs.do'

GET_URL = 'http://zhjwxk.cic.tsinghua.edu.cn/xkYjs.vxkYjsXkbBs.do'

GET_HEADERS = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cache-Control': 'no-cache',
	'Connection': 'keep-alive',
	'Pragma': 'no-cache',
	'Referer': 'http://zhjwxk.cic.tsinghua.edu.cn/xkYjs.vxkYjsXkbBs.do',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}

HEADERS = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cache-Control': 'no-cache',
	'Connection': 'keep-alive',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Origin': 'http://zhjwxk.cic.tsinghua.edu.cn',
	'Pragma': 'no-cache',
	'Referer': 'http://zhjwxk.cic.tsinghua.edu.cn/xkYjs.vxkYjsXkbBs.do',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}

ALL_PAYLOAD = {
	#'token': '',
	'p_xnxq': XNXQ,
	'tabType': '',
	'page': '',
	'p_kch': '',
	'p_kcm': '',
	#'p_xwk_id': '2022-2023-1;60230014;202;',
}

CID_STR = [None] * CNUM

CID_STR[XWK]  = 'p_xwk_id'
CID_STR[FXWK] = 'p_fxwk_id'
CID_STR[TYK]  = 'p_tyk_id'

PAYLOAD = [None] * CNUM

PAYLOAD[XWK] = {
	'm': 'saveXwKc',
	'p_xnxq': XNXQ,
	'tokenPriFlag': 'xwk',
}
PAYLOAD[FXWK] = {
	'm': 'saveFxwKc',
	'p_xnxq': XNXQ,
	'tokenPriFlag': 'fxwk',
}
PAYLOAD[TYK] = {
	'm': 'saveTykKc',
	'p_xnxq': XNXQ,
	'tokenPriFlag': 'tyk',
}

PARAMS = [None] * CNUM

PARAMS[XWK] = {
	'm': 'xwkSearch',
	'p_xnxq': XNXQ,
	'tokenPriFlag': 'xwk',
}

PARAMS[FXWK] = {
	'm': 'fxwkSearch',
	'p_xnxq': XNXQ,
	'tokenPriFlag': 'fxwk',
}

PARAMS[TYK] = {
	'm': 'tykSearch',
	'p_xnxq': XNXQ,
	'tokenPriFlag': 'tyk',
}

# For login:

LOGIN_URL = 'http://zhjwxk.cic.tsinghua.edu.cn/xklogin.do'

LOGIN_HEADERS = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Connection': 'keep-alive',
	'Host': 'zhjwxk.cic.tsinghua.edu.cn',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

LOGIN2_URL = 'https://zhjwxk.cic.tsinghua.edu.cn/xklogin.do'

LOGIN2_HEADERS = {
	'authority': 'zhjwxk.cic.tsinghua.edu.cn',
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'accept-language': 'zh-CN,zh;q=0.9',
	'referer': 'http://zhjwxk.cic.tsinghua.edu.cn/',
	'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': '"Windows"',
	'sec-fetch-dest': 'document',
	'sec-fetch-mode': 'navigate',
	'sec-fetch-site': 'cross-site',
	'upgrade-insecure-requests': '1',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

CAPTCAH_PREF = 'https://zhjwxk.cic.tsinghua.edu.cn'

CAPTCHA_HEADERS = {
	'authority': 'zhjwxk.cic.tsinghua.edu.cn',
	'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
	'accept-language': 'zh-CN,zh;q=0.9',
	'referer': 'https://zhjwxk.cic.tsinghua.edu.cn/xklogin.do',
	'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': '"Windows"',
	'sec-fetch-dest': 'image',
	'sec-fetch-mode': 'no-cors',
	'sec-fetch-site': 'same-origin',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

LOGINC_URL = 'https://zhjwxk.cic.tsinghua.edu.cn/j_acegi_formlogin_xsxk.do'

LOGINC_HEADERS = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cache-Control': 'max-age=0',
	'Connection': 'keep-alive',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Origin': 'https://zhjwxk.cic.tsinghua.edu.cn',
	'Referer': 'https://zhjwxk.cic.tsinghua.edu.cn/xklogin.do',
	'Sec-Fetch-Dest': 'document',
	'Sec-Fetch-Mode': 'navigate',
	'Sec-Fetch-Site': 'same-origin',
	'Sec-Fetch-User': '?1',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
	'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': '"Windows"',
}

LOGINC_DATA = {
	'j_username': USER_NAME,
	'j_password': PASSWORD,
	#'captchaflag': 'login1',
}

PIC_FILE = 'captcha.jpg'

MAIN_URL = 'http://zhjwxk.cic.tsinghua.edu.cn/xkYjs.vxkYjsXkbBs.do?m=main'