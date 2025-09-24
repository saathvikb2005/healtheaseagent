# Simple in-memory storage
ORDERS_DB = {"orders": {}, "next_id": 1}
DRUG_DB = {
    # Existing Drugs
    "aspirin": {"name": "Acetylsalicylic Acid", "price": 5.99,
                "description": "Non-steroidal anti-inflammatory drug for pain relief and fever reduction",
                "quantity": 30},
    "ibuprofen": {"name": "Ibuprofen", "price": 7.99,
                  "description": "Anti-inflammatory medication for pain and inflammation management", "quantity": 20},
    "acetaminophen": {"name": "Acetaminophen", "price": 6.99,
                      "description": "Analgesic and antipyretic medication for pain and fever control", "quantity": 25},
    "metformin": {"name": "Metformin Hydrochloride", "price": 12.50,
                  "description": "Biguanide antidiabetic medication for type 2 diabetes management", "quantity": 60},
    "lisinopril": {"name": "Lisinopril", "price": 8.75,
                   "description": "ACE inhibitor for hypertension and heart failure treatment", "quantity": 30},
    "atorvastatin": {"name": "Atorvastatin Calcium", "price": 15.25,
                     "description": "HMG-CoA reductase inhibitor for cholesterol management", "quantity": 30},
    "omeprazole": {"name": "Omeprazole", "price": 11.99,
                   "description": "Proton pump inhibitor for acid reflux and ulcer treatment", "quantity": 28},
    "amlodipine": {"name": "Amlodipine Besylate", "price": 9.50,
                   "description": "Calcium channel blocker for hypertension and angina", "quantity": 30},
    "metoprolol": {"name": "Metoprolol Tartrate", "price": 7.25,
                   "description": "Beta-blocker for hypertension and heart rhythm disorders", "quantity": 30},
    "sertraline": {"name": "Sertraline Hydrochloride", "price": 13.75,
                   "description": "Selective serotonin reuptake inhibitor for depression and anxiety", "quantity": 30},

    # Expanded Drug List
    "simvastatin": {"name": "Simvastatin", "price": 14.50,
                    "description": "Statin medication used to lower cholesterol and triglyceride levels.", "quantity": 30},
    "levothyroxine": {"name": "Levothyroxine Sodium", "price": 10.20,
                      "description": "Thyroid hormone used to treat hypothyroidism.", "quantity": 30},
    "hydrochlorothiazide": {"name": "Hydrochlorothiazide", "price": 6.80,
                            "description": "Diuretic used to treat high blood pressure and fluid retention.", "quantity": 30},
    "losartan": {"name": "Losartan Potassium", "price": 11.50,
                 "description": "ARB used to treat high blood pressure.", "quantity": 30},
    "gabapentin": {"name": "Gabapentin", "price": 18.90,
                   "description": "Anti-epileptic drug, also used for nerve pain.", "quantity": 90},
    "albuterol": {"name": "Albuterol Sulfate", "price": 25.00,
                  "description": "Bronchodilator used to treat asthma and COPD.", "quantity": 1},
    "prednisone": {"name": "Prednisone", "price": 9.75,
                   "description": "Corticosteroid used to treat inflammation.", "quantity": 20},
    "amoxicillin": {"name": "Amoxicillin", "price": 8.50,
                    "description": "Penicillin antibiotic used to treat bacterial infections.", "quantity": 21},
    "azithromycin": {"name": "Azithromycin", "price": 12.00,
                     "description": "Macrolide antibiotic used for various bacterial infections.", "quantity": 5},
    "tramadol": {"name": "Tramadol Hydrochloride", "price": 16.40,
                 "description": "Opioid analgesic for moderate to severe pain.", "quantity": 30},
    "citalopram": {"name": "Citalopram Hydrobromide", "price": 11.80,
                   "description": "SSRI antidepressant for depression.", "quantity": 30},
    "fluticasone": {"name": "Fluticasone Propionate", "price": 22.50,
                    "description": "Corticosteroid nasal spray for allergies.", "quantity": 1},
    "bupropion": {"name": "Bupropion Hydrochloride", "price": 19.99,
                  "description": "Antidepressant and smoking cessation aid.", "quantity": 60},
    "pravastatin": {"name": "Pravastatin Sodium", "price": 13.90,
                    "description": "Statin medication to lower cholesterol.", "quantity": 30},
    "carvedilol": {"name": "Carvedilol", "price": 8.90,
                   "description": "Beta-blocker for high blood pressure and heart failure.", "quantity": 60},
    "trazodone": {"name": "Trazodone Hydrochloride", "price": 10.50,
                  "description": "Antidepressant, also used for insomnia.", "quantity": 30},
    "potassium": {"name": "Potassium Chloride", "price": 7.00,
                  "description": "Electrolyte supplement.", "quantity": 60},
    "clonazepam": {"name": "Clonazepam", "price": 14.20,
                   "description": "Benzodiazepine for seizure and panic disorders.", "quantity": 30},
    "glipizide": {"name": "Glipizide", "price": 9.30,
                  "description": "Oral anti-diabetic medication.", "quantity": 60},
    "warfarin": {"name": "Warfarin Sodium", "price": 11.10,
                 "description": "Anticoagulant (blood thinner).", "quantity": 30},
    "cyclobenzaprine": {"name": "Cyclobenzaprine Hydrochloride", "price": 8.60,
                        "description": "Muscle relaxant.", "quantity": 30},
    "tamsulosin": {"name": "Tamsulosin Hydrochloride", "price": 21.00,
                   "description": "Alpha-blocker for benign prostatic hyperplasia (BPH).", "quantity": 30},
    "zolpidem": {"name": "Zolpidem Tartrate", "price": 17.80,
                 "description": "Sedative-hypnotic for insomnia.", "quantity": 30},
    "rosuvastatin": {"name": "Rosuvastatin Calcium", "price": 16.70,
                     "description": "Statin medication for high cholesterol.", "quantity": 30},
    "escitalopram": {"name": "Escitalopram Oxalate", "price": 12.90,
                     "description": "SSRI antidepressant for depression and anxiety.", "quantity": 30},
    "venlafaxine": {"name": "Venlafaxine Hydrochloride", "price": 15.60,
                    "description": "SNRI antidepressant.", "quantity": 60},
    "ranitidine": {"name": "Ranitidine Hydrochloride", "price": 9.99,
                   "description": "H2 blocker for stomach acid reduction.", "quantity": 60},
    "furosemide": {"name": "Furosemide", "price": 6.50,
                   "description": "Loop diuretic (water pill).", "quantity": 30},
    "duloxetine": {"name": "Duloxetine Hydrochloride", "price": 20.50,
                   "description": "SNRI for depression, anxiety, and nerve pain.", "quantity": 30},
    "naproxen": {"name": "Naproxen", "price": 8.20,
                 "description": "NSAID for pain and inflammation.", "quantity": 60},
    "fluoxetine": {"name": "Fluoxetine Hydrochloride", "price": 10.80,
                   "description": "SSRI antidepressant.", "quantity": 30},
    "oxycodone": {"name": "Oxycodone Hydrochloride", "price": 28.00,
                  "description": "Opioid analgesic for severe pain.", "quantity": 30},
    "allopurinol": {"name": "Allopurinol", "price": 7.80,
                    "description": "Used to treat gout and kidney stones.", "quantity": 30},
    "pantoprazole": {"name": "Pantoprazole Sodium", "price": 13.40,
                     "description": "Proton pump inhibitor for acid reflux.", "quantity": 30},
    "meloxicam": {"name": "Meloxicam", "price": 12.70,
                  "description": "NSAID for arthritis pain.", "quantity": 30},
    "lorazepam": {"name": "Lorazepam", "price": 13.00,
                  "description": "Benzodiazepine for anxiety.", "quantity": 30},
    "clopidogrel": {"name": "Clopidogrel Bisulfate", "price": 19.50,
                    "description": "Antiplatelet agent to prevent blood clots.", "quantity": 30},
    "cephalexin": {"name": "Cephalexin", "price": 9.60,
                   "description": "Cephalosporin antibiotic.", "quantity": 28},
    "spironolactone": {"name": "Spironolactone", "price": 8.10,
                       "description": "Potassium-sparing diuretic.", "quantity": 30},
    "buspirone": {"name": "Buspirone Hydrochloride", "price": 11.20,
                  "description": "Anxiolytic for anxiety disorders.", "quantity": 60},
    "finasteride": {"name": "Finasteride", "price": 25.50,
                    "description": "Used to treat BPH and male pattern hair loss.", "quantity": 30},
    "risperidone": {"name": "Risperidone", "price": 22.00,
                    "description": "Antipsychotic medication.", "quantity": 60},
    "doxycycline": {"name": "Doxycycline Hyclate", "price": 14.80,
                    "description": "Tetracycline antibiotic.", "quantity": 14},
    "montelukast": {"name": "Montelukast Sodium", "price": 23.10,
                    "description": "Used for asthma and allergies.", "quantity": 30},
    "famotidine": {"name": "Famotidine", "price": 9.40,
                   "description": "H2 blocker for ulcers and acid reflux.", "quantity": 60},
    "insulin": {"name": "Insulin Glargine", "price": 45.00,
                "description": "Long-acting insulin for diabetes.", "quantity": 1},
    "topiramate": {"name": "Topiramate", "price": 18.20,
                   "description": "Used to treat seizures and prevent migraines.", "quantity": 60},
    "quetiapine": {"name": "Quetiapine Fumarate", "price": 21.80,
                   "description": "Antipsychotic for schizophrenia and bipolar disorder.", "quantity": 60},
    "diclofenac": {"name": "Diclofenac Sodium", "price": 11.50,
                   "description": "NSAID for pain and arthritis.", "quantity": 60},
    "ondansetron": {"name": "Ondansetron Hydrochloride", "price": 17.20,
                    "description": "Anti-nausea medication.", "quantity": 12}
}


def get_drug_info(drug_name):
    """Get drug information."""
    drug = DRUG_DB.get(drug_name.lower())
    if drug:
        return {
            "name": drug["name"],
            "description": drug["description"],
            "price": drug["price"],
            "quantity": drug["quantity"]
        }
    return {"error": f"Drug '{drug_name}' not found"}


def place_order(customer_name, drug_name):
    """Place a simple order with predefined quantity."""
    drug = DRUG_DB.get(drug_name.lower())
    if not drug:
        return {"error": f"Drug '{drug_name}' not found"}

    order_id = ORDERS_DB["next_id"]
    ORDERS_DB["next_id"] += 1

    order = {
        "id": order_id,
        "customer": customer_name,
        "drug": drug["name"],
        "quantity": drug["quantity"],
        "total": drug["price"],
        "status": "pending"
    }
    ORDERS_DB["orders"][order_id] = order

    return {
        "order_id": order_id,
        "message": f"Order {order_id} placed: {drug['quantity']} {drug['name']} for ${order['total']:.2f}",
        "total": order['total'],
        "quantity": drug['quantity']
    }


def lookup_order(order_id):
    """Look up an order."""
    order = ORDERS_DB["orders"].get(int(order_id))
    if order:
        return {
            "order_id": order_id,
            "customer": order["customer"],
            "drug": order["drug"],
            "quantity": order["quantity"],
            "total": order["total"],
            "status": order["status"]
        }
    return {"error": f"Order {order_id} not found"}


def call_ambulance():
    """Simulates calling an ambulance for an emergency."""
    print("SIMULATING CALL TO EMERGENCY SERVICES")
    return {"status": "success", "message": "Connecting you to the ambulance service now. Please stay on the line."}


def schedule_appointment(location, doctor_specialty, date, time):
    """Simulates scheduling a doctor's appointment."""
    print(f"SIMULATING appointment scheduling for a {doctor_specialty} in {location} on {date} at {time}.")
    # In a real app, this would interact with a calendar or booking API.
    return {
        "status": "success",
        "message": f"Okay, I've scheduled an appointment for you with a {doctor_specialty} near {location} on {date} at {time}. You will receive a confirmation shortly."
    }


# Function mapping dictionary
FUNCTION_MAP = {
    'get_drug_info': get_drug_info,
    'place_order': place_order,
    'lookup_order': lookup_order,
    'call_ambulance': call_ambulance,
    'schedule_appointment': schedule_appointment
}

