def planner(question):
    if "delay" in question.lower():
        return "sql_agent"

    return "summary_agent"