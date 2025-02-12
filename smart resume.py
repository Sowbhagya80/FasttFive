def get_input(prompt, optional=False):
    """
    Helper function to get user input with optional check.
    """
    user_input = input(prompt).strip()
    if optional and not user_input:
        return None
    return user_input

def collect_personal_info():
    print("\nStep 1: Personal Information")
    name = get_input("Enter your full name: ")
    contact_info = get_input("Enter your contact info (email/phone): ")
    location = get_input("Enter your location (city, country): ")
    career_objective = get_input("Enter your career objective (optional): ", optional=True)
    return name, contact_info, location, career_objective

def collect_education():
    print("\nStep 2: Education Details")
    education = []
    while True:
        degree = get_input("Enter your degree (e.g., Bachelor's in Computer Science, or 'done' to finish): ")
        if degree.lower() == 'done':
            break
        school = get_input("Enter your school/university name: ")
        graduation_year = get_input("Enter the year of graduation: ")
        education.append({"degree": degree, "school": school, "year": graduation_year})
    return education

def collect_work_experience():
    print("\nStep 3: Work Experience")
    work_experience = []
    
    has_experience = get_input("Do you have any work experience? (yes/no): ").strip().lower()
    
    if has_experience == "yes":
        while True:
            job_title = get_input("Enter your job title (or 'done' to finish): ")
            if job_title.lower() == 'done':
                break
            company_name = get_input("Enter the company name: ")
            job_duration = get_input("Enter the duration of your job (e.g., Jan 2020 - Dec 2022): ")
            job_description = get_input("Enter a short description of your job responsibilities: ")
            work_experience.append({"title": job_title, "company": company_name, "duration": job_duration, "description": job_description})
    
    return work_experience

def collect_skills():
    print("\nStep 4: Skills")
    skills = get_input("Enter your skills (comma-separated): ")
    return [skill.strip() for skill in skills.split(',')]

def generate_resume(name, contact_info, location, career_objective, education, work_experience, skills):
    print("\nGenerating Resume...")

    resume = f"\n{'='*40}\n"
    resume += f"Resume of {name}\n"
    resume += f"Contact Info: {contact_info}\n"
    resume += f"Location: {location}\n"
    resume += f"{'='*40}\n"
    if career_objective:
        resume += f"Objective:\n{career_objective}\n{'-'*40}\n"
    
    resume += "Education:\n"
    for edu in education:
        resume += f"- {edu['degree']} from {edu['school']} ({edu['year']})\n"
    resume += f"{'-'*40}\n"

    resume += "Work Experience:\n"
    if work_experience:
        for job in work_experience:
            resume += f"- {job['title']} at {job['company']} ({job['duration']})\n"
            resume += f"  Responsibilities: {job['description']}\n"
    else:
        resume += "No work experience provided.\n"
    resume += f"{'-'*40}\n"

    resume += "Skills:\n"
    resume += ', '.join([skill for skill in skills])
    resume += f"\n{'='*40}\n"

    # Save the resume to a text file
    filename = f"{name.replace(' ', '_')}_resume.txt"
    with open(filename, "w") as file:
        file.write(resume)
    
    print(f"\nYour resume has been saved to {filename}!")

def smart_resume_generator():
    print("Welcome to the Smart Resume Generator!")

    # Collecting input from the user
    name, contact_info, location, career_objective = collect_personal_info()
    education = collect_education()
    work_experience = collect_work_experience()
    skills = collect_skills()

    # Generate and save the resume
    generate_resume(name, contact_info, location, career_objective, education, work_experience, skills)

if __name__ == "__main__":
    smart_resume_generator()
