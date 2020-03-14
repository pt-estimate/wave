import os
import swell as sw
import yaml

def main():
	swell = sw.Swell(os.environ['DATASRC'])
	extractor = sw.SwellExtractor()

	print(extractor.extract(swell, 'tf-idf'))

if __name__ == '__main__':
	main()
