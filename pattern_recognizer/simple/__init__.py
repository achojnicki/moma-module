from pprint import pprint


class Simple:
	def __init__(self):
		self.to_zero=0

	def calc_match(self, sample, pattern):
		if pattern != 0:
			return (sample-self.to_zero)*100/ pattern

		else:
			return (sample*100)/self.to_zero

	def match(self, value, match_value_min, match_value_max):
		return True if value>=match_value_min and value<=match_value_max else False

	def match_status(
		self,
		result,
		avg_match,
		matching_values,
		match_value_min,
		match_value_max,
		matching_min,
		must_match_indexes=None,
		):
		if (avg_match>=match_value_min and avg_match<=match_value_max) and matching_values>=matching_min:

			if not must_match_indexes:
				return True
			else:
				for a in result['results']:
					if a['index'] in must_match_indexes:
						if not a['matching']:
							return False
				return True

		else:
			return False

	def get_simple_patterns(self, simple_patterns, patterns_base):
		gen=[]

		#print(patterns_base)
		for pattern in simple_patterns:
			#print(pattern)
			item={}
			gen.append(pattern|patterns_base[pattern['pattern_name']])

		#pprint(gen)
		return gen

	def match_to_pattern(self, sample, pattern, match_value_min, match_value_max, matching_min, must_match_indexes):
		#print(f"len(sample)={len(sample)}")
		#print(f"len(pattern)={len(pattern)}")
		#print('---')

		#pprint(sample)
		
		assert len(pattern) == len(sample), "mismatch of size"

		avg=0
		matching_values=0
		results=[]
		
		self.to_zero=sample[0]['close']

		for index in range(0,len(sample)):
			match_value=self.calc_match(sample[index]['close'], pattern[index])
			matching=self.match(
				value=match_value,
				match_value_min=match_value_min,
				match_value_max=match_value_max,
			)

			avg+=match_value

			if matching:
				matching_values+=1


			item={
				"index":index, 
				"value":sample[index]['close'],
				"match_value":match_value, 
				"matching": matching,
				"timestamp": sample[index]['timestamp']
				}

			results.append(item)
			index+=1

		avg=avg/len(sample)
		result={
			"results":results,
			"matching": matching_values,
			"avg": avg,
		}
		match_status=self.match_status(
			result=result,
			avg_match=avg,
			matching_values=matching_values,
			matching_min=matching_min,
			match_value_min=match_value_min,
			match_value_max=match_value_max,
			must_match_indexes=must_match_indexes
			)
		return [match_status, result]
		

	def find_patterns(self, sample, matching_min):
		matching=[]

		for pattern in self.patterns:
			match, result=self.match_to_pattern(
				sample=sample,
				pattern=pattern['pattern'],
				match_value_min=pattern['match_value_min'],
				match_value_max=pattern['match_value_max'],
				must_match_indexes=pattern['must_match_indexes'],
				matching_min=matching_min
			)

			if match:
				result['name']=pattern['pattern_name']
				matching.append(result)


		return [match, matching]




