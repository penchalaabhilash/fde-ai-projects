def analyze_log(log: str):
    if "error" in log.lower():
        return "⚠️ Issue detected"
    return "✅ No issues"

if __name__ == "__main__":
    sample = "Error: database connection failed"
    print(analyze_log(sample))