models = ['Volkswagen - Golf','Renault - Clio','Volkswagen - Polo',
'Ford - Fiesta','Nissan - Qashqai','Peugeot - 208','VW - Tiguan','Skoda - Octavia',
'Toyota - Yaris','Opel - Corsa','Dacia - Sandero','Renault - Captur','Citroen - C3',
'Peugeot - 3008','Ford - Focus','Fiat - 500','Dacia - Duster','Peugeot - 2008',
'Skoda - Fabia','Fiat - Panda','Opel - Astra','VW - Passat','Mercedes-Benz - A-Class',
'Peugeot - 308','Ford - Kuga']

sales2018 = ['445,754','336,268','299,920','270,738','233,026','230,049','224,788',
'223,352','217,642','217,036','216,306','214,720','210,082','204,197','196,583',
'191,205','182,100','180,204','172,511','168,697','160,275','157,986','156,020',
'155,925','154,125']

sales2017 = ['483,105','327,395','272,061','254,539','247,939','244,615','234,916',
'230,116','199,182','232,738','196,067','212,768','207,299','166,784','214,661',
'189,928','NA','180,868','180,136','187,322','217,813','184,123','NA','NA','NA']

sales2016 = ['492,952','315,115','308,561','300,528','234,340','249,047','180,198',
'230,255','193,969','264,844','170,300','217,105','134,560','NA','214,435',
'183,730','NA','NA','177,301','191,617','253,483','208,575','NA','195,653','NA']

answer1 = "" # wskaż nazwę modelu jako string
answer2 = "" # wskaż producenta jako string
answer3 = [] # wskaż odpowiedź jako listę zawierającą wszystkie modele spełniające kryteria
answer4 = "" # wskaż nazwę modelu jako string
answer5 = "" # odpowiedź podaj w formacie procentowym jako string. Np. '21%'

def answer_1():
  top_sales_model = 0
  for key, value in cars.items():
    for key2, value2 in value.items():
      for key3, value3 in value2.items():
        if value3['2017'] > top_sales_model:
          top_sales_model = value3['2016']
          answer1 = str(key2)
          return answer1
        

def answer_2():
  top_sales_producer = 0
  top_sales_producer_dict = {}
  for key, value in cars.items():
    for key2, value2 in value.items():
      if key not in top_sales_producer_dict.keys():
        top_sales_producer_dict[key]= [value2['sales']['2018']]
      else:
        top_sales_producer_dict[key].append(value2['sales']['2018'])
  for brand,sale in top_sales_producer_dict.items():
    if top_sales_producer < sum(sale):
      top_sales_producer = sum(sale)
      return brand

def answer_3():
  for key, value in cars.items():
    for key2, value2 in value.items():
      if cars[key][key2]['sales']['2016'] == 0 and cars[key][key2]['sales']['2017'] != 0:
        answer3.append(key2)
        return answer3

def answer_4():
  leastesell_brand = 1000000000
  leastesell_brand_dict = {}
  for key, value in cars.items():
    for key2, value2 in value.items():
      if key not in leastesell_brand_dict.keys():
        leastesell_brand_dict[key2]= [value2['sales']['2018'],value2['sales']['2017'],value2['sales']['2016']] 
      else:
        leastesell_brand_dict[key2].append(value2['sales']['2018'])
        leastesell_brand_dict[key2].append(value2['sales']['2017'])
        leastesell_brand_dict[key2].append(value2['sales']['2016'])
    
  for key, item in leastesell_brand_dict.items():
    if sum(item) < leastesell_brand:
      leastesell_brand = sum(item)
  return key

#funkcja 5 niedokonczona
def answer_5():
  leastesell_brand = 1000000000
  leastesell_brand_dict = {}
  result = ''
  a = 0
  for key, value in cars.items():
    for key2, value2 in value.items():
      if key == 'Peugeot' and '2017' not in leastesell_brand_dict.keys():
        leastesell_brand_dict['2017'] = {key2:value2['sales']['2017']}
        leastesell_brand_dict['2018'] = {key2:value2['sales']['2018']}
      elif key == 'Peugeot' and '2017' in leastesell_brand_dict.keys():
        leastesell_brand_dict['2017'].update({key2:value2['sales']['2017']})
        leastesell_brand_dict['2018'].update({key2:value2['sales']['2018']})
      else:
        continue
  for key,value in leastesell_brand_dict.items():
    for key2,value2 in value.items():
      print (key2, value2)    

def convert(number_as_string):
    if number_as_string == "NA":
        return 0
    return int(number_as_string.replace(",", ""))

def handle_exceptions(brand):
    if brand == "VW":
        return "Volkswagen"
    return brand

cars = {}

for index, model in enumerate(models):
    brand, car_model = model.split(" - ")
    brand = handle_exceptions(brand)
    if brand not in cars:
        cars[brand] = {}
    if car_model not in cars[brand]:
        cars[brand][car_model] = {
            "sales": {
                "2016": convert(sales2016[index]),
                "2017": convert(sales2017[index]),
                "2018": convert(sales2018[index]),
            }
        }


answer1 = str(answer_1())
answer2 = str(answer_2())
answer3 = answer_3()
answer4 = answer_4()

print (answer1)
print (answer2)
print (answer3)
print(answer4)




'''
#fist program cars dict creation method, working but not that efficient as figured out later on

sales2016_int = []
for i in range(0, len(sales2016)):
  sales2016[i] = sales2016[i].replace(',', '')
  sales2017[i] = sales2017[i].replace(',', '')
  sales2018[i] = sales2018[i].replace(',', '')


warstwa1 = {}
warstwa2 = {}
warstwa3 = {}

index = 0
for each in models:
  warstwa1 = {}
  if sales2016[index] == 'NA':
    warstwa1.update({'2016': 0}) 
  else:
    warstwa1.update({'2016': int(sales2016[index])})
  
  if sales2017[index] == 'NA':
    warstwa1.update({'2017': int(0)}) 
  else:
    warstwa1.update({'2017': int(sales2017[index])})

  if sales2018[index] == 'NA':
    warstwa1.update({'2018': int(0)}) 
  else:
    warstwa1.update({'2018': int(sales2018[index])})

  splitted_models = each.split(' - ')
  warstwa2 = {splitted_models[1]:warstwa1} 


  if splitted_models[0] == 'VW':
    warstwa3['Volkswagen'].update(warstwa2) 
    index +=1
    continue
  
  if splitted_models[0] in warstwa3.keys():
    warstwa3[splitted_models[0]].update(warstwa2)
    index +=1
    continue
  
  warstwa3[splitted_models[0]] = warstwa2
  index +=1
  
print (warstwa3)

#this is something that is written to test the test bracj
'''