# tours_data.py
# Phase 1: hardcoded tour data.
# Phase 2: this will be replaced by live data pulled from WordPress via API.
# Keep the structure clean — each key here will map to a WordPress field later.

TOURS = [
    {
        "id": "3-day-maasai-mara",
        "title": "3 Days Maasai Mara Safari",
        "duration_days": 3,
        "destinations": ["Maasai Mara"],
        "category": "Kenya Safaris - Road Safari",
        "style": ["Wildlife"],
        "accommodation": "Lodge",
        "price_from_usd": 650,
        "overview": (
            "A short, action-packed safari into the world-famous Maasai Mara, "
            "ideal for travellers with limited time who still want a genuine wildlife experience."
        ),
        "highlights": [
            "Big Five game drives",
            "Maasai village visit (optional)",
            "Sunset over the savannah",
        ],
        "itinerary": [
            "Day 1: Nairobi to Maasai Mara, afternoon game drive",
            "Day 2: Full day game drives in the Mara",
            "Day 3: Morning game drive, return to Nairobi",
        ],
        "included": [
            "Transport",
            "Park fees",
            "Accommodation",
            "All meals on safari",
            "Professional driver-guide",
        ],
        "excluded": [
            "International flights",
            "Visa fees",
            "Travel insurance",
            "Tips",
        ],
    },
    {
        "id": "4-day-mara-nakuru",
        "title": "4 Days Maasai Mara & Lake Nakuru",
        "duration_days": 4,
        "destinations": ["Maasai Mara", "Lake Nakuru"],
        "category": "Kenya Safaris - Road Safari",
        "style": ["Wildlife"],
        "accommodation": "Lodge",
        "price_from_usd": 820,
        "overview": (
            "Combines the Mara's big cat sightings with Lake Nakuru's flamingos "
            "and rhino sanctuary — a great balance of variety and pace."
        ),
        "highlights": [
            "Maasai Mara game drives",
            "Lake Nakuru rhino sanctuary",
            "Flamingo viewing",
        ],
        "itinerary": [
            "Day 1: Nairobi to Maasai Mara",
            "Day 2: Full day Maasai Mara game drives",
            "Day 3: Mara to Lake Nakuru, afternoon game drive",
            "Day 4: Morning game drive, return to Nairobi",
        ],
        "included": [
            "Transport",
            "Park fees",
            "Accommodation",
            "All meals on safari",
            "Professional driver-guide",
        ],
        "excluded": [
            "International flights",
            "Visa fees",
            "Travel insurance",
            "Tips",
        ],
    },
    {
        "id": "6-day-mara-nakuru-amboseli",
        "title": "6 Days Maasai Mara, Lake Nakuru & Amboseli",
        "duration_days": 6,
        "destinations": ["Maasai Mara", "Lake Nakuru", "Amboseli"],
        "category": "Kenya Safaris - Road Safari",
        "style": ["Wildlife", "Honeymoon"],
        "accommodation": "Lodge",
        "price_from_usd": 1450,
        "overview": (
            "Our signature safari — three of Kenya's best parks in one trip, "
            "finishing with Amboseli's classic views of Mount Kilimanjaro over the plains."
        ),
        "highlights": [
            "Maasai Mara Big Five",
            "Lake Nakuru flamingos & rhinos",
            "Amboseli elephants with Kilimanjaro backdrop",
        ],
        "itinerary": [
            "Day 1: Nairobi to Maasai Mara",
            "Day 2: Full day Maasai Mara game drives",
            "Day 3: Mara to Lake Nakuru",
            "Day 4: Nakuru to Amboseli",
            "Day 5: Full day Amboseli game drives",
            "Day 6: Morning game drive, return to Nairobi",
        ],
        "included": [
            "Transport",
            "Park fees",
            "Accommodation",
            "All meals on safari",
            "Professional driver-guide",
        ],
        "excluded": [
            "International flights",
            "Visa fees",
            "Travel insurance",
            "Tips",
        ],
    },
]


def format_tours_for_prompt(tours: list[dict]) -> str:
    """
    Converts the TOURS list into clean, readable text for the Claude system prompt.
    Never dump raw Python dict syntax into a prompt — Claude reads formatted text better,
    and it is much easier to debug when something goes wrong.
    """
    lines = []

    for tour in tours:
        lines.append(f"{'─' * 60}")
        lines.append(f"TOUR: {tour['title']}")
        lines.append(f"Duration: {tour['duration_days']} days")
        lines.append(f"Destinations: {', '.join(tour['destinations'])}")
        lines.append(f"Style: {', '.join(tour['style'])}")
        lines.append(f"Accommodation: {tour['accommodation']}")
        lines.append(f"Price from: ${tour['price_from_usd']} USD per person")
        lines.append(f"Overview: {tour['overview']}")

        lines.append("Highlights:")
        for h in tour["highlights"]:
            lines.append(f"  • {h}")

        lines.append("Itinerary:")
        for day in tour["itinerary"]:
            lines.append(f"  {day}")

        lines.append("Included: " + ", ".join(tour["included"]))
        lines.append("Not included: " + ", ".join(tour["excluded"]))
        lines.append("")

    return "\n".join(lines)