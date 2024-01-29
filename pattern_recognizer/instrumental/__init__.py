from pprint import pprint

class Instrumental:
	def __init__(self, patterns, simple_pattern_recognizer):
		self.patterns=patterns
		self.simple_pattern_recognizer=simple_pattern_recognizer



	def match_to_pattern(self, sample, pattern, pattern_name):
		avg_match=0

		entry_point_pattern=pattern['instrumental_patterns']['entry_point']
		self.simple_pattern_recognizer.patterns=self.simple_pattern_recognizer.get_simple_patterns(
			simple_patterns=entry_point_pattern['patterns'],
			patterns_base=pattern['simple_patterns']
		)
		#pprint(entry_point_pattern)

		entry_point_match_result, entry_point_match_details=self.simple_pattern_recognizer.find_patterns(
			sample=sample,
			matching_min=entry_point_pattern['matching_min'],
			)
		if entry_point_match_result:
			pass
			pprint(entry_point_match_details)


	def find_pattern(self, sample):
		for pattern in self.patterns:
			self.match_to_pattern(sample, pattern, pattern['name'])