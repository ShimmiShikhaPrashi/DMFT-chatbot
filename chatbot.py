# chatbot.py
#
# Single-district DMFT chatbot logic for Uttar Bastar Kanker (Chhattisgarh).
#
# NOTE ON DATA: the KANKER_PROJECTS list below is SAMPLE/placeholder data,
# written in the typical style of DMFT-funded works (health, water,
# education, roads) using real tehsils of the district (Kanker, Antagarh,
# Bhanupratappur, Charama, Durgukondal, Narharpur, Koyalibeda). Replace it
# with the district's actual approved project list from:
#   - https://dmf.cg.nic.in/          (Chhattisgarh state DMF portal)
#   - https://kanker.gov.in/en/dmft/  (district DMFT page, if available)

KANKER_PROJECTS = [
    "🚰 Rural Piped Water Supply Scheme — Koyalibeda tehsil",
    "🏥 Upgradation of Community Health Centre — Charama",
    "🎓 Model School / Hostel Construction — Antagarh",
    "🛣️ All-weather Road Connectivity — Bhanupratappur block",
    "☀️ Solar Dual Pump Water Supply — Durgukondal",
    "👩‍🌾 Skill Development & Livelihood Centre — Narharpur",
]


def get_response(message: str) -> str:
    message = message.lower().strip()

    if "hello" in message or "hi" in message or "नमस्ते" in message or "नमस्कार" in message:
        return (
            "👋 Welcome to DMFT Sahayak — Uttar Bastar Kanker!\n\n"
            "I can help you with:\n"
            "1. About DMFT\n"
            "2. DMFT Schemes\n"
            "3. DMFT Projects\n"
            "4. Fund Utilization\n"
            "5. Grievances"
        )

    elif "dmft" in message and ("what" in message or "क्या" in message or "about" in message):
        return (
            "DMFT (District Mineral Foundation Trust) — Uttar Bastar Kanker "
            "works for the welfare and development of areas and people "
            "affected by mining in the district, as per Section 9B of the "
            "MMDR Act, 1957 and the PMKKKY guidelines."
        )

    elif "scheme" in message or "योजना" in message:
        return (
            "DMFT Uttar Bastar Kanker supports development activities such as:\n"
            "🏥 Health\n"
            "🎓 Education\n"
            "💼 Skill Development\n"
            "💧 Drinking Water\n"
            "🏗️ Infrastructure"
        )

    elif "project" in message or "परियोजना" in message:
        return (
            "📍 Sample DMFT Projects — Uttar Bastar Kanker district:\n\n"
            + "\n".join(KANKER_PROJECTS)
            + "\n\n(Placeholder data — replace with the district's official "
              "approved project list.)"
        )

    elif "grievance" in message or "complaint" in message or "शिकायत" in message:
        return (
            "📝 To register a grievance, please provide:\n"
            "1. Name\n"
            "2. Mobile Number\n"
            "3. Description of your complaint\n\n"
            "(District is set to Uttar Bastar Kanker by default.)"
        )

    else:
        return (
            "Sorry, I couldn't understand your question. "
            "Please ask about DMFT, schemes, projects, or grievances."
        )