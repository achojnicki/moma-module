from pprint import pprint

class Instrumental:
	def __init__(self, patterns, simple_pattern_recognizer):
		self.patterns=patterns
		self.simple_pattern_recognizer=simple_pattern_recognizer



	def match_to_pattern(self, sample, pattern):
		avg_match=0

		for p in pattern['instrumental_patterns']:
			
			pat=pattern['instrumental_patterns'][p]

			self.simple_pattern_recognizer.patterns=self.simple_pattern_recognizer.get_simple_patterns(
				simple_patterns=pat['patterns'],
				patterns_base=pattern['simple_patterns']
			)

			pattern_match_result, pattern_match_details=self.simple_pattern_recognizer.find_patterns(
				sample=sample,
				matching_min=pat['matching_min'],
			)

			if pattern_match_result:
				for a in pattern_match_details:
					a['pattern_name']=pattern['pattern_name']
					a['event_name']=pat['event']
				return [pattern_match_result,  pattern_match_details]

		return None

	def find_pattern(self, sample):
		for pattern in self.patterns:
			result=self.match_to_pattern(sample, pattern)
			if result and len(result)==2:
				return result

		return None