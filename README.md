# AI-Decision-Assistant

## Project Description

This project simulates an AI-based decision-making system to determine the best commute option based on several conditions. The system considers factors such as weather, traffic, and public transport availability to suggest whether you should work from home, drive, or take public transport.

### Commute Options:
1. **Work From Home (WFH)**: Preferred if it's raining or if there is an early meeting.
2. **Drive**: Preferred if it's not raining, traffic is light, and there are no road construction issues.
3. **Public Transport**: Preferred if there is no strike and it's not raining.

### Additional Rules:
- If you have a medical appointment, driving is preferred even if other conditions might suggest otherwise.
- If there is road construction, driving might not be ideal.

## Features

- **Dynamic decision-making**: The system evaluates various real-world conditions like weather, traffic, and strikes to suggest the best commute option.
- **Customizable**: You can easily modify the conditions or add new rules to reflect other factors that may influence your decision.
- **Scenario testing**: Several predefined scenarios are included to demonstrate how the AI system adapts its suggestions based on different conditions.

## How to Run the Code

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/AI-Decision-Assistant.git
   cd AI-Decision-Assistant
