    import numpy as np
    import matplotlib.pyplot as plt

    def read_resume(filename):
    <!-- Reads resume content from a text file. -->
    try:
        with open(filename, "r") as file:
            return file.read().lower()
    except FileNotFoundError:
        print("File not found. Please check the filename.")
        return None

    def analyze_keywords(content, keywords):
    <!-- Checks how many keywords from the array exist inside resume content. -->
    match_array = np.array([1 if word in content else 0 for word in keywords])
    return np.sum(match_array), match_array

    def plot_analysis(categories, counts):
    <!-- Displays bar graph based on keyword match. -->
    plt.figure(figsize=(7,5))
    plt.bar(categories, counts)
    plt.title("Resume Keyword Match Analysis")
    plt.xlabel("Keyword Categories")
    plt.ylabel("Match Count")
    plt.show()

    def save_output(score, missing_sections, filename="resume_analysis_output.txt"):
    <!-- Stores analysis result into an output text file. -->
    with open(filename, "w") as file:
        file.write(f"Resume Score: {score}/100\n\n")

        if missing_sections:
            file.write("⚠ Missing Sections:\n")
            for section in missing_sections:
                file.write(f" - {section}\n")

    print(f"\n Results saved in: {filename}")

    def main():
    filename = input("Enter the resume file name (e.g., resume.txt): ")
    content = read_resume(filename)
    if content is None:
    return

    # ------------------------------
    # Keyword Lists (Stored as numpy arrays)
    # ------------------------------
    technical_skills = np.array(["python", "java", "sql", "html", "css", "javascript", "machine learning"])
    soft_skills = np.array(["communication", "leadership", "teamwork", "problem solving", "creativity"])
    resume_sections = np.array(["objective", "skills", "education", "experience", "projects"])

    # ------------------------------
    # Keyword Matching & Score Calculation
    # ------------------------------
    tech_score, tech_match = analyze_keywords(content, technical_skills)
    soft_score, soft_match = analyze_keywords(content, soft_skills)
    section_score, section_match = analyze_keywords(content, resume_sections)

    # Normalize score to 100 scale
    final_score = (tech_score * 30/len(technical_skills)) + \
                  (soft_score * 20/len(soft_skills)) + \
                  (section_score * 50/len(resume_sections))

    final_score = round(final_score, 2)

    print("\n----- RESUME ANALYSIS REPORT -----")
    print(f"Technical Skills Match: {tech_score}/{len(technical_skills)}")
    print(f"Soft Skills Match:      {soft_score}/{len(soft_skills)}")
    print(f"Section Completeness:   {section_score}/{len(resume_sections)}")
    print(f"\n Resume Score: {final_score}/100")

    # Determine missing sections
    missing_sections = [section for section in resume_sections if section not in content]

    if missing_sections:
        print("\n⚠ Missing Important Sections:")
        for section in missing_sections:
            print(f" - {section}")

    # Plot the matching results
    plot_analysis(
        ["Tech Skills", "Soft Skills", "Sections"],
        [tech_score, soft_score, section_score]
    )

    # Save analysis
    save_output(final_score, missing_sections)


    # ---- Run Program ----
    main()
