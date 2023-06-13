
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
import speech_recognition as sr
import pyaudio
import wave
from joblib import load
model = load('./SavedModel/model.joblib')
# Create your views here.
def home(request):
    return render(request,'home.html',{'home_link':'http://127.0.0.1:8000/'})
def predict_disease(request):
    if request.method == "post":
        itching = request.POST['itching']
        skin_rash = request.POST['skin_rash']
        nodal_skin_eruptions = request.POST['nodal_skin_eruptions']
        continuous_sneezing = request.POST['continuous_sneezing']
        shivering = request.POST['shivering']
        chills = request.POST['chills']
        joint_pain = request.POST['joint_pain']
        stomach_pain = request.POST['stomach_pain']
        acidity = request.POST['acidity']
        ulcers_on_tongue = request.POST['ulcers_on_tongue']
        muscle_wasting = request.POST['muscle_wasting']
        vomiting = request.POST['vomiting']
        burning_micturition = request.POST['burning_micturition']
        spotting_urination = request.POST['spotting_urination']
        fatigue = request.POST['fatigue']
        weight_gain = request.POST['weight_gain']
        anxiety = request.POST['anxiety']
        cold_hands_and_feet = request.POST['cold_hands_and_feet']
        mood_swings = request.POST['mood_swings']
        weight_loss = request.POST['weight_loss']
        restlessness = request.POST['restlessness']
        lethargy = request.POST['lethargy']
        patches_in_throat = request.POST['patches_in_throat']
        irregular_sugar_level = request.POST['irregular_sugar_level']
        cough = request.POST['cough']
        high_fever = request.POST['high_fever']
        sunken_eyes = request.POST['sunken_eyes']
        breathlessness = request.POST['breathlessness']
        sweating = request.POST['sweating']
        dehydration = request.POST['dehydration']
        indigestion = request.POST['indigestion']
        headache = request.POST['headache']
        yellowish_skin = request.POST['yellowish_skin']
        dark_urine = request.POST['dark_urine']
        nausea = request.POST['nausea']
        loss_of_appetite = request.POST['loss_of_appetite']
        pain_behind_the_eyes = request.POST['pain_behind_the_eyes']
        back_pain = request.POST['back_pain']
        constipation = request.POST['constipation']
        abdominal_pain = request.POST['abdominal_pain']
        diarrhoea = request.POST['diarrhoea']
        mild_fever = request.POST['mild_fever']
        yellow_urine = request.POST['yellow_urine']
        yellowing_of_eyes = request.POST['yellowing_of_eyes']
        acute_liver_failure = request.POST['acute_liver_failure']
        fluid_overload = request.POST['fluid_overload']
        swelling_of_stomach = request.POST['swelling_of_stomach']
        swelled_lymph_nodes = request.POST['swelled_lymph_nodes']
        malaise = request.POST['malaise']
        blurred_and_distorted_vision = request.POST['blurred_and_distorted_vision']
        phlegm = request.POST['phlegm']
        throat_irritation = request.POST['throat_irritation']
        redness_of_eyes = request.POST['redness_of_eyes']
        sinus_pressure = request.POST['sinus_pressure']
        runny_nose = request.POST['runny_nose']
        congestion = request.POST['congestion']
        chest_pain = request.POST['chest_pain']
        weakness_in_limbs = request.POST['weakness_in_limbs']
        fast_heart_rate = request.POST['fast_heart_rate']
        pain_during_bowel_movements = request.POST['pain_during_bowel_movements']
        pain_in_anal_region = request.POST['pain_in_anal_region']
        bloody_stool = request.POST['bloody_stool']
        irritation_in_anus = request.POST['irritation_in_anus']
        neck_pain = request.POST['neck_pain']
        dizziness = request.POST['dizziness']
        cramps = request.POST['cramps']
        bruising = request.POST['bruising']
        obesity = request.POST['obesity']
        swollen_legs = request.POST['swollen_legs']
        swollen_blood_vessels = request.POST['swollen_blood_vessels']
        puffy_face_and_eyes = request.POST['puffy_face_and_eyes']
        enlarged_thyroid = request.POST['enlarged_thyroid']
        brittle_nails = request.POST['brittle_nails']
        swollen_extremeties = request.POST['swollen_extremeties']
        excessive_hunger = request.POST['excessive_hunger']
        extra_marital_contacts = request.POST['extra_marital_contacts']
        drying_and_tingling_lips = request.POST['drying_and_tingling_lips']
        slurred_speech = request.POST['slurred_speech']
        knee_pain = request.POST['knee_pain']
        hip_joint_pain = request.POST['hip_joint_pain']
        muscle_weakness = request.POST['muscle_weakness']
        stiff_neck = request.POST['stiff_neck']
        swelling_joints = request.POST['swelling_joints']
        movement_stiffness = request.POST['movement_stiffness']
        spinning_movements = request.POST['spinning_movements']
        loss_of_balance = request.POST['loss_of_balance']
        unsteadiness = request.POST['unsteadiness']
        weakness_of_one_body_side = request.POST['weakness_of_one_body_side']
        loss_of_smell = request.POST['loss_of_smell']
        bladder_discomfort = request.POST['bladder_discomfort']
        foul_smell_of_urine = request.POST['foul_smell_of_urine']
        continuous_feel_of_urine = request.POST['continuous_feel_of_urine']
        passage_of_gases = request.POST['passage_of_gases']
        internal_itching = request.POST['internal_itching']
        toxic_look = request.POST['toxic_look']
        depression = request.POST['depression']
        irritability = request.POST['irritability']
        muscle_pain = request.POST['muscle_pain']
        altered_sensorium = request.POST['altered_sensorium']
        red_spots_over_body = request.POST['red_spots_over_body']
        belly_pain = request.POST['belly_pain']
        abnormal_menstruation = request.POST['abnormal_menstruation']
        dischromic_patches = request.POST['dischromic_patches']
        watering_from_eyes = request.POST['watering_from_eyes']
        increased_appetite = request.POST['increased_appetite']
        polyuria = request.POST['polyuria']
        family_history = request.POST['family_history']
        mucoid_sputum = request.POST['mucoid_sputum']
        rusty_sputum = request.POST['rusty_sputum']
        lack_of_concentration = request.POST['lack_of_concentration']
        visual_disturbances = request.POST['visual_disturbances']
        receiving_blood_transfusion = request.POST['receiving_blood_transfusion']
        receiving_unsterile_injections = request.POST['receiving_unsterile_injections']
        coma = request.POST['coma']
        stomach_bleeding = request.POST['stomach_bleeding']
        distention_of_abdomen = request.POST['distention_of_abdomen']
        history_of_alcohol_consumption = request.POST['history_of_alcohol_consumption']
        fluid_overload = request.POST['fluid_overload']
        blood_in_sputum = request.POST['blood_in_sputum']
        prominent_veins_on_calf = request.POST['prominent_veins_on_calf']
        palpitations = request.POST['palpitations']
        painful_walking = request.POST['painful_walking']
        pus_filled_pimples = request.POST['pus_filled_pimples']
        blackheads = request.POST['blackheads']
        scurring = request.POST['scurring']
        skin_peeling = request.POST['skin_peeling']
        silver_like_dusting = request.POST['silver_like_dusting']
        small_dents_in_nails = request.POST['small_dents_in_nails']
        inflammatory_nails = request.POST['inflammatory_nails']
        blister = request.POST['blister']
        red_sore_around_nose = request.POST['red_sore_around_nose']
        yellow_crust_ooze = request.POST['yellow_crust_ooze']
        y_pred = model.predict([[itching, skin_rash, nodal_skin_eruptions,continuous_sneezing,shivering,chills ,joint_pain,stomach_pain,
        acidity,ulcers_on_tongue,muscle_wasting,vomiting,burning_micturition,spotting_urination,fatigue,
        weight_gain,anxiety,cold_hands_and_feet,mood_swings,weight_loss,restlessness,lethargy,
        patches_in_throat,irregular_sugar_level,cough,high_fever,sunken_eyes,breathlessness,sweating,
        dehydration,indigestion,headache,yellowish_skin,dark_urine,nausea,loss_of_appetite,pain_behind_the_eyes,
        back_pain,constipation,abdominal_pain,diarrhoea,mild_fever,yellow_urine,yellowing_of_eyes,
        acute_liver_failure,fluid_overload,swelling_of_stomach,swelled_lymph_nodes,malaise,
        blurred_and_distorted_vision,phlegm,throat_irritation,redness_of_eyes,sinus_pressure,runny_nose,
        congestion,chest_pain,weakness_in_limbs,fast_heart_rate,pain_during_bowel_movements,pain_in_anal_region,
        bloody_stool,irritation_in_anus,neck_pain,dizziness,cramps,bruising,obesity,swollen_legs,
        swollen_blood_vessels,puffy_face_and_eyes,enlarged_thyroid,brittle_nails,swollen_extremeties,
        excessive_hunger,extra_marital_contacts,drying_and_tingling_lips,slurred_speech,knee_pain,hip_joint_pain,
        muscle_weakness,stiff_neck,swelling_joints,movement_stiffness,spinning_movements,loss_of_balance,
        unsteadiness,weakness_of_one_body_side,loss_of_smell,bladder_discomfort,foul_smell_of_urine,
        continuous_feel_of_urine,passage_of_gases,internal_itching,toxic_look,depression,irritability,
        muscle_pain,altered_sensorium,red_spots_over_body,belly_pain,abnormal_menstruation,dischromic_patches,
        watering_from_eyes,increased_appetite,polyuria,family_history,mucoid_sputum,rusty_sputum,
        lack_of_concentration,visual_disturbances,receiving_blood_transfusion,receiving_unsterile_injections,
        coma,stomach_bleeding,distention_of_abdomen,history_of_alcohol_consumption,fluid_overload,blood_in_sputum,
        prominent_veins_on_calf,palpitations,painful_walking,pus_filled_pimples,blackheads,scurring,skin_peeling,
        silver_like_dusting,small_dents_in_nails,inflammatory_nails,blister,red_sore_around_nose,
        yellow_crust_ooze]])
        print(y_pred)
        return render(request,'predict_disease.html', {'result': y_pred})
    return render(request,'predict_disease.html')

def predict_symptoms(request):
    user_input = request.POST.get('name')
    print(user_input)
    disease_symptoms = {
   # "disease1": ["symptom1", "symptom2", "symptom3"],
   # "disease2": ["symptom4", "symptom5", "symptom6"],
    "fungal infection":["itching", "skin_rash", "nodal_skin_eruptions","dischromic_patches"],
    "allergy":["continuous_sneezing", "shivering", "chills","watering_from_eyes"],
    "gerd":["stomach_pain", "acidity", "ulcers_on_tongue","vomiting","cough","chest_pain"],
    "chronic cholestasis":["vomiting", "yellowish_skin", "nausea","loss_of_appetite","abdominal_pain","yellowing_of_eyes"],
    "drug Reaction":["itching", "skin_rash", "stomach_pain","burning_micturition","spotting_urination"],
    "peptic ulcer disease":["vomiting", "loss_of_appetite", "abdominal_pain","passage_of_gases","internal_itching"],
    "aids":["muscle_wasting", "patches_in_throat", "extra_marital_contacts"],
    "diabetes":["fatigue", "weight_loss", "restlessness","lethargy","irregular_sugar_level","blurred_and_distorted_vision","obesity","excessive_hunger","increased_appetite","polyuria"],
    "gastroenteritis":["vomiting", "sunken_eyes", "dehydration","diarrhoea"],
    "asthma":["cough", "high_fever", "breathlessness","family_history","mucoid_sputum"],
    "hypertension":["headache", "chest_pain", "dizziness","loss_of_balance","lack_of_concentration"],
    "migraine":["acidity", "indigestion", "blurred_and_distorted_vision","excessive_hunger","stiff_neck","depression","irritability","visual_disturbances"],
    "cervical spondylosis":["back_pain", "weakness_in_limbs", "neck_pain","dizziness","loss_of_balance"],
    "paralysis for brain hemorrhage":["vomiting", "headache", "altered_sensorium"],
    "jaundice":["itching", "vomiting", "fatigue","weight_loss","high_fever","yellowish_skin","dark_urine","abdominal_pain"],
    "malaria":["chills", "vomiting", "high_fever","sweating","headache","nausea","diarrhoea","muscle_pain"],
    "chicken pox":["itching", "fatigue", "lethargy","high_fever","headache","loss_of_appetite","mild_fever","swelled_lymph_nodes","malaise","red_spots_over_body"],
    "dengue":["skin_rash", "chills", "joint_pain","vomiting","fatigue","high_fever","headache","nausea","loss_of_appetite","pain_behind_the_eyes","back_pain","muscle_pain","red_spots_over_body"],
    "typhoid":["chills", "vomiting", "fatigue","high_fever","headache","nausea","abdominal_pain","diarrhoea","toxic_look_(typhos)","belly_pain"],
    "hepatitis A":["joint_pain", "vomiting", "yellowish_skin","dark_urine","nausea","loss_of_appetite","abdominal_pain","diarrhoea","mild_fever","yellowing_of_eyes","muscle_pain"],
    "hepatitis B":["itching", "lethargy", "yellowish_skin","dark_urine","loss_of_appetite","abdominal_pain","yellow_urine","yellowing_of_eyes","malaise","receiving_blood_transfusion","receiving_unsterile_injections"],
    "hepatitis C":["fatigue", "yellowish_skin", "nausea","yellowing_of_eyes","family_history"],
    "hepatitis D":["vomiting", "fatigue", "yellowish_skin","dark_urine","nausea","loss_of_appetite","abdominal_pain","yellowing_of_eyes"],
    "hepatitis E":["joint_pain", "vomiting", "high_fever","yellowish_skin","dark_urine","nausea","loss_of_appetite","abdominal_pain","yellowing_of_eyes","acute_liver_failure","coma","stomach_bleeding"],
    "alcoholic hepatitis":["vomiting", "abdominal_pain", "swelling_of_stomach","distention_of_abdomen","history_of_alcohol_consumption","fluid_overload"],
    "tuberculosis":["vomiting", "fatigue", "weight_loss","cough","high_fever","breathlessness","sweating","loss_of_appetite","mild_fever","yellowing_of_eyes","swelled_lymph_nodes","malaise","phlegm","chest_pain","blood_in_sputum"],
    "common cold":["continuous_sneezing", "chills", "fatigue","cough","high_fever","headache","swelled_lymph_nodes","malaise","phlegm","throat_irritation","redness_of_eyes","sinus_pressure","runny_nose","congestion","chest_pain","loss_of_smell","muscle_pain"],
    "pneumonia":["chills", "fatigue", "cough","high_fever","breathlessness","sweating","malaise","phlegm","chest_pain","fast_heart_rate","rusty_sputum"],
    "dimorphic hemmorhoids":["constipation", "pain_during_bowel_movements", "pain_in_anal_region","bloody_stool","irritation_in_anus"],
    "heart attack":["vomiting", "sweating", "chest_pain","breathlessness"],
    "varicose veins":["fatigue", "cramps", "bruising","obesity","swollen_legs","swollen_blood_vessels","prominent_veins_on_calf"],
    "hypothyroidism":["weight_gain", "cold_hands_and_feets", "mood_swings","lethargy","dizziness","puffy_face_and_eyes","enlarged_thyroid","brittle_nails","swollen_extremeties","depression","irritability","abnormal_menstruation"],
    "hyperthyroidism":["mood_swings", "weight_loss", "restlessness","sweating","diarrhoea","fast_heart_rate","excessive_hunger","muscle_weakness","irritability","abnormal_menstruation"],
    "hypoglycemia":["vomiting", "fatigue", "anxiety","sweating","headache","nausea","blurred_and_distorted_vision","excessive_hunger","slurred_speech","irritability","palpitations"],
    "osteoarthristis":["joint_pain", "neck_pain", "knee_pain","hip_joint_pain","swelling_joints","painful_walking"],
    "arthritis":["muscle_weakness", "stiff_neck", "swelling_joints","movement_stiffness","painful_walking"],
    "paroxysmal  positional vertigo":["vomiting", "headache", "nausea","spinning_movements","loss_of_balance","unsteadiness"],
    "acne":["skin_rash", "pus_filled_pimples", "blackheads","scurring"],
    "urinary tract infection":["burning_micturition", "bladder_discomfort", "foul_smell_of_urine","continuous_feel_of_urine"],
    "psoriasis":["skin_rash", "joint_pain", "skin_peeling","silver_like_dusting","small_dents_in_nails","inflammatory_nails"],
    "impetigo":["skin_rash", "high_fever", "blister","red_sore_around_nose","yellow_crust_ooze"],
    "abdominal aortic aneurysm":[" pulsating feeling in your stomach", "back pain", "abdominal pain","rapid heartbeat (tachycardia)","dizziness","sweaty and clammy skin","shortness of breath","loss of consciousness"],
    "acute cholecystitis":["a high temperature (fever)", "vomiting", "vomiting","sweating","loss of appetite","yellowing of the skin"],
    "acute lymphoblastic leukaemia":["lethargic", "anaemia", "lack of red blood cells","aches and pains","swollen lymph glands"],
    "acute myeloid leukaemia":["pale skin", "tiredness", "breathlessness","a high temperature (fever)","excessive sweating","weight loss","frequent infections"," unusual bleeding gums or nosebleeds","easily bruised skin","bone and joint pain","vomiting"],
    "acute pancreatitis":["severe, dull pain around the top of your stomach", "nausea", "diarrhoea","indigestion","a high temperature (fever) of 38C","jaundice","swelling of the abdomen"],
    "addison disease":["fatigue ", "lethargy ", "muscle weakness","low mood","loss of appetite","increased thirst","craving for salty foods","Dehydration"],
    "alzheimer":["forget about recent conversations or events, or misplace items", "repeat themselves regularly, such as asking the same question several times", "become less flexible and more hesitant to try new things"],
    "anal cancer":["itching and pain around the anus", "a discharge of mucus from the anus", "loss of bowel control (bowel incontinence)","small lumps around the anus"],
    "anaphylaxis":["itchy skin", "swollen eyes", "wheezing","swelling of the mouth, throat or tongue","abdominal pain","nausea","vomiting","collapse ","unconsciousness"],
    "ankylosing spondylitis":["Back pain and stiffness", "Arthritis", "Enthesitis","Fatigue"],
    "anorexia nervosa":["fear of ‘being fat’ or gaining weight", "problems with self-esteem and body image when it comes to food and weigh", "restricting food intake and keeping your body weight low, to the point it’s unhealthy"],
    "anxiety":["restlessness", "a sense of dread", "feeling constantly on edge","difficulty concentrating","irritability","dizziness","tiredness","trembling","excessive sweating","shortness of breath","feeling sick"],
    "appendicitis":["feeling sick (nausea)", "being sick", "loss of appetite","diarrhoea","a high temperature (fever)","gastroenteritis","severe irritable bowel syndrome (IBS)","constipation","bladder or urine infections","Crohn's disease","pelvic infection"],
    "bile duct cancer":["yellowing of the skin", "jaundice", "unintentional weight loss ","abdominal pain","high temperature (fever) of 38C","loss of appetite"],
    "bipolar disorder":["Episodes of mania", "depression", "lacking energy","self-doubt","feeling full of energy","not eating"],
    "sepsis":["a high temperature", "chills and shivering", "a fast heartbeat","fast breathing","diarrhoea","vomiting","nausea ","severe breathlessness","feeling dizzy or faint","loss of consciousness","pale or mottled skin"],
    "bone cancer":["Bone pain", "a high temperature (fever) of 38C", "unexplained weight loss","sweating, particularly at night","welling and rednes"],
    "bowel cancer":["blood in the stools", " abdominal(tummy) pain", " change in bowel habit"],
    "brain stem death":["a person must be unconscious and fail to respond to outside stimulation", "a person's heartbeat and breathing can only be maintained using a ventilator"],
    "bronchitis":["your cough is severe or lasts longer than three weeks", "you have a constant fever", "you cough up mucus streaked with blood","you have an underlying heart or lung condition, such as asthma or heart failure"],
    "bulimia":["bingeing – overeating in a particular pattern", "purging", "focus on food","problems with self-esteem"],
    "brain tumours":["severe, persistent headaches", "seizures (fits)", "persistent nausea","vomiting","mental or behavioural changes, such as memory problems","paralysis on one side of the body","vision problems","speech problems"],
    "cerebral palsy":["struggle with movement and balance", "struggle to speak", "have difficulties with eating, drinking and swallowing","experience pain symptoms","have problems with their vision","experience fatigue","have a learning disability","have epilepsy","tightness in joints and muscles"],
    "cervical cancer":["Unusual bleeding", "constipation", "loss of bladder control","bone pain","swelling of one of your legs","loss of appetite","weight loss","tiredness and a lack of energy","hydronephrosis"],
    "chest infection":["a persistent cough", "breathlessness", "wheezing","a high temperature (fever)","a rapid heartbeat","chest pain or tightness","feeling confused and disorientated"],
    "chronic kidney disease":["weight loss and poor appetite", "swollen ankles, feet or hands", "shortness of breath","insomnia","itchy skin","muscle cramps","high blood pressure (hypertension)","nausea"],
    "chronic myeloid leukaemia":["tiredness", "frequent infections", "unexplained weight loss","a feeling of bloating","swollen lymph nodes","severe fatigue","bone pain","night sweats","easily bruised skin"],
    "chronic pancreatitis":["episodes of abdominal (tummy) pain", "digestion problems", "nausea and vomiting","loss of appetite","jaundice","weight loss"],
    "congenital heart disease":["palpitations", "fatigue", "fainting","chest pains","breathing problems","delayed growth"],
    "crohn disease":["recurring diarrhoea", "abdominal pain", "cramping","unintended weight loss","extreme tiredness","feeling sick (nausea)","joint pain and swelling","mouth ulcers"],
    "dementia":["memory loss", "increasing difficulties with tasks", "depression","changes in personality and mood","periods of mental confusion","difficulty finding the right words"],
    "diarrhoea":["a severe or continuous stomach ache", "persistent vomiting", "weight loss","lightheaded or dizzy"],
    "ebola virus disease":["a high temperature (fever)", "a headache", "joint and muscle pain","a sore throat","severe muscle weakness","vomiting","Diarrhoea"],
    "epilepsy":["repeated seizures"],
    "eye cancer":["blurred vision", "shadows, flashes of light", "partial or total loss of vision","a dark patch in your eye that's getting bigger","bulging of one eye","pain in or around your eye","a lump on your eyelid"],
    "gallbladder cancer":["abdominal (stomach) pain", "feeling sick", "jaundice"],
    "gum disease":["red and swollen gums", "bleeding gums after brushing or flossing your teeth", "bad breath (halitosis)","loose teeth that can make eating difficult","gum abscesses (collections of pus that develop under your gums or teeth)"],
    "garyngeal cancer":["a change in the voice", "difficulty or pain when swallowing", "noisy breathing","shortness of breath","a persistent cough","a lump or swelling in your neck"],
    "hay fever":["frequent sneezing", "runny or blocked nose", "itchy, red or watery eyes","an itchy throat, mouth, nose and ears","the loss of your sense of smell (anosmia)","facial pain","tiredness and fatigue"],
    "hodgkin lymphoma":["night sweats", "unintentional weight loss", "a high temperature (fever)","a persistent cough ","breathlessness","persistent itching of the skin all over the body"],
    "huntington disease":["a lack of emotions and not recognising the needs of others", "apathy", "cough","irritability and impulsiveness","difficulty concentrating on more than one task and handling complex situations","psychiatric problems","uncontrollable movements of the face","communication problems","balance problems"],
    "hyperhidrosis":["you avoid physical contact", "you don't take part in activities", "excessive sweating","you're having problems with normal daily activities, such as driving"],
    "kidney cancer":["unintentional weight loss", "blood in your urine (haematuria)", "a persistent pain in your side, just below the ribs","a lump or swelling in the area of your kidneys","night sweats"],
    "kidney infection":["high temperature", "shivering or chill", "feeling very weak or tired","loss of appetite","feeling sick or being sick","diarrhoea","blood in your urine","pain or a burning sensation during urination"],
    "kidney stones":["a persistent ache in the lower back", "intense pain in the back or side of your abdomen", "feeling restless and unable to lie still","nausea (feeling sick)","pain when you urinate (dysuria)"],
    "laryngeal cancer":["a change in your voice, such as sounding hoarse", "pain when swallowing", "a lump or swelling in your neck","a long-lasting cough","a persistent sore throat or earache","in severe cases, difficulty breathing"],
    "lung cancer":["a long-standing cough that gets worse", "persistent chest infections", "coughing up blood","an ache or pain when breathing or coughing","persistent breathlessness","persistent tiredness or lack of energy"],
    "lyme disease":["tiredness (fatigue)", "muscle pain", "joint pain","headaches","a high temperature (fever)","chills","neck stiffness"],
    "liver tumours":["lump or swelling in the abdomen", "weight loss", "a loss of appetite,","feeling sick (nausea)"],
    "measles":["a runny or blocked nose", "sneezing", "watery eyes","swollen eyelids","small greyish-white spots in the mouth","loss of appetite","tiredness"," irritability"],
    "motor neurone disease ":["The limbs will become weaker", "Speaking and swallowing difficulties", "Saliva problems","Excessive yawning","Emotional changes","Breathing difficulties"],
    "meniere's disease":["vertigo", "tinnitus", "hearing loss"],
    "nasopharyngeal cancer":["a lump in the neck", "hearing loss", "tinnitus ","a blocked or stuffy nose","nosebleeds"],
    "oesophageal cancer":["Difficulty swallowing", "persistent indigestion or heartburn", "bringing up food soon after eating","loss of appetite and weight loss","persistent vomiting","a persistent cough","hoarseness","tiredness","vomiting blood"],
    "osteosarcoma":["Pain in the affected bone", "swelling around the affected bone"],
    "ovarian cancer":["increased abdominal size and persistent bloating", "persistent pelvic and abdominal pain", "difficulty eating and feeling full quickly, or feeling nauseous","back pain"],
    "pancreatic cancer":["pain in the stomach or back", "jaundice", "weight loss","nausea and vomiting","bowel changes","fever and shivering","indigestion","blood clots"],
    "parkinson's disease":["tremor – shaking", "slowness of movement", "muscle stiffness (rigidity)","balance problems","loss of sense of smell (anosmia)","constipation","dizziness"],
    "peripheral neuropathy":["prickling and tingling sensation in the affected body part pins and needles", "a burning or sharp pain, usually in the feet", "loss of balance","twitching and muscle cramps","thinning (wasting) of muscles"],
    "scabies":["intense itching", "rash in areas of the body where the mites have burrowed"],
    "bladder cancer":["pelvic pain","bone pain","unintentional weight loss ","swelling of the legs"]
    # ... Add other diseases and their symptoms
    }

    # Function to get symptoms for a given disease
    def get_symptoms(disease):
        if disease in disease_symptoms:
            return disease_symptoms[disease]
        #else:
         #   return "No symptoms found for the given disease."

    # Get the symptoms for the entered disease
    symptoms = get_symptoms(user_input)

    # Display the symptoms to the user
   # if isinstance(symptoms, list):
    #    for symptom in symptoms:
       #     print(symptom)
   # else:
    #    print(symptoms)
    
    return render(request,'predict_symptoms.html',{'user_input':user_input,'symptoms':symptoms})
    # Define the disease-symptoms dictionary


