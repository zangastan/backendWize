from enum import Enum

class UserRole(str, Enum):
    patient = "patient"
    staff = "staff"
    admin = "admin"
    department_head = "department_head"

class Gender(str, Enum):
    male = "Male"
    female = "Female"
    rather_not_say = "Rather not say"

class StaffRoleWithin(str, Enum):
    doctor = "doctor"
    nurse = "nurse"
    ambulance_driver = "ambulance_driver"
    technician = "technician"
    other = "other"

class AppointmentStatus(str, Enum):
    scheduled = "scheduled"
    checked_in = "checked_in"
    completed = "completed"
    cancelled = "cancelled"
    no_show = "no_show"

class AmbulancePriority(str, Enum):
    high = "high"
    medium = "medium"
    low = "low"

class AmbulanceStatus(str, Enum):
    requested = "requested"
    dispatched = "dispatched"
    on_route = "on_route"
    arrived = "arrived"
    completed = "completed"
    cancelled = "cancelled"

class InquiryStatus(str, Enum):
    open = "open"
    pending = "pending"
    resolved = "resolved"
    closed = "closed"

class MessageSenderType(str, Enum):
    patient = "patient"
    staff = "staff"
    system = "system"

class NotificationRecipientType(str, Enum):
    single_user = "single_user"
    departments = "departments"
    staff_members = "staff_members"
    patients = "patients"
    all = "all"

class NotificationType(str, Enum):
    announcement = "Announcement"
    event = "Event"
    alert = "Alert"
    emergency = "Emergency"

class ActorType(str, Enum):
    user = "user"
    system = "system"
