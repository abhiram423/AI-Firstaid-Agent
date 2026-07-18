import os
import json
import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import APIKEY, Patient
from .agents.guidance_data import get_guidance

def home(request):
    return render(request, 'home.html')

def get_ai_medical_report(body_part, incident, severity, extra_details=""):
    """
    Connects to the OpenAI API endpoint using the system environment variable.
    Forces the model to output a highly comprehensive, step-by-step detailed 
    JSON structure matching report.html fields.
    """
    api_key = os.getenv('HEALTH_CARE_API_KEY')

    # No live API key configured — serve the local, hand-curated guidance
    # database instead. get_guidance() matches the exact body_part +
    # incident + severity combination selected by the user, so the output
    # is specific to their selection rather than a generic placeholder.
    if not api_key:
        return get_guidance(body_part, incident, severity)

    # Constructing a precise system safety prompt
    prompt = f"""
    You are an expert emergency medicine physician and first-aid specialist.
    Provide a highly detailed, comprehensive, and exhaustive first-aid assessment report for the following scenario:
    - Affected Body Part/Region: {body_part}
    - Symptom / Injury Type: {incident}
    - User-Reported Severity Scale: {severity}
    - Specific Contextual Notes: {extra_details if extra_details else 'None provided'}

    CRITICAL INSTRUCTIONS FOR COMPLETENESS:
    1. 'summary': Write a thorough, detailed 3-4 sentence clinical explanation of what might be happening, why it happens, and a protective medical disclaimer.
    2. 'first_aid': Provide a minimum of 5 to 7 sequential, exhaustive, step-by-step actions that must be taken immediately. Do not use short bullet points; write complete, detailed action sentences.
    3. 'avoid': Provide at least 4 distinct, descriptive actions, substances, or movements the patient must absolutely avoid to prevent worsening the injury.
    4. 'emergency_signs': Provide at least 5 critical red-flag signs or progressive symptoms specific to this body part and injury type that mean they must drop everything and run to an ER or call 911.
    5. 'recovery': Provide at least 3-4 detailed home care, cleaning, elevation, resting, or monitoring guidelines for the next 24-48 hours.
    6. 'prevention': Provide 3 detailed safety rules to prevent this precise incident from happening again in the future.
    7. 'medications': Provide a highly descriptive list. Include safe, standard over-the-counter options (like Ibuprofen, Acetaminophen, or topical antiseptics if applicable) with clear instructions, AND include specific common drugs that must be avoided for this specific condition (e.g., avoiding NSAIDs/Aspirin if heavy bleeding or severe stomach pain is present) explaining exactly why.

    You MUST respond with ONLY a valid JSON object. Do not include markdown code block backticks (like ```json).
    Use this exact JSON schema structure: {{
        "condition": "Specific suspected primary medical issue name",
        "summary": "Verbose detailed clinical context and evaluation mapping",
        "risk": "Low or Medium or High",
        "emergency": true or false,
        "first_aid": ["Detailed step 1...", "Detailed step 2...", "Detailed step 3...", "Detailed step 4...", "Detailed step 5..."],
        "avoid": ["Detailed item to avoid 1...", "Detailed item to avoid 2...", "Detailed item to avoid 3...", "Detailed item to avoid 4..."],
        "emergency_signs": ["Red flag warning sign 1...", "Red flag warning sign 2...", "Red flag warning sign 3...", "Red flag warning sign 4...", "Red flag warning sign 5..."],
        "recovery": ["Detailed recovery timeline protocol 1...", "Detailed recovery timeline protocol 2..."],
        "prevention": ["Preventative baseline strategy 1...", "Preventative baseline strategy 2..."],
        "medications": [
            {{"name": "Medication Name/Class", "dose": "Standard adult dose range", "freq": "Frequency interval", "use": "Detailed clinical reasoning for usage", "ok": true}},
            {{"name": "Medication to Avoid", "dose": "AVOID", "freq": "AVOID", "use": "Explicit detailed physiological reason why this option is dangerous here", "ok": false}}
        ]
    }}
    """

    try:
        # Updated to official OpenAI endpoint route
        url = "https://api.openai.com/v1/chat/completions"        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}' # Standard OpenAI format
        }
        
        # Payload tailored for OpenAI models with forced JSON object responses
        payload = {
            "model": "gpt-4o-mini", # Fast and cheap, or use "gpt-4o" if preferred
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "response_format": { "type": "json_object" }, # Forces OpenAI to reply in clean JSON
            "temperature": 0.3,
            "max_tokens": 1500
        }
        
        response = requests.post(url, headers=headers, json=payload, timeout=12)
        
        if response.status_code == 200:
            raw_text = response.json()['choices'][0]['message']['content']
            return json.loads(raw_text)
        else:
            print(f"OpenAI API Error Status: {response.status_code} - {response.text}")
            
    except Exception as e:
        print(f"Pipeline error encountered: {str(e)}")

    # If the live API call failed or errored out, fall back to the local
    # guidance database rather than a generic placeholder — still gives the
    # user a precise, combination-matched first aid report.
    return get_guidance(body_part, incident, severity)

def guide(request):
    """4-step guided workflow parsing backend input parameters to live OpenAI Engines."""
    if request.method == 'POST':
        # Safely capture hidden field tokens string payloads generated inside browser context
        body_part = request.POST.get('body_part', '').strip().lower()
        incident  = request.POST.get('incident', '').strip().lower()
        severity  = request.POST.get('severity', '').strip().lower()
        
        # Optional metadata parameters processing block area
        name      = request.POST.get('name', '').strip()
        age       = request.POST.get('age', '').strip()
        details   = request.POST.get('details', '').strip()

        # Debug console tracking tool logic validation check logs lines
        print(f"Backend Triage Payloads Extracted Metrics -> Body Part: '{body_part}', Incident: '{incident}', Severity: '{severity}'")

        # 🌟 STRICT TRIAGE VERIFICATION ONLY: Stop execution if wizard step options are dropped
        if not all([body_part, incident, severity]):
            messages.error(request, 'Please complete the basic injury selection steps before compiling data reports.')
            return redirect('guide')

        # Save to SQLite Database Model instances if optional fields hold value data arrays parameters
        # Allows processing even if patient leaves user fields blank safely!
        parsed_age = int(age) if (age and age.isdigit()) else None
        Patient.objects.create(
            name=name if name else "Anonymous Patient",
            age=parsed_age,
            details=details if details else "None specified"
        )

        # Connect straight into OpenAI endpoint pipeline function safely
        guidance = get_ai_medical_report(body_part, incident, severity, details)

        # Set standard session properties context parameters trackers array objects
        request.session['guidance']       = guidance
        request.session['patient_name']   = name if name else "Anonymous Patient"
        request.session['patient_age']    = age if age else "N/A"
        request.session['patient_detail'] = details if details else "None specified"

        request.session['body_part'] = body_part
        request.session['incident'] = incident
        request.session['severity'] = severity
        
        return redirect('report')

    return render(request, 'guide.html')

def report(request):
    guidance     = request.session.get('guidance', {})
    patient_name = request.session.get('patient_name', '')
    patient_age  = request.session.get('patient_age', '')
    details      = request.session.get('patient_detail', '')

    body_part    = request.session.get('body_part', '')
    incident     = request.session.get('incident', '')
    severity     = request.session.get('severity', '')

    if not guidance:
        messages.warning(request, 'Please complete the guided workflow first.')
        return redirect('guide')

    context = {
        'guidance':      guidance,
        'patient_name':  patient_name,
        'patient_age':   patient_age,
        'details':       details,
        'body_part':     body_part,
        'incident':      incident,
        'severity':      severity,
    }
    return render(request, 'report.html', context)

def assess(request):
    return render(request, 'assess.html')