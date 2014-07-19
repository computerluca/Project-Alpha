import urllib
import json
import datetime
import os

api_url = "http://api.openweathermap.org/data/2.5/find?" 
api_key = "" # put your key here


while True :
	os.system('clear')
	city = raw_input("Enter city: ")
	data_format = raw_input("Write 'c' for Celsius or 'f' for Fahrenheit: ")
	data_format = data_format.lower()
	print data_format
	
	# validate de user input
	# TO_DO: improve validation ej. "only recieve alpha characters"
	
	if len(city) < 1 :
		print "City:",city,"not valid. Please write other city"
		continue
	if data_format != "c" and data_format != "f" :
	 	print "Please write 'C' or 'F' to chose a valid measure system"
	 	continue
	 	
	 	
	if data_format == "c" :
	 	measure_system = "metric"
	else :
		measure_system = "imperial"
		
		
		#Make the conection and read the data
		
		
	url = api_url + urllib.urlencode({"q":city,"type":"like","units":measure_system,"APPID":api_key})
	request = urllib.urlopen(url)
	data =  request.read()
	
	try : 
		js = json.loads(str(data))
	except :
		js = None
		print "======== Fail Retrieving information ========="
		continue
	
	# Printing data
	
	
	if js["count"] == 1 :
	 
		# Assigning values
		 	
		city_retrieved = js["list"][0]["name"]
		country_retrieved = js["list"][0]["sys"]["country"]
		date_retrieved = datetime.datetime.fromtimestamp(int(js["list"][0]["dt"])).strftime('%d-%m-%Y')
		temp_actual_retrieved = js["list"][0]["main"]["temp"]
		temp_max_retrieved = js["list"][0]["main"]["temp_max"]
		temp_min_retrieved = js["list"][0]["main"]["temp_min"]
		 	
		 # Printing results 
		 	
		print "\n\nThe temperature for",date_retrieved
		print "in",city_retrieved,country_retrieved,"is"
		print "Current",temp_actual_retrieved,data_format.upper()
		print "Maximum",temp_max_retrieved,data_format.upper()
		print "Minimum",temp_min_retrieved,data_format.upper(),"\n\n"
	
	
	
	
	
	
	
	
	
	if js["count"] > 1 :
	
		while True :
		
			print "\nThere are",js["count"],"results matching",city
			print "Please choose the number corresponding the city you want\n"
			
			city_count = 0
			city_count_list = list()
			
			# Create a list of number and print cities retreived 
			
			for resultados in range(len(js["list"])) :
				city_count_list.append(city_count + 1)
				print city_count + 1,js["list"][city_count]["name"],js["list"][city_count]["sys"]["country"]
				city_count = city_count + 1
			
			city_number = raw_input("Enter number: ")
			
			# Validate user input
			# To do : improve validation
			
			try :
				city_number = int(city_number)
			except :
				print "City number:",city_number,"not valid"
				continue
		 	
			if city_number not in city_count_list :
		 		print "City number:",city_number,"not valid"
		 		continue
		 		
		 	# Assigning values
		 		
		 	city_retrieved = js["list"][city_number - 1]["name"]
		 	country_retrieved = js["list"][city_number - 1]["sys"]["country"]
		 	date_retrieved = datetime.datetime.fromtimestamp(int(js["list"][city_count - 1]["dt"])).strftime('%d-%m-%Y')
		 	temp_actual_retrieved = js["list"][city_number - 1]["main"]["temp"]
		 	temp_max_retrieved = js["list"][city_number - 1]["main"]["temp_max"]
		 	temp_min_retrieved = js["list"][city_number - 1]["main"]["temp_min"]
		 	
		 	# Printing results 
		 	
		 	print "\n\nThe temperature the",date_retrieved
		 	print "in",city_retrieved,country_retrieved,"is"
		 	print "Current",temp_actual_retrieved,data_format.upper()
		 	print "Maximum",temp_max_retrieved,data_format.upper()
		 	print "Minimum",temp_min_retrieved,data_format.upper(),"\n\n"
		 	
		 	break
	 	
	 	
	
    
	while True :
    
		answer_input = raw_input("Would you like to make another search, 'y' or 'n' ? ")
		if answer_input != "y" and answer_input != "n" :
			print "Please write 'y' or 'n'"
			continue
		elif answer_input == "n" :
			print "Goodbye"
			exit()
		elif answer_input == "y" :
			break
			
	continue
		
    
	 	
	 	
	 	
	
