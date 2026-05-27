from agents.planner_agent import planner
from tools.sql_tool import run_query

question = "Why are flights delayed?"

decision = planner(question)

print("Planner selected:", decision)

if decision == "sql_agent":
    result = run_query(
        "SELECT * FROM flight_delays"
    )

    print(result)

print("\nClaude-style response:")
print("Weather congestion caused delays.")