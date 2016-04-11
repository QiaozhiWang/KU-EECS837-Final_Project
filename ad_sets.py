import numpy as np
import pprint as pp 
from io import StringIO
from functools import reduce
import re, timeit, collections

def ad_sets(vectors):
	build = timeit.default_timer()
	#print(vectors)
	d_set = []
	a_sets = []
	d_set_dict = {}
	a_set_dict = {}
	a_dict_list = []
	try:
		col_num = len(vectors[1,:])
		case_num = len(vectors[:,1])
		#print(col_num)
		#print(case_num)
		oc_dict = []
		total_set = []	
		for i in range(0, col_num):	
			column = vectors[:,i]
			#print("V: ", V)
			uniques =  np.unique(column)
			#print(uniques)
			a_set = []
			for key in uniques:
				#print("key: ",key)
				s_set = np.where(column == key)[0]
				if i == col_num-1:
					d_set_dict[key]	= s_set
					d_set.append(s_set)
				else:
					a_set_dict[key] = s_set
					a_set.append(s_set)
			if not a_set == []:
				a_sets.append(a_set)
		a_dict_list.append(a_set_dict)
		a_build = timeit.default_timer()
	except IndexError:		#1d-vector
		uniques =  np.unique(vectors)
		for key in uniques:
			s_set = np.where(vectors == key)[0]
			d_set.append(s_set)
			d_set_dict[key] = s_set
		a_sets = ""
		a_set_dicts = {}
	ad_build = timeit.default_timer()
	print("******Time for a and d*********: ", ad_build-build)
	#print(d_set)
	#print(d_set_dict)		
	return d_set, a_sets, d_set_dict, a_dict_list

def A_set(vectors):	
	"""
	#=====================Use sets' intersection to calculate A===================#
	#----------put all A_sets in one list, except total_set[0]-----------#
	comp = [sub_set for A_set in total_set[0:-1] for sub_set in A_set] 	 
	#print(comp)
	elem_set = np.linspace(0,case_num-1,case_num)		
	while True:
		try:		
			#print(elem_set[0])
			its_set=[cset for cset in comp if np.in1d(cset,elem_set[0],assume_unique=True).any()]
			#print(elem_set[0], its_set)
			p_result = reduce(np.intersect1d, (its_set))
			A_sets.append(p_result)
			#print(p_result)
			elem_set = np.setdiff1d(elem_set,p_result)
			#print(elem_set)
			#print(p_result)
		except:
			break
	"""
	#===================Use brute compare to cal A=========================#
	A_build = timeit.default_timer()
	Attrs = vectors.tolist()
	A_set =[]
	#unique_vecs = [vec for vec in set(tuple(x.tolist()) for x in Attrs)]
	vec_set = [list(vec) for vec in set(tuple(x) for x in Attrs)]
	for vec in vec_set:
		#print(vec)
		#A_set.append(np.where(np.prod(vectors==vec,axis=-1))[0])
		A_set.append([pos for pos, y in enumerate(Attrs) if y==vec])
	#print(A_set)
	stop = timeit.default_timer()
	print("****Time for A_set: ", stop-A_build)
	return A_set