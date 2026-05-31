# Help Desk Ticket Analyzer
# Beginner Python project by Ruth Okorley

tickets = [
    {
        "ticket_id": 1,
        "issue": "Slow computer performance",
        "category": "Performance",
        "escalation_needed": "No"
    },
    {
        "ticket_id": 2,
        "issue": "Wi-Fi connected but no internet",
        "category": "Network",
        "escalation_needed": "No"
    },
    {
        "ticket_id": 3,
        "issue": "Windows update/security warning",
        "category": "Security/Updates",
        "escalation_needed": "Yes"
    },
    {
        "ticket_id": 4,
        "issue": "Startup apps slowing boot time",
        "category": "Performance",
        "escalation_needed": "No"
    },
    {
        "ticket_id": 5,
        "issue": "Software/application not opening",
        "category": "Application Support",
        "escalation_needed": "Yes"
    }
]

total_tickets = len(tickets)
escalations = 0
no_escalations = 0
categories = {}

for ticket in tickets:
    if ticket["escalation_needed"] == "Yes":
        escalations += 1
    else:
        no_escalations += 1

    category = ticket["category"]

    if category in categories:
        categories[category] += 1
    else:
        categories[category] = 1

print("HELP DESK TICKET ANALYSIS")
print("--------------------------")
print(f"Total tickets reviewed: {total_tickets}")
print(f"Tickets requiring escalation: {escalations}")
print(f"Tickets resolved without escalation: {no_escalations}")

print("\nTicket categories:")
for category, count in categories.items():
    print(f"- {category}: {count}")

print("\nTicket summary:")
for ticket in tickets:
    print(f"Ticket {ticket['ticket_id']}: {ticket['issue']} | Escalation: {ticket['escalation_needed']}")
