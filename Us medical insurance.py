import csv
with open("insurance.csv") as insurance_csv:
    insurance_reader = csv.DictReader(insurance_csv)
    insurance_list = [row for row in insurance_reader]

southwest_region = [insurance for insurance in insurance_list if insurance["region"] == "southwest"]
southeast_region = [insurance for insurance in insurance_list if insurance["region"] == "southeast"]
northwest_region = [insurance for insurance in insurance_list if insurance["region"] == "northwest"]
northeast_region = [insurance for insurance in insurance_list if insurance["region"] == "northeast"]
regions = [southwest_region, southeast_region, northwest_region, northeast_region]

def average_function(persons,parameter):
    soma = 0
    for person in persons:
        soma += float(person[parameter])
    return soma/(len(persons))

#average age
average_age = average_function(insurance_list,"age")
"The average age in the data is {}".format(round(average_age,1))

#average bmi
average_bmi = average_function(insurance_list,"bmi")
"The average BMI value is {}".format(round(average_bmi,3))

#average children
def average_children(persons):
    soma = 0
    person_list = [person for person in persons if float(person["age"]) > 25]
    for person in person_list:
        soma += float(person["children"])
    return soma/(len(person_list))

"These people have on average {} children.".format(round(average_children(insurance_list),2))

#average insurance cost
average_insurance_cost = {"Southwest":round(average_function(southwest_region,"charges"),3), "Southeast": round(average_function(southeast_region,"charges"),3), 
                          "Northwest":round(average_function(northwest_region,"charges"),3), "Northeast":round(average_function(northeast_region,"charges"),3)}
"The average insurance cost by region is: {}.".format(average_insurance_cost)

#Number of smokers
def number_smoker(regions):
    soma = 0
    for region in regions:
        if region["smoker"] == "yes":
            soma += 1
    return soma

smokers = {"Southwest":number_smoker(southwest_region), "Southeast": number_smoker(southeast_region), 
            "Northwest":number_smoker(northwest_region), "Northeast":number_smoker(northeast_region)}
"The number of smokers by region are: {}".format(smokers)

#Classification bmi
def bmi_classification_function(persons):
    underweight = 0
    normal_weight = 0
    overweight = 0
    obesity = 0
    for person in persons:
        if float(person["bmi"]) < 18.5:
            underweight += 1
        elif 18.5 <= float(person["bmi"]) < 25:
            normal_weight += 1
        elif 25 <= float(person["bmi"]) < 30:
            overweight += 1
        else:
            obesity += 1
    return {"Underweight": underweight, "Normal weight": normal_weight, "Overweight":overweight, "Obesity":obesity}

bmi_classification_regions = [bmi_classification_function(region) for region in regions]
region_name = ["Southwest", "Southeast",  "Northwest", "Northeast"]
for i in range(len(regions)):
    print("{region}: {bmi_classification}".format(region=region_name[i], bmi_classification=bmi_classification_regions[i]))

    bmi_classification_general = bmi_classification_function(insurance_list)
"All regions: {bmi_classification}".format(bmi_classification=bmi_classification_general)

def age_classification_function(persons):
    age_0_20 = 0
    age_20_30 = 0
    age_30_40 = 0
    age_40_50 = 0
    age_50_60 = 0
    age_60 = 0
    for person in persons:
        if float(person["age"]) <= 20:
            age_0_20 += 1
        elif 20 < float(person["age"]) <= 30:
            age_20_30 += 1
        elif 30 < float(person["age"]) <= 40:
            age_30_40 += 1
        elif 40 < float(person["age"]) <= 50:
            age_40_50 += 1
        elif 50 < float(person["age"]) <= 60:
            age_50_60 += 1
        else:
            age_60 += 1
    return {"0-20": age_0_20, "20-30": age_20_30, "30-40": age_30_40, "40-50": age_40_50, "50-60":age_50_60, ">60":age_60}

age_classification_regions = [age_classification_function(region) for region in regions]
region_name = ["Southwest", "Southeast",  "Northwest", "Northeast"]
for i in range(len(regions)):
    print("{region}: {age_classification}".format(region=region_name[i], age_classification=age_classification_regions[i]))

    age_classification_general = age_classification_function(insurance_list)
"All regions: {age_classification}".format(age_classification=age_classification_general)

def children_classification_function(persons):
    zero_children = 0
    one_child = 0
    two_children = 0
    three_more_children = 0
    person_list = [person for person in persons if float(person["age"]) > 25]
    for person in person_list:
        if float(person["children"]) == 0:
            zero_children += 1
        elif float(person["children"]) == 1:
            one_child += 1
        elif float(person["children"]) == 2:
            two_children += 1
        else:
            three_more_children += 1
    return {"0":zero_children, "1": one_child, "2": two_children, ">3":three_more_children}

children_classification_regions = [children_classification_function(region) for region in regions]
region_name = ["Southwest", "Southeast",  "Northwest", "Northeast"]
for i in range(len(regions)):
    print("{region}: {children_classification}".format(region=region_name[i], children_classification=children_classification_regions[i]))

    children_classification_general = children_classification_function(insurance_list)
"All regions: {children_classification}".format(children_classification=children_classification_general)