# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from typing import Any, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.types import DomainDict
import uuid




class ActionRaisePasswordResetTicket(Action):
    def name(self):
        return "action_raise_password_reset_ticket"

    def run(self, dispatcher, tracker, domain):
        user_id = tracker.sender_id
        # Integrate your ticketing API here
        dispatcher.utter_message(text=f"A password reset ticket has been raised for user ID {user_id}.")
        return []



class ActionCreateLockTicket(Action):
    def name(self):
        return "action_create_lock_ticket"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):
        
        user_id = tracker.sender_id
        # Simulate ticket creation
        dispatcher.utter_message(text=f"A support ticket has been created for your locked account. Ticket ID: IT-LOCK-{user_id[-4:]}")
        return []


class ActionCreateVPNTicket(Action):
    def name(self):
        return "action_create_vpn_ticket"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):

        user_id = tracker.sender_id
        dispatcher.utter_message(text=f"A support ticket has been created for your VPN issue. Ticket ID: VPN-{user_id[-4:]}")
        return []


class ActionCreateWiFiTicket(Action):
    def name(self):
        return "action_create_wifi_ticket"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):
        user_id = tracker.sender_id
        dispatcher.utter_message(
            text=f"A support ticket has been created for your Wi-Fi issue. Ticket ID: WIFI-{user_id[-4:]}")
        return []


class ActionCreateOutlookTicket(Action):
    def name(self):
        return "action_create_outlook_ticket"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):
        user_id = tracker.sender_id
        dispatcher.utter_message(
            text=f"A support ticket has been raised for your Outlook issue. Ticket ID: OUTLOOK-{user_id[-4:]}")
        return []



class ActionCreateSlowSystemTicket(Action):
    def name(self):
        return "action_create_slow_system_ticket"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):
        user_id = tracker.sender_id
        dispatcher.utter_message(
            text=f"A ticket has been raised for system performance issues. Ticket ID: SLOWPC-{user_id[-4:]}")
        return []



class ActionHandleSoftwareInstallRequest(Action):
    def name(self):
        return "action_handle_software_install_request"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):
        
        software_name_7 = tracker.get_slot("software_name_7")
        
        if software_name_7:
            dispatcher.utter_message(
                text=f"Your request to install {software_name_7} has been submitted. IT will get back to you shortly.")
        else:
            dispatcher.utter_message(
                text="I didn’t catch the software name. Could you please tell me which software you want installed?")
        
        return []


class ActionHandlePrinterIssue(Action):
    def name(self) -> str:
        return "action_handle_printer_issue"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):

        dispatcher.utter_message(response="utter_ask_printer_error_details")
        dispatcher.utter_message(response="utter_troubleshoot_printer_steps")
        dispatcher.utter_message(response="utter_printer_ticket_created")
        return []


class SubmitHardwareRequest(Action):
    def name(self) -> Text:
        return "submit_hardware_request_9"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        hardware = tracker.get_slot("hardware_type_9")
        reason = tracker.get_slot("justification_9")

        # Simulate request logging
        dispatcher.utter_message(text=f"Request logged: {hardware} | Justification_9: {reason}")
        dispatcher.utter_message(response="utter_submit_hardware_request_9")
        return []



# Simulate ticket database
TICKET_DB = {
    "12345": "Open - Waiting for technician",
    "56789": "In Progress - Being resolved",
    "99999": "Closed - Resolved"
}

class SubmitTicketStatus(Action):
    def name(self) -> str:
        return "submit_ticket_status_10"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict) -> list:

        ticket_id_10 = tracker.get_slot("ticket_id_10")

        # Lookup simulated DB
        status_10 = TICKET_DB.get(ticket_id_10, "not found. Please check your ticket ID.")

        dispatcher.utter_message(text=f"The status of ticket {ticket_id_10} is: {status_10}")
        return [SlotSet("ticket_status", status_10)]




class SubmitSupportTicket(Action):
    def name(self) -> str:
        return "submit_support_ticket_11"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        
        issue_type_11 = tracker.get_slot("issue_type_11")
        issue_description_11 = tracker.get_slot("issue_description_11")

        # Simulate creating a ticket
        generated_ticket_id_11 = str(uuid.uuid4())[:8]

        dispatcher.utter_message(
            text=f"Your support ticket for '{issue_type_11}' has been logged.\nDetails: {issue_description_11}\nTicket ID: {generated_ticket_id_11}"
        )

        return [SlotSet("ticket_id_11", generated_ticket_id_11)]


class SubmitFolderAccessRequest(Action):
    def name(self) -> str:
        return "submit_folder_access_request"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        
        folder = tracker.get_slot("folder_name")
        reason = tracker.get_slot("reason")
        access_id = str(uuid.uuid4())[:8]

        dispatcher.utter_message(
            text=f"Access request submitted for folder '{folder}' for reason: {reason}.\nRequest ID: {access_id}"
        )

        return [SlotSet("access_request_id", access_id)]

class SubmitAntivirusIssue(Action):
    def name(self) -> str:
        return "submit_antivirus_issue"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        
        antivirus = tracker.get_slot("antivirus_name")
        error = tracker.get_slot("error_message_13")
        ticket_id_13 = str(uuid.uuid4())[:8]

        dispatcher.utter_message(
            text=f"Thanks. Your antivirus issue with '{antivirus}' has been logged as: {error}.\nTicket ID: {ticket_id_13}. Our team will get back to you soon."
        )

        return [SlotSet("issue_id_13", ticket_id_13)]

class SubmitLostFileRecovery(Action):
    def name(self) -> str:
        return "submit_lost_file_recovery_14"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        
        file_name_14 = tracker.get_slot("file_name_14")
        file_location_14 = tracker.get_slot("file_location_14")
        ticket_id_14 = str(uuid.uuid4())[:8]

        dispatcher.utter_message(
            text=f"Thanks. We’ve logged your file recovery request for '{file_name_14}' from '{file_location_14}'. Ticket ID: {ticket_id_14}. Our IT team will assist you shortly."
        )

        return [SlotSet("issue_id_14", ticket_id_14)]


class SubmitNetworkDriveIssue(Action):
    def name(self) -> str:
        return "submit_network_drive_issue"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        
        drive_letter = tracker.get_slot("drive_letter")
        error_message_15 = tracker.get_slot("error_message_15")
        ticket_id_15 = str(uuid.uuid4())[:8]

        dispatcher.utter_message(
            text=f"Thanks. Your network drive issue for '{drive_letter}' has been logged with the error: '{error_message_15}'. Ticket ID: {ticket_id_15}."
        )

        return [SlotSet("ticket_id_15", ticket_id_15)]


class SubmitEscalation(Action):
    def name(self) -> str:
        return "submit_escalation_16"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:

        ticket_id_16 = tracker.get_slot("ticket_id_16")
        reason_16 = tracker.get_slot("escalate_reason_16")

        # Placeholder for actual escalation logic (e.g., database or API call)
        dispatcher.utter_message(
            text=f"Your ticket {ticket_id_16} has been escalated for the following reason: '{reason_16}'. A senior engineer will respond soon."
        )

        return []

class ActionSubmitFeedback(Action):
    def name(self) -> str:
        return "action_submit_feedback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:

        rating = tracker.get_slot("rating")
        comment = tracker.get_slot("comment")

        # Simulate storing feedback (replace with DB/API logic if needed)
        dispatcher.utter_message(
            text=f"Thanks! You rated us {rating}/5. We appreciate your comment: \"{comment}\""
        )

        return [SlotSet("rating", None), SlotSet("comment", None)]

class ActionLogPhishingEmail(Action):
    def name(self) -> str:
        return "action_log_phishing_email"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        # Example: Log or forward phishing email report
        sender_email = tracker.latest_message.get('text')
        print(f"Phishing email report received: {sender_email}")
        return []

class ActionSubmitOnboardingRequest(Action):
    def name(self) -> str:
        return "action_submit_onboarding_request"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        name = tracker.get_slot("employee_name")
        date = tracker.get_slot("joining_date")
        dept = tracker.get_slot("department")

        # You can log or send this data to a backend or API
        print(f"Onboarding Request: {name}, {date}, {dept}")

        return []


class ActionSubmitCalendarSyncIssue(Action):
    def name(self) -> str:
        return "action_submit_calendar_sync_issue"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        calendar_app = tracker.get_slot("calendar_app")
        device_21 = tracker.get_slot("device_type_21")

        # Log or send to backend
        print(f"Calendar Sync Issue Reported: App - {calendar_app}, Device - {device_21}")

        return []

class ActionSubmitSoftwareCrash(Action):
    def name(self) -> str:
        return "action_submit_software_crash_22"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        software_22 = tracker.get_slot("software_name_22")
        device_22 = tracker.get_slot("device_type_22")

        # Log or connect to ticket system here
        print(f"Software Crash Reported: {software_22} on {device_22}")

        return []


class ActionSubmitDiskSpaceForm(Action):
    def name(self) -> str:
        return "action_submit_disk_space_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        device_23 = tracker.get_slot("device_type_23")
        
        # Simulate logging or API call here
        print(f"Disk space issue reported on {device_23}")
        
        return []


class ActionSubmitBlueScreenForm(Action):
    def name(self) -> str:
        return "action_submit_blue_screen_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[str, Any]) -> List[Dict[str, Any]]:
        
        device_24 = tracker.get_slot("device_type_24")
        version = tracker.get_slot("windows_version")

        # Simulated logging or escalation
        print(f"[ALERT] Blue screen reported on {device_24} running {version}.")

        return []


class ActionSubmitConfigurationSupportForm(Action):
    def name(self) -> str:
        return "action_submit_configuration_support_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[str, Any]) -> List[Dict[str, Any]]:

        config = tracker.get_slot("config_type")
        os = tracker.get_slot("device_os")

        # Simulated log or backend integration
        print(f"[CONFIG REQUEST] Configuration support for {config} on {os} system.")

        dispatcher.utter_message(text=f"Our support team will reach out to assist with {config} configuration on your {os} system.")

        return []

class ActionSubmitReportLostDeviceForm(Action):
    def name(self) -> str:
        return "action_submit_report_lost_device_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[str, Any]) -> List[Dict[str, Any]]:

        device_26 = tracker.get_slot("device_type_26")
        location = tracker.get_slot("last_seen_location")
        date = tracker.get_slot("report_date")

        # Simulated logging or backend integration
        print(f"[DEVICE LOSS REPORT] {device_26} lost at {location} on {date}.")

        dispatcher.utter_message(text=f"A report has been submitted for your {device_26} lost at {location} on {date}. IT security has been notified.")

        return []

class ActionSubmitSetupRemoteAccessForm(Action):
    def name(self) -> str:
        return "action_submit_setup_remote_access_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[str, Any]) -> List[Dict[str, Any]]:

        device_27 = tracker.get_slot("device_type_27")
        os_27 = tracker.get_slot("operating_system_27")
        access_type_27 = tracker.get_slot("access_type_27")

        # Simulate logging or sending to a ticket system
        print(f"[REMOTE ACCESS REQUEST] {access_type_27} setup for {device_27} running {os_27}.")

        dispatcher.utter_message(
            text=f"A request to set up {access_type_27} access from your {device_27} running {os_27} has been submitted. The IT team will follow up shortly."
        )

        return []


class ActionSubmitFirewallPolicyIssueForm(Action):
    def name(self) -> str:
        return "action_submit_firewall_policy_issue_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[str, Any]) -> List[Dict[str, Any]]:

        application_28 = tracker.get_slot("application_name_28")
        access_time_28 = tracker.get_slot("access_time_28")

        # Log or create support ticket
        print(f"[FIREWALL ISSUE] App/Website: {application_28}, Time: {access_time_28}")

        dispatcher.utter_message(
            text=f"Your report regarding access to '{application_28}' being blocked at {access_time_28} has been submitted. The IT security team will investigate the policy restrictions."
        )

        return []


class ActionProvideITFAQ(Action):
    def name(self) -> str:
        return "action_provide_it_faq"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[str, Any]) -> List[Dict[str, Any]]:

        user_message = tracker.latest_message.get("text", "").lower()

        if "working hours" in user_message or "support hours" in user_message or "timing" in user_message:
            dispatcher.utter_message(response="utter_general_it_working_hours")
        elif "escalate" in user_message or "escalation" in user_message or "matrix" in user_message:
            dispatcher.utter_message(response="utter_general_it_escalation_matrix")
        else:
            dispatcher.utter_message(text="Could you please clarify your question regarding IT support?")

        return []


