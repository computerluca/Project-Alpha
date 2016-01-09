import urllib
import json
import datetime
import os

api_key = "" # put your key here

def geoLocation(api_key,measure_system) :

    '''
    geoLocation() returns the weather at the user location.
    This function uses the freegeoip.net API the get the location.
    The location is obtained by the user's ip.
    
    '''
    # retreaving geoLocation from  freegeoip
    url_free_geo_ip = "http://freegeoip.net/json"
    request_free_geo_ip = urllib.urlopen(url_free_geo_ip)
    data_free_geo_ip = request_free_geo_ip.read()
    js_free_geo_ip = json.loads(str(data_free_geo_ip))
    longitude = str(js_free_geo_ip["longitude"])
    latitude = str(js_free_geo_ip["latitude"])
    
    # retreaving weather from openweathermap using freegeoip data
    
    openweathermap_url = "http://api.openweathermap.org/data/2.5/weather?"
    url_geolocation = openweathermap_url + urllib.urlencode({"lat":latitude,"lon":longitude,"units":measure_system,"APPID":api_key})
    
    request_open_weather = urllib.urlopen(url_geolocation)
    data_open_weather =  request_open_weather.read()
    return json.loads(str(data_open_weather))
    
def clearScreenCommand() :
    '''
    clearScreenCommand() retrieves the OS from the user and return the command line to clear the shell.
    '''
    if os.name == "posix" :
        return "clear"
    else :
        return "cls"
        
        
def measureSystem(measure_system_input) :
    '''
    measureSystem() returns the measure system chosen.
    '''
    if measure_system_input == "c" :
        return "metric"
    else:
        return "imperial"
        
def currentWeather(api_key,measure_system,city) :
    '''
    current_weather() retrieves information from openweathermap.
    '''
    openweathermap_url = "http://api.openweathermap.org/data/2.5/find?"
    url_current_weather = openweathermap_url + urllib.urlencode({"q":city,"type":"like","units":measure_system,"APPID":api_key})
    
    request_open_weather = urllib.urlopen(url_current_weather)
    data_open_weather =  request_open_weather.read()
    return json.loads(str(data_open_weather))

    
def forecastWeather(api_key,measure_system) :
    '''
    Forecast_weather() retrieves the forecast from a city up to 16 days in advance.
    '''
    
        
def weatherInformation(api_key) :
    '''
    weatherInformation() is the main function.
    '''
    while True :
        os.system(clearScreenCommand())
        measure_system_input = raw_input("Please choose the measure system of your choice. Write 'c' for Celsius or 'f' for Fahrenheit: ")
        
        # Validate user input
        if measure_system_input not in ["c","f"] :
            print "Input s% is not valid" % (measure_system_input)
            continue
        
        user_location_weather = geoLocation(api_key,measureSystem(measure_system_input)) 
        user_location_city = user_location_weather["name"]
        while True :
            print 30 * "-"
            print "Main - Menu"
            print 30 * "-"
            print "1.- Would you like to know the weather from you current location? "+ user_location_city
            print "2.- Would you like to know the weather from another city?"
            print "3.- Exit"
            main_menu_input = raw_input("Enter your choice [1-3] : ")
            
            #Validate user input
            if main_menu_input not in ["1","2","3"] :
                print "Input s% is not valid" % (main_menu_input)
                continue
            if main_menu_input == "1" :
                os.system(clearScreenCommand())
                print "City:",user_location_weather["name"]
                print "Country:",user_location_weather["sys"]["country"]
                print "Current temp:",user_location_weather["main"]["temp"]
                print "Temp max:",user_location_weather["main"]["temp_max"]
                print "Temp min:",user_location_weather["main"]["temp_min"]
            
            elif main_menu_input == "2" :
                while True :
                    user_city_input = str(raw_input("Enter city: Enter q to return to the menu "))
	            
		    
                    
                    # validate de user input
                    # TO_DO: improve validation ej. "only recieve alpha characters"

                    if len(user_city_input) < 1 :
                        print "City:",user_city_input,"not valid. Please write other city"
                        continue
		    elif not user_city_input.isalpha():
			print "You can input only characters"
			continue
		    elif user_city_input =="q":

        		break
                    else :
                        current_weather_city = currentWeather(api_key,measureSystem(measure_system_input),user_city_input)
                        if current_weather_city ["count"] == 1 :
                            print "\n\nThe temperature for the ",datetime.datetime.fromtimestamp(int(current_weather_city["list"][0]["dt"])).strftime('%d-%m-%Y')
                            print "in",current_weather_city["list"][0]["name"],current_weather_city["list"][0]["sys"]["country"]
                            print "Current temp:",current_weather_city["list"][0]["main"]["temp"]
                            print "Temp max:",current_weather_city["list"][0]["main"]["temp_max"]
                            print "Temp min:",current_weather_city["list"][0]["main"]["temp_min"]
                        if current_weather_city ["count"] > 1 : 
                            while True :
                                print "\nThere are",current_weather_city["count"],"results matching",user_city_input
                                print "Please choose the number corresponding the city you want\n"
                                city_count = 0
                                city_count_list = list()
                                for result in range(len(current_weather_city["list"])) :
                                    city_count_list.append(city_count + 1)
                                    print city_count + 1,current_weather_city["list"][city_count]["name"],current_weather_city["list"][city_count]["sys"]["country"]
                                    city_count = city_count + 1
                                    
                                city_number_input = raw_input("Enter number: ")
                                    # Validate user input
                                    # To do : improve validation
                                    
                                try :
                                    city_number_input = int(city_number_input)
                                except:
                                    print "City number:",city_number_input,"not valid"
                                    continue
                                    if city_number_input not in city_count_list :
                                        print "City number:",city_number_input,"not valid"
                                        continue
                                   
                                print "\n\nThe temperature for the ",datetime.datetime.fromtimestamp(int(current_weather_city["list"][city_number_input - 1]["dt"])).strftime('%d-%m-%Y') 
                                print "in",current_weather_city["list"][city_number_input - 1]["name"],current_weather_city["list"][city_number_input - 1]["sys"]["country"]
                                print "Current temp:",current_weather_city["list"][city_number_input - 1]["main"]["temp"]
                                print "Temp max:",current_weather_city["list"][city_number_input - 1]["main"]["temp_max"]
                                print "Temp min:",current_weather_city["list"][city_number_input - 1]["main"]["temp_min"]
                                break
                            break
                
            elif main_menu_input == "3" :
                break
            
        print "Good - bye!"
        break
                
            
             

weatherInformation(api_key)
