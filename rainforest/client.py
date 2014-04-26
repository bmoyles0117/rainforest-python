class Rainforest(object):
	"""
	A client to interact with the RainforestQA API

	:param str client_token: Your account's API Client Token
	"""
	def __init__(self, client_token):
		self.client_token = client_token