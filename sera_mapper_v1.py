# 
# Mapping used from http://etd.aau.edu.et/bitstream/handle/123456789/1245/Daniel%20Zegeye.pdf
# ==============================================================================

'''Amharic text to SERA(latin) standard converter [ATTS v1.o] converter --Python 2.7 and 3 

'''
import sys
import time
import codecs


_start_time = time.time()
_map_file = 'SERA_NORMALIZED'
_out = '_SERA'


def read_data(_file):
	_data= codecs.open(_file, 'r', 'utf-8').read()
	return _data

def write_to_file(_converted_cont,_out_file):
	_data = codecs.open(_out_file,'w','utf-8')
	_data.write(_converted_cont)
	print ('Convertion written to %s ' % (_out_file))
	_data.close()
	
def to_dic():
	''' Read the mapping file into a dictionary '''
	_delimator = '='
	_data = read_data(_map_file)
	_mapper = {}
	for line in _data.splitlines():
		_key = line.split(_delimator)[0].strip() ; _value = line.split(_delimator)[1].strip()
		_mapper[_key] = _value
	return _mapper

def convert_file(_file_name,_mapper):
	'''Convert the file content to SERA'''
	_converted_cont = ''
	_data = read_data(_file_name)
	for k,v in _mapper.items():
		_data = _data.replace(k,v)
	return _data

def convert_string(_string,_mapper):
	'''Convert the string content to SERA '''
	_converted_cont = ''
	for k,v in _mapper.items():
		_string = _string.replace(k,v)
	return _string 

def _start(arg1,arg2):
	_mapper = to_dic()
	if arg1 == '-f':
		_file_name = arg2
		print ('File %s read for convert ' % _file_name)
		_converted_cont = convert_file(_file_name,_mapper)
		_out_file = _file_name + _out
		write_to_file(_converted_cont,_out_file)
	elif arg1 == '-s':
		_string = sys.argv[2]
		_converted = convert_string(_string,_mapper)
		print ('		%s' % _converted)
	else:
		print ('		Use python sera_mapper_v1.py -f file_name to for file conversion or ')
		print ('		 python sera_mapper_v1.py -s \'your string here \' for direct string conversion ')
	print ('		Total time elapsed %f ' % (time.time() - _start_time))

	
if __name__ == '__main__':
	try:
		if sys.argv[1] and sys.argv[2]:
			_start(sys.argv[1],sys.argv[2])
	except IndexError:
		print ('		Use python sera_mapper_v1.py -f file_name to for file conversion or ')
		print ('		 python sera_mapper_v1.py -s \'your string here \' for direct string conversion ')
	

		

	
'''	
  Run -- python sera_mapper_v1.py -f file_name to for file conversion
  Run -- python sera_mapper_v1.py -s 'your string here' for direct string conversion	
  '''

