import os 
import subprocess
for file in os.listdir('media/'):
	file_name = 'media/'+file
	file_lenght=file
	print(file_name)
	extension=os.path.splitext(file)[-1].lower()

	if extension==".jpg":


		if not os.path.exists('media/' + "/compresse"):
			os.makedirs('media/' + "/compresse")
		print('yeh file hai',file_lenght)
		file_size=os.stat('media/'+file_lenght).st_size
		file_size_mb=file_size/(1024*1024)
		print('file size is',file_size_mb)
		if (file_size_mb >=1  and file_size_mb <=2):
			media_in='media/'+'/'+file
			print("media_in===",media_in)
			media_out='media/'+'/compresses/'+file
			print(media_out)

			subprocess.run(" ffmpeg -i " + media_in.replace(" ","\\")+ " -vcodec libx265 -crf 25 " + media_out.replace(" ","\\"),shell=True)
			print('yeh  1mb se bda aur 2 mb se chota file hai ============',file_name)
		elif (file_size_mb >=2  and file_size_mb<=10):
			media_in='media/'+'/'+file
			media_out='media/'+'/compresses/'+file
			subprocess.run(" ffmpeg -i " + media_in.replace(" ","\\")+ " -vcodec libx265 -crf 25 " + media_out.replace(" ","\\"),shell=True)
			print('yeh 2 to 10 size ki file hai ============',file_name)
		elif (file_size_mb>10):
			media_in='media/'+'/'+file
			media_out='media/'+'/compresses/'+file
			subprocess.run(" ffmpeg -i " + media_in.replace(" ","\\")+ " -vcodec libx265 -crf 25 " + media_out.replace(" ","\\"),shell=True)
			print('yeh10 mb se bdaa file hai ============',file_name)


		print('yeh jpg file hai ============',file_name)

	if extension==".mp4":
		print('yeh file hai',file_lenght)
		file_size=os.stat('media/'+file_lenght).st_size
		file_size_mb=file_size/(1024*1024)
		print('file size is',file_size_mb)
		if (file_size_mb >=1  and file_size_mb <=2):
			media_in='media/'+'/'+file
			media_out='media/'+'/compresses/'+file
			subprocess.run(" ffmpeg -i " + media_in.replace(" ","\\")+ " -vcodec libx265 -crf 25 " + media_out.replace(" ","\\"),shell=True)
			print('yeh 2 mb se chota file hai ============',file_name)
		elif file_size_mb >=2 and (file_size_mb<=10):
			media_in='media/'+'/'+file
			media_out='media/'+'/compresses/'+file
			subprocess.run(" ffmpeg -i " + media_in.replace(" ","\\")+ " -vcodec libx265 -crf 26 " + media_out.replace(" ","\\"),shell=True)
			print('yeh 2 to 10 size ki file hai ============',file_name)
		elif (file_size_mb>10):
			media_in='media/'+'/'+file
			media_out='media/'+'/compresses/'+file
			subprocess.run(" ffmpeg -i " + media_in.replace(" ","\\")+ " -vcodec libx265 -crf 28 " + media_out.replace(" ","\\"),shell=True)
			print('yeh10 mb se bdaa file hai ============',file_name)
	elif extension==".png":

		print('yeh file hai',file_lenght)
		file_size=os.stat('media/'+file_lenght).st_size
		file_size_mb=file_size/(1024*1024)
		print('file size is',file_size_mb)
		if (file_size_mb >=1  and file_size_mb <=2):
			media_in='media/'+'/'+file
			media_out='media/'+'/compresses/'+file
			subprocess.run(" ffmpeg -i " + media_in.replace(" ","\\")+ " -vcodec libx265 -crf 25 " + media_out.replace(" ","\\"),shell=True)
		# print('yeh png file hai ============',file_name)
			print('yeh 2 mb se chota file hai ============',file_name)
		elif file_size_mb >=2 and (file_size_mb<=10):
			media_in='media/'+'/'+file
			media_out='media/'+'/compresses/'+file
			subprocess.run(" ffmpeg -i " + media_in.replace(" ","\\")+ " -vcodec libx265 -crf 25 " + media_out.replace(" ","\\"),shell=True)
			print('yeh 2 to 10 size ki file hai ============',file_name)
		elif (file_size_mb>10):
			media_in='media/'+'/'+file
			media_out='media/'+'/compresses/'+file
			subprocess.run(" ffmpeg -i " + media_in.replace(" ","\\")+ " -vcodec libx265 -crf 25 " + media_out.replace(" ","\\"),shell=True)
			print('yeh10 mb se bdaa file hai ============',file_name)







# import os

# for file in os.listdir('path'):
# 	if '.jpg' in file or '.mp4' in file:
# 		file_size = ''
# 		if file_size <=2:
# 			pass
# 		elif file_size = 10:
# 			pass

# 		elif file_size >10:
# 			pass
# 		else:
# 			pass

