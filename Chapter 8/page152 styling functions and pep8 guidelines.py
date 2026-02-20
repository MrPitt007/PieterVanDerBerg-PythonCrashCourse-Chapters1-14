

def calculate_average_speed_kmh(distance_km, time_hours):
    """Return the average speed (km/h) given distance in km and time in hours."""
    return distance_km / time_hours


def format_user_badge(first_name, last_name, role="developer"):
    """
    Return a formatted user badge string.
    Demonstrates: descriptive name, parameters, default value, and docstring.
    """
    full_name = f"{first_name.title()} {last_name.title()}"
    return f"{full_name} — {role.title()}"


def connect(host, port=5432, use_ssl=True):
    """Example showing no spaces around '=' for defaults in the signature."""
    return f"Connecting to {host}:{port} (SSL={use_ssl})"



connection_msg = connect(host="db.internal", port=15432, use_ssl=False)
print(connection_msg)


def create_report(
    title,
    author,
    created_at,
    section_1,
    section_2,
    section_3,
    footer_note="All values are provisional.",
):
    """Return a text report. Signature wrapped to keep lines readable."""
    parts = [
        f"# {title}",
        f"Author: {author} — {created_at}",
        "",
        section_1,
        "",
        section_2,
        "",
        section_3,
        "",
        f"Note: {footer_note}",
    ]
    return "\n".join(parts)


demo_report = create_report(
    title="Weekly Metrics",
    author="Data Team",
    created_at="2026-02-20",
    section_1="• Users: 12,340",
    section_2="• Sessions: 81,992",
    section_3="• Conversion: 3.9%",
)
print("\n--- REPORT ---")
print(demo_report)


def sum_list(values):
    """Return the sum of a list of numbers."""
    return sum(values)


def mean_list(values):
    """Return the arithmetic mean of a list of numbers."""
    return sum(values) / len(values) if values else 0.0


print("\nSum:", sum_list([1, 2, 3]))
print("Mean:", mean_list([1, 2, 3]))

