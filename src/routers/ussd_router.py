# # src/routers/ussd_router.py
# from fastapi import APIRouter, Form
# from africastalking import initialize

# router = APIRouter()

# # 🟢 Sandbox credentials
# USERNAME = "sandbox"
# API_KEY = "atsk_1ecced10d1046f288e803841be9b0144dbfaab4b7442b72eab4f0c100376009b7be99ff1"

# # ⚡ Initialize Africa's Talking safely (skip WhatsApp)
# _africa = initialize(username=USERNAME, api_key=API_KEY)

# # Remove WhatsApp to avoid sandbox exception
# if hasattr(_africa, "Whatsapp"):
#     delattr(_africa, "Whatsapp")

# # Only use USSD
# ussd = _africa.USSD

# @router.post("/ussd")
# async def ussd_callback(
#     sessionId: str = Form(...),
#     serviceCode: str = Form(...),
#     phoneNumber: str = Form(...),
#     text: str = Form("")
# ):
#     """
#     USSD request handler for Wezi Medical Centre.
#     """

#     user_response = text.split("*")

#     if text == "":
#         response = (
#             "CON Welcome to Wezi Medical Centre:\n"
#             "1. Services\n"
#             "2. Book Appointment\n"
#             "3. Emergency\n"
#             "4. Directions"
#         )
#     elif user_response[0] == "1":
#         response = (
#             "CON Select Service:\n"
#             "1. Outpatient\n"
#             "2. Inpatient\n"
#             "3. Antenatal\n"
#             "4. Theatre"
#         )
#     elif user_response[0] == "2":
#         response = "CON Enter your name to book an appointment:"
#     elif user_response[0] == "3":
#         response = (
#             "END Emergency contacts:\n"
#             "Ambulance: 123-456\n"
#             "Emergency Room: 789-012"
#         )
#     elif user_response[0] == "4":
#         response = (
#             "END Directions:\n"
#             "From main road, turn left to Wezi Clinic. Ground floor, Building A."
#         )
#     else:
#         response = "END Invalid option. Try again."

#     return response
