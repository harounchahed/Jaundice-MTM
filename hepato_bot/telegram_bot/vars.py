import pandas as pd 
import numpy as np 
# from tkinter import *

class User:
    def __init__(self):
        self.name = None
        self.age = None
        self.sex = None
        # Dictionary of symptoms
        self.symptoms = dict()

        # Dictionary of risk factors 
        self.factors = dict() 

        # Dictionary of tests 
        self.tests = dict()

        # Dictionary of underlying causes 
        self.underlying_causes = dict()
        self.underlying_causes["hemolysis"] = []
        self.underlying_causes["cholestasis"] = []
        self.underlying_causes["cirrhosis"] = []
        self.underlying_causes["heposemia"] = []
        self.underlying_causes["hepatitis"] = []
        self.underlying_causes["carcinoma of the pancreas"] = []
        self.underlying_causes["genetic_disease"] = []
        self.underlying_causes["hepatic_defect"] = []
        self.underlying_causes["necrosis"] = []
        self.underlying_causes["inflammation"] = []
        self.underlying_causes["chronic"] = []
        self.underlying_causes["hepatocyte_lesion"] = []

    def diagnose(self, symp_acronyms, fact_acronyms, test_acronyms): 
        if self.symptoms["pruritus"]:
            self.underlying_causes["chronic"].append(symp_acronyms["pruritus"])
            self.underlying_causes["cholestasis"].append(symp_acronyms["pruritus"])

        if self.symptoms["anorexia"]: 
            self.underlying_causes["hepatitis"].append(symp_acronyms["anorexia"])
            self.underlying_causes["cholestasis"].append(symp_acronyms["anorexia"])

        if self.symptoms["anorexia_1"]: 
            self.underlying_causes["chronic"].append(symp_acronyms["anorexia_1"])

        if self.symptoms["fever"]: 
            self.underlying_causes["hepatitis"].append(symp_acronyms["fever"])
            self.underlying_causes["cholestasis"].append(symp_acronyms["fever"])

        if (self.symptoms["soft_liver_edge"]) and (self.symptoms["liver_edge_extension"]) and (self.symptoms["painful_liver"]):
            self.underlying_causes['inflammation'].append([symp_acronyms["soft_liver_edge"], symp_acronyms["liver_edge_extension"], symp_acronyms["painful_liver"]])

        if (self.symptoms["firm_liver"]) and (self.symptoms["nodular_liver"]) and not (self.symptoms["painful_liver"]):
            self.underlying_causes['inflammation'].append([symp_acronyms["firm_liver"], symp_acronyms["nodular_liver"], "Not " + symp_acronyms["painful_liver"]])

        print("underlyinc causes: after symptoms", self.underlying_causes)

        ## Risk factors 
        if self.factors["alcohol"]: 
            self.underlying_causes["hepatitis"].append(fact_acronyms["alcohol"])

        if self.factors["chronic_hyperbilirubinemic_conditions"]: 
            self.underlying_causes["genetic_disease"].append(fact_acronyms["chronic_hyperbilirubinemic_conditions"])

        if self.factors["autoimmune_disease"]: 
            self.underlying_causes["cholestasis"].append(fact_acronyms["autoimmune_disease"])

        if self.factors["tattoo"]: 
            self.underlying_causes["hepatitis"].append(fact_acronyms["tattoo"])

        if self.factors["sex"]: 
            self.underlying_causes["hepatitis"].append(fact_acronyms["sex"])

        if self.factors["hepatitis"]: 
            self.underlying_causes["hepatitis"].append(fact_acronyms["hepatitis"])

        if self.factors["fava"]: 
            self.underlying_causes["hemolysis"].append(fact_acronyms["fava"])

        print("underlyinc causes: after risks", self.underlying_causes)

        # tests 
        if self.tests['urine']:
            if self.tests['choluria']: 
                self.underlying_causes["cholestasis"].append(test_acronyms["choluria"])

        if self.tests['blood']:
            if self.tests['bilirubin_u'] <= 0.2 or self.tests['bilirubin_u'] >= 0.8: 
                self.underlying_causes["cirrhosis"].append("Unconjugated componenet of bilirubin outside normal range [0.2 mg/dl : 0.8 mg/dl]")

        if self.tests['blood']:
            if self.tests['bilirubin_u'] >= 0.8 and self.tests['bilirubin_c'] >= 0.2: 
                self.underlying_causes["hepatocyte_lesion"].append("Excess in both unconjugated (>0.8) and conjugated (>0.2) bilirubin")

        if self.tests['blood']:
            if self.sex == "male" and self.tests['anemia'] <= 14: 
                self.underlying_causes["hemolysis"].append("anemia for male diagnosed by hemoglobin values less than 14 g/dl")

        if self.tests['blood']:
            if self.sex == "female" and self.tests['anemia'] <= 12: 
                self.underlying_causes["hemolysis"].append("anemia for femal diagnosed by hemoglobin values less than 12 g/dl")

        if self.tests['blood']:
            if self.tests["proth"] <= 70:
                self.underlying_causes["cirrhosis"].append("Decreased " + test_acronyms["proth"])
                self.underlying_causes["hepatitis"].append("Decreased " + test_acronyms["proth"])

        if self.tests['blood']:
            if self.tests["proth"] >= 80:
                self.underlying_causes["cirrhosis"].append("Increased " + test_acronyms["proth"] + " with normal AK level")
                self.underlying_causes["hepatitis"].append("Increased " + test_acronyms["proth"] + " with normal AK level")

        if self.tests['blood']:
            if self.tests["alk"] >= 130 and self.tests["gamma"] >= 49:
                self.underlying_causes["cirrhosis"].append("Simultaneous increase in alkaline phosphatase (AF > 130 U/L) and Gamma-glutamyl transferase (GammaGT > 49 U/L)")

        if self.tests['blood']:
            if (self.tests["alt"] >= self.tests["ast"]) and (not self.factors["alcohol"]): 
                self.underlying_causes["hepatitis"].append("ALT level > AST level for non-alchoholic patient")

        if self.tests['blood']:
            if self.tests['ast'] >= 40 and self.tests['K'] <= 3.2 and self.tests['K'] >= 0.2: 
                self.underlying_causes["hepatocye_lesion"].append("Increase in " + test_acronyms["AST"] + "with normal level of vitamin K")

        if self.tests['blood']:    
            if self.tests['alt'] >= 35:
                self.underlying_causes["hepatitis"].append("Increased " + test_acronyms["alt"])
                self.underlying_causes["hepatocyte_lesion"].append("Increased " + test_acronyms["alt"])
                self.underlying_causes["cholestasis"].append("Increased " + test_acronyms["alt"])
                self.underlying_causes["cirrhosis"].append("Increased " + test_acronyms["alt"])

        if self.tests['murphy']:
            if self.tests['murphy_result']: 
                self.underlying_causes["hemolysis"].append(test_acronyms["murphy_result"])

        print("underlyinc causes: after tests", self.underlying_causes)
        ## Diagnois 
        # print("\n\n\n\nThank you for answering the questions %s! I have ordered the possible underlying causes of your jaundice below. They are ordered by likelihood (first one is most likely).\n" % (name))
        diagnosis = "Thank you for answering the questions %s! I have ordered the possible underlying causes of your jaundice below. They are ordered by likelihood (first one is most likely)." % self.name
        rank = 0
        for uc in sorted(self.underlying_causes, key=lambda uc: len(self.underlying_causes[uc]), reverse=True): 
            rank += 1 
            diagnosis += "\n"
            if len(self.underlying_causes[uc]) > 0:
                diagnosis += "\n%d. One possible underlying cause is %s.\nI considered this underlying cause for the reasons below:" % (rank, underlying_causes_acronyms[uc])
                for uc_symps in self.underlying_causes[uc]:
                    if isinstance(uc_symps, list): 
                        diagnosis += "\n -"
                        for uc_symp in uc_symps: 
                            diagnosis += "%s - " % uc_symp
                    else: 
                        diagnosis += "\n - %s" % uc_symps
        # print(diagnosis)
        return diagnosis

## email lock yu 
## add nlp 
## build gui 
## write summary for paper 
## clear data for wei liang 
## explain why causal models don't work using identifiablity conditions 
## do the survey for EP 
## read paper and get back to wei liang

def str2bool(v):
   return str(v).lower() in ("yes", "true", "correct", "t", "1", "yeah", "yea", "y")

def isDigit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def read_float(text): 
    result = input(text)
    if not text.is_digit(result): 
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
symp_acronyms["pruritus"] = "Pruritus: sever itching of the skin"
symp_acronyms["anorexia"] = "Anorexia (eating disorder), weight loss, or nausea within 2 weeks prior to the onset of jaundice"
symp_acronyms["anorexia_1"] = "Anorexia (eating disorder), weight loss, or nausea within more than 2 weeks prior to the onset of jaundice"
symp_acronyms["fever"] = "Fever"
symp_acronyms["soft_liver_edge"] = "Soft liver edge"
symp_acronyms["liver_edge_extension"] = "Liver edge extension"
symp_acronyms["painful_liver"] = "Painful liver"
symp_acronyms["firm_liver"] = "Firm liver"
symp_acronyms["nodular_liver"] = "Nodular liver"
symp_acronyms["acholia"] = "Lack or absence of bile secretion (lack of the normal brown color in feces or pale feces)"

fact_acronyms = dict() 
fact_acronyms["alcohol"] = "Alcohol intake of more than 2 servings per day on average"
fact_acronyms["chronic_hyperbilirubinemic_conditions"] = "Family history of chronic hyperbilirubinemic conditions"
fact_acronyms["autoimmune_disease"] = "Family history of autoimmune disease or inflammatory bowel disease"
fact_acronyms["tattoo"] = "Exposure to needles (e.g. tattoo)"
fact_acronyms["sex"] = "History of unprotected sexual contact"
fact_acronyms["unsanitary_invironment"] = "Exposure to unsanitary environment"
fact_acronyms["hepatitis"] = "Contact with Hepatitis"
fact_acronyms["surgery"] = "Surgical history"
fact_acronyms["fava"] = "Eating fava beans"

test_acronyms = dict()
# int 
test_acronyms["bilirubin"] = "Level of biliribin as indicated in urine test results in mg/dl"
test_acronyms["bilirubin_c"] = "Level of conjugated biliribin as indicated in urine test results in mg/dl"
test_acronyms["bilirubin_u"] = "Level of unconjugated biliribin as indicated in urine test results in mg/dl"
test_acronyms["anemia"] = "Level of hemoglobin as indicated in blood test results in g/dl"
test_acronyms["ast"] = "Aspartate aminotransferase level (AST - marker of liver damage but also present in the myocardium and muscle) as indicated in blood test results in U/L" # normal 15-40U/L
test_acronyms["alt"] = "Alanine aminotransferase level (AST - marker of liver damage) as indicated in blood test results in U/L" # normal 5-35U/L
test_acronyms["proth"] = "Prothrombin activity (vitam K factor) as indicated in blood test results in %" # normal 70-80%
test_acronyms["alk"] = "Alkaline phosphatase level as indicated in blood test results in %" # normal 40-130 
test_acronyms["gamma"] = "Gamma-glutamyl transferase level as indicated in blood test results in %" # normal 10-49
test_acronyms["K"] = "Vitamin K level as indicated in blood test results in ng/mL" # normal 0.2-3.2 ng/mL


# bool 
test_acronyms["urine"] = "Have you taken a urine test?"
test_acronyms["blood"] = "Have you taken a blood test and have the complete blood count results?"
test_acronyms["choluria"] = "Presence of bile in urine (Choluria) as indicated in urine test results"
test_acronyms["murphy"] = "Have you taken a murphy's sign test?"
test_acronyms["murphy_result"] = "A positive murphy's sign test"




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



# # Welcome message 
# print("\nHi! I am an elementary version of a mini Turing machine for jaundice diagnosis. I am going to help out find you the underlying causes of your jaundice. Please answer the questions to the best of your knowledge. Press \"okay\" to pass from one question to the other\n")

# # General information 
# name = input("\nPlease input your name:\n")
# email = input("\nPlease input your email:\n")
# gender = input("\nPlease input your gender (male/female):\n")

## email lock yu 
## add nlp 
## build gui 
## write summary for paper 
## clear data for wei liang 
## explain why causal models don't work using identifiablity conditions 
## do the survey for EP 
## read paper and get back to wei liang
