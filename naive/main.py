# JOB APPLICANTS CLASSIFIER 

# STATIC DATA where we will base the classifying of input data
job_applicants = [
    ["Low", "Bachelor's", "Low", "Reject"],
    ["Medium", "Master's", "High", "Hire"],
    ["High", "PhD", "Medium", "Hire"],
    ["Low", "Bachelor's", "Medium", "Reject"],
    ["High", "Master's", "High", "Hire"],
    ["Medium", "Bachelor's", "Low", "Reject"],
    ["High", "PhD", "High", "Hire"],
    ["Low", "Master's", "Medium", "Reject"],
    ["Medium", "PhD", "High", "Hire"],
    ["High", "Bachelor's", "Medium", "Hire"],
    ["Medium", "Master's", "Medium", "Hire"],
    ["Low", "PhD", "Low", "Reject"]
]
features = ("experience", "education_level", "interview_score")

total_hire = sum(applicant.count("Hire") for applicant in job_applicants)
total_reject = sum(applicant.count("Reject") for applicant in job_applicants)
total_applicants = total_hire + total_reject

def get_probability(feature, feature_data, label): # Get the probability of "feature" being "label"
    total = 0
    for applicant in job_applicants:
        if applicant[features.index(feature)] == feature_data and applicant[-1] == label:
            total += 1
    if label == "Hire":
        return total/total_hire
    elif label == "Reject":
        return total/total_reject

def classify(experience, education_level, interview_score):
    hire_probability = (get_probability("experience", experience, "Hire")) * (get_probability("education_level", education_level, "Hire")) * (get_probability("interview_score", interview_score, "Hire")) * (total_hire/total_applicants)
    reject_probability = (get_probability("experience", experience, "Reject")) * (get_probability("education_level", education_level, "Reject")) * (get_probability("interview_score", interview_score, "Reject")) * (total_reject/total_applicants)

    print(f"Hire: {hire_probability} \nReject: {reject_probability}\n")
    return "Hire" if hire_probability > reject_probability else "Reject"

experience = input("Enter Job Applicant's Experience(Low, Medium, High): ")
education_level = input("Enter Job Applicant's Education Level(Bachelor's, Master's, PhD): ")
interview_score = input("Enter Job Applicant's Interview Score(Low, Medium, High): ")

print(classify(experience, education_level, interview_score))



