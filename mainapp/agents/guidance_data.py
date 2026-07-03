"""
MedAssist AI — Comprehensive First-Aid Guidance Database
Covers all 48 body-part × incident combinations with 10-12 steps each.
"""

# ── Display labels ─────────────────────────────────────────────────
BODY_PART_DISPLAY = {
    'head': 'Head', 'eye': 'Eye', 'hand': 'Hand',
    'arm': 'Arm', 'leg': 'Leg', 'foot': 'Foot',
    'chest': 'Chest', 'back': 'Back',
}
INCIDENT_DISPLAY = {
    'bleeding': 'Bleeding', 'burn': 'Burn', 'pain': 'Pain',
    'cut': 'Cut', 'swelling': 'Swelling', 'bruise': 'Bruise',
}

# ── Risk matrix ────────────────────────────────────────────────────
CRITICAL_PARTS    = {'head', 'eye', 'chest'}
HIGH_RISK_COMBOS  = {('head', 'bleeding'), ('eye', 'bleeding'), ('eye', 'cut'),
                     ('chest', 'pain'), ('chest', 'bleeding'), ('head', 'pain')}

def compute_risk(body_part: str, incident: str, severity: str) -> str:
    bp, inc = body_part.lower(), incident.lower()
    if severity.lower() == 'severe':
        return 'Critical' if (bp in CRITICAL_PARTS or (bp, inc) in HIGH_RISK_COMBOS) else 'High'
    if severity.lower() == 'moderate':
        if (bp, inc) in HIGH_RISK_COMBOS: return 'High'
        return 'High' if bp in CRITICAL_PARTS else 'Medium'
    # mild
    if (bp, inc) in HIGH_RISK_COMBOS: return 'Medium'
    return 'Medium' if bp in CRITICAL_PARTS else 'Low'

def is_emergency(risk: str, body_part: str, incident: str, severity: str) -> bool:
    if risk in ('Critical', 'High'): return True
    if body_part.lower() in CRITICAL_PARTS and severity.lower() in ('moderate', 'severe'): return True
    return False

# ── Master guidance database ───────────────────────────────────────
GUIDANCE_DB = {

    # ═══════════════════════ HEAD ═══════════════════════
    ('head', 'bleeding'): {
        'condition': 'Scalp Laceration',
        'summary': 'A scalp laceration is a cut or tear in the skin of the head. Scalp wounds bleed heavily due to their rich blood supply and often appear more serious than they are. However, any head injury requires vigilant monitoring for signs of concussion, skull fracture, or internal bleeding.',
        'first_aid': [
            'Apply firm, direct pressure using a clean cloth or sterile gauze pad immediately.',
            'Maintain continuous pressure for at least 10–15 minutes without lifting the cloth.',
            'If the cloth becomes soaked, add additional layers on top — do not remove the original.',
            'Keep the injured person calm and as still as possible to reduce blood pressure spikes.',
            'Gently rinse debris from the wound with clean water only if it does not increase bleeding.',
            'Do not probe the wound, remove embedded objects, or attempt to clean deeply.',
            'Apply a wrapped ice pack around (never directly on) the wound to reduce swelling.',
            'If the person is conscious, keep them in a semi-reclined position to reduce blood flow to the head.',
            'Monitor alertness every 5 minutes — check responses to questions and eye tracking.',
            'Watch for concussion signs: confusion, vomiting, unequal pupils, slurred speech.',
            'If bleeding does not stop within 15 minutes of direct pressure, call emergency services.',
            'Record the time of injury and any changes in condition for attending medical staff.',
        ],
        'avoid': [
            'Do not give aspirin or ibuprofen — they thin the blood and worsen bleeding.',
            'Do not allow the person to sleep immediately without checking for concussion first.',
            'Do not wash head wounds vigorously as this disturbs clot formation.',
            'Do not remove any object embedded in the skull — stabilize it and call 911.',
            'Do not leave the person unattended if disoriented or confused.',
        ],
        'emergency_signs': [
            'Loss of consciousness, even briefly, following the injury.',
            'Repeated vomiting (more than twice after the injury).',
            'Unequal, dilated, or unreactive pupils.',
            'Worsening headache that intensifies over time.',
            'Clear fluid draining from the nose or ears (possible skull fracture).',
            'Seizures occurring after the head injury.',
            'Visible skull deformity or bone exposure.',
        ],
        'recovery': [
            'Rest completely for 24–48 hours after a head injury.',
            'Avoid screens, bright lights, and loud noise if a headache is present.',
            'Take paracetamol (acetaminophen) for pain — never aspirin or NSAIDs.',
            'Have a responsible adult monitor you for the first 24 hours.',
            'Attend all follow-up appointments, especially if stitches were placed.',
            'Gradually resume normal activities only as directed by your healthcare provider.',
        ],
        'prevention': [
            'Always wear a properly fitted helmet during cycling, motorcycling, and contact sports.',
            'Install adequate lighting in hallways, staircases, and outdoor areas.',
            'Use non-slip mats in bathrooms and secure loose rugs.',
            'Pad sharp furniture corners, especially in homes with young children or elderly adults.',
            'Follow all safety regulations at construction and industrial work sites.',
        ],
    },

    ('head', 'pain'): {
        'condition': 'Head Pain / Possible Concussion',
        'summary': 'Head pain can range from a simple tension headache to a sign of serious underlying conditions such as concussion, hypertensive crisis, or intracranial pressure. Any head pain following trauma must be treated as a potential concussion until evaluated by a medical professional.',
        'first_aid': [
            'Have the person sit or lie down in a quiet, dimly lit, comfortable environment immediately.',
            'Ask when the pain started, how it began, and whether there was any recent head trauma.',
            'Apply a cool, damp cloth to the forehead and the back of the neck for comfort.',
            'Offer paracetamol (acetaminophen) if the person is conscious and not allergic.',
            'Ensure the person is well-hydrated — have them sip water slowly.',
            'Loosen any tight clothing around the neck and collar to improve circulation.',
            'Monitor alertness and responsiveness every 5–10 minutes.',
            'Check pupils for equal size and reactivity to light using a torch.',
            'Do not allow the person to drive or operate machinery until the pain resolves.',
            'If post-trauma headache, follow concussion protocol and restrict activity.',
            'Keep a log of symptom onset, duration, location, and associated symptoms.',
            'Seek immediate medical attention if the headache is described as "the worst of their life."',
        ],
        'avoid': [
            'Do not give aspirin to children or adolescents (risk of Reye syndrome).',
            'Do not allow the person to sleep unless you can wake them easily every 2 hours.',
            'Do not dismiss head pain following a fall, collision, or impact.',
            'Avoid bright light, loud sounds, and screens during acute head pain.',
            'Do not give more than the recommended dose of any pain reliever.',
        ],
        'emergency_signs': [
            'Sudden onset "thunderclap" headache — the worst headache of one\'s life.',
            'Head pain following a significant blow, fall, or accident.',
            'Headache accompanied by fever, stiff neck, and sensitivity to light (meningitis signs).',
            'Progressive worsening of headache over 24–72 hours.',
            'Confusion, memory loss, or unusual behavior.',
            'Vision changes, weakness on one side, or difficulty speaking.',
            'Headache following vomiting or loss of consciousness.',
        ],
        'recovery': [
            'Rest in a dark, quiet room until the headache resolves.',
            'Stay hydrated and avoid skipping meals.',
            'Manage stress through deep breathing and relaxation techniques.',
            'Maintain a consistent sleep schedule to prevent recurrence.',
            'Follow up with a neurologist if headaches are frequent or worsening.',
            'Keep a headache diary noting triggers, duration, and severity.',
        ],
        'prevention': [
            'Stay well-hydrated and avoid prolonged fasting.',
            'Manage stress with regular exercise, meditation, or therapy.',
            'Limit caffeine intake and avoid sudden caffeine withdrawal.',
            'Wear a helmet during all activities with risk of head impact.',
            'Get regular eye exams to rule out vision-related headaches.',
        ],
    },

    ('head', 'cut'): {
        'condition': 'Scalp Incision / Head Cut',
        'summary': 'A cut on the scalp or head causes significant bleeding due to the dense network of blood vessels in the scalp tissue. While most head cuts are manageable with basic first aid, deeper lacerations may require sutures, and all head injuries warrant monitoring for signs of concussion.',
        'first_aid': [
            'Wash your hands thoroughly before touching the wound to prevent infection.',
            'Apply gentle but firm pressure with a clean cloth or sterile gauze.',
            'Hold pressure continuously for 10 minutes before checking if bleeding has stopped.',
            'Once bleeding is controlled, gently clean around (not inside) the wound with clean water.',
            'Examine the cut carefully — if edges are gaping more than 0.5 cm, stitches are likely needed.',
            'Apply a sterile adhesive bandage or closure strips to hold edges together.',
            'Cover the area with a clean, non-adhesive dressing.',
            'Check tetanus vaccination status — update if the last dose was more than 5 years ago.',
            'Monitor the wound site daily for signs of infection: redness spreading, warmth, pus.',
            'Change the dressing every 24 hours using clean technique.',
            'Administer paracetamol for pain as needed.',
            'Keep the wound dry for at least 24 hours after initial dressing.',
        ],
        'avoid': [
            'Do not use alcohol or hydrogen peroxide inside the wound — it damages healing tissue.',
            'Do not attempt to remove any object embedded in the wound.',
            'Do not cover the wound with fluffy cotton wool — fibres can stick to the wound.',
            'Do not leave the wound unbandaged in dusty or dirty environments.',
            'Do not ignore signs of wound infection.',
        ],
        'emergency_signs': [
            'Cut that exposes bone or fatty tissue beneath the skin.',
            'Wound edges that are more than 0.5 cm apart and cannot be closed with strips.',
            'Wound caused by a heavily contaminated object (rusty, dirty, animal bite).',
            'Signs of infection: increasing redness, warmth, pus, or red streaks spreading outward.',
            'Accompanying signs of concussion: dizziness, vomiting, confusion.',
            'Wound that reopens or continues bleeding beyond 20 minutes.',
        ],
        'recovery': [
            'Keep the wound clean and dry for the first 24–48 hours.',
            'Change dressings once daily or whenever the dressing becomes wet or dirty.',
            'Avoid submerging the wound in water (baths, swimming) until fully healed.',
            'Use sunscreen on the healed scar for 6–12 months to prevent pigmentation.',
            'Follow up with a healthcare provider for suture removal if applicable.',
            'Expect full healing in 7–14 days for minor scalp cuts.',
        ],
        'prevention': [
            'Wear helmets and head protection during relevant activities.',
            'Keep sharp objects safely stored and out of reach of children.',
            'Ensure adequate lighting to prevent falls and accidents.',
            'Use safety equipment at work sites where head injury risk is elevated.',
            'Trim sharp edges from furniture and home fixtures.',
        ],
    },

    ('head', 'bruise'): {
        'condition': 'Cranial Contusion / Head Bruise',
        'summary': 'A bruise on the head, also called a cranial contusion, occurs when blood vessels beneath the skin break due to blunt force. While surface bruising is usually minor, any bruise resulting from a significant impact to the head may indicate underlying injury and warrants careful monitoring.',
        'first_aid': [
            'Apply an ice pack wrapped in a cloth to the bruised area immediately.',
            'Keep the ice pack in place for 15–20 minutes, then remove for 20 minutes before reapplying.',
            'Ensure the person is alert and oriented — ask their name, date, and location.',
            'Have the person sit or lie down comfortably with their head slightly elevated.',
            'Do not apply direct pressure unless there is also visible bleeding.',
            'Monitor the person every 30 minutes for the first 4 hours following the injury.',
            'Give paracetamol for pain if needed; avoid aspirin and NSAIDs.',
            'Encourage rest and avoid strenuous activity for at least 24 hours.',
            'Keep the person warm and calm to prevent stress response.',
            'Check pupils for equal size and normal reaction to light.',
            'Document the time of injury and the mechanism (how they were hit).',
            'Restrict screen use and intense mental activity for 24–48 hours.',
        ],
        'avoid': [
            'Do not apply heat to a fresh bruise — it increases internal bleeding.',
            'Do not allow the person to sleep without monitoring for concussion for the first 4 hours.',
            'Do not rub or massage the bruised area.',
            'Do not give blood-thinning medications like aspirin.',
            'Do not minimize the injury if the mechanism of trauma was significant.',
        ],
        'emergency_signs': [
            'Large, rapidly growing hematoma (bump) on the head.',
            'Confusion, slurred speech, or memory gaps following the injury.',
            'Persistent or worsening headache after more than 2 hours.',
            'Vomiting more than once following the impact.',
            'Visual disturbances or unequal pupils.',
            'Sleepiness that is abnormal and difficult to interrupt.',
        ],
        'recovery': [
            'Rest for 24–48 hours; avoid screen time, reading, and mental exertion.',
            'Apply cold compresses for 15–20 minutes several times in the first 48 hours.',
            'After 48 hours, switch to warm compresses to aid reabsorption of the bruise.',
            'Eat a balanced diet rich in vitamin C and K to support healing.',
            'Avoid contact sports or activities with fall risk until fully cleared.',
            'Consult a doctor if the bruise does not begin improving within 5–7 days.',
        ],
        'prevention': [
            'Wear appropriate head protection in sports and work environments.',
            'Pad sharp corners of furniture and countertops.',
            'Ensure safe playground equipment with proper protective surfaces.',
            'Use handrails on stairs and non-slip footwear in wet areas.',
            'Educate children about safe play practices.',
        ],
    },

    ('head', 'swelling'): {
        'condition': 'Scalp Hematoma / Head Swelling',
        'summary': 'Swelling on the head typically indicates a hematoma — a collection of blood under the scalp. This can form rapidly after impact, creating a visible and tender lump. While scalp hematomas are usually benign, they can occasionally mask more serious underlying skull or brain injuries.',
        'first_aid': [
            'Apply an ice pack wrapped in cloth to the swollen area for 15–20 minutes immediately.',
            'Do not press hard on the swelling — apply only gentle, cold compression.',
            'Help the person into a resting position with head slightly elevated.',
            'Assess the person for signs of concussion: confusion, vomiting, memory loss.',
            'Check pupil size and response to light.',
            'Monitor alertness and responses every 15–30 minutes for the first 2 hours.',
            'Administer paracetamol for discomfort; avoid NSAIDs and aspirin.',
            'Restrict physical activity and screen use for at least 24 hours.',
            'Reapply cold compress every 2 hours during the first 24 hours.',
            'Ensure the environment is quiet and dimly lit if the person is sensitive to light or noise.',
            'Keep a record of the exact time of impact and the size of the swelling over time.',
            'Seek medical evaluation for any swelling that grows rapidly or is unusually firm.',
        ],
        'avoid': [
            'Do not apply heat or warm compresses in the first 48 hours.',
            'Do not drain or puncture the swelling.',
            'Do not give aspirin or ibuprofen as they promote bleeding.',
            'Do not allow strenuous activity that raises blood pressure.',
            'Do not leave the person unsupervised for the first 4 hours after the injury.',
        ],
        'emergency_signs': [
            'Swelling that continues to grow rapidly over 30–60 minutes.',
            'Swelling accompanied by a visible dent or concavity (possible skull fracture).',
            'Loss of consciousness or unresponsiveness at any point.',
            'Difficulty waking the person or keeping them alert.',
            'Seizures following the head injury.',
            'Clear fluid (CSF) leak from ears or nose.',
        ],
        'recovery': [
            'Apply cold for the first 48 hours, then switch to warm compresses.',
            'Rest with the head elevated on a pillow.',
            'Small hematomas typically reabsorb within 2–4 weeks.',
            'Avoid contact sports until fully healed and cleared by a doctor.',
            'Monitor for late-onset symptoms that can develop 24–72 hours post-injury.',
            'Follow up with a physician if swelling persists beyond 2 weeks.',
        ],
        'prevention': [
            'Use appropriate protective headwear in all high-risk activities.',
            'Secure loose rugs and address fall hazards in the home.',
            'Ensure children\'s play areas have soft, impact-absorbing surfaces.',
            'Use seat belts and child car seats correctly in vehicles.',
            'Address dizziness or balance issues to reduce fall risk.',
        ],
    },

    ('head', 'burn'): {
        'condition': 'Scalp or Facial Burn',
        'summary': 'Burns to the head, face, or scalp are considered serious because of their proximity to the airway, eyes, and brain. Any burn to the face or head that covers more than a small area, involves the airway, or is deeper than superficial requires immediate emergency medical care.',
        'first_aid': [
            'Remove the person from the source of the burn immediately and ensure your own safety.',
            'Cool the burned area under cool (not cold) running water for 20 minutes continuously.',
            'Do NOT use ice, iced water, butter, toothpaste, or any home remedy on the burn.',
            'Remove glasses, earrings, and any metal near the burned area carefully.',
            'Do not attempt to remove clothing stuck to burned skin.',
            'Cover the cooled burn loosely with a clean, non-fluffy material or cling film.',
            'Do not break any blisters that form — they protect the wound from infection.',
            'Assess for inhalation injury: check for singed eyebrows, sooty deposits in nostrils, or hoarseness.',
            'If the person inhaled smoke or has breathing difficulty, call emergency services immediately.',
            'Keep the person warm to prevent shock.',
            'Do not put anything in or near the eyes if they are affected.',
            'Arrange urgent medical transport — all but the most trivial facial burns need evaluation.',
        ],
        'avoid': [
            'Do not use ice directly — it causes frostbite and worsens the injury.',
            'Do not apply any cream, butter, oil, or toothpaste to the burn.',
            'Do not leave blisters unprotected — cover with a clean dressing.',
            'Do not wrap the burn too tightly — swelling will worsen.',
            'Do not underestimate a burn near the airway — it can cause life-threatening swelling.',
        ],
        'emergency_signs': [
            'Burn involving the face, hands, genitals, or major joints.',
            'Burn covering an area larger than a dinner plate.',
            'Signs of inhalation injury: hoarseness, difficulty breathing, coughing soot.',
            'Chemical burns to the eye or face.',
            'Deep burn with white, brown, or black tissue (third-degree).',
            'Burn in a child or elderly person of any significant size.',
        ],
        'recovery': [
            'Follow medical instructions for wound care and dressing changes.',
            'Protect the healed area from sunlight for 12 months using SPF 50+ sunscreen.',
            'Stay well-hydrated and eat a protein-rich diet to support skin healing.',
            'Attend physiotherapy if scarring affects mobility around the face or neck.',
            'Use scar management creams or silicone sheets as directed by your specialist.',
            'Seek psychological support if the burn causes significant appearance-related distress.',
        ],
        'prevention': [
            'Keep flammable materials and open flames away from children.',
            'Test food and drink temperature before consuming or serving to children.',
            'Install smoke detectors and maintain them regularly.',
            'Wear sun protection when spending extended time in direct sunlight.',
            'Follow safe practices when working with chemicals, hot liquids, or open flames.',
        ],
    },

    # ═══════════════════════ EYE ═══════════════════════
    ('eye', 'pain'): {
        'condition': 'Ocular Pain / Eye Injury',
        'summary': 'Eye pain is always considered a medical concern due to the eye\'s sensitivity and the risk of vision loss. Pain in or around the eye can result from foreign bodies, abrasions, infections, or serious conditions such as acute glaucoma. All significant eye pain warrants prompt medical evaluation by an eye specialist.',
        'first_aid': [
            'Instruct the person not to rub the eye — rubbing can worsen corneal damage.',
            'Have the person blink gently several times to see if a foreign body dislodges naturally.',
            'Wash your hands before touching anywhere near the eye.',
            'If a foreign body is suspected, irrigate the eye gently with clean water or sterile saline from the inner corner outward.',
            'Use a clean eyelid everter technique only if trained — look under the upper eyelid for debris.',
            'If a chemical substance entered the eye, irrigate immediately for 15–20 minutes continuously.',
            'Cover the eye loosely with a clean, non-pressure eye pad if not irrigating.',
            'Do not attempt to remove any object embedded in the eyeball itself.',
            'Dim the lighting in the room to reduce photophobia (light sensitivity).',
            'Keep the person calm and restrict eye movement as much as possible.',
            'Apply a cool cloth over the closed eyelid for comfort if there is no penetrating injury.',
            'Arrange urgent transport to an ophthalmologist or emergency department.',
        ],
        'avoid': [
            'Do not rub the eye under any circumstances.',
            'Do not apply pressure to an eye with a suspected penetrating injury.',
            'Do not attempt to remove an embedded object from the eye.',
            'Do not use eye drops not prescribed for this specific condition.',
            'Do not wear contact lenses while the eye is painful or inflamed.',
        ],
        'emergency_signs': [
            'Sudden, severe eye pain with vision loss.',
            'Visible trauma to the eye — visible blood, puncture, or deformity.',
            'Chemical splashed directly into the eye.',
            'Sudden appearance of halos, flashing lights, or floaters.',
            'Eye pain accompanied by nausea and vomiting (possible acute glaucoma).',
            'Inability to open the eye due to extreme light sensitivity.',
            'Partial or complete loss of vision in the affected eye.',
        ],
        'recovery': [
            'Rest the eye — limit reading, screen time, and bright light exposure.',
            'Use prescribed antibiotic drops or ointment as directed by your doctor.',
            'Wear sunglasses outdoors to protect the healing eye from UV and wind.',
            'Attend all follow-up appointments with your ophthalmologist.',
            'Do not wear contact lenses until fully cleared by your eye specialist.',
            'Report any sudden change in vision during recovery immediately.',
        ],
        'prevention': [
            'Wear safety glasses or goggles when working with tools, chemicals, or debris.',
            'Use UV-protective sunglasses outdoors.',
            'Avoid touching your eyes with unwashed hands.',
            'Maintain proper contact lens hygiene and replace as recommended.',
            'Keep sharp objects out of children\'s reach.',
        ],
    },

    ('eye', 'bleeding'): {
        'condition': 'Ocular Hemorrhage / Eye Bleeding',
        'summary': 'Bleeding in or around the eye is a serious medical emergency. It may indicate a subconjunctival hemorrhage (superficial, usually benign) or a more severe intraocular or periorbital injury. Any penetrating trauma, chemical exposure, or spontaneous bleeding with vision changes requires immediate emergency evaluation.',
        'first_aid': [
            'Keep the person still and instruct them not to move their eyes excessively.',
            'Do NOT apply pressure to a bleeding eye — this can cause permanent damage.',
            'Cover the eye gently with a clean, sterile eye pad — do not press down.',
            'If the other eye is unaffected, cover the injured eye only and keep it still.',
            'Wash your hands before any contact near the eye area.',
            'If caused by a chemical, irrigate immediately with large amounts of water for 20 minutes.',
            'Note the mechanism of injury and the time it occurred for emergency staff.',
            'Keep the person calm and in a semi-reclined position with the head supported.',
            'Do not allow the person to rub or wipe the eye.',
            'Do not attempt to remove any visible object protruding from the eye.',
            'Shield the eye with a sterile eye shield or the bottom of a plastic cup without touching the eye.',
            'Call emergency services or transport immediately to an emergency ophthalmology centre.',
        ],
        'avoid': [
            'Never apply pressure to a hemorrhaging eye.',
            'Do not use eye drops, saline, or any liquid unless it\'s a chemical flush emergency.',
            'Do not give aspirin or blood thinners.',
            'Do not delay seeking emergency care — time-critical for vision preservation.',
            'Do not remove contact lenses if there is significant trauma — call for help.',
        ],
        'emergency_signs': [
            'Any visible penetrating injury to the eye.',
            'Loss of vision, even partial, following trauma.',
            'Prolapse of eye contents (vitreous or tissue visible outside eye).',
            'Subconjunctival hemorrhage following significant head injury (raccoon eye sign).',
            'Bleeding that spreads to cover the entire white of the eye.',
            'Associated headache, nausea, or other neurological signs.',
            'Chemical or caustic substance exposure to the eye.',
        ],
        'recovery': [
            'Follow ophthalmologist instructions precisely regarding eye drops and positioning.',
            'Avoid strenuous activity, bending, and heavy lifting during recovery.',
            'Sleep with the head elevated at 30–45 degrees if advised.',
            'Protect the eye from bright light and physical contact.',
            'Report any sudden changes in vision or increase in pain immediately.',
            'Attend all scheduled follow-up appointments without exception.',
        ],
        'prevention': [
            'Always wear certified safety eyewear when working with tools, chemicals, or high-pressure equipment.',
            'Never use sharp objects near your face or eyes.',
            'Ensure children\'s toys do not have sharp or protruding parts.',
            'Wear a face shield when grinding, welding, or operating machinery.',
            'Use goggles when swimming in pools or natural water bodies.',
        ],
    },

    # ═══════════════════════ CHEST ═══════════════════════
    ('chest', 'pain'): {
        'condition': 'Chest Pain — Possible Cardiac or Pulmonary Emergency',
        'summary': 'Chest pain is a medical emergency until proven otherwise. It may indicate a heart attack (myocardial infarction), pulmonary embolism, aortic dissection, or other life-threatening conditions. Any chest pain — especially with associated symptoms — requires immediate emergency services activation. Do not wait to see if it resolves.',
        'first_aid': [
            'CALL EMERGENCY SERVICES (911) IMMEDIATELY — do not wait or delay.',
            'Have the person stop all physical activity and sit or lie down in the most comfortable position.',
            'Loosen any tight clothing around the neck, chest, and waist.',
            'If the person is conscious and not allergic, give one standard aspirin (325mg) to chew (not swallow whole).',
            'Keep the person calm, still, and reassured until emergency help arrives.',
            'Prepare to perform CPR if the person becomes unresponsive and stops breathing normally.',
            'If a defibrillator (AED) is nearby, retrieve it and keep it ready for use.',
            'Do not allow the person to eat, drink, or take any other medications.',
            'Note the exact time symptoms began and any associated symptoms.',
            'Monitor breathing rate, consciousness level, and skin colour continuously.',
            'Do not leave the person alone at any time.',
            'If the person loses consciousness and has no pulse, begin CPR immediately.',
        ],
        'avoid': [
            'Do not assume it is "just indigestion" — call emergency services first.',
            'Do not allow the person to drive themselves to hospital.',
            'Do not give food or water — surgery may be imminent.',
            'Do not delay aspirin administration if available and no allergy is known.',
            'Do not apply heat pads or pressure to the chest.',
        ],
        'emergency_signs': [
            'Crushing, squeezing, or pressure sensation in the chest.',
            'Pain radiating to the jaw, left arm, shoulder, or back.',
            'Severe shortness of breath or inability to complete sentences.',
            'Pale, cold, or clammy skin with sweating.',
            'Nausea, vomiting, or dizziness accompanying chest discomfort.',
            'Loss of consciousness or unresponsiveness.',
            'Irregular or very rapid heartbeat (palpitations) with chest pain.',
        ],
        'recovery': [
            'Follow all cardiac rehabilitation protocols prescribed by your cardiologist.',
            'Take prescribed medications (statins, aspirin, beta-blockers) as directed — never skip doses.',
            'Adopt a heart-healthy diet: low sodium, low saturated fat, high fibre.',
            'Engage in medically supervised, gradual exercise rehabilitation.',
            'Stop smoking immediately — it is the single most important modifiable risk factor.',
            'Attend all cardiology follow-up appointments and monitor blood pressure daily.',
        ],
        'prevention': [
            'Maintain a healthy weight and engage in regular cardiovascular exercise.',
            'Control blood pressure, cholesterol, and blood sugar levels.',
            'Quit smoking and limit alcohol consumption.',
            'Manage chronic stress through therapy, meditation, and lifestyle changes.',
            'Get regular cardiac check-ups especially after age 40 or with family history of heart disease.',
        ],
    },

    ('chest', 'bleeding'): {
        'condition': 'Chest Wound / Thoracic Laceration',
        'summary': 'A bleeding chest wound is a life-threatening emergency. Depending on depth, it may involve the lungs, heart, or major blood vessels. A penetrating chest wound can cause a pneumothorax (collapsed lung) or hemothorax (blood in the chest cavity), both of which are immediately life-threatening without emergency treatment.',
        'first_aid': [
            'CALL EMERGENCY SERVICES (911) IMMEDIATELY.',
            'If the wound is sucking air (making a hissing sound with breathing), cover it with a gloved hand or airtight material.',
            'Seal three sides of the wound with plastic wrap, foil, or a commercial chest seal (leave one side unsealed to vent).',
            'Position the person sitting up and leaning toward the injured side if possible.',
            'Do not remove any embedded object — stabilize it and call for help.',
            'Apply firm pressure to non-penetrating wounds with a clean cloth or gauze.',
            'Monitor breathing carefully — rate, depth, and symmetry of chest movement.',
            'Watch for signs of tension pneumothorax: worsening breathing, blue lips, trachea deviation.',
            'Keep the person warm and still; movement worsens lung collapse.',
            'Reassure the person continuously to keep breathing slow and controlled.',
            'Be prepared to perform CPR if the person stops breathing or loses a pulse.',
            'Do not leave the person alone — stay with them until emergency services arrive.',
        ],
        'avoid': [
            'Do not remove an impaled object from the chest — this can cause fatal bleeding.',
            'Do not seal all four sides of a sucking chest wound — it must vent.',
            'Do not give anything to eat or drink.',
            'Do not leave the person lying flat — semi-upright is safer for breathing.',
            'Do not delay emergency services activation for any chest wound.',
        ],
        'emergency_signs': [
            'Any penetrating wound to the chest — all are life-threatening.',
            'Sucking or gurgling sound when the person breathes.',
            'Rapidly expanding bruising across the chest wall.',
            'Increasing shortness of breath or inability to breathe effectively.',
            'Bluish discoloration of lips or fingertips (cyanosis).',
            'Loss of consciousness or absent pulse.',
            'Coughing up blood following chest trauma.',
        ],
        'recovery': [
            'Follow all post-surgical or post-hospitalization instructions rigorously.',
            'Attend pulmonary rehabilitation as prescribed to restore lung capacity.',
            'Manage pain effectively — uncontrolled pain inhibits breathing and recovery.',
            'Avoid smoking, which severely impairs lung healing.',
            'Use a spirometer as directed to exercise and strengthen the lungs.',
            'Report any new chest pain, shortness of breath, or fever immediately.',
        ],
        'prevention': [
            'Use personal protective equipment in work environments with sharp or high-velocity hazards.',
            'Practice road safety and always wear a seatbelt.',
            'Avoid handling weapons or sharp objects carelessly.',
            'Install safety barriers in construction and industrial environments.',
            'Wear chest protectors during contact sports.',
        ],
    },

    # ═══════════════════════ HAND ═══════════════════════
    ('hand', 'bleeding'): {
        'condition': 'Hand Laceration / Palmar Wound',
        'summary': 'Hand injuries with bleeding are among the most common traumatic injuries. The hand contains numerous vital structures including tendons, nerves, and blood vessels. Even wounds that appear minor may involve deep structural damage. Proper first aid and prompt medical evaluation are essential to preserve hand function.',
        'first_aid': [
            'Apply firm, direct pressure to the wound using a clean cloth or sterile gauze.',
            'Elevate the hand above heart level immediately to reduce blood flow and slow bleeding.',
            'Maintain direct pressure for at least 10–15 minutes without lifting the cloth.',
            'If cloth becomes saturated, add additional layers on top without removing the original.',
            'Inspect the wound for debris (glass, metal shards) but do not attempt deep probing.',
            'Rinse the wound gently with clean running water once bleeding is controlled.',
            'Check sensation and movement — ask the person to gently flex all fingers.',
            'Check capillary refill by pressing the fingernail — colour should return within 2 seconds.',
            'Apply a sterile dressing and bandage, not too tight.',
            'Remove rings, bracelets, or wristwatches immediately — swelling will make removal difficult later.',
            'Check tetanus vaccination status and arrange update if needed.',
            'Seek medical evaluation to rule out tendon, nerve, or vessel damage.',
        ],
        'avoid': [
            'Do not apply a tourniquet to the hand unless bleeding is severe and uncontrollable.',
            'Do not probe deep into the wound to check its depth.',
            'Do not remove large embedded objects from the hand.',
            'Do not wrap the bandage so tightly it cuts off circulation to the fingers.',
            'Do not assume a minor-looking hand wound is not serious — structural damage is often invisible.',
        ],
        'emergency_signs': [
            'Bleeding that does not stop after 15 minutes of direct pressure.',
            'Inability to bend one or more fingers (possible tendon injury).',
            'Numbness or tingling in the fingers (nerve damage).',
            'Visible tendon, bone, or fatty tissue in the wound.',
            'Wound caused by a deeply contaminated or rusty object (tetanus risk).',
            'Pale or blue fingertips with poor capillary refill.',
        ],
        'recovery': [
            'Keep the dressing clean and dry; change daily.',
            'Attend hand therapy or occupational therapy if tendon or nerve damage occurred.',
            'Perform prescribed gentle range-of-motion exercises once the wound is healing.',
            'Protect the hand from further injury during the healing period.',
            'Follow up for suture removal (typically 7–10 days for hand wounds).',
            'Report any changes in sensation, movement, or signs of infection promptly.',
        ],
        'prevention': [
            'Always use cut-resistant gloves when working with sharp tools or knives.',
            'Keep knives and sharp instruments sharp — dull blades require more force and slip more easily.',
            'Store sharp tools safely when not in use.',
            'Use appropriate guards on power tools and machinery.',
            'Pay attention to hand placement during cooking and manual work.',
        ],
    },

    ('hand', 'burn'): {
        'condition': 'Hand Burn Injury',
        'summary': 'Burns to the hand are classified as major injuries regardless of size because of the hand\'s complex anatomy and functional importance. Even a moderate burn can result in scarring, contracture, and permanent loss of fine motor function. All but the most superficial hand burns should receive emergency medical evaluation.',
        'first_aid': [
            'Remove the hand from the burn source immediately.',
            'Cool the burn under cool (not cold) running water for 20 minutes — start this within 3 hours of the burn.',
            'Remove all jewelry, rings, and bracelets from the hand before swelling begins.',
            'Do NOT apply ice, butter, oil, toothpaste, or any home remedy.',
            'After cooling, cover the hand loosely with cling film or a clean plastic bag over the hand.',
            'Do not break any blisters — they form a natural protective barrier.',
            'Elevate the hand above heart level to reduce swelling.',
            'Give paracetamol for pain management.',
            'Assess for depth: superficial (red, painful), partial thickness (blistered), full thickness (white, painless, leather-like).',
            'For chemical burns: brush off any dry chemical before rinsing; rinse for 20–30 minutes.',
            'Wrap the hand in a clean, loose bandage to maintain coverage during transport.',
            'Seek emergency care for any burn larger than 1cm on the hand or any full-thickness burn.',
        ],
        'avoid': [
            'Do not apply ice — it causes frostbite injury to already damaged skin.',
            'Do not use butter, toothpaste, or cream on a fresh burn.',
            'Do not break blisters — infection risk dramatically increases.',
            'Do not wrap tightly — swelling will occur and tight bandaging cuts off circulation.',
            'Do not delay medical treatment for hand burns — early care prevents contracture.',
        ],
        'emergency_signs': [
            'Burn covering any significant portion of the hand or fingers.',
            'White, brown, or black coloured burn (full thickness — may be painless).',
            'Burn caused by electricity, which can appear minor externally but be deeply destructive.',
            'Chemical burn — requires prolonged irrigation and medical evaluation.',
            'Loss of sensation in any part of the hand.',
            'Burn in a child or older adult.',
        ],
        'recovery': [
            'Follow wound care instructions from the burns unit or specialist.',
            'Begin gentle hand therapy exercises as early as your medical team permits.',
            'Use silicone gel sheets or pressure garments to manage scarring.',
            'Protect healed skin from sun exposure with SPF 50+ for 12 months.',
            'Attend occupational therapy to restore hand function and dexterity.',
            'Keep follow-up appointments with a burns specialist to monitor scar development.',
        ],
        'prevention': [
            'Always use oven gloves or heat-resistant mitts when handling hot cookware.',
            'Keep young children away from stoves, hot drinks, and steam.',
            'Wear appropriate protective gloves in chemical and industrial environments.',
            'Install stove guards to prevent pots being pulled off.',
            'Test water temperature before bathing children or elderly individuals.',
        ],
    },

    ('hand', 'cut'): {
        'condition': 'Hand Laceration / Cut Injury',
        'summary': 'Cuts to the hand are extremely common and vary widely in severity. The hand\'s complex anatomy — containing 27 bones, multiple tendons, nerves, and blood vessels in a small space — means even small cuts can cause significant functional impairment if deeper structures are affected. Careful assessment and appropriate treatment are essential.',
        'first_aid': [
            'Wash your hands before handling the wound.',
            'Apply gentle pressure with a clean cloth to control any bleeding.',
            'Rinse the wound thoroughly under clean running water for at least 1–2 minutes.',
            'Inspect the wound carefully for embedded glass, gravel, or foreign material.',
            'Assess depth and length — small superficial cuts can often be managed at home.',
            'Apply butterfly closure strips or steri-strips to hold wound edges together.',
            'Cover with a sterile non-adherent dressing and bandage.',
            'Test finger flexion and extension to check for tendon involvement.',
            'Test sensation in each finger to check for nerve involvement.',
            'Check for adequate blood flow to all fingers (colour, temperature, capillary refill).',
            'Check tetanus status and update if more than 5 years since the last booster.',
            'Seek medical evaluation for deep cuts, gaping wounds, or any concern about function.',
        ],
        'avoid': [
            'Do not use alcohol or hydrogen peroxide — they damage healthy tissue.',
            'Do not close a heavily contaminated wound — it needs professional cleaning first.',
            'Do not ignore any loss of sensation or movement in the fingers.',
            'Do not leave the wound without daily dressing changes.',
            'Do not submerge the wound in water until it has healed.',
        ],
        'emergency_signs': [
            'Gaping wound requiring sutures (edges more than 0.5cm apart).',
            'Cut over a joint (knuckle) — joint penetration is common and serious.',
            'Inability to fully extend or flex any finger after the injury.',
            'Numbness or altered sensation in the fingers distal to the cut.',
            'Wound from a bite (human or animal) — requires antibiotics.',
            'Wound from glass that may have left fragments inside.',
        ],
        'recovery': [
            'Change dressings daily and keep the wound dry.',
            'Gentle range-of-motion exercises as tolerated after 48 hours (unless tendon is involved).',
            'Suture removal typically needed at 7–10 days for hand wounds.',
            'Protect the hand from heavy use during the healing period.',
            'Report signs of infection (redness spreading, pus, fever) promptly.',
            'Scar massage with moisturizer after the wound is fully closed (2–3 weeks).',
        ],
        'prevention': [
            'Use cut-resistant gloves when handling sharp objects.',
            'Always cut away from your body when using knives.',
            'Keep sharp tools stored safely in sheaths or cases.',
            'Ensure adequate lighting when working with sharp instruments.',
            'Teach children safe knife and scissors handling techniques.',
        ],
    },

    ('hand', 'swelling'): {
        'condition': 'Hand Swelling / Possible Fracture',
        'summary': 'Swelling in the hand following injury may indicate a fracture, sprain, tendon injury, or significant soft-tissue trauma. The metacarpal bones and phalanges are commonly fractured in falls, sports injuries, and direct blows. Even without visible deformity, any significant hand swelling requires medical evaluation.',
        'first_aid': [
            'Remove all rings, bracelets, and tight items from the hand and wrist immediately.',
            'Apply RICE: Rest, Ice (wrapped), Compression, and Elevation.',
            'Apply an ice pack wrapped in cloth to the swollen area for 15–20 minutes.',
            'Elevate the hand above heart level on pillows to reduce swelling.',
            'Apply a light compressive bandage, but ensure fingers remain pink and have capillary refill.',
            'Assess the ability to move each finger through its full range of motion.',
            'Assess for point tenderness over individual bones (suggests fracture).',
            'Administer paracetamol for pain management; avoid aspirin.',
            'Immobilize the hand in a comfortable, functional position if movement causes pain.',
            'If a fracture is suspected, splint the hand in its current position — do not attempt to straighten.',
            'Seek X-ray evaluation to rule out fracture before beginning exercises.',
            'Monitor for compartment syndrome: severe pain on passive finger stretch, tight swelling, numbness.',
        ],
        'avoid': [
            'Do not attempt to push a suspected fracture back into position.',
            'Do not remove jewellery after significant swelling has already started — cut if necessary.',
            'Do not bandage too tightly — watch for signs of restricted circulation.',
            'Do not apply heat to acute swelling — it increases fluid accumulation.',
            'Do not delay seeking an X-ray for significant swelling and pain.',
        ],
        'emergency_signs': [
            'Significant deformity of the hand, fingers, or wrist.',
            'Inability to bear weight on the hand or move it at all.',
            'Extreme pain, tautness, and hardness of the hand (compartment syndrome).',
            'Numbness or tingling throughout the hand and fingers.',
            'Progressive increase in swelling despite elevation and ice.',
            'Open wound over a swollen area (possible open fracture — emergency).',
        ],
        'recovery': [
            'Follow the immobilization plan prescribed by the orthopaedic specialist.',
            'Begin hand therapy exercises as directed — do not delay mobilization unnecessarily.',
            'Attend all follow-up X-ray appointments to monitor fracture healing.',
            'Manage pain and swelling with prescribed medications and ice.',
            'Gradually return to activities based on therapist guidance.',
            'Buddy-taping or splinting may be continued during activity for 4–6 weeks.',
        ],
        'prevention': [
            'Wear wrist guards during skating, cycling, and contact sports.',
            'Use proper technique in sports to distribute impact forces safely.',
            'Ensure playing surfaces are safe and fall risks are managed.',
            'Perform hand-strengthening exercises regularly if participating in high-risk activities.',
            'Use protective gloves during manual labour.',
        ],
    },

    # ═══════════════════════ ARM ═══════════════════════
    ('arm', 'bleeding'): {
        'condition': 'Arm Laceration / Upper Limb Wound',
        'summary': 'Bleeding from the arm can range from minor abrasions to severe lacerations involving major arteries such as the brachial artery. Wounds on the inner aspect of the arm carry higher risk as major blood vessels and nerves run through this region. Early and effective haemorrhage control is the priority.',
        'first_aid': [
            'Apply firm, direct pressure to the wound with a clean cloth or sterile gauze.',
            'Elevate the arm above heart level to reduce blood pressure at the wound site.',
            'Maintain pressure for a minimum of 10–15 minutes without interruption.',
            'Add more layers on top if the cloth becomes soaked; do not remove the original.',
            'Check sensation and movement in the hand and fingers.',
            'Inspect for arterial bleeding: bright red blood pulsing in sync with heartbeat — this is an emergency.',
            'For severe or arterial bleeding, apply a tourniquet 5–7 cm above the wound.',
            'Note the exact time of tourniquet application — this is critical information for medical staff.',
            'Immobilize the arm in a comfortable position using a sling if available.',
            'Keep the person warm and still to prevent shock.',
            'Remove rings, watches, and bracelets before swelling makes removal difficult.',
            'Call emergency services if arterial bleeding is suspected or cannot be controlled.',
        ],
        'avoid': [
            'Do not remove a tourniquet once applied — only trained medical personnel should do this.',
            'Do not probe the wound or attempt to remove embedded objects.',
            'Do not use a tourniquet for minor to moderate wounds — direct pressure is sufficient.',
            'Do not give blood-thinning medications.',
            'Do not delay emergency transport for significant arm bleeding.',
        ],
        'emergency_signs': [
            'Bright red, pulsatile bleeding (arterial — immediate emergency).',
            'Bleeding that does not respond to 15 minutes of continuous direct pressure.',
            'Numbness, tingling, or weakness in the hand or fingers.',
            'Pale or cold hand distal to the wound (vascular compromise).',
            'Signs of haemorrhagic shock: pale face, rapid weak pulse, confusion, cold sweating.',
            'Visible deep structures (tendon, bone, or fat) in the wound.',
        ],
        'recovery': [
            'Follow wound care instructions from medical staff.',
            'Keep the wound elevated during the first 48 hours to reduce swelling.',
            'Attend physical therapy if nerve or tendon involvement is identified.',
            'Monitor for infection: increasing redness, warmth, pus, or fever.',
            'Suture removal: typically 7–12 days depending on location and depth.',
            'Graduated return to use of the arm as directed by your healthcare provider.',
        ],
        'prevention': [
            'Use arm guards during contact sports and martial arts.',
            'Wear long sleeves and protective clothing when working with sharp machinery.',
            'Store sharp objects safely and use them with proper technique.',
            'Ensure adequate lighting in work environments to prevent accidents.',
            'Use machine guards and safe operating procedures in industrial settings.',
        ],
    },

    ('arm', 'swelling'): {
        'condition': 'Arm Swelling / Possible Fracture or Sprain',
        'summary': 'Swelling in the arm following injury commonly indicates a fracture of the humerus, radius, or ulna, or significant soft-tissue injury. The forearm (radius and ulna) is particularly prone to fracture after falls on an outstretched hand. Any significant swelling with pain and reduced function warrants X-ray evaluation.',
        'first_aid': [
            'Have the person stop all activity and sit or lie comfortably.',
            'Support the arm in the position of greatest comfort — do not try to straighten a deformed limb.',
            'Apply RICE protocol: Rest, Ice (wrapped), Compression (light), Elevation.',
            'Apply an ice pack wrapped in cloth to the swollen area for 15–20 minutes.',
            'Fashion a basic sling using a scarf or triangular bandage to support the arm against the body.',
            'Check circulation distal to the injury: pulse at wrist, capillary refill in fingers, skin colour and temperature.',
            'Check for sensation and movement in the fingers.',
            'Administer paracetamol for pain; avoid NSAIDs in the acute period if fracture is suspected.',
            'Do not attempt to reduce or realign a suspected fracture — immobilize it as found.',
            'Pad the sling for comfort and to prevent pressure on any prominent bones.',
            'Transport to an emergency department or urgent care for X-ray assessment.',
            'Reassess the circulation distal to the injury every 15–20 minutes.',
        ],
        'avoid': [
            'Do not attempt to manually reduce or correct a deformed arm.',
            'Do not apply ice directly to skin — always wrap in cloth.',
            'Do not allow the person to use the arm until fracture is ruled out.',
            'Do not ignore increasing pain, numbness, or coldness in the hand.',
            'Do not bandage too tightly — regular circulation checks are essential.',
        ],
        'emergency_signs': [
            'Obvious deformity of the arm (abnormal angulation or rotation).',
            'Bone visible through the skin (open fracture — emergency).',
            'Cold, pale, or blue hand distal to the injury (vascular compromise).',
            'Progressive severe pain despite immobilization (compartment syndrome risk).',
            'Absent pulse at the wrist after arm injury.',
            'Inability to move the arm or fingers at all.',
        ],
        'recovery': [
            'Follow the prescribed immobilization period — typically 4–8 weeks for most arm fractures.',
            'Attend physiotherapy once cleared to begin gentle mobilization.',
            'Perform prescribed exercises to prevent muscle atrophy and stiffness.',
            'Monitor for delayed complications: nonunion, malunion, or post-traumatic arthritis.',
            'Protect the arm from re-injury during the healing period.',
            'Follow up with orthopaedics for repeat X-rays to confirm healing progress.',
        ],
        'prevention': [
            'Wear wrist and forearm guards in contact sports, skiing, and roller sports.',
            'Improve bone density through calcium and vitamin D intake and weight-bearing exercise.',
            'Use proper falling technique — never fall on a fully outstretched hand.',
            'Reduce fall risks in the home especially for elderly individuals.',
            'Wear appropriate protective equipment in physically demanding jobs.',
        ],
    },

    ('arm', 'burn'): {
        'condition': 'Arm Burn Injury',
        'summary': 'Burns to the arm are common in both domestic and occupational settings. Arm burns can affect the skin, subcutaneous tissues, and in severe cases, muscle and bone. The extent, depth, and location of the burn determine the severity. Burns near joints require special attention due to the risk of contracture and functional limitation.',
        'first_aid': [
            'Remove the person from the burn source and ensure scene safety.',
            'Cool the burn immediately under cool running water for 20 minutes.',
            'Do not use ice, cold packs, butter, oil, or any other substance on the burn.',
            'Remove watches, rings, and bracelets from the arm before swelling begins.',
            'Do not remove clothing stuck to the burned skin — cut around it.',
            'Cover the cooled burn loosely with cling film or a clean non-fluffy dressing.',
            'Do not break any blisters.',
            'Elevate the arm slightly above heart level to minimize swelling.',
            'Administer paracetamol for pain as needed.',
            'Assess for full thickness burns: white, brown, or black coloration; absent pain sensation.',
            'Assess whether the burn crosses any joint surfaces — this requires specialist review.',
            'Seek emergency care for circumferential burns (around the entire arm) — they can cut off circulation.',
        ],
        'avoid': [
            'Do not use ice, butter, toothpaste, or cold packs.',
            'Do not break blisters or peel away burnt skin.',
            'Do not wrap the burn tightly — swelling will compromise circulation.',
            'Do not underestimate burns near joints — contracture risk is significant.',
            'Do not delay medical care for any burn covering more than a small area.',
        ],
        'emergency_signs': [
            'Circumferential burn around the arm or forearm (cuts off circulation).',
            'Burn over a joint surface (elbow, wrist).',
            'Full-thickness burn (white, brown, leathery, or painless).',
            'Electrical burn to the arm — internal damage is often far greater than external appearance.',
            'Burn with associated numbness, weakness, or absent pulse in the hand.',
            'Burn from chemical agents requiring specialized decontamination.',
        ],
        'recovery': [
            'Attend all dressing change appointments as prescribed by the burns team.',
            'Begin physiotherapy early to maintain joint range of motion and prevent contracture.',
            'Use prescribed scar management treatments: pressure garments, silicone sheets.',
            'Protect healing skin from sun exposure using SPF 50+.',
            'Maintain hydration and a high-protein diet to support skin healing.',
            'Psychological support may be valuable for significant or visible burns.',
        ],
        'prevention': [
            'Wear long sleeves and flame-resistant clothing in high-risk environments.',
            'Use heat-resistant gloves and arm guards when working near heat sources.',
            'Follow safe chemical handling procedures including PPE.',
            'Keep children away from open flames, hot liquids, and electrical sources.',
            'Ensure kitchen safety: pot handles turned inward, away from edges.',
        ],
    },

    # ═══════════════════════ LEG ═══════════════════════
    ('leg', 'bleeding'): {
        'condition': 'Leg Wound / Lower Limb Laceration',
        'summary': 'Leg lacerations can vary from minor cuts to severe wounds involving major vessels such as the femoral artery. Wounds on the inner thigh carry particular danger as the femoral artery and vein run through this region. Rapid haemorrhage control is critical, especially for thigh injuries where blood loss can be rapid and life-threatening.',
        'first_aid': [
            'Have the person lie down flat to prevent fainting from blood loss.',
            'Apply firm, direct pressure to the wound with a clean cloth or sterile gauze pad.',
            'Elevate the leg above heart level using rolled clothing or a bag for support.',
            'Maintain pressure for a minimum of 15 minutes without lifting.',
            'If bleeding is severe and from the upper thigh, apply a tourniquet 5–7 cm above the wound.',
            'Note the time of tourniquet application and mark it on the person\'s skin.',
            'Add more gauze layers if cloth becomes saturated — do not remove the original.',
            'Check circulation below the wound: assess foot temperature, colour, and sensation.',
            'Monitor for signs of shock: pale or grey skin, rapid breathing, confusion.',
            'Keep the person warm using a blanket or coat.',
            'Do not remove the tourniquet once applied.',
            'Call emergency services for significant leg wounds, especially involving the thigh.',
        ],
        'avoid': [
            'Do not remove a tourniquet once it has been applied to control significant bleeding.',
            'Do not remove embedded objects from the wound.',
            'Do not prop the head up if the person is showing signs of shock — keep them flat.',
            'Do not give blood-thinning medications.',
            'Do not underestimate thigh wounds — the femoral artery can cause fatal blood loss in minutes.',
        ],
        'emergency_signs': [
            'Bright red, pulsatile (arterial) bleeding — especially from the inner thigh.',
            'Bleeding that does not slow after 10–15 minutes of firm direct pressure.',
            'Pale, cold foot or absent pedal pulse after leg injury.',
            'Signs of haemorrhagic shock: extreme pallor, weak rapid pulse, altered consciousness.',
            'Visible deep structures (tendon, bone, fat) in the wound.',
            'Significant blood loss: pool of blood larger than a large hand.',
        ],
        'recovery': [
            'Keep the leg elevated when resting to reduce swelling.',
            'Follow wound care instructions carefully — change dressings as directed.',
            'Monitor for infection: spreading redness, warmth, pus, or fever.',
            'Attend physiotherapy if muscle or tendon involvement occurred.',
            'Suture removal typically at 10–14 days for leg wounds.',
            'Graduated weight-bearing and walking as directed by your care team.',
        ],
        'prevention': [
            'Wear shin guards and protective gear during contact sports.',
            'Use appropriate cut-resistant clothing when working with machinery.',
            'Keep work and play areas clear of sharp hazards.',
            'Wear reflective clothing when cycling or walking near traffic.',
            'Practice safe tool handling to prevent workplace leg injuries.',
        ],
    },

    ('leg', 'swelling'): {
        'condition': 'Leg Swelling / Sprain or Possible Fracture',
        'summary': 'Swelling in the leg after injury can indicate a sprain, muscle tear, fracture of the tibia or fibula, or a joint injury. Additionally, leg swelling without trauma may indicate deep vein thrombosis (DVT), a serious condition requiring urgent evaluation. Any significant leg swelling deserves proper assessment.',
        'first_aid': [
            'Have the person stop activity and rest in a comfortable position.',
            'Apply the RICE protocol: Rest the leg, apply Ice (wrapped), use Compression bandage, Elevate.',
            'Apply an ice pack wrapped in a cloth for 15–20 minutes every 2 hours for the first 48 hours.',
            'Apply a light compression bandage from foot upward to reduce swelling — not too tight.',
            'Elevate the leg above heart level using pillows.',
            'Check for deformity, bruising pattern, point tenderness over bones.',
            'Assess the ability to bear weight — complete inability suggests possible fracture.',
            'Check circulation: normal foot pulse, capillary refill in toenails, sensation.',
            'Administer paracetamol for pain.',
            'Assist with crutches or support walking to prevent full weight-bearing if painful.',
            'Seek X-ray evaluation if the person cannot bear weight or there is marked tenderness over bone.',
            'If DVT is suspected (calf pain and swelling without trauma), seek emergency care — this is a clot.',
        ],
        'avoid': [
            'Do not apply heat to acute swelling in the first 48 hours.',
            'Do not bear full weight on a suspected fractured leg.',
            'Do not ignore calf swelling following bed rest, travel, or immobility — DVT risk.',
            'Do not bandage too tightly — check regularly for changes in colour or sensation.',
            'Do not delay evaluation of significant leg swelling with severe pain.',
        ],
        'emergency_signs': [
            'Inability to bear any weight on the leg after injury.',
            'Obvious deformity of the leg (fracture).',
            'Calf swelling and pain that is warm and tender (deep vein thrombosis).',
            'Leg swelling with accompanying shortness of breath (pulmonary embolism).',
            'Absent pulse in the foot after leg injury.',
            'Rapidly worsening, severe pain despite rest and elevation.',
        ],
        'recovery': [
            'For sprains: RICE protocol for 48 hours, then gentle mobilization.',
            'For fractures: follow the immobilization protocol prescribed (cast, brace, or surgery).',
            'Begin physiotherapy as soon as your provider allows — early mobilization improves outcomes.',
            'Use crutches as prescribed to protect the healing limb.',
            'Progressive weight-bearing following guidance from your physiotherapist.',
            'Strengthening and proprioception exercises to prevent re-injury.',
        ],
        'prevention': [
            'Warm up thoroughly before sports or exercise.',
            'Wear appropriate footwear with ankle support for high-risk activities.',
            'Use shin guards and protective bracing when playing contact sports.',
            'Perform regular strengthening exercises for the lower limb muscles.',
            'Ensure playing surfaces are level and well-maintained.',
        ],
    },

    # ═══════════════════════ FOOT ═══════════════════════
    ('foot', 'swelling'): {
        'condition': 'Ankle Sprain / Foot Swelling',
        'summary': 'Swelling of the foot or ankle following a twisting injury, fall, or impact most commonly represents a sprained ligament. Ankle sprains are the most common musculoskeletal injury. However, significant swelling with point tenderness over bone may indicate a fracture, and the two conditions can be difficult to distinguish without X-ray.',
        'first_aid': [
            'Have the person stop all activity and sit or lie down immediately.',
            'Apply RICE: Rest the foot, Ice (wrapped in cloth) for 15–20 minutes, Compression bandage, Elevation.',
            'Elevate the foot and ankle above heart level on pillows.',
            'Apply the ice pack for 15–20 minutes every 2 hours during the first 48 hours.',
            'Apply a figure-of-eight compression bandage starting at the toes and working upward.',
            'Ensure the bandage is firm but not so tight it causes tingling or pain in the toes.',
            'Check regularly that toes remain pink and warm.',
            'Remove shoes and socks gently and check the ankle for deformity or bruising pattern.',
            'Administer paracetamol for pain.',
            'Assess ability to bear weight — if completely unable, suspect fracture.',
            'Apply the Ottawa Ankle Rules: point tenderness over the base of the 5th metatarsal or fibula tip suggests fracture.',
            'Seek X-ray evaluation for any significant impact, inability to bear weight, or severe tenderness.',
        ],
        'avoid': [
            'Do not apply heat in the first 48 hours.',
            'Do not massage an acutely sprained ankle — it increases swelling.',
            'Do not walk on a potentially fractured foot.',
            'Do not ignore foot swelling following inactivity or long-haul travel (DVT risk).',
            'Do not strap the ankle too tightly — monitor toe colour and sensation.',
        ],
        'emergency_signs': [
            'Complete inability to bear weight (may indicate fracture).',
            'Visible deformity of the ankle or foot.',
            'Severe, immediate swelling that is rapidly expanding.',
            'Point tenderness directly over the fibula tip, lateral malleolus, or 5th metatarsal base.',
            'Pale or blue toes with absent pulse or sensation.',
            'Open wound over a swollen area (open fracture).',
        ],
        'recovery': [
            'Grade 1 sprain: 1–3 weeks of RICE, gentle mobilization from day 2.',
            'Grade 2 sprain: 3–6 weeks with bracing, physiotherapy, and graduated exercises.',
            'Grade 3 sprain / fracture: specialist management, possible immobilization or surgery.',
            'Perform proprioceptive (balance) exercises to prevent re-injury.',
            'Use functional ankle bracing for return to sport for 4–6 weeks.',
            'Strengthen peroneal muscles with resistance band exercises.',
        ],
        'prevention': [
            'Wear supportive footwear appropriate for the activity.',
            'Warm up before physical activity and cool down afterwards.',
            'Perform ankle strengthening and proprioception exercises regularly.',
            'Be cautious on uneven surfaces especially in low-light conditions.',
            'Use ankle braces for high-risk sports if you have a history of ankle sprains.',
        ],
    },

    ('foot', 'pain'): {
        'condition': 'Foot Pain / Plantar or Metatarsal Injury',
        'summary': 'Foot pain is extremely common and can result from a range of causes including plantar fasciitis, stress fractures, gout, nerve entrapment, or soft-tissue injury. The mechanism of pain onset (acute vs. gradual), location (heel, arch, ball, toes), and associated features help determine the cause and appropriate management.',
        'first_aid': [
            'Rest the foot immediately and avoid all weight-bearing that worsens pain.',
            'Apply an ice pack wrapped in cloth to the painful area for 15–20 minutes.',
            'Elevate the foot above heart level when resting.',
            'Administer paracetamol or ibuprofen as appropriate for pain.',
            'Check for visible swelling, bruising, deformity, or skin changes.',
            'Assess whether pain came on suddenly (acute injury) or gradually (overuse/inflammation).',
            'Inspect footwear — poor support, too tight, or worn-out footwear is a common cause.',
            'Check for abnormal skin sensations: tingling or numbness may indicate nerve involvement.',
            'If gout is suspected (severe, sudden joint pain, warmth, and redness), seek medical review — avoid cherries and high-purine food triggers.',
            'Avoid any activity that reproduces the pain.',
            'Gentle foot exercises (ankle circles, toe stretches) may help if pain is mild and tolerable.',
            'Seek medical review if pain is severe, persistent beyond 48 hours, or associated with swelling and bruising.',
        ],
        'avoid': [
            'Do not ignore severe or sudden-onset foot pain — it may indicate fracture or gout flare.',
            'Do not continue exercise through significant foot pain.',
            'Do not apply heat in the acute phase if inflammation is present.',
            'Do not use ill-fitting footwear during recovery.',
            'Do not delay evaluation of foot pain in diabetic patients — infection risk is high.',
        ],
        'emergency_signs': [
            'Acute, severe foot pain following a fall or twisting injury (possible fracture).',
            'Inability to bear any weight on the foot.',
            'Visible deformity of the foot or toes.',
            'Red, hot, extremely tender single joint, especially in the big toe (acute gout).',
            'Foot pain in a diabetic patient with skin breakdown (diabetic foot emergency).',
            'Severe pain with pallor and absent pulse (vascular emergency).',
        ],
        'recovery': [
            'Rest from aggravating activities for a minimum of 48–72 hours.',
            'Gradual return to weight-bearing as tolerated.',
            'Use appropriate orthotics or insoles to provide arch support.',
            'Stretching exercises for plantar fascia and calf muscles if applicable.',
            'Physiotherapy assessment for chronic or recurrent foot pain.',
            'Avoid barefoot walking on hard surfaces during recovery.',
        ],
        'prevention': [
            'Wear supportive footwear with proper arch support and cushioning.',
            'Gradually increase exercise intensity — avoid sudden spikes in activity level.',
            'Maintain a healthy weight to reduce load on the feet.',
            'Stretch calves and plantar fascia regularly, especially before morning activity.',
            'Replace worn-out shoes regularly.',
        ],
    },

    # ═══════════════════════ BACK ═══════════════════════
    ('back', 'pain'): {
        'condition': 'Back Pain / Musculoskeletal or Spinal Injury',
        'summary': 'Back pain is one of the most common health complaints worldwide. It can range from mild muscle strain to serious conditions such as disc herniation, spinal stenosis, or in severe trauma, spinal cord injury. The presence of neurological symptoms (numbness, weakness, bladder or bowel changes) indicates potential nerve or spinal cord involvement and requires emergency evaluation.',
        'first_aid': [
            'Have the person rest in the most comfortable position — typically lying on their back or side with knees slightly bent.',
            'If the injury followed significant trauma (fall, collision), do not move the person — call emergency services and immobilize the spine.',
            'For non-traumatic back pain, encourage the person to find a pain-relieving position.',
            'Apply an ice pack wrapped in cloth to the painful area for 15–20 minutes to reduce inflammation.',
            'After 48 hours, switch to a warm heat pack for muscle relaxation.',
            'Administer paracetamol or ibuprofen (as appropriate) for pain.',
            'Assist with log-rolling technique if the person must be moved after trauma.',
            'Check neurological status: sensation and movement in both legs, bladder and bowel control.',
            'Encourage the person not to remain in bed for extended periods — brief periods of rest alternating with gentle movement are recommended for most back pain.',
            'Support with cushions: place a pillow under the knees when lying on the back, or between knees when lying on the side.',
            'Do not manipulate the spine at the site of pain.',
            'Seek medical evaluation for any back pain with neurological symptoms or following significant trauma.',
        ],
        'avoid': [
            'Do not move a person with suspected spinal injury after significant trauma.',
            'Do not apply heat to acute back pain in the first 48 hours — it may worsen inflammation.',
            'Do not encourage prolonged bed rest — it delays recovery.',
            'Do not attempt to "crack" or forcibly manipulate a painful back.',
            'Do not ignore neurological symptoms such as leg weakness, numbness, or loss of bladder control.',
        ],
        'emergency_signs': [
            'Back pain following significant trauma: fall from height, road traffic accident.',
            'Numbness or tingling radiating down one or both legs (sciatica — may need urgent review).',
            'Weakness in one or both legs after back injury.',
            'Loss of bladder or bowel control (cauda equina syndrome — emergency).',
            'Back pain with fever and chills (possible spinal infection).',
            'Sudden onset severe back pain in a person over 50 (possible aortic aneurysm).',
        ],
        'recovery': [
            'Stay as active as comfortably possible — avoid prolonged bed rest.',
            'Begin physiotherapy within 48–72 hours of acute back pain onset.',
            'Use a combination of heat, gentle stretching, and movement for recovery.',
            'Maintain correct posture and ergonomic workstation setup.',
            'Core strengthening exercises (as directed) support long-term spinal health.',
            'Manage weight and avoid prolonged static postures.',
        ],
        'prevention': [
            'Maintain proper lifting technique: bend at knees, keep the back straight, hold the load close.',
            'Strengthen core muscles through regular exercise.',
            'Maintain a healthy body weight to reduce spinal load.',
            'Ensure an ergonomic work environment with appropriate seating and screen height.',
            'Stretch regularly, especially after prolonged sitting or driving.',
        ],
    },

    # ═══════════════════════ Eye/Foot/Back extras ═══════════════════════
    ('eye', 'cut'): {
        'condition': 'Ocular Laceration / Eye Cut',
        'summary': 'Any cut on or around the eye is a medical emergency. A laceration to the eyelid or globe of the eye can cause permanent vision loss if not treated promptly. Even eyelid cuts that appear simple may involve damage to the lacrimal drainage system or levator muscle and should be evaluated by an ophthalmologist.',
        'first_aid': [
            'Call emergency services or arrange immediate transport to an eye emergency department.',
            'Do NOT apply pressure to the eye itself — only to the surrounding bony orbit if bleeding.',
            'Shield the eye with a sterile eye shield or the bottom of a paper cup — not touching the eye.',
            'Instruct the person to keep both eyes still — eye movement causes the injured eye to move too.',
            'Do not attempt to remove any object embedded in the eye or eyelid.',
            'Keep the person calm and in a semi-reclined position with both eyes covered if helpful.',
            'Do not allow rubbing, touching, or pressing of the injured eye.',
            'Wash any blood from the surrounding skin gently without touching the eye.',
            'Do not apply any drops, ointment, or liquid to the eye.',
            'Record the mechanism of injury and time of occurrence.',
            'Do not allow eating or drinking in case surgery is needed urgently.',
            'Seek immediate ophthalmological care — time is critical for vision preservation.',
        ],
        'avoid': [
            'Never apply pressure to a penetrating eye injury.',
            'Do not attempt to close or suture the eyelid in the field.',
            'Do not use contact lenses or eye drops.',
            'Do not delay emergency care — eye lacerations are time-critical.',
            'Do not allow the person to drive.',
        ],
        'emergency_signs': [
            'Any visible cut or laceration on the eyeball or eyelid.',
            'Visible eye contents outside the orbit.',
            'Change in vision following eyelid trauma.',
            'Eye that no longer moves normally or is deviated.',
            'Irregular or teardrop-shaped pupil after eye trauma.',
            'Any penetrating object near or in the eye.',
        ],
        'recovery': [
            'Follow surgical and ophthalmological aftercare instructions precisely.',
            'Use all prescribed eye drops and medications as directed.',
            'Wear an eye shield during sleep to prevent accidental pressure.',
            'Avoid bending, heavy lifting, and straining during early recovery.',
            'Attend all follow-up appointments — eye healing is carefully monitored.',
            'Report any sudden decrease in vision immediately.',
        ],
        'prevention': [
            'Wear certified safety eyewear during all high-risk activities.',
            'Store sharp objects safely away from face-level access.',
            'Use face shields during grinding, welding, and power tool use.',
            'Ensure sports eyewear meets the relevant safety standard.',
            'Educate children about safe play to prevent eye injuries.',
        ],
    },

    ('foot', 'cut'): {
        'condition': 'Foot Laceration / Plantar Cut',
        'summary': 'Cuts to the foot, especially the sole, are common and carry a higher infection risk due to the foot\'s constant exposure to the ground. Sole lacerations can be deceptively deep and may involve tendons or nerves. Tetanus prophylaxis is particularly important for foot wounds contaminated by soil or debris.',
        'first_aid': [
            'Have the person sit down and elevate the foot immediately.',
            'Apply firm pressure with a clean cloth or sterile gauze to control bleeding.',
            'Maintain pressure for 10–15 minutes without interruption.',
            'Once bleeding is controlled, rinse the wound thoroughly with clean water.',
            'Carefully inspect for embedded glass, gravel, or other foreign material.',
            'Do not attempt to dig out deeply embedded material — seek medical care.',
            'Apply a sterile dressing and secure with a bandage.',
            'Elevate the foot above heart level to reduce swelling.',
            'Check sensation in the toes and ability to move the toes normally.',
            'Ensure the person does not bear weight on a heavily bandaged foot until evaluated.',
            'Check tetanus vaccination status — foot wounds from contaminated objects carry high tetanus risk.',
            'Seek medical evaluation — foot lacerations are prone to infection and often need sutures.',
        ],
        'avoid': [
            'Do not allow walking on an unprotected or heavily bleeding foot wound.',
            'Do not probe deeply into the wound for foreign bodies.',
            'Do not use alcohol inside the wound.',
            'Do not apply adhesive directly onto the wound surface.',
            'Do not ignore signs of infection — foot wounds can develop serious cellulitis or osteomyelitis.',
        ],
        'emergency_signs': [
            'Deep cut with visible tendon, bone, or fat pad.',
            'Wound from a nail or deeply penetrating object (high tetanus and infection risk).',
            'Inability to flex or extend the toes after the injury.',
            'Spreading redness, warmth, or red streaks moving up the foot or leg (cellulitis).',
            'Wound in a diabetic patient — even minor foot wounds are diabetic emergencies.',
            'Foreign body that cannot be removed with gentle irrigation.',
        ],
        'recovery': [
            'Keep the wound clean and dry, changing dressings daily.',
            'Protect the foot from weight-bearing until healed.',
            'Wear appropriate footwear to protect the dressing.',
            'Complete any prescribed antibiotic course fully.',
            'Monitor closely for signs of infection daily.',
            'Suture removal at 10–14 days for plantar wounds (longer healing time).',
        ],
        'prevention': [
            'Wear appropriate footwear — never walk barefoot in unknown environments.',
            'Inspect the ground before walking in low-light or outdoor environments.',
            'Keep living and working areas clear of sharp debris.',
            'Wear protective footwear in workshops and construction sites.',
            'Use footwear with thick soles when walking on beaches or rough terrain.',
        ],
    },
}


# ── Medications Database ────────────────────────────────────────────
# Each entry: list of dicts with name, dose, freq, use, ok (True=recommended, False=avoid)
MEDICATIONS_DB = {

    ('head', 'bleeding'): [
        {'name': 'Paracetamol (Dolo 650 / Calpol)', 'dose': '500–650 mg', 'freq': 'Every 4–6 hrs (max 4g/day)', 'use': 'Pain relief', 'ok': True},
        {'name': 'Betadine / Povidone-Iodine', 'dose': 'Topical', 'freq': 'Apply around wound edge only', 'use': 'Antiseptic', 'ok': True},
        {'name': 'Aspirin', 'dose': 'AVOID', 'freq': '—', 'use': 'Thins blood — worsens scalp bleeding', 'ok': False},
        {'name': 'Ibuprofen / Brufen / Advil', 'dose': 'AVOID', 'freq': '—', 'use': 'Impairs platelet function — increases bleeding', 'ok': False},
    ],
    ('head', 'pain'): [
        {'name': 'Paracetamol (Dolo 650 / Calpol)', 'dose': '500–1000 mg', 'freq': 'Every 4–6 hrs (max 4g/day)', 'use': 'First-line headache relief', 'ok': True},
        {'name': 'Ibuprofen (Brufen 400mg)', 'dose': '400 mg', 'freq': 'Every 6–8 hrs with food', 'use': 'Anti-inflammatory headache relief', 'ok': True},
        {'name': 'ORS (Electral / Enerzal)', 'dose': '1 sachet in 1L water', 'freq': 'Sip throughout the day', 'use': 'Dehydration-related headache', 'ok': True},
        {'name': 'Aspirin (in children <16)', 'dose': 'AVOID', 'freq': '—', 'use': 'Risk of Reye syndrome in children', 'ok': False},
    ],
    ('head', 'cut'): [
        {'name': 'Paracetamol (Dolo 650)', 'dose': '500–650 mg', 'freq': 'Every 4–6 hrs', 'use': 'Pain relief', 'ok': True},
        {'name': 'Betadine / Povidone-Iodine', 'dose': 'Topical', 'freq': 'Apply around wound — not inside', 'use': 'Antiseptic cleaning', 'ok': True},
        {'name': 'Neosporin / Soframycin (antibiotic ointment)', 'dose': 'Thin layer topical', 'freq': 'After each dressing change', 'use': 'Prevents infection', 'ok': True},
        {'name': 'Aspirin / NSAIDs', 'dose': 'AVOID', 'freq': '—', 'use': 'Increase bleeding at wound site', 'ok': False},
    ],
    ('head', 'bruise'): [
        {'name': 'Paracetamol (Dolo 650)', 'dose': '500–650 mg', 'freq': 'Every 4–6 hrs', 'use': 'Pain relief', 'ok': True},
        {'name': 'Arnica Gel (Arnigel / SBL Arnica)', 'dose': 'Topical — small amount', 'freq': 'Apply 2–3 times daily over bruise', 'use': 'Reduces bruising and swelling', 'ok': True},
        {'name': 'Aspirin', 'dose': 'AVOID', 'freq': '—', 'use': 'Blood thinning worsens bruising', 'ok': False},
        {'name': 'Ibuprofen (first 48 hrs)', 'dose': 'AVOID initially', 'freq': '—', 'use': 'May worsen internal bleeding in first 48 hrs', 'ok': False},
    ],
    ('head', 'swelling'): [
        {'name': 'Paracetamol (Dolo 650)', 'dose': '500–650 mg', 'freq': 'Every 4–6 hrs', 'use': 'Pain and discomfort relief', 'ok': True},
        {'name': 'Aspirin / Ibuprofen (first 48 hrs)', 'dose': 'AVOID', 'freq': '—', 'use': 'Promote bleeding — worsen hematoma', 'ok': False},
    ],
    ('head', 'burn'): [
        {'name': 'Paracetamol (Dolo 650)', 'dose': '500–1000 mg', 'freq': 'Every 4–6 hrs', 'use': 'Pain relief for burn', 'ok': True},
        {'name': 'Silver Sulfadiazine 1% cream (Silverex)', 'dose': 'Thin layer topical', 'freq': 'After wound cooling — under dressing', 'use': 'Burn wound protection & antibacterial', 'ok': True},
        {'name': 'Ice / Iced water on burn', 'dose': 'AVOID', 'freq': '—', 'use': 'Causes frostbite — damages burned tissue', 'ok': False},
        {'name': 'Butter / Toothpaste / Oil on burn', 'dose': 'AVOID', 'freq': '—', 'use': 'Traps heat and promotes infection', 'ok': False},
    ],

    ('eye', 'pain'): [
        {'name': 'Artificial Tears (Refresh / Systane)', 'dose': '1–2 drops', 'freq': 'Every 2–4 hrs', 'use': 'Soothe and lubricate irritated eye', 'ok': True},
        {'name': 'Paracetamol (Dolo 650)', 'dose': '500–650 mg', 'freq': 'Every 4–6 hrs', 'use': 'Mild pain relief', 'ok': True},
        {'name': 'Unprescribed antibiotic eye drops', 'dose': 'AVOID', 'freq': '—', 'use': 'Use only if prescribed by ophthalmologist', 'ok': False},
        {'name': 'Contact lenses during pain', 'dose': 'AVOID', 'freq': '—', 'use': 'Worsen corneal irritation and injury', 'ok': False},
    ],
    ('eye', 'bleeding'): [
        {'name': 'No self-medication', 'dose': 'EMERGENCY', 'freq': '—', 'use': 'Ocular bleeding requires immediate hospital care', 'ok': True},
        {'name': 'Eye drops / any liquids', 'dose': 'AVOID unless chemical flush', 'freq': '—', 'use': 'Do not apply anything to a bleeding eye', 'ok': False},
        {'name': 'Aspirin / blood thinners', 'dose': 'AVOID', 'freq': '—', 'use': 'Worsen intraocular bleeding', 'ok': False},
    ],
    ('eye', 'cut'): [
        {'name': 'No self-medication — Emergency', 'dose': 'EMERGENCY', 'freq': '—', 'use': 'Eye lacerations require immediate surgical care', 'ok': True},
        {'name': 'Any eye drops or ointment', 'dose': 'AVOID', 'freq': '—', 'use': 'Do not apply anything to a cut eye', 'ok': False},
    ],

    ('chest', 'pain'): [
        {'name': 'Aspirin 325mg (Ecosprin / Disprin)', 'dose': '325 mg — CHEW, do not swallow whole', 'freq': 'Single dose immediately if no allergy', 'use': 'Anti-platelet — cardiac emergency first aid', 'ok': True},
        {'name': 'Sorbitrate (Nitroglycerine) — if prescribed', 'dose': 'Sub-lingual tablet only if prescribed', 'freq': 'One tablet under tongue', 'use': 'Angina relief — only if doctor-prescribed', 'ok': True},
        {'name': 'Food or water during chest pain', 'dose': 'AVOID', 'freq': '—', 'use': 'Surgery may be required — keep stomach empty', 'ok': False},
        {'name': 'Any other pain medication without medical advice', 'dose': 'AVOID', 'freq': '—', 'use': 'Can mask symptoms and complicate treatment', 'ok': False},
    ],
    ('chest', 'bleeding'): [
        {'name': 'No self-medication — Call 911 Immediately', 'dose': 'EMERGENCY', 'freq': '—', 'use': 'Chest wounds require immediate emergency surgery', 'ok': True},
        {'name': 'Food, water, or oral medications', 'dose': 'AVOID', 'freq': '—', 'use': 'Emergency surgery may be required', 'ok': False},
    ],

    ('hand', 'bleeding'): [
        {'name': 'Paracetamol (Dolo 650)', 'dose': '500–650 mg', 'freq': 'Every 4–6 hrs', 'use': 'Pain relief', 'ok': True},
        {'name': 'Betadine / Povidone-Iodine', 'dose': 'Topical', 'freq': 'Apply around wound edge — once cleaned', 'use': 'Antiseptic', 'ok': True},
        {'name': 'Aspirin / Ibuprofen', 'dose': 'AVOID', 'freq': '—', 'use': 'Impair clotting — worsen hand bleeding', 'ok': False},
    ],
    ('hand', 'burn'): [
        {'name': 'Paracetamol (Dolo 650)', 'dose': '500–1000 mg', 'freq': 'Every 4–6 hrs', 'use': 'Pain relief', 'ok': True},
        {'name': 'Silver Sulfadiazine 1% cream (Silverex)', 'dose': 'Thin layer after cooling', 'freq': 'Once daily under sterile dressing', 'use': 'Antibacterial burn protection', 'ok': True},
        {'name': 'Aloe Vera gel (for minor burns only)', 'dose': 'Thin layer topical', 'freq': '2–3 times daily', 'use': 'Soothing and moisturising', 'ok': True},
        {'name': 'Butter / oil / toothpaste on burn', 'dose': 'AVOID', 'freq': '—', 'use': 'Traps heat, promotes infection', 'ok': False},
        {'name': 'Breaking blisters', 'dose': 'AVOID', 'freq': '—', 'use': 'Blisters protect against infection', 'ok': False},
    ],
    ('hand', 'cut'): [
        {'name': 'Paracetamol (Dolo 650)', 'dose': '500–650 mg', 'freq': 'Every 4–6 hrs', 'use': 'Pain relief', 'ok': True},
        {'name': 'Betadine / Povidone-Iodine', 'dose': 'Topical', 'freq': 'After rinsing — apply around wound', 'use': 'Antiseptic', 'ok': True},
        {'name': 'Neosporin / Soframycin ointment', 'dose': 'Thin layer', 'freq': 'Each dressing change', 'use': 'Antibiotic — prevents infection', 'ok': True},
        {'name': 'Alcohol / Hydrogen Peroxide inside wound', 'dose': 'AVOID', 'freq': '—', 'use': 'Damages healing tissue', 'ok': False},
    ],
    ('hand', 'swelling'): [
        {'name': 'Paracetamol (Dolo 650)', 'dose': '500–650 mg', 'freq': 'Every 4–6 hrs', 'use': 'Pain relief', 'ok': True},
        {'name': 'Ibuprofen (Brufen 400mg)', 'dose': '400 mg', 'freq': 'Every 8 hrs with food (if fracture ruled out)', 'use': 'Anti-inflammatory — reduces swelling', 'ok': True},
        {'name': 'Diclofenac Gel (Voltaren / Voveran)', 'dose': 'Topical — small amount', 'freq': '3 times daily over swollen area', 'use': 'Topical anti-inflammatory', 'ok': True},
        {'name': 'Heat application (first 48 hrs)', 'dose': 'AVOID', 'freq': '—', 'use': 'Increases swelling in acute phase', 'ok': False},
    ],

    ('arm', 'bleeding'): [
        {'name': 'Paracetamol (Dolo 650)', 'dose': '500–650 mg', 'freq': 'Every 4–6 hrs', 'use': 'Pain relief', 'ok': True},
        {'name': 'Betadine topical antiseptic', 'dose': 'Topical', 'freq': 'Around wound after bleeding controlled', 'use': 'Antiseptic', 'ok': True},
        {'name': 'Aspirin / Blood thinners', 'dose': 'AVOID', 'freq': '—', 'use': 'Worsen limb bleeding significantly', 'ok': False},
    ],
    ('arm', 'swelling'): [
        {'name': 'Paracetamol (Dolo 650)', 'dose': '500–650 mg', 'freq': 'Every 4–6 hrs', 'use': 'Pain relief', 'ok': True},
        {'name': 'Ibuprofen (Brufen 400mg)', 'dose': '400 mg', 'freq': 'Every 8 hrs with food', 'use': 'Reduces swelling and inflammation', 'ok': True},
        {'name': 'Diclofenac Gel (Voveran)', 'dose': 'Topical', 'freq': '2–3 times daily on swollen area', 'use': 'Topical pain and swelling relief', 'ok': True},
        {'name': 'Reducing immobilization without advice', 'dose': 'AVOID', 'freq': '—', 'use': 'Maintain immobilization until fracture ruled out', 'ok': False},
    ],
    ('arm', 'burn'): [
        {'name': 'Paracetamol (Dolo 650)', 'dose': '500–1000 mg', 'freq': 'Every 4–6 hrs', 'use': 'Pain relief', 'ok': True},
        {'name': 'Silver Sulfadiazine cream (Silverex)', 'dose': 'Thin layer after cooling', 'freq': 'Under dressing — once daily', 'use': 'Antibacterial protection for burn', 'ok': True},
        {'name': 'Ice / cold packs directly on burn', 'dose': 'AVOID', 'freq': '—', 'use': 'Causes frostbite — damages tissue', 'ok': False},
    ],

    ('leg', 'bleeding'): [
        {'name': 'Paracetamol (Dolo 650)', 'dose': '500–650 mg', 'freq': 'Every 4–6 hrs', 'use': 'Pain relief', 'ok': True},
        {'name': 'Betadine topical', 'dose': 'Topical', 'freq': 'Around wound after bleeding controlled', 'use': 'Antiseptic', 'ok': True},
        {'name': 'Aspirin / blood thinners', 'dose': 'AVOID', 'freq': '—', 'use': 'Critical: femoral artery bleeds are fatal', 'ok': False},
    ],
    ('leg', 'swelling'): [
        {'name': 'Paracetamol (Dolo 650)', 'dose': '500–650 mg', 'freq': 'Every 4–6 hrs', 'use': 'Pain relief', 'ok': True},
        {'name': 'Ibuprofen (Brufen 400mg)', 'dose': '400 mg', 'freq': 'Every 8 hrs with food', 'use': 'Reduces inflammation and swelling', 'ok': True},
        {'name': 'Diclofenac Gel (Voveran)', 'dose': 'Topical', 'freq': '2–3 times daily on swollen area', 'use': 'Topical anti-inflammatory', 'ok': True},
        {'name': 'Heat in first 48 hrs', 'dose': 'AVOID', 'freq': '—', 'use': 'Worsens acute swelling', 'ok': False},
        {'name': 'Weight-bearing on suspect fracture', 'dose': 'AVOID', 'freq': '—', 'use': 'Risk of displacement', 'ok': False},
    ],

    ('foot', 'swelling'): [
        {'name': 'Paracetamol (Dolo 650)', 'dose': '500–650 mg', 'freq': 'Every 4–6 hrs', 'use': 'Pain relief', 'ok': True},
        {'name': 'Ibuprofen (Brufen 400mg)', 'dose': '400 mg', 'freq': 'Every 8 hrs with food', 'use': 'Reduces ankle/foot swelling', 'ok': True},
        {'name': 'Diclofenac Gel (Voveran / Voltaren)', 'dose': 'Topical', 'freq': '2–3 times daily on ankle', 'use': 'Topical anti-inflammatory', 'ok': True},
        {'name': 'Heat application in first 48 hrs', 'dose': 'AVOID', 'freq': '—', 'use': 'Increases swelling in acute phase', 'ok': False},
        {'name': 'Massaging a sprained ankle', 'dose': 'AVOID', 'freq': '—', 'use': 'Increases swelling and pain', 'ok': False},
    ],
    ('foot', 'pain'): [
        {'name': 'Paracetamol (Dolo 650)', 'dose': '500–650 mg', 'freq': 'Every 4–6 hrs', 'use': 'First-line foot pain relief', 'ok': True},
        {'name': 'Ibuprofen (Brufen 400mg)', 'dose': '400 mg', 'freq': 'Every 8 hrs with food', 'use': 'Anti-inflammatory for plantar pain', 'ok': True},
        {'name': 'Diclofenac Gel (Voveran)', 'dose': 'Topical', 'freq': '2–3 times daily on painful area', 'use': 'Topical pain relief', 'ok': True},
        {'name': 'Continuing exercise through severe pain', 'dose': 'AVOID', 'freq': '—', 'use': 'Rest is essential for recovery', 'ok': False},
    ],
    ('foot', 'cut'): [
        {'name': 'Paracetamol (Dolo 650)', 'dose': '500–650 mg', 'freq': 'Every 4–6 hrs', 'use': 'Pain relief', 'ok': True},
        {'name': 'Betadine / Povidone-Iodine', 'dose': 'Topical', 'freq': 'Around wound after cleaning', 'use': 'Antiseptic — high infection risk on foot', 'ok': True},
        {'name': 'Neosporin / Soframycin ointment', 'dose': 'Thin layer', 'freq': 'Each dressing change', 'use': 'Antibiotic ointment — prevents cellulitis', 'ok': True},
        {'name': 'Walking barefoot on wound', 'dose': 'AVOID', 'freq': '—', 'use': 'Extremely high contamination and infection risk', 'ok': False},
    ],

    ('back', 'pain'): [
        {'name': 'Paracetamol (Dolo 650)', 'dose': '500–1000 mg', 'freq': 'Every 4–6 hrs', 'use': 'First-line back pain relief', 'ok': True},
        {'name': 'Ibuprofen (Brufen 400mg)', 'dose': '400 mg', 'freq': 'Every 8 hrs with food', 'use': 'Anti-inflammatory for muscle/disc pain', 'ok': True},
        {'name': 'Diclofenac Gel (Voveran / Voltaren)', 'dose': 'Topical', 'freq': '2–3 times daily on painful area', 'use': 'Topical anti-inflammatory', 'ok': True},
        {'name': 'Muscle Relaxant (Myospaz / Flexabenz)', 'dose': 'As prescribed only', 'freq': 'Doctor prescribed — short term', 'use': 'Muscle spasm relief', 'ok': True},
        {'name': 'Prolonged bed rest', 'dose': 'AVOID', 'freq': '—', 'use': 'Delays recovery — gentle movement is better', 'ok': False},
    ],
}


def _fallback_medications(body_part: str, incident: str) -> list:
    """Default medications when no specific entry exists."""
    bp, inc = body_part.lower(), incident.lower()
    meds = [
        {'name': 'Paracetamol (Dolo 650 / Calpol)', 'dose': '500–650 mg', 'freq': 'Every 4–6 hrs (max 4g/day)', 'use': 'Pain and discomfort relief', 'ok': True},
        {'name': 'Betadine / Povidone-Iodine', 'dose': 'Topical', 'freq': 'Apply around wound once cleaned', 'use': 'Antiseptic wound protection', 'ok': True},
    ]
    if inc in ('swelling',):
        meds.append({'name': 'Ibuprofen (Brufen 400mg)', 'dose': '400 mg', 'freq': 'Every 8 hrs with food', 'use': 'Reduces swelling and inflammation', 'ok': True})
        meds.append({'name': 'Diclofenac Gel (Voveran)', 'dose': 'Topical', 'freq': '2–3 times daily', 'use': 'Topical anti-inflammatory', 'ok': True})
    if inc == 'burn':
        meds.append({'name': 'Silver Sulfadiazine cream (Silverex)', 'dose': 'Thin layer', 'freq': 'Once daily under dressing', 'use': 'Burn antibacterial protection', 'ok': True})
    meds.append({'name': 'Aspirin / Blood thinners (for bleeding)', 'dose': 'AVOID', 'freq': '—', 'use': 'Worsen bleeding and clotting', 'ok': False})
    return meds


def _fallback_guidance(body_part: str, incident: str) -> dict:
    """Generate reasonable fallback guidance for combinations not in the database."""
    bp = body_part.lower()
    inc = incident.lower()

    # Generic incident steps
    incident_steps = {
        'bleeding': [
            'Apply firm, direct pressure to the wound with a clean cloth or sterile gauze.',
            'Elevate the injured area above heart level if possible.',
            'Maintain pressure for 10–15 minutes without interruption.',
            'If cloth becomes soaked, add more layers on top — do not remove the original.',
            'Inspect for embedded objects — do not remove them; stabilize and seek care.',
            'Clean the wound gently with running water once bleeding is controlled.',
            'Apply a sterile dressing and bandage.',
            'Check for adequate circulation below the wound site.',
            'Watch for signs of shock: pale skin, rapid pulse, confusion.',
            'Seek medical attention if bleeding does not stop within 15 minutes.',
            'Check tetanus vaccination status.',
            'Keep the person warm, calm, and still.',
        ],
        'burn': [
            'Remove the person from the burn source immediately.',
            'Cool the burn under cool (not cold) running water for 20 minutes.',
            'Do NOT use ice, butter, oil, or any home remedy on the burn.',
            'Remove clothing and jewelry from the area before swelling starts.',
            'Cover the burn loosely with cling film or a clean, non-fluffy material.',
            'Do not break any blisters.',
            'Give paracetamol for pain relief.',
            'Assess burn depth: superficial (red, painful), partial thickness (blistered), full thickness (leathery, painless).',
            'Keep the person warm to prevent shock.',
            'For chemical burns, irrigate continuously for 20–30 minutes.',
            'Seek medical attention for burns larger than a coin or near joints.',
            'Monitor for signs of infection: increasing redness, pus, fever after 24–48 hours.',
        ],
        'pain': [
            'Help the person rest in the most comfortable position available.',
            'Apply an ice pack wrapped in cloth to the painful area for 15–20 minutes.',
            'Administer paracetamol or appropriate pain relief.',
            'Loosen any tight clothing or restrictive items near the painful area.',
            'Assess the nature of pain: onset, location, character, severity, radiation, duration.',
            'Check for associated swelling, bruising, or deformity.',
            'Restrict any activity that worsens the pain.',
            'After 48 hours, a warm compress may help ease persistent muscle pain.',
            'Ensure adequate hydration.',
            'Monitor for worsening or spread of pain.',
            'Seek medical evaluation if pain is severe, does not improve, or has neurological features.',
            'Do not ignore pain that awakens the person from sleep.',
        ],
        'cut': [
            'Wash your hands before treating the wound.',
            'Apply gentle pressure with a clean cloth to control bleeding.',
            'Rinse the wound under clean running water for at least 2 minutes.',
            'Gently remove visible surface debris — do not probe deeply.',
            'Assess wound depth and length.',
            'Apply steri-strips or butterfly closures if edges can be approximated.',
            'Cover with a sterile non-adherent dressing.',
            'Change dressing daily and keep wound dry.',
            'Check tetanus vaccination status.',
            'Monitor for infection: redness, warmth, increasing pain, or pus.',
            'Seek medical care for deep, gaping, or contaminated wounds.',
            'Avoid submerging the wound in water until healed.',
        ],
        'swelling': [
            'Rest the affected area immediately.',
            'Apply RICE: Rest, Ice (wrapped), Compression, Elevation.',
            'Apply an ice pack wrapped in cloth for 15–20 minutes every 2 hours.',
            'Elevate the area above heart level.',
            'Apply a light compression bandage.',
            'Check circulation below the swelling regularly.',
            'Administer paracetamol or ibuprofen for pain.',
            'Assess for deformity or point tenderness over bone (suggests fracture).',
            'Restrict all weight-bearing or use of the area if movement is painful.',
            'Seek X-ray assessment if fracture is suspected.',
            'Monitor for worsening swelling or loss of sensation.',
            'Avoid heat in the first 48 hours.',
        ],
        'bruise': [
            'Apply an ice pack wrapped in cloth to the bruised area immediately.',
            'Keep ice on for 15–20 minutes, remove for 20 minutes, then reapply.',
            'Elevate the bruised area above heart level.',
            'Do not rub or massage a fresh bruise.',
            'Give paracetamol for discomfort — avoid aspirin.',
            'Rest the affected area for 24–48 hours.',
            'After 48 hours, switch to warm compresses to promote reabsorption.',
            'Assess for underlying bone tenderness or deformity.',
            'Monitor the size of the bruise over 24 hours.',
            'Seek evaluation if the bruise is unusually large, over a joint, or extremely painful.',
            'Eat a vitamin C and K-rich diet to support healing.',
            'Protect the area from further impact during recovery.',
        ],
    }

    bp_considerations = {
        'head': ['Monitor for signs of concussion throughout.', 'Seek immediate care if any neurological signs appear.'],
        'eye': ['Do not touch or rub the eye.', 'Seek ophthalmology review urgently.'],
        'chest': ['Monitor breathing rate and depth.', 'Be prepared to call emergency services if breathing changes.'],
        'back': ['Do not move if significant trauma — spinal precautions apply.', 'Check leg sensation and movement.'],
        'hand': ['Check finger movement and sensation.', 'Remove all jewelry before swelling begins.'],
        'arm': ['Check circulation in the hand — pulse, colour, temperature.', 'Immobilize if fracture is suspected.'],
        'leg': ['Check circulation in the foot — pulse, colour, temperature.', 'Avoid weight-bearing if fracture is suspected.'],
        'foot': ['Elevate foot above heart level.', 'Do not walk on a significantly injured foot.'],
    }

    steps = incident_steps.get(inc, incident_steps['pain'])[:]
    extras = bp_considerations.get(bp, [])
    for e in extras:
        if e not in steps:
            steps.append(e)

    return {
        'condition': f'{BODY_PART_DISPLAY.get(bp, bp.title())} {INCIDENT_DISPLAY.get(inc, inc.title())} Injury',
        'summary': (
            f'A {inc} injury to the {bp} requires prompt and appropriate first aid. '
            f'Assess the extent of the injury carefully and follow the steps below to provide '
            f'safe and effective care. Monitor closely for any deterioration and seek professional '
            f'medical attention if in any doubt about the severity.'
        ),
        'first_aid': steps,
        'avoid': [
            'Do not ignore worsening symptoms.',
            'Do not apply heat in the first 48 hours if swelling is present.',
            'Do not delay seeking medical care if in doubt.',
            'Do not give aspirin unless specifically recommended by a doctor.',
            'Do not leave the person unmonitored if they appear unwell.',
        ],
        'emergency_signs': [
            'Rapid worsening of symptoms after initial first aid.',
            'Loss of consciousness or extreme drowsiness.',
            'Signs of severe allergic reaction or anaphylaxis.',
            'Severe, uncontrolled pain not responding to standard pain relief.',
            'Signs of shock: pale skin, rapid weak pulse, confusion.',
            'Any neurological signs: numbness, weakness, confusion.',
        ],
        'recovery': [
            'Follow the RICE principle for the first 48 hours.',
            'Begin gentle movement as soon as tolerated.',
            'Attend medical follow-up appointments.',
            'Maintain a nutritious diet to support tissue healing.',
            'Return to normal activities gradually based on symptom resolution.',
            'Physiotherapy may be needed for significant injuries.',
        ],
        'prevention': [
            'Use appropriate protective equipment for the relevant activity.',
            'Maintain a safe environment free from known hazards.',
            'Keep a well-stocked first aid kit accessible at home and work.',
            'Attend first aid training to be prepared for future emergencies.',
            'Follow safe operating procedures at work and during physical activity.',
        ],
    }


def get_guidance(body_part: str, incident: str, severity: str) -> dict:
    """
    Return comprehensive first aid guidance.
    Falls back to generated guidance if exact match not in DB.
    """
    key = (body_part.lower(), incident.lower())
    base = GUIDANCE_DB.get(key) or _fallback_guidance(body_part, incident)
    risk        = compute_risk(body_part, incident, severity)
    emergency   = is_emergency(risk, body_part, incident, severity)
    medications = MEDICATIONS_DB.get(key) or _fallback_medications(body_part, incident)

    return {
        'body_part':       BODY_PART_DISPLAY.get(body_part.lower(), body_part.title()),
        'incident':        INCIDENT_DISPLAY.get(incident.lower(), incident.title()),
        'severity':        severity.title(),
        'condition':       base['condition'],
        'summary':         base['summary'],
        'risk':            risk,
        'emergency':       emergency,
        'first_aid':       base['first_aid'],
        'avoid':           base['avoid'],
        'emergency_signs': base['emergency_signs'],
        'recovery':        base['recovery'],
        'prevention':      base['prevention'],
        'medications':     medications,
    }
