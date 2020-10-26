import pandas as pd 
import numpy as np 
# from tkinter import *

def str2bool(v):
   return str(v).lower() in ("yes", "true", "correct", "t", "1")

def is_digit(check_input):
    '''
    function checking if your string is a pure digit, int
    return : bool
    '''
    if check_input.isdigit():
        return True
    return False

def read_float(text): 
    result = input(text)
    if not is_digit(result): 
        read_float(text)
    else:
        return float(result)



# def printtext():
#     global e
#     text = e.get() 
#     print (text)

# root = Tk()

# root.title('Name')

# e = Entry(root)
# e.pack()
# e.focus_set()

# b = Button(root,text='okay',command=printtext)
# b.pack(side='bottom')
# root.mainloop()

# Acronym names 
symp_acronyms = dict()
symp_acronyms["pruritus"] = "Pruritus: sever itching of the skin\n"
symp_acronyms["anorexia"] = "Anorexia (eating disorder), weight loss, or nausea within 2 weeks prior to the onset of jaundice\n"
symp_acronyms["anorexia_1"] = "Anorexia (eating disorder), weight loss, or nausea within more than 2 weeks prior to the onset of jaundice\n"
symp_acronyms["fever"] = "Fever\n"
symp_acronyms["soft_liver_edge"] = "Soft liver edge\n"
symp_acronyms["liver_edge_extension"] = "Liver edge extension\n"
symp_acronyms["painful_liver"] = "Painful liver\n"
symp_acronyms["firm_liver"] = "Firm liver\n"
symp_acronyms["nodular_liver"] = "Nodular liver\n"
symp_acronyms["acholia"] = "Lack or absence of bile secretion (lack of the normal brown color in feces or pale feces)\n"

fact_acronyms = dict() 
fact_acronyms["alcohol"] = "Alcohol intake of more than 2 servings per day on average\n"
fact_acronyms["chronic_hyperbilirubinemic_conditions"] = "Family history of chronic hyperbilirubinemic conditions\n"
fact_acronyms["autoimmune_disease"] = "Family history of autoimmune disease or inflammatory bowel disease\n"
fact_acronyms["tattoo"] = "Exposure to needles (e.g. tattoo)\n"
fact_acronyms["sex"] = "History of unprotected sexual contact\n"
fact_acronyms["unsanitary_invironment"] = "Exposure to unsanitary environment\n"
fact_acronyms["hepatitis"] = "Contact with Hepatitis\n"
fact_acronyms["surgery"] = "Surgical history\n"
fact_acronyms["fava"] = "Eating fava beans\n"

test_acronyms = dict()
# int 
test_acronyms["bilirubin"] = "Level of biliribin as indicated in urine test results in mg/dl\n"
test_acronyms["bilirubin_c"] = "Level of conjugated biliribin as indicated in urine test results in mg/dl\n"
test_acronyms["bilirubin_u"] = "Level of unconjugated biliribin as indicated in urine test results in mg/dl\n"
test_acronyms["anemia"] = "Level of hemoglobin as indicated in blood test results in g/dl\n"
test_acronyms["ast"] = "Aspartate aminotransferase  level (AST - marker of liver damage but also present in the myocardium and muscle) as indicated in blood test results in U/L\n" # normal 15-40U/L
test_acronyms["alt"] = "Alanine aminotransferase  level (AST - marker of liver damage) as indicated in blood test results in U/L\n" # normal 5-35U/L
test_acronyms["proth"] = "Prothrombin activity (vitam K factor) as indicated in blood test results in %\n" # normal 70-80%
test_acronyms["alk"] = "Alkaline phosphatase level as indicated in blood test results in %\n" # normal 40-130 
test_acronyms["gamma"] = "Gamma-glutamyl transferase level as indicated in blood test results in %\n" # normal 10-49
test_acronyms["K"] = "Vitamin K level as indicated in blood test results in ng/mL\n" # normal 0.2-3.2 ng/mL


# bool 
test_acronyms["urine"] = "Have you taken a urine test?\n"
test_acronyms["blood"] = "Have you taken a blood test and have the complete blood count results?\n"
test_acronyms["choluria"] = "Presence of bile in urine (Choluria) as indicated in urine test results\n"
test_acronyms["murphy"] = "Have you taken a murphy's sign test?\n"
test_acronyms["murphy_result"] = "A positive myphy's sign test\n"




# Dictionary of underlying causes acronyms
underlying_causes_acronyms = dict()
underlying_causes_acronyms["hemolysis"] = "Hemolysis"
underlying_causes_acronyms["cholestasis"] = "Cholestasis"
underlying_causes_acronyms["cirrhosis"] = "Cirrhosis"
underlying_causes_acronyms["heposemia"] = "Heposemia"
underlying_causes_acronyms["hepatitis"] = "Hepatitis"
underlying_causes_acronyms["carcinoma of the pancreas"] = "Carcinoma of the pancreas"
underlying_causes_acronyms["genetic_disease"] = "Genetic diseases of chronic hyperbilirubinemic conditions: \n1.Crigle-Najjar syndrome (rare) \n2.Gilbert syndrome (caucasian)  \n3.Dubin-Johnson syndrome  \n4.Rotor's syndrome"
underlying_causes_acronyms["hepatic_defect"] = "Hepatic defect in the bilirubin uptake or conjugation"
underlying_causes_acronyms["necrosis"] = "Hepatic necrosis (mild Cirrhosis)"
underlying_causes_acronyms["inflammation"] = "Inflammation with liver capsule distention"
underlying_causes_acronyms["chronic"] = "Chronic Liver Disease"
underlying_causes_acronyms["hepatocyte_lesion"] = "Hepatocyte lesion"

# Dictionary of underlying causes 
underlying_causes = dict()
underlying_causes["hemolysis"] = []
underlying_causes["cholestasis"] = []
underlying_causes["cirrhosis"] = []
underlying_causes["heposemia"] = []
underlying_causes["hepatitis"] = []
underlying_causes["carcinoma of the pancreas"] = []
underlying_causes["genetic_disease"] = []
underlying_causes["hepatic_defect"] = []
underlying_causes["necrosis"] = []
underlying_causes["inflammation"] = []
underlying_causes["chronic"] = []
underlying_causes["hepatocyte_lesion"] = []

# Dictionary of symptoms
symptoms = dict()

# Dictionary of risk factors 
factors = dict() 

# Dictionary of tests 
tests = dict()


# Welcome message 
print("\nHi! I am an elementary version of a mini Turing machine for jaundice diagnosis. I am going to help out find you the underlying causes of your jaundice. Please answer the questions to the best of your knowledge. Press \"okay\" to pass from one question to the other\n")

# General information 
name = input("\nPlease input your name:\n")
email = input("\nPlease input your email:\n")
gender = input("\nPlease input your gender (male/female):\n")



# Symptoms 
print("\nFor the following symptoms, please type T/True/true if you have that symptom and F/False/false otherwise\n")
for symp in symp_acronyms.keys(): 
    symptoms[symp] = str2bool(input(symp_acronyms[symp]))

# Risk factos
print("\nFor the following risk factors, please type T/True/true if they apply to you and F/False/false otherwise\n")
for fact in fact_acronyms.keys(): 
    factors[fact] = str2bool(input(fact_acronyms[fact]))

# Tests 
tests['urine'] = str2bool(input(test_acronyms["urine"]))
print("\nFor the following tests, please type T/True/true, F/False/false, or with a number as indicated in your test results\n")
if tests['urine']: 
    tests['choluria'] = str2bool(input(test_acronyms["choluria"]))

tests['blood'] = str2bool(input(test_acronyms["blood"]))
print("\nFor the following tests, please type T/True/true, F/False/false, or with a number as indicated in your test results\n")
if tests['blood']: 
    tests['bilirubin'] = read_float(test_acronyms["bilirubin"])
    tests['bilirubin_c'] = read_float(test_acronyms["bilirubin_c"])
    tests['bilirubin_u'] = read_float(test_acronyms["bilirubin_u"])
    tests['anemia'] = read_float(test_acronyms["anemia"])
    tests['ast'] = read_float(test_acronyms["ast"])
    tests['alt'] = read_float(test_acronyms["alt"])
    tests['proth'] = read_float(test_acronyms["proth"])
    tests['alk'] = read_float(test_acronyms["alk"])
    tests['gamma'] = read_float(test_acronyms["gamma"])
    tests['K'] = read_float(test_acronyms["K"])


tests['murphy'] = str2bool(input(test_acronyms["murphy"]))
print("\nFor the following tests, please type T/True/true, F/False/false, or with a number as indicated in your test results\n")
if tests['murphy']: 
    tests['murphy_result'] = str2bool(input(test_acronyms["murphy_result"]))

# test_acronyms["murphy"] = "Have you taken a murphy's sign test?\n"
# test_acronyms["murphy_result"] = "Was the result for the myphy's sign test positive?\n"

# Diagnosis: 
## Symptoms 
## https://www.medscape.com/answers/185856-109710/what-are-the-treatment-options-for-mild-pruritus-in-cirrhosis#:~:text=Pruritus%20is%20a%20common%20complaint,to%20be%20the%20culprit%20pruritogen.
if symptoms["pruritus"] == 1: 
    underlying_causes["chronic"].append(symp_acronyms["pruritus"])
    underlying_causes["cholestasis"].append(symp_acronyms["pruritus"])

if symptoms["anorexia"] == 1: 
    underlying_causes["hepatitis"].append(symp_acronyms["anorexia"])
    underlying_causes["cholestasis"].append(symp_acronyms["anorexia"])

if symptoms["anorexia_1"] == 1: 
    underlying_causes["chronic"].append(symp_acronyms["anorexia_1"])

if symptoms["fever"] == 1: 
    underlying_causes["hepatitis"].append(symp_acronyms["fever"])
    underlying_causes["cholestasis"].append(symp_acronyms["fever"])

if (symptoms["soft_liver_edge"] == 1) and (symptoms["liver_edge_extension"] == 1) and (symptoms["painful_liver"] == 1):
    underlying_causes['inflammation'].append([symp_acronyms["soft_liver_edge"], symp_acronyms["liver_edge_extension"], symp_acronyms["painful_liver"]])

if (symptoms["firm_liver"] == 1) and (symptoms["nodular_liver"] == 1) and (symptoms["painful_liver"] == 0):
    underlying_causes['inflammation'].append([symp_acronyms["firm_liver"], symp_acronyms["nodular_liver"], "Not " + symp_acronyms["painful_liver"]])


## Risk factors 
if factors["alcohol"] == 1: 
    underlying_causes["hepatitis"].append(fact_acronyms["alcohol"])

if factors["chronic_hyperbilirubinemic_conditions"] == 1: 
    underlying_causes["genetic_disease"].append(fact_acronyms["chronic_hyperbilirubinemic_conditions"])

if factors["autoimmune_disease"] == 1: 
    underlying_causes["cholestasis"].append(fact_acronyms["autoimmune_disease"])

if factors["tattoo"] == 1: 
    underlying_causes["hepatitis"].append(fact_acronyms["tattoo"])

if factors["sex"] == 1: 
    underlying_causes["hepatitis"].append(fact_acronyms["sex"])

if factors["hepatitis"] == 1: 
    underlying_causes["hepatitis"].append(fact_acronyms["hepatitis"])

if factors["fava"] == 1: 
    underlying_causes["hemolysis"].append(fact_acronyms["fava"])


# tests 
if tests['choluria'] == 1: 
    underlying_causes["cholestasis"].append(test_acronyms["choluria"])

if tests['bilirubin_u'] <= 0.2 or tests['bilirubin_u'] >= 0.8: 
    underlying_causes["cirrhosis"].append("Unconjugated componenet of bilirubin outside normal range [0.2 mg/dl : 0.8 mg/dl]")

if tests['bilirubin_u'] >= 0.8 and tests['bilirubin_c'] >= 0.2: 
    underlying_causes["hepatocyte_lesion"].append("Excess in both unconjugated (>0.8) and conjugated (>0.2) bilirubin")

if gender == "male" and tests['anemia'] <= 14: 
    underlying_causes["hemolysis"].append("anemia for male diagnosed by hemoglobin values less than 14 g/dl")

if gender == "female" and tests['anemia'] <= 12: 
    underlying_causes["hemolysis"].append("anemia for femal diagnosed by hemoglobin values less than 12 g/dl")

if tests["proth"] <= 70:
    underlying_causes["cirrhosis"].append("Decreased " + test_acronyms["proth"])
    underlying_causes["hepatitis"].append("Decreased " + test_acronyms["proth"])

if tests["proth"] >= 80:
    underlying_causes["cirrhosis"].append("Increased " + test_acronyms["proth"] + " with normal AK level")
    underlying_causes["hepatitis"].append("Increased " + test_acronyms["proth"] + " with normal AK level")

if tests["alk"] >= 130 and tests["gamma"] >= 49:
    underlying_causes["cirrhosis"].append("Simultaneous increase in alkaline phosphatase (AF > 130 U/L) and Gamma-glutamyl transferase (GammaGT > 49 U/L)")

if (tests["alt"] >= tests["ast"]) and (not factors["alcohol"]): 
    underlying_causes["hepatitis"].append("ALT level > AST level for non-alchoholic patient")

if tests['ast'] >= 40 and tests['K'] <= 3.2 and tests['K'] >= 0.2: 
    underlying_causes["hepatocye_lesion"].append("Increase in " + test_acronyms["AST"] + "with normal level of vitamin K")
 
if tests['alt'] >= 35:
    underlying_causes["hepatitis"].append("Increased " + test_acronyms["alt"])
    underlying_causes["hepatocyte_lesion"].append("Increased " + test_acronyms["alt"])
    underlying_causes["cholestasis"].append("Increased " + test_acronyms["alt"])
    underlying_causes["cirrhosis"].append("Increased " + test_acronyms["alt"])

if tests['murphy_result']: 
    underlying_causes["hemolysis"].append(test_acronyms["murphy_result"])


## Diagnois 
print("\n\n\n\nThank you for answering the questions %s! I have ordered the possible underlying causes of your jaundice below. They are ordered by likelihood (first one is most likely).\n" % (name))
diagnosis = ''
for uc in sorted(underlying_causes, key=lambda uc: len(underlying_causes[uc]), reverse=True): 
    diagnosis += "\n"
    if len(underlying_causes[uc]) > 0:
        diagnosis += "\nOne possible underlying cause is %s.\nI considered this underlying cause for the reasons below:" % underlying_causes_acronyms[uc]
        for uc_symps in underlying_causes[uc]:
            if isinstance(uc_symps, list): 
                diagnosis += "\n\t -"
                for uc_symp in uc_symps: 
                    diagnosis += "%s; " % uc_symps
            else: 
                diagnosis += "\n\t - %s" % uc_symps
print(diagnosis)




## email lock yu 
## add nlp 
## build gui 
## write summary for paper 
## clear data for wei liang 
## explain why causal models don't work using identifiablity conditions 
## do the survey for EP 
## read paper and get back to wei liang