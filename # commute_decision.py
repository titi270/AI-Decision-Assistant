# commute_decision.py
# Project: AI Decision System for Daily Commutes Based on Transport Conditions
# Author: Timothé LAVAL
# Date: 2024-10-01

# Main function to determine the commute option
def check_commute_options(rain, heavy_traffic, early_meeting, strike, appointment, road_construction):
    """
    Function to determine the best commute option based on the conditions.
    :param rain: It's raining (True/False)
    :param heavy_traffic: Heavy traffic (True/False)
    :param early_meeting: Early meeting (True/False)
    :param strike: Public transport strike (True/False)
    :param appointment: Medical appointment (True/False)
    :param road_construction: Road construction (True/False)
    :return: Suggestions for commute options (WFH, Drive, PublicTransport)
    """

    # Rule for working from home (WFH): It's raining or there's an early meeting
    WFH = rain or early_meeting

    # Rule for driving: No rain, light traffic, no road construction
    Drive = not rain and not heavy_traffic and not road_construction

    # If there's a medical appointment, driving is recommended even if other conditions are unfavorable
    if appointment:
        Drive = True

    # Rule for taking public transport: No strike, no rain
    PublicTransport = not strike and not rain

    return {
        'WorkFromHome': WFH,
        'Drive': Drive,
        'PublicTransport': PublicTransport
    }

# Function to display the final decision
def display_commute_decision(rain, heavy_traffic, early_meeting, strike, appointment, road_construction):
    """
    Displays the best commute option based on the conditions.
    """
    decision = check_commute_options(rain, heavy_traffic, early_meeting, strike, appointment, road_construction)

    print("Current conditions:")
    print(f" - Rain: {rain}")
    print(f" - Heavy traffic: {heavy_traffic}")
    print(f" - Early meeting: {early_meeting}")
    print(f" - Public transport strike: {strike}")
    print(f" - Medical appointment: {appointment}")
    print(f" - Road construction: {road_construction}")
    print("\nCommute decision:")

    if decision['WorkFromHome']:
        print(" -> You should work from home (WFH).")
    elif decision['Drive']:
        print(" -> You should drive.")
    elif decision['PublicTransport']:
        print(" -> You should take public transport.")
    else:
        print(" -> No ideal commute option is available.")

# Simulation of different scenarios
def run_scenarios():
    """
    Tests different scenarios and displays the commute decision for each.
    """

    print("---- Scenario 1: It's raining and there is heavy traffic ----")
    display_commute_decision(rain=True, heavy_traffic=True, early_meeting=False, strike=False, appointment=False, road_construction=False)

    print("\n---- Scenario 2: Public transport strike but it's not raining ----")
    display_commute_decision(rain=False, heavy_traffic=False, early_meeting=False, strike=True, appointment=False, road_construction=False)

    print("\n---- Scenario 3: No rain, light traffic, no strike ----")
    display_commute_decision(rain=False, heavy_traffic=False, early_meeting=False, strike=False, appointment=False, road_construction=False)

    print("\n---- Scenario 4: Medical appointment, no rain but road construction ----")
    display_commute_decision(rain=False, heavy_traffic=False, early_meeting=False, strike=False, appointment=True, road_construction=True)

if __name__ == "__main__":
    run_scenarios()
