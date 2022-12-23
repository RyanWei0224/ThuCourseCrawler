import requests
import re
import time
import os
import pickle

#from lxml import etree

from config import *
from util import *

def main():
	x = CoreCrawler(cookies = COOKIES, intv = INTV)
	'''
	if TRY_LOGIN:
		while not x.login():
			s = input('retry? (Type anything to stop, tap enter to continue)')
			if s:
				return 0
	'''
	x.crawl_courses(COURSES)

class CoreCrawler():
	def __init__(self, cookies = dict(), intv = 3):
		try:
			with open('cookies.pkl', 'rb') as f:
				self.cookies = pickle.load(f)
			assert self.is_logged_in()
		except Exception as e:
			self.cookies = requests.utils.cookiejar_from_dict(cookies)

		self.intv = intv
		self.logFile = 'log.txt'

	def __del__(self):
		with open('cookies.pkl', 'wb') as f:
			pickle.dump(self.cookies, f)

	def log(self, txt):
		with open(self.logFile, 'w', encoding = 'utf-8') as f:
			print(txt, file = f)

	def try_get(self, url, method = 'get', **kwargs):
		err = None
		for i in range(3):
			try:
				if method == 'get':
					res = requests.get(url, timeout = 3.05, cookies = self.cookies, **kwargs)
				elif method == 'post':
					res = requests.post(url, timeout = 3.05, cookies = self.cookies, **kwargs)
				else:
					assert False, f'Unrecognized method {method}'
				res.raise_for_status()
			except Exception as e:
				print(e)
				err = e
			else:
				self.cookies.update(res.cookies)
				return res
		raise err


	def login(self):
		res = self.try_get(LOGIN_URL, headers = LOGIN_HEADERS)
		self.cookies.update(res.request._cookies)

		res = self.try_get(LOGIN2_URL, headers = LOGIN2_HEADERS)
		'''
		html = etree.fromstring(res.text, etree.HTMLParser())
		cap_url = html.xpath()
		'''
		match = re.search(r'<img id="captcha" src="(/login-jcaptcah\.jpg\?captchaflag=([^"]+))"', res.text)
		assert match is not None, 'Cannot find captcha image.'
		cap_url = CAPTCAH_PREF + match[1]
		res = self.try_get(cap_url, headers = CAPTCHA_HEADERS)
		with open(PIC_FILE, 'wb') as f:
			f.write(res.content)
		os.system(PIC_FILE)
		captcha = input('Input captcha:')
		data = {
			'captchaflag': match[2],
			'_login_image_': captcha,
		}
		data.update(LOGINC_DATA)
		res = self.try_get(LOGINC_URL, headers = LOGINC_HEADERS, data = data, method = 'post')
		if res.url == MAIN_URL:
			print('Login Successful!')
			os.remove(PIC_FILE)
			return True
		elif '登录失败：验证码不正确！' in res.text:
			print('Login failed! Wrong captcha.')
			return False
		elif '登录失败' in res.text:
			print('Login failed!')
			return False
		print('Don\'t know what\'s wrong.')
		return False

	def try_login(self):
		while not self.login():
			s = input('retry? (Type anything to stop, tap enter to continue)')
			if s:
				return False
		return True

	def assert_login(self):
		print('Timeout, trying to login...')
		try:
			assert self.try_login()
		except Exception as e:
			assert False, 'Login failed'

	def is_logged_in(self):
		params = PARAMS[XWK]
		res = self.try_get(GET_URL, headers = GET_HEADERS, params = params)
		m = re.search(r'<input\s+type="hidden"\s+name="token"\s+value="([0-9a-z]+)">', res.text)
		if m is None:
			if TIMEOUT_STR in res.text:
				return False
			else:
				print('Warning: timeout string not found!')
				return False
		return True

	def get_token(self, xwk):
		while True:
			params = PARAMS[xwk]
			res = self.try_get(GET_URL, headers = GET_HEADERS, params = params)
			m = re.search(r'<input\s+type="hidden"\s+name="token"\s+value="([0-9a-z]+)">', res.text)
			if m is None:
				if TIMEOUT_STR in res.text:
					self.assert_login()
					continue
				self.log(res.text)
				assert False, 'Get token failed.'
			return m[1]

	def crawl_course(self, cl):
		cid, cord, xwk = cl

		payload = ALL_PAYLOAD.copy()
		payload.update(PAYLOAD[xwk])

		course_id = f'{XNXQ};{cid};{cord};'
		payload[CID_STR[xwk]] = course_id

		while True:
			token = self.get_token(xwk)
			#print(token)
			payload['token'] = token
			res = self.try_get(URL, headers = HEADERS, data = payload, method = 'post')
			m = re.search(r'showMsg\("(.*?)"\);', res.text)
			if m is None:
				if TIMEOUT_STR in res.text:
					self.assert_login()
					continue
				self.log(res.text)
				assert False, 'Get response failed.'
			break
		msg = m[1]
		print(msg)

		if msg == '提交选课成功;':
			print(course_id, '选课成功')
			return True
		elif msg.find('课余量已无,不能再选,不能提交 !') != -1:
			return False
		else:
			raise ValueError(msg)

	def crawl_courses(self, courses):
		t = time.time() + self.intv
		while True:
			for course in courses:
				if self.crawl_course(course):
					return True
				t -= time.time()
				if t > 0:
					time.sleep(t)
				t = time.time() + self.intv

if __name__ == '__main__':
	main()