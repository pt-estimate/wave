import pandas as pd

class Swell:
	def __init__(self, data_src):
		self.data_src = data_src

class SwellExtractor:
	def extract(self, swell, format):
		extractor = self._get_extractor(format)
		return extractor(swell)

	def _get_extractor(self, format):
		if format == 'tf-idf':
			return self._extract_tf_idf
		elif format == 'tf-icf':
			return 'carry out tf-icf extraction'
		else:
			raise ValueError(format)

	def _extract_tf_idf(self, swell):
		df = pd.read_csv(swell.data_src)
		print(df.shape)
		return 'carry out tf-idf extraction'
		

